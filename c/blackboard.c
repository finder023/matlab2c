void do_get_blackboard_id( blackboard_name_t blackboard_name, blackboard_id_t* blackboard_id, return_code_t* return_code) {

    blackboard_t* bboard = get_blackboard_by_name(blackboard_name);
    if ( bboard == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    *blackboard_id = bboard->id;
    *return_code = NO_ERROR;
}

void do_create_blackboard( blackboard_name_t blackboard_name, size_t max_message_size, blackboard_id_t* blackboard_id, return_code_t* return_code) {

    partition_t* part = current->part;
    if ( part->blackboard_num >= MAX_NUMBER_OF_BLACKBOARDS ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    blackboard_t* blackboard = get_blackboard_by_name(blackboard_name);
    if ( blackboard != NULL ) {
        *return_code = NO_ACTION;
        return;
    }
    if ( max_message_size <= 0 ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( part->status.operating_mode == NORMAL ) {
        *return_code = INVALID_MODE;
        return;
    }
    blackboard = alloc_blackboard(max_message_size);
    if ( blackboard == NULL ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    blackboard->status.max_message_size = max_message_size;
    blackboard->status.waiting_processes = 0;
    strcpy(blackboard->name, blackboard_name);
    // add_blackboard
    list_add_after(&part->all_blackboard, &blackboard->bb_link);
    part->blackboard_num = part->blackboard_num + 1;
    *blackboard_id = blackboard->id;
    *return_code = NO_ERROR;
}

void do_display_blackboard( blackboard_id_t blackboard_id, system_addr_t message_addr, size_t len, return_code_t* return_code) {

    blackboard_t* bboard = get_blackboard_by_id(blackboard_id);
    if ( bboard == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( len > bboard->status.max_message_size ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( len <= 0 ) {
        *return_code = INVALID_PARAM;
        return;
    }
    bboard->status.empty_indicator = OCCUPIED;
    memcpy(bboard->buff, message_addr, len);
    bboard->length = len;
    // stop_all_timer
    list_entry_t *le = bboard->waiting_thread.next;
    struct proc_struct *proc;
    while ( le != &bboard->waiting_thread ) {
        proc = le2proc(le, run_link);
        if ( proc->status.process_state == WAITING && test_wg_flag(proc, WT_TIMER) ) {
            clear_wt_flag(proc, WT_TIMER);
            timer_t* timer = proc->timer;
            del_timer(timer);
            kfree(timer);
        }
        le = list_next(le);
    }
    // wakeup_waiting_proc
    list_entry_t *le = bboard->waiting_thread.next;
    struct proc_struct *proc;
    while ( le != &bboard->waiting_thread ) {
        proc = le2proc(le, run_link);
        if ( proc->status.process_state == WAITING && test_wg_flag(proc, WT_BBOARD) ) {
            clear_wt_flag(proc, WT_BBOARD);
            list_del(&proc->run_link);
            if ( proc->wait_state == 0 ) {
                wakeup_proc(proc);
            }
        }
        le = list_next(le);
    }
    bboard->status.waiting_processes = 0;
    if ( PREEMPTION != 0 ) {
        schedule();
    }
    *return_code = NO_ERROR;
}

void do_read_blackboard( blackboard_id_t blackboard_id, system_time_t time_out, system_addr_t message_addr, size_t* len, return_code_t* return_code) {

    blackboard_t* bboard = get_blackboard_by_id(blackboard_id);
    struct proc_struct* proc = current;
    if ( bboard == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( time_out > MAX_TIME_OUT ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( bboard->status.empty_indicator == OCCUPIED ) {
        memcpy(message_addr, bboard->buff, bboard->length);
        *len = bboard->length;
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
        proc->status.process_state = WAITING;
        list_del_init(&proc->run_link);
        set_wt_flag(proc, WT_BBOARD);
        list_add_before(&bboard->waiting_thread, &proc->run_link);
        bboard->status.waiting_processes = bboard->status.waiting_processes + 1;
        schedule();
        memcpy(message_addr, bboard->buff, bboard->length);
        *len = bboard->length;
        *return_code = NO_ERROR;
    }
    else {
        // set_proc_waiting
        proc->status.process_state = WAITING;
        list_del_init(&proc->run_link);
        set_wt_flag(proc, WT_BBOARD);
        list_add_before(&bboard->waiting_thread, &proc->run_link);
        // add_timer
        timer_t *timer = kmalloc(sizeof(timer_t));
        timer_init(timer, proc, timeout);
        set_wt_flag(proc, WT_TIMER);
        add_timer(timer);
        proc->timer = timer;
        bboard->status.waiting_processes = bboard->status.waiting_processes + 1;
        schedule();
        if ( proc->timer == NULL ) {
            *len = 0;
            *return_code = TIMED_OUT;
        }
        else {
            proc->timer = NULL;
            memcpy(message_addr, bboard->buff, bboard->length);
            *len = bboard->length;
            *return_code = NO_ERROR;
        }
    }
}

void do_clear_blackboard( blackboard_id_t blackboard_id, return_code_t* return_code) {

    blackboard_t* bboard = get_blackboard_by_id(blackboard_id);
    if ( bboard == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    bboard->status.empty_indicator = EMPTY;
    *return_code = NO_ERROR;
}

void do_get_blackboard_status( blackboard_id_t blackboard_id, blackboard_status_t blackboard_status, return_code_t* return_code) {

    blackboard_t* bboard = get_blackboard_by_id(blackboard_id);
    if ( bboard == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    blackboard_status = bboard->status;
    *return_code = NO_ERROR;
}

