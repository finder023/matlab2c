function [return_code] = STOP(process_id)
    proc = find_proc(process_id);
    if proc == []
        return_code = INVALID_PARAM;
        return;
    end

    if proc.status.process_state == DORMANT
        return_code = NO_ACTION;
        return;
    end

    set_proc_dormant(proc);

    if test_wt_flag(proc, WT_TIMER)
        stop_timer(proc);
    end
    return_code = NO_ERROR;

end