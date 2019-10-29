function [id, return_code] = CREATE_QUEUING_PORT(name, max_msg_size, max_nb_msg, port_direction, queuing_discipline)
    if nr_queuing_port >= MAX_NUMBER_OF_QUEUING_PORTS
        return_code = INVALID_CONFIG;
        return;
    end
    
    queue = get_queue_by_name(name);
    if queue ~= NULL
        return_code = NO_ACTION;
        return;
    end

    if max_msg_size <= 0
        return_code = INVALID_CONFIG;
        return;
    end

    if max_nb_msg > SYSTEM_LIMIT_NUMBER_OF_MESSAGES
        return_code = INVALID_CONFIG;
        return;
    end

    if port_direction ~= SOURCE && port_direction ~= DESTINATION
        return_code = INVALID_CONFIG;
        return;
    end

    part = current.part;
    if part.status.operating_mode == NORMAL
        return_code = INVALID_MODE;
        return;
    end
    queue = alloc_queuing_port(max_msg_size);
    if queue == []
        return_code = INVALID_CONFIG;
        return;
    end

    queue.status.max_message_size = max_msg_size;
    queue.status.port_direction = port_direction;
    queue.status.nb_message = 0;
    queue.status.max_nb_message = max_nb_msg;
    queue.status.waiting_process = 0;
    strcpy(queue.name,name);

    id = queue.id;
    return_code = NO_ERROR;
        
end