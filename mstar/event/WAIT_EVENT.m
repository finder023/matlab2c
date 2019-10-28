function [return_code] = WAIT_EVENT(event_id, time_out)
    event = get_event_by_id(event_id);
    if event == []
        return_code = INVALID_PARAM;
        return;
    end
    
    if time_out > MAX_TIME_OUT
        return_code = INVALID_PARAM;
        return;
    end

    if event.status.event_state == UP
        return_code = NO_ERROR;
        return;
    elseif time_out == 0
        return_code = NOT_AVAILABLE;
        return;
    elseif PREEMPTION == 0
        return_code = INVALID_MODE;
        return;
    elseif time_out == INFINITE_TIME_VALUE
        set_proc_waiting(current, WT_EVENT, event);
        event.status.waiting_processes = event.status.waiting_processes + 1;
        schedule();
        return_code = NO_ERROR;
    else
        set_proc_waiting(current, WT_EVENT, event);
        event.status.waiting_processes = event.status.waiting_processes + 1;
        add_timer(current, time_out);
        schedule();
        if current.timer == []
            return_code = TIMED_OUT;
        else
            current.timer = [];
            return_code = NO_ERROR;
        end
    end
end