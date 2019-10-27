function [len, return_code] = RECEIVE_BUFFER(buffer_id, time_out, message_addr)
    buffer = get_buffer_by_id(buffer_id);
    if buffer == []
        return_code = INVALID_PARAM;
        return;
    end
    
    if time_out > MAX_TIME_OUT
        return_code = INVALID_PARAM;
        return;
    end

    msg = null_msg();
    if buffer.status.nb_message ~= 0
        msg = del_message(buffer);
        memcpy(message_addr, msg.buff, msg.length);
        buffer.status.nb_message = buffer.status.nb_message - 1;
        len = msg.length;

        if buffer.status.waiting_processes ~= 0
            proc = select_waiting_proc(buffer);
            if proc.timer ~= []
                stop_timer(proc);
            end
            clear_wt_flag(proc, WT_BUFFER);
            wakeup_proc(proc);
            buffer.status.waiting_processes = buffer.status.waiting_processes - 1;
            if PREEMPTION ~= 0
                sechdule();
            end
        end
        return_code = NO_ERROR;
    elseif time_out == 0
        len = 0;
        return_code = NO_ERROR;
    elseif PREEMPTION == 0
        len = 0;
        return_code = INVALID_MODE;
    elseif time_out == INFINITE_TIME_VALUE
        set_proc_waiting(current, WT_BUFFER, buffer);
        buffer.status.waiting_processes = buffer.status.waiting_processes + 1;
        sechdule();
        msg = del_message(buffer);
        memcpy(message_addr, msg.buff, msg.length);
        buffer.status.nb_message = buffer.status.nb_message - 1;
        len = msg.length;
        return_code = NO_ERROR;
    else
        add_timer(current, time_out);
        set_proc_waiting(current, WT_BUFFER, buffer);
        buffer.status.waiting_processes = buffer.status.waiting_processes + 1;
        schedule();
        clear_wt_flag(proc, WT_BUFFER);
        if current.timer == []
            len = 0;
            return_code = TIMED_OUT;
        else
            msg = del_message(buffer);
            memcpy(message_addr, msg.buff, msg.length);
            buffer.status.nb_message = buffer.status.nb_message - 1;
            len = msg.length;
            return_code = NO_ERROR;
        end
    end
end 