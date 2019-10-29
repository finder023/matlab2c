function [return_code] = DISPLAY_BLACKBOARD(blackboard_id, message_addr, len)
    bboard = get_blackboard_by_id(blackboard_id);
    proc = current;
    if bboard == []
        return_code = INVALID_PARAM;
        return;
    end
    
    if len > bboard.status.max_message_size
        return_code = INVALID_PARAM;
        return;
    end

    if len <= 0
        return_code = INVALID_PARAM;
        return;
    end

    bboard.status.empty_indicator = OCCUPIED;
    memcpy(bboard.buff, message_addr, len);
    bboard.length = len;

    stop_all_timer(bboard);
    wakeup_waiting_proc(WT_BBOARD, bboard);
    bboard.status.waiting_processes = 0;

    if PREEMPTION ~= 0
        schedule();
    end

    return_code = NO_ERROR;

end