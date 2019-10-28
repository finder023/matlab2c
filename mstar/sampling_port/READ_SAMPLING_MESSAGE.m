function [len, validity, return_code] = READ_SAMPLING_MESSAGE(sampling_port_id, msg_addr)
    sample = get_sample_by_id(sampling_port_id);
    if sample == []
        return_code = INVALID_PARAM;
        return;
    end

    if sample.length == 0
        len = 0;
        validity = INVALID;
        return_code = NO_ACTION;
    else
        memcpy(msg_addr, sample.buff, sample.length);
        len = sample.length;
        if sample.status.last_msg_validity == VALID
            validity = VALID;
        else
            validity = INVALID;
        end
        return_code = NO_ERROR;
    end

    if ticks - sample.last_time_stamp > sample.status.refresh_period
        sample.status.last_msg_validity = INVALID;
    else
        sample.status.last_msg_validity = VALID;
    end
    return_code = NO_ERROR;
end