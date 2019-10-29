function [return_code] = SET_EVENT(event_id)
    event = get_event_by_id(event_id);
    proc = current;
    if event == []
        return_code = INVALID_PARAM;
        return;
    end

    event.status.event_state = UP;
    stop_all_timer(event);
    wakeup_waiting_proc(WT_EVENT, event);
    event.status.waiting_processes = 0;
    if PREEMPTION ~= 0
        schedule();
    end
end