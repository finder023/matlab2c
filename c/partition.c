void do_get_partition_status( partition_status_t* status, return_code_t* return_code) {

    partition_t* part = current->part;
    *status = part->status;
    *return_code = NO_ERROR;
}

void do_set_partition_mode( partition_mode_t mode, return_code_t* return_code) {

    partition_t* part = current->part;
    if ( mode >= 4 ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( part->status.operating_mode == NORMAL && mode == NORMAL ) {
        *return_code = NO_ACTION;
        return;
    }
    if ( part->status.operating_mode == COLD_START && mode == WARM_START ) {
        *return_code = INVALID_MODE;
        return;
    }
    part->status.operating_mode = mode;
    if ( mode == IDLE ) {
        part->scheduling = 0;
    }
    if ( mode == NORMAL ) {
        // wakeup_waiting_proc
        list_entry_t *le = part->proc_set.next;
        struct proc_struct *proc;
        while ( le != &part->proc_set ) {
            proc = le2proc(le, part_link);
            if ( proc->status.process_state == WAITING && test_wg_flag(proc, WT_PNORMAL) ) {
                clear_wt_flag(proc, WT_PNORMAL);
                list_del(&proc->run_link);
                if ( proc->wait_state == 0 ) {
                    wakeup_proc(proc);
                }
            }
            le = list_next(le);
        }
        part->scheduling = 1;
        if ( part->first_run == 0 ) {
            part->first_run = 1;
        }
        part->status.lock_level = 0;
    }
    *return_code = NO_ERROR;
}

