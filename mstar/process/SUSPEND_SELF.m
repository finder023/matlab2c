function [ return_code ] = SUSPEND_SELF(time_out)


    if PREEMPTION ~= 1
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
        set_proc_waiting(proc, WT_SUSPEND, []);
        if time_out ~= INFINITE_TIME_VALUE
            add_timer(proc, time_out);
        end

        schedule();

        if proc.timer == []
            return_code = TIMED_OUT;
            return;
        else 
            proc.timer = [];
            return_code = NO_ERROR;
            return;
        end
    end
end