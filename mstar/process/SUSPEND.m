function [return_code ] = SUSPEND(process_id)
    if PREEMPTION ~= 1
        return_code = INVALID_MODE;
        return;
    end

    proc = find_proc(process_id);
    if proc == [] || proc == current
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
        set_proc_waiting(proc, WT_SUSPEND, []);
    end

end