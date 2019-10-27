function [len, return_code] = RECEIVE_QUEUING_MESSAGE(id, time_out, message_addr)
    queue = get_queue_by_id(id);
    msg = null_msg();
    if queue == NULL
        return_code = INVALID_PARAM;
        return;
    end
    
    if time_out > MAX_TIME_OUT
        return_code = INVALID_PARAM;
        return;
    end

    if queue.status.nb_message > 0
        msg = remove_message(queue);
        memcpy(message_addr, msg.buff, msg.length);
        len = msg.length;
        queue.status.nb_message = queue.status.nb_message - 1;

        if queue.status.nb_message + 1 == SYSTEM_LIMIT_NUMBER_OF_MESSAGES
            proc = select_waiting_proc(queue);
            clear_wt_flag(proc, WT_QUEUE);
            wakeup_proc(proc);
            schedule();
        end
        return_code = NO_ERROR;
    elseif time_out == 0
        len = 0;
        return_code = NOT_AVAILABLE;
    elseif PREEMPTION == 0
        len = 0;
        return_code = INVALID_MODE;
    elseif time_out == INFINITE_TIME_VALUE
        set_proc_waiting(current, WT_QUEUE, queue);
        queue.status.waiting_process = queue.status.waiting_process + 1;
        schedule();
        queue.status.waiting_process = queue.status.waiting_process - 1;
        msg = remove_message(queue);
        memcpy(message_addr, msg.buff, msg.length);
        len = msg.length;
        queue.status.nb_message = queue.status.nb_message - 1;
        return_code = NO_ERROR;
    else
        add_timer(current, time_out);
        set_proc_waiting(current, WT_QUEUE, queue);
        queue.status.waiting_process = queue.status.waiting_process + 1;
        schedule();
        queue.status.waiting_process = queue.status.waiting_process - 1;

        if current.timer == []
            return_code = TIMED_OUT;
        else
            current.timer = [];
            msg = remove_message(queue);
            memcpy(message_addr, msg.buff, msg.length);
            len = msg.length;
            queue.status.nb_message = queue.status.nb_message - 1;
            return_code = NO_ERROR;
        end
    end 
end