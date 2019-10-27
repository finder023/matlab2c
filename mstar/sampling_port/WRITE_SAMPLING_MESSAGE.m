function [return_code] = WRITE_SAMPLING_MESSAGE(sampling_port_id, msg_addr, len)
    sample = get_sample_by_id(sampling_port_id);
    if sample == []
        return_code = INVALID_PARAM;
        return;
    end
    
    if len > sample.status.max_message_size
        return_code = INVALID_CONFIG;
        return;
    end

    if len <= 0
        return_code = INVALID_PARAM;
        return;
    end

    memcpy(sample.buff, msg_addr, len);
    sample.length = len;
    sample.last_time_stamp = ticks;
    return_code = NO_ERROR;
end