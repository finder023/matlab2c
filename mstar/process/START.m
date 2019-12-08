function [return_code] = START(process_id)
    
    global INVALID_PARAM;
    global DORMANT;
    global NO_ACTION;
    global INFINITE_TIME_VALUE;
    global NORMAL;
    global PREEMPTION;
    global WT_PNORMAL;
    global NO_ERROR;

    proc = find_proc(process_id);
    if isequal(proc, [])
        return_code = INVALID_PARAM;
        return;
    end
    
    if proc.status.process_state ~= DORMANT
        return_code = NO_ACTION;
        return;
    end

    if proc.status.attributes.period == INFINITE_TIME_VALUE
        proc.status.current_priority = proc.status.attributes.base_priority;
        init_proc_context(proc);
        part = proc.part;
        if part.status.operating_mode == NORMAL
            proc.time_slice = proc.status.attributes.time_capacity;
            proc = wakeup_proc(proc);
            if PREEMPTION ~= 0
                schedule();
            end
        else
            set_proc_waiting(proc, WT_PNORMAL, []);
        end
    end
    update_proc(proc);
    return_code = NO_ERROR;
end