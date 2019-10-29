function [len, return_code] = READ_BLACKBOARD(blackboard_id, time_out, message_addr)
    bboard = get_blackboard_by_id(blackboard_id);
    proc = current;
    if bboard == []
        return_code = INVALID_PARAM;
        return;
    end
    
    if time_out > MAX_TIME_OUT
        return_code = INVALID_PARAM;
        return;
    end

    if bboard.status.empty_indicator == OCCUPIED
        memcpy(message_addr, bboard.buff, bboard.length);
        len = bboard.length;
        return_code = NO_ERROR;
    elseif time_out == 0
        len = 0;
        return_code = NOT_AVAILABLE;
    elseif PREEMPTION == 0
        len = 0;
        return_code = INVALID_MODE;
    elseif time_out == INFINITE_TIME_VALUE
        set_proc_waiting(proc, WT_BBOARD, bboard);
        bboard.status.waiting_processes = bboard.status.waiting_processes + 1;

        schedule();

        memcpy(message_addr, bboard.buff, bboard.length);
        len = bboard.length;
        return_code = NO_ERROR;
    else
        set_proc_waiting(proc, WT_BBOARD, bboard);
        add_timer(proc, time_out);
        bboard.status.waiting_processes = bboard.status.waiting_processes + 1;
        
        schedule();

        if proc.timer == []
            len = 0;
            return_code = TIMED_OUT;
        else
            proc.timer = [];
            memcpy(message_addr, bboard.buff, bboard.length);
            len = bboard.length;
            return_code = NO_ERROR;
        end
    end
end