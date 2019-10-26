function [return_code] = START(process_id)
    proc = find_proc(process_id);
    if proc == []
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
            wakeup_proc(proc);
            if PREEMPTION ~= 0
                schedule();
            end
        end
    else
        set_proc_waiting(proc, WT_PNORMAL, []);
    end
    return_code = NO_ERROR;
end