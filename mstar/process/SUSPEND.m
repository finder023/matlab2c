function [return_code ] = SUSPEND(process_id)
    global PREEMPTION;
    global INVALID_MODE;
    global INVALID_PARAM;
    global DORMANT;
    global INFINITE_TIME_VALUE;
    global WAITING;
    global WT_SUSPEND;
    global NO_ACTION;
    global current;
    
    
    if PREEMPTION ~= 1
        return_code = INVALID_MODE;
        return;
    end

    proc = find_proc(process_id);
    if isequal(proc, []) || isequal(current, proc)
        return_code = INVALID_PARAM;
        return;
    end

    if proc.status.process_state == DORMANT
        return_code = INVALID_MODE;
        return;
    end

    if proc.status.attributes.period ~= INFINITE_TIME_VALUE
        return_code = INVALID_MODE;
        return;
    end

    if proc.status.process_state == WAITING && test_wt_flag(proc, WT_SUSPEND)
        return_code = NO_ACTION;
        return;
    else
        proc = set_proc_waiting(proc, WT_SUSPEND, []);
    end
    update_proc(proc);

end