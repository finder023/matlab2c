void do_get_semaphore_id( semaphore_name_t semaphore_name, semaphore_id_t* semaphore_id, return_code_t* return_code) {

    sem_t* sem = get_sem_by_name(semaphore_name);
    if ( sem == NULL ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    *semaphore_id = sem->sem_id;
    *return_code = NO_ERROR;
}

void do_get_semaphore_status( semaphore_id_t semaphore_id, semaphore_status_t* semaphore_status, return_code_t* return_code) {

    sem_t* sem = get_sem_by_id(semaphore_id);
    if ( sem == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    *semaphore_status = sem->sem_status;
    *return_code = NO_ERROR;
}

void do_signal_semaphore( semaphore_id_t semaphore_id, return_code_t* return_code) {

    sem_t* sem = get_sem_by_id(semaphore_id);
    if ( sem == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( sem->sem_status.current_value == sem->sem_status.max_value ) {
        *return_code = NO_ACTION;
        return;
    }
    if ( sem->sem_status.waiting_processes == 0 ) {
        sem->sem_status.current_value = sem->sem_status.current_value + 1;
        *return_code = NO_ERROR;
    }
    else {
        // select_waiting_proc
        list_entry_t *elem = sem->waiting_thread.next;
        struct proc_struct *proc = le2proc(elem, run_link);
        list_del_init(&proc->run_link);
        if ( test_wt_flag(proc, WT_TIMER) != 0 ) {
            // stop_timer
            timer_t *timer = proc->timer;
            del_timer(timer);
            clear_wt_flag(proc, WT_TIMER);
            kfree_timer(timer);
        }
        clear_wt_flag(proc, WT_KSEM);
        if ( test_wt_flag(proc, WT_SUSPEND) == 0 ) {
            wakeup_proc(proc);
            if ( PREEMPTION != 0 ) {
                schedule();
            }
        }
        *return_code = NO_ERROR;
    }
}

void do_wait_semaphore( semaphore_id_t semaphore_id, system_time_t time_out, return_code_t* return_code) {

    struct proc_struct* proc = current;
    sem_t* sem = get_sem_by_id(semaphore_id);
    if ( sem == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( time_out > MAX_TIME_OUT ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( sem->sem_status.current_value > 0 ) {
        sem->sem_status.current_value = sem->sem_status.current_value - 1;
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
    else if ( time_out == INFINITE_TIME_VALUE) {
        // set_proc_waiting
        proc->status.process_state = WAITING;
        list_del_init(&proc->run_link);
        set_wt_flag(proc, WT_KSEM);
        list_add_before(&sem->waiting_thread, &proc->run_link);
        sem->sem_status.waiting_processes = sem->sem_status.waiting_processes + 1;
        schedule();
        sem->sem_status.waiting_processes = sem->sem_status.waiting_processes - 1;
        *return_code = NO_ERROR;
        return;
    }
    else {
        // add_timer
        timer_t *timer = kmalloc(sizeof(timer_t));
        timer_init(timer, proc, time_out);
        set_wt_flag(proc, WT_TIMER);
        add_timer(timer);
        proc->timer = timer;
        // set_proc_waiting
        proc->status.process_state = WAITING;
        list_del_init(&proc->run_link);
        set_wt_flag(proc, WT_KSEM);
        list_add_before(&sem->waiting_thread, &proc->run_link);
        sem->sem_status.waiting_processes = sem->sem_status.waiting_processes + 1;
        schedule();
        sem->sem_status.waiting_processes = sem->sem_status.waiting_processes - 1;
        if ( proc->timer == NULL ) {
            *return_code = TIMED_OUT;
        }
        else {
            proc->timer = NULL;
            *return_code = NO_ERROR;
        }
        return;
    }
}

void do_create_semaphore( semaphore_name_t semaphore_name, semaphore_value_t current_value, semaphore_value_t max_value, queuing_discipline_t queuing_discipline, semaphore_id_t* semaphore_id, return_code_t* return_code) {

    partition_t* part = current->part;
    if ( part->sem_num >= MAX_NUMBER_OF_SEMAPHORES ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    sem_t* sem = get_sem_by_name(semaphore_name);
    if ( sem != NULL ) {
        *return_code = NO_ACTION;
        return;
    }
    if ( current_value > MAX_SEMAPHORE_VALUE ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( max_value > MAX_SEMAPHORE_VALUE ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( queuing_discipline != FIFO && queuing_discipline != PRIORITY ) {
        *return_code = INVALID_PARAM;
        return;
    }
    sem = alloc_sem();
    if ( sem == NULL ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    strcpy(sem->sem_name, semaphore_name);
    *semaphore_id = sem->sem_id;
    sem->sem_status.current_value = current_value;
    sem->sem_status.max_value = max_value;
    sem->sem_status.waiting_processes = 0;
// add_sem
    list_add_after(&part->all_sem, &sem->sem_link);
    part->sem_num = part->sem_num + 1;
    *return_code = NO_ERROR;
}

