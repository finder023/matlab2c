function [return_code] = STOP(process_id)
    global INVALID_PARAM;
    global DORMANT;
    global NO_ACTION;
    global WT_TIMER;
    global NO_ERROR;
    
    proc = find_proc(process_id);
    if isequal(proc, [])
        return_code = INVALID_PARAM;
        return;
    end

    if proc.status.process_state == DORMANT
        return_code = NO_ACTION;
        return;
    end

    proc = set_proc_dormant(proc);

    if test_wt_flag(proc, WT_TIMER)
        stop_timer(proc);
    end
    update_proc(proc);
    return_code = NO_ERROR;

end