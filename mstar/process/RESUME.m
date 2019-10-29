function [return_code] = resume(process_id)
    proc = find_proc(process_id);
   
    if proc == []
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

    if test_wt_flag(proc, WT_SUSPEND) == 0
        return_code = NO_ACTION;
        return;
    end

    if test_wt_flag(proc, WT_SUSPEND) ~= 0 && test_wt_flag(proc, WT_SUSPEND) ~= 0
        stop_timer(proc);
    end

    clear_wt_flag(proc, WT_SUSPEND);
     
    if proc.wait_state == 0
        wakeup_proc(proc);
        if PREEMPTION ~= 0
            schedule();
        end
    end
    return_code = NO_ERROR;
end