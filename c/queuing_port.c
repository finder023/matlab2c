#include < queuing_port >

void do_clear_queuing_port( queuing_port_id_t id, return_code_t* return_code) {

    queuing_port_t* queue = get_queue_by_id(id);
    if ( queue == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( queue->status.port_direction != DESTINATION ) {
        *return_code = INVALID_MODE;
        return;
    }
    list_entry_t* cmle = queue->msg_set.next;
    message_t *msg = NULL;
    while ( cmle != &queue->msg_set ) {
        list_del(cmle);
        msg = le2msg(cmle, msg_link);
        free_message(msg);
        cmle = list_next(cmle);
    }
    queue->status.nb_message = 0;
    *return_code = NO_ERROR;
}


void do_create_queuing_port( queuing_port_name_t name, message_size_t max_msg_size, message_range_t max_nb_msg, port_direction_t port_direction, queuing_discipline_t queuing_discipline, queuing_port_id_t* id, return_code_t* return_code) {

    if ( nr_queuing_port >= MAX_NUMBER_OF_QUEUING_PORTS ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    queuing_port_t* queue = get_queue_by_name(name);
    if ( queue != NULL ) {
        *return_code = NO_ACTION;
        return;
    }
    if ( max_msg_size <= 0 ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    if ( max_nb_msg > SYSTEM_LIMIT_NUMBER_OF_MESSAGES ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    if ( port_direction != SOURCE && port_direction != DESTINATION ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    partition_t* part = current->part;
    if ( part->status.operating_mode == NORMAL ) {
        *return_code = INVALID_MODE;
        return;
    }
    queue = alloc_queuing_port(max_msg_size);
    if ( queue == NULL ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    queue->status.max_message_size = max_msg_size;
    queue->status.port_direction = port_direction;
    queue->status.nb_message = 0;
    queue->status.max_nb_message = max_nb_msg;
    queue->status.waiting_process = 0;
    strcpy(queue->name, name);
    *id = queue->id;
    *return_code = NO_ERROR;
}


void do_get_queuing_port_id( queuing_port_name_t name, queuing_port_id_t* id, return_code_t* return_code) {

    queuing_port_t* queue = get_queue_by_name(name);
    if ( queue == NULL ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    *id = queue->id;
    *return_code = NO_ERROR;
}


void do_get_queuing_port_status( queuing_port_id_t id, queuing_port_status_t* status, return_code_t* return_code) {

    queuing_port_t* queue = get_queue_by_id(id);
    if ( queue == NULL ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    *status = queue->status;
    *return_code = NO_ERROR;
}


void do_receive_queuing_message( queuing_port_id_t id, system_time_t time_out, message_addr_t message_addr, message_size_t* len, return_code_t* return_code) {

    queuing_port_t* queue = get_queue_by_id(id);
    message_t* msg = NULL;
    if ( queue == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( time_out > MAX_TIME_OUT ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( queue->status.nb_message > 0 ) {
        // remove_message
        list_entry_t *rmle = queue->msg_set.next;
        list_del_init(rmle);
        msg = le2msg(rmle, msg_link);
        memcpy(message_addr, msg->buff, msg->length);
        *len = msg->length;
        queue->status.nb_message = queue->status.nb_message - 1;
        if ( queue->status.nb_message + 1 == SYSTEM_LIMIT_NUMBER_OF_MESSAGES ) {
            // select_waiting_proc
            list_entry_t *elem = queue->waiting_thread.next;
            struct proc_struct *proc = le2proc(elem, run_link);
            list_del_init(&proc->run_link);
            clear_wt_flag(proc, WT_QUEUE);
            wakeup_proc(proc);
            schedule();
        }
        *return_code = NO_ERROR;
    }
    else if ( time_out == 0) {
        *len = 0;
        *return_code = NOT_AVAILABLE;
    }
    else if ( PREEMPTION == 0) {
        *len = 0;
        *return_code = INVALID_MODE;
    }
    else if ( time_out == INFINITE_TIME_VALUE) {
        // set_proc_waiting
        current->status.process_state = WAITING;
        list_del_init(&current->run_link);
        set_wt_flag(current, WT_QUEUE);
        list_add_before(&queue->waiting_thread, &current->run_link);
        queue->status.waiting_process = queue->status.waiting_process + 1;
        schedule();
        queue->status.waiting_process = queue->status.waiting_process - 1;
        // remove_message
        list_entry_t *rmle = queue->msg_set.next;
        list_del_init(rmle);
        msg = le2msg(rmle, msg_link);
        memcpy(message_addr, msg->buff, msg->length);
        *len = msg->length;
        queue->status.nb_message = queue->status.nb_message - 1;
        *return_code = NO_ERROR;
    }
    else {
        // add_timer
        timer_t *timer = kmalloc(sizeof(timer_t));
        timer_init(timer, current, time_out);
        set_wt_flag(current, WT_TIMER);
        add_timer(timer);
        current->timer = timer;
        // set_proc_waiting
        current->status.process_state = WAITING;
        list_del_init(&current->run_link);
        set_wt_flag(current, WT_QUEUE);
        list_add_before(&queue->waiting_thread, &current->run_link);
        queue->status.waiting_process = queue->status.waiting_process + 1;
        schedule();
        queue->status.waiting_process = queue->status.waiting_process - 1;
        if ( current->timer == NULL ) {
            *return_code = TIMED_OUT;
        }
        else {
            current->timer = NULL;
            // remove_message
            list_entry_t *rmle = queue->msg_set.next;
            list_del_init(rmle);
            msg = le2msg(rmle, msg_link);
            memcpy(message_addr, msg->buff, msg->length);
            *len = msg->length;
            queue->status.nb_message = queue->status.nb_message - 1;
            *return_code = NO_ERROR;
        }
    }
}


void do_send_queuing_message( queuing_port_id_t id, message_addr_t msg_addr, message_size_t len, system_time_t time_out, return_code_t* return_code) {

    queuing_port_t* queue = get_queue_by_id(id);
    if ( queue == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( time_out > MAX_TIME_OUT ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( len > queue->status.max_message_size ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    if ( len <= 0 ) {
        *return_code = INVALID_PARAM;
        return;
    }
    message_t* msg = alloc_message(queue->status.max_message_size);
    if ( queue->status.max_nb_message > queue->status.nb_message ) {
        memcpy(msg->buff, msg_addr, len);
        msg->length = len;
        list_add_before(&queue->msg_set, &msg->msg_link);
        queue->status.nb_message = queue->status.nb_message + 1;
        if ( queue->status.nb_message == 1 ) {
            if ( queue->status.waiting_process > 0 ) {
                // select_waiting_proc
                list_entry_t *elem = queue->waiting_thread.next;
                struct proc_struct *proc = le2proc(elem, run_link);
                list_del_init(&proc->run_link);
                clear_wt_flag(proc, WT_QUEUE);
                if ( test_wt_flag(proc, WT_TIMER) != 0 ) {
                    // stop_timer
                    timer_t *timer = proc->timer;
                    del_timer(timer);
                    clear_wt_flag(proc, WT_TIMER);
                    kfree(timer);
                }
                wakeup_proc(proc);
                schedule();
            }
        }
        *return_code = NO_ERROR;
    }
    else if ( time_out == 0) {
        *return_code = NOT_AVAILABLE;
        return;
    }
    else if ( PREEMPTION == 0) {
        *return_code = INVALID_MODE;
        return;
    }
    else if ( time_out != INFINITE_TIME_VALUE) {
        // add_timer
        timer_t *timer = kmalloc(sizeof(timer_t));
        timer_init(timer, current, time_out);
        set_wt_flag(current, WT_TIMER);
        add_timer(timer);
        current->timer = timer;
        // set_proc_waiting
        current->status.process_state = WAITING;
        list_del_init(&current->run_link);
        set_wt_flag(current, WT_QUEUE);
        list_add_before(&queue->waiting_thread, &current->run_link);
        queue->status.waiting_process = queue->status.waiting_process + 1;
        schedule();
        queue->status.waiting_process = queue->status.waiting_process - 1;
        if ( current->timer == NULL ) {
            *return_code = TIMED_OUT;
        }
        else {
            current->timer = NULL;
            memcpy(msg->buff, msg_addr, len);
            msg->length = len;
            list_add_before(&queue->msg_set, &msg->msg_link);
            queue->status.nb_message = queue->status.nb_message + 1;
            *return_code = NO_ERROR;
        }
    }
    else {
        // set_proc_waiting
        current->status.process_state = WAITING;
        list_del_init(&current->run_link);
        set_wt_flag(current, WT_QUEUE);
        list_add_before(&queue->waiting_thread, &current->run_link);
        queue->status.waiting_process = queue->status.waiting_process + 1;
        schedule();
        queue->status.waiting_process = queue->status.waiting_process - 1;
        memcpy(msg->buff, msg_addr, len);
        msg->length = len;
        list_add_before(&queue->msg_set, &msg->msg_link);
        queue->status.nb_message = queue->status.nb_message + 1;
        *return_code = NO_ERROR;
    }
}


