function [return_code] = SET_PRIORITY(process_id, priority)
    proc = find_proc(process_id);

    if proc == []
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
    return_code = NO_ERROR;
    
end