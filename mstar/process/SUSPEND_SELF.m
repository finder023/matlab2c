function [ return_code ] = SUSPEND_SELF(time_out)
    global PREEMPTION;
    global INVALID_MODE;
    global MAX_TIME_OUT;
    global INFINITE_TIME_VALUE;
    global NO_ERROR;
    global WT_SUSPEND;
    global current;

    if PREEMPTION == 0
        return_code = INVALID_MODE;
        return;
    end

    if time_out > MAX_TIME_OUT
        return_code = INVALID_MODE;
        return;
    end

    if current.status.attributes.period == INFINITE_TIME_VALUE
        return_code = INVALID_MODE;
        return;
    end

    if time_out == 0
        return_code = NO_ERROR;
        return;
    else
        proc = current;
        proc = set_proc_waiting(proc, WT_SUSPEND, []);
        if time_out ~= INFINITE_TIME_VALUE
            add_timer(proc, time_out);
        end

        schedule();

        if isequal(proc.timer, [])
            return_code = TIMED_OUT;
            return;
        else 
            proc.timer = [];
            return_code = NO_ERROR;
            return;
        end
    end
    update_proc(proc);
end