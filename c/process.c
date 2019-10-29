void do_resume( process_id_t process_id, return_code_t* return_code) {

    struct proc_struct* proc = find_proc(process_id);
    if ( proc == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( proc->status.process_state == DORMANT ) {
        *return_code = INVALID_MODE;
        return;
    }
    if ( proc->status.attributes.period != INFINITE_TIME_VALUE ) {
        *return_code = INVALID_MODE;
        return;
    }
    if ( test_wt_flag(proc, WT_SUSPEND) == 0 ) {
        *return_code = NO_ACTION;
        return;
    }
    if ( test_wt_flag(proc, WT_SUSPEND) != 0 && test_wt_flag(proc, WT_SUSPEND) != 0 ) {
        // stop_timer
        timer_t *timer = proc->timer;
        del_timer(timer);
        clear_wt_flag(proc, WT_TIMER);
        kfree(timer);
    }
    clear_wt_flag(proc, WT_SUSPEND);
    if ( proc->wait_state == 0 ) {
        wakeup_proc(proc);
        if ( PREEMPTION != 0 ) {
            schedule();
        }
    }
    *return_code = NO_ERROR;
}

void do_get_process_status( process_id_t process_id, process_status_t* process_status, return_code_t* return_code) {

    struct proc_struct* proc = find_proc(process_id);
    if ( proc == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    *process_status = proc->status;
    *return_code = NO_ERROR;
}

void do_create_process( process_attribute_t* attr, process_id_t* pid, return_code_t* return_code) {

    partition_t* part = current->part;
    if ( valid_nr_proc() == 0 ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    if ( find_proc_name(attr->name) != NULL ) {
        *return_code = NO_ACTION;
        return;
    }
    if ( attr->stack_size > MAX_STACK_SIZE ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( attr->base_priority > MAX_PRIORITY_VALUE ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( attr->period > MAX_PROC_PERIOD ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( attr->time_capacity > MAX_TIME_CAPA ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( part->status.operating_mode == NORMAL ) {
        *return_code = INVALID_MODE;
        return;
    }
    struct proc_struct* proc = alloc_proc();
    if ( proc == NULL ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    proc->status.attributes = *attr;
    proc->part = current->part;
    if ( setup_ustack(proc) != 0 ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    if ( setup_kstack(proc) != 0 ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    init_proc_context(proc);
    set_proc_link(proc);
    set_mm(proc);
    proc->status.process_state = DORMANT;
    *pid = proc->pid;
    *return_code = NO_ERROR;
    return;
}

void do_stop_self( ) {

    struct proc_struct* proc = current;
    // set_proc_dormant
    proc->status.process_state = DORMANT;
    list_del_init(&proc->run_link);
    list_add_before(&proc->part->dormant_set, &proc->run_link);
    schedule();
}

void do_lock_preemption( lock_level_t* lock_level, return_code_t* return_code) {

    partition_t* part = current->part;
    if ( part->status.operating_mode != NORMAL ) {
        *return_code = NO_ACTION;
        return;
    }
    if ( part->status.lock_level > MAX_LOCK_LEVEL ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    part->status.lock_level = part->status.lock_level + 1;
    *lock_level = part->status.lock_level;
    *return_code = NO_ERROR;
}

void do_start( process_id_t process_id, return_code_t* return_code) {

    struct proc_struct* proc = find_proc(process_id);
    if ( proc == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( proc->status.process_state != DORMANT ) {
        *return_code = NO_ACTION;
        return;
    }
    if ( proc->status.attributes.period == INFINITE_TIME_VALUE ) {
        proc->status.current_priority = proc->status.attributes.base_priority;
        init_proc_context(proc);
        partition_t* part = proc->part;
        if ( part->status.operating_mode == NORMAL ) {
            proc->time_slice = proc->status.attributes.time_capacity;
            wakeup_proc(proc);
            if ( PREEMPTION != 0 ) {
                schedule();
            }
        }
        else {
            // set_proc_waiting
            proc->status.process_state = WAITING;
            list_del_init(&proc->run_link);
            set_wt_flag(proc, WT_PNORMAL);
        }
    }
    *return_code = NO_ERROR;
}

void do_get_my_id( process_id_t* process_id, return_code_t* return_code) {

    *process_id = current->pid;
    *return_code = NO_ERROR;
}

void do_suspend_self( system_time_t time_out, return_code_t* return_code) {

    if ( PREEMPTION == 0 ) {
        *return_code = INVALID_MODE;
        return;
    }
    if ( time_out > MAX_TIME_OUT ) {
        *return_code = INVALID_MODE;
        return;
    }
    if ( current->status.attributes.period == INFINITE_TIME_VALUE ) {
        *return_code = INVALID_MODE;
        return;
    }
    if ( time_out == 0 ) {
        *return_code = NO_ERROR;
        return;
    }
    else {
        struct proc_struct* proc = current;
        // set_proc_waiting
        proc->status.process_state = WAITING;
        list_del_init(&proc->run_link);
        set_wt_flag(proc, WT_SUSPEND);
        if ( time_out != INFINITE_TIME_VALUE ) {
            // add_timer
            timer_t *timer = kmalloc(sizeof(timer_t));
            timer_init(timer, proc, time_out);
            set_wt_flag(proc, WT_TIMER);
            add_timer(timer);
            proc->timer = timer;
        }
        schedule();
        if ( proc->timer == NULL ) {
            *return_code = TIMED_OUT;
            return;
        }
        else {
            proc->timer = NULL;
            *return_code = NO_ERROR;
            return;
        }
    }
}

void do_suspend( process_id_t process_id, return_code_t* return_code) {

    if ( PREEMPTION != 1 ) {
        *return_code = INVALID_MODE;
        return;
    }
    struct proc_struct* proc = find_proc(process_id);
    if ( proc == NULL || proc == current ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( proc->status.process_state == DORMANT ) {
        *return_code = INVALID_MODE;
        return;
    }
    if ( proc->status.attributes.period != INFINITE_TIME_VALUE ) {
        *return_code = INVALID_MODE;
        return;
    }
    if ( proc->status.process_state == WAITING && test_wt_flag(proc, WT_SUSPEND) ) {
        *return_code = NO_ACTION;
        return;
    }
    else {
        // set_proc_waiting
        proc->status.process_state = WAITING;
        list_del_init(&proc->run_link);
        set_wt_flag(proc, WT_SUSPEND);
    }
}

void do_stop( process_id_t process_id, return_code_t* return_code) {

    struct proc_struct* proc = find_proc(process_id);
    if ( proc == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( proc->status.process_state == DORMANT ) {
        *return_code = NO_ACTION;
        return;
    }
    // set_proc_dormant
    proc->status.process_state = DORMANT;
    list_del_init(&proc->run_link);
    list_add_before(&proc->part->dormant_set, &proc->run_link);
    if ( test_wt_flag(proc, WT_TIMER) ) {
        // stop_timer
        timer_t *timer = proc->timer;
        del_timer(timer);
        clear_wt_flag(proc, WT_TIMER);
        kfree(timer);
    }
    *return_code = NO_ERROR;
}

void do_set_priority( process_id_t process_id, priority_t priority, return_code_t* return_code) {

    struct proc_struct* proc = find_proc(process_id);
    if ( proc == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( priority > MAX_PRIORITY_VALUE ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( proc->status.process_state == DORMANT ) {
        *return_code = INVALID_MODE;
        return;
    }
    proc->status.current_priority = priority;
    if ( PREEMPTION == 1 ) {
        schedule();
    }
    *return_code = NO_ERROR;
}

void do_get_process_id( process_name_t process_name, process_id_t* process_id, return_code_t* return_code) {

    struct proc_struct* proc = find_proc_name(process_name);
    if ( proc == NULL ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    *process_id = proc->pid;
    *return_code = NO_ERROR;
    return;
}

void do_unlock_preemption( lock_level_t* lock_level, return_code_t* return_code) {

    partition_t* part = current->part;
    if ( part->status.operating_mode != NORMAL || part->status.lock_level == 0 ) {
        *return_code = NO_ACTION;
        return;
    }
    part->status.lock_level = part->status.lock_level - 1;
    if ( part->status.lock_level == 0 ) {
        *lock_level = 0;
        schedule();
    }
    *lock_level = part->status.lock_level;
    *return_code = NO_ERROR;
}

