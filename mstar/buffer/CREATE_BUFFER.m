function [buffer_id, return_code] = CREATE_BUFFER(buffer_name, max_message_size, max_nb_message, queuing_discipline)
    part = current.part;
    if part.buffer_num >= MAX_NUMBER_OF_BUFFERS
        return_code = INVALID_CONFIG;
        return;
    end

    buffer = get_buffer_by_name(buffer_name);
    if buffer ~= []
        return_code = NO_ACTION;
        return;
    end

    if max_message_size <= 0
        return_code = INVALID_CONFIG;
        return;
    end

    if max_nb_message > MAX_NUMBER_OF_MESSAGE
        return_code = INVALID_PARAM;
        return;
    end

    if queuing_discipline ~= FIFO && queuing_discipline ~= PRIORITY
        return_code = INVALID_PARAM;
        return;
    end

    if part.status.operating_mode == NORMAL
        return_code = INVALID_MODE;
        return;
    end
    buffer = alloc_buffer();
    if buffer == []
        return_code = INVALID_CONFIG;
        return;
    end

    buffer.discipline = queuing_discipline;
    strcpy(buffer.name, buffer_name);
    buffer.status.max_message_size = max_message_size;
    buffer.status.max_nb_message = max_nb_message;
    add_buffer(part, buffer);

    buffer_id = buffer.id;
    return_code = NO_ERROR;

end