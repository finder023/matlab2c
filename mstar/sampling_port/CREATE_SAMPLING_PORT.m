function [sampling_port_id, return_code] = CREATE_SAMPLING_PORT(name, max_msg_size, port_direction, refresh_period)
    if nr_sampling_port >= MAX_NUMBER_OF_SAMPLING_PORT
        return_code = INVALID_CONFIG;
        return;
    end
    
    sample = get_sample_by_name(name);
    part = current.part;

    if max_msg_size <= 0
        return_code = INVALID_CONFIG;
        return;
    end

    if port_direction ~= SOURCE && port_direction ~= DISTINATION
        return_code = INVALID_CONFIG;
        return;
    end

    if refresh_period >= MAX_TIME_OUT
        return_code = INVALID_CONFIG;
        return;
    end

    if part.status.operating_mode == NORMAL
        return_code = INVALID_MODE;
        return;
    end

    sample = alloc_sampling_port(max_msg_size);
    if sample == []
        return_code = INVALID_CONFIG;
        return;
    end
    sample.status.max_message_size = max_msg_size;
    sample.status.port_direction = port_direction;
    sample.status.refresh_period = refresh_period;
    strcpy(sample.name, name);

    return_code = NO_ERROR;
end