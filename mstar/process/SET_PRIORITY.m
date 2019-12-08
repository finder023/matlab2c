function [return_code] = SET_PRIORITY(process_id, priority)
    global INVALID_PARAM;
    global MAX_PRIORITY_VALUE;
    global DORMANT;
    global INVALID_MODE;
    global PREEMPTION;
    global NO_ERROR;
    
    proc = find_proc(process_id);

    if isequal(proc, [])
        return_code = INVALID_PARAM;
        return;
    end

    if priority > MAX_PRIORITY_VALUE
        return_code = INVALID_PARAM;
        return;
    end

    if proc.status.process_state == DORMANT
        return_code = INVALID_MODE;
        return;
    end

    proc.status.current_priority = priority;
    if PREEMPTION == 1
        schedule();
    end
    update_proc(proc);
    return_code = NO_ERROR;
    
end