function [return_code] = SEND_BUFFER(buffer_id, message_addr, len, time_out)
    buffer = get_buffer_by_id(buffer_id);
    msg = null_msg();
    if buffer == []
        return_code = INVALID_PARAM;
        return;
    end

    if len > buffer.status.max_message_size
        return_code = INVALID_PARAM;
        return;
    end

    if len <= 0
        return_code = INVALID_PARAM;
        return;
    end

    if time_out > MAX_TIME_OUT
        return_code = INVALID_PARAM;
        return;
    end

    if buffer.status.nb_message < buffer.status.max_nb_message
        if buffer.status.waiting_processes == 0
            msg = alloc_message(buffer.status.max_message_size);
            msg.length = len;
            memcpy(msg.buff, message_addr, len);
            add_message(buffer, msg);
        else
            proc = select_waiting_proc(buffer);
            clear_wt_flag(proc, WT_BUFFER);
            wakeup_proc(proc);
            buffer.status.waiting_processes = buffer.status.waiting_processes - 1;
            if test_wt_flag(proc, WT_TIMER)
                stop_timer(proc);
            end

            msg = alloc_message(buffer.status.max_message_size);
            msg.length = len;
            memcpy(msg.buff, message_addr, len);
            add_message(buffer, msg);

            if PREEMPTION ~= 0
                schedule();
            end
            return_code = NO_ERROR;
        end
    elseif time_out == 0
        return_code = NOT_AVAILABLE;
        return;
    elseif PREEMPTION == 0
        return_code = INVALID_MODE;
        return;
    elseif time_out == INFINITE_TIME_VALUE
        set_proc_waiting(current, WT_BUFFER, buffer);
        buffer.status.waiting_processes = buffer.status.waiting_processes + 1;

        schedule();
        msg = alloc_message(buffer.status.max_message_size);
        msg.length = len;
        memcpy(msg.buff, message_addr, len);
        add_message(buffer, msg);
        return_code = NO_ERROR;
    else
        set_proc_waiting(current, WT_BUFFER, buffer);
        add_timer(current, WT_TIMER);
        buffer.status.waiting_processes = buffer.status.waiting_processes + 1;
        schedule();
        if current.timer == []
            return_code = TIMED_OUT;
        else
            current.timer = [];
            msg = alloc_message(buffer.status.max_message_size);
            msg.length = len;
            memcpy(msg.buff, message_addr, len);
            add_message(buffer, msg);
            return_code = NO_ERROR;
        end
    end
end