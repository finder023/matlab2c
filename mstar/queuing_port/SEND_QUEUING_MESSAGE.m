function [return_code] = SEND_QUEUING_MESSAGE(id, msg_addr, len, time_out)
    queue = get_queue_by_id(id);
    if queue == []
        return_code = INVALID_PARAM;
        return;
    end

    if time_out > MAX_TIME_OUT
        return_code = INVALID_PARAM;
        return;
    end

    if len > queue.status.max_message_size
        return_code = INVALID_CONFIG;
        return;
    end

    if len <= 0
        return_code = INVALID_PARAM;
        return;
    end

    msg = alloc_message(queue.status.max_message_size);
    if queue.status.max_nb_message > queue.status.nb_message
        memcpy(msg.buff, msg_addr, len);
        msg.length = len;
        add_message(queue, msg);

        if queue.status.nb_message == 1
            if queue.status.waiting_process > 0
                proc = select_waiting_proc(queue);
                clear_wt_flag(proc, WT_QUEUE);
                if test_wt_flag(proc, WT_TIMER) ~= 0
                    stop_timer(proc);
                end
                wakeup_proc(proc);
                schedule();
            end
        end
        return_code = NO_ERROR;
    elseif time_out == 0
        return_code = NOT_AVAILABLE;
        return;
    elseif PREEMPTION == 0
        return_code = INVALID_MODE;
        return;
    elseif time_out ~= INFINITE_TIME_VALUE
        add_timer(current, time_out);
        set_proc_waiting(current, WT_QUEUE, queue);
        queue.status.waiting_process = queue.status.waiting_process + 1;
        schedule();

        queue.status.waiting_process = queue.status.waiting_process - 1;
        if current.timer == []
            return_code = TIMED_OUT;
        else
            current.timer = [];
            memcpy(msg.buff, msg_addr, len);
            msg.length = len;
            add_message(queue, msg);
            return_code = NO_ERROR;
        end
    else
        set_proc_waiting(current, WT_QUEUE, queue);
        queue.status.waiting_process = queue.status.waiting_process + 1;
        schedule();

        queue.status.waiting_process = queue.status.waiting_process - 1;
        memcpy(msg.buff, msg_addr, len);
        msg.length = len;
        add_message(queue, msg);
        return_code = NO_ERROR;
    end
end