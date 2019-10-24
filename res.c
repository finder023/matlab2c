[]
void create_process( process_attributes_t* attr, process_id_t* pid, return_code_t* return_code) {


    if ( valid_nr_proc() == 0 ) {
        *return_code = INVALID_CONFIG;        // 2.1
        return;        // 2.2
    }        // 2

    if ( find_proc_name() != NULL ) {
        *return_code = NO_ACTION;        // 3.1
        return;        // 3.2
    }        // 3

    if ( attr->stack_size > MAX_STACK_SIZE ) {
        *return_code = INVALID_PARAM;        // 4.1
        return;        // 4.2
    }        // 4

    if ( attr->base_priority > MAX_PRIORITY_VALUE ) {
        *return_code = INVALID_PARAM;        // 5.1
        return;        // 5.2
    }        // 5

    if ( attr->period > MAX_PROC_PERIOD ) {
        *return_code = INVALID_PARAM;        // 6.1
        return;        // 6.2
    }        // 6

    if ( attr->time_capacity > MAX_TIME_CAPA ) {
        *return_code = INVALID_PARAM;        // 7.1
        return;        // 7.2
    }        // 7

    if ( attr->status.operating_mode == NORMAL ) {
        *return_code = INVLAID_MODE;        // 8.1
        return;        // 8.2
    }        // 8

    struct proc_struct* proc = alloc_proc();        // 9
    if ( proc == NULL ) {
        *return_code = INVALID_CONFIG;        // 10.1
        return;        // 10.2
    }        // 10

    proc->status.attributes = *attr;        // 11
    proc->part = current->part;        // 12
    if ( setup_ustack(proc) != 0 ) {
        *return_code = INVALID_CONFIG;        // 13.1
        return;        // 13.2
    }        // 13

    if ( setup_kstack(proc) != 0 ) {
        *return_code = INVALID_CONFIG;        // 14.1
        return;        // 14.2
    }        // 14

    init_proc_context(proc);        // 15
    set_proc_link(proc);        // 16
    proc->status.process_state = DORMANT;        // 17
    *pid = proc->pid;        // 18
    *return_code = NO_ERROR;        // 19
    return;        // 20
}        // 


