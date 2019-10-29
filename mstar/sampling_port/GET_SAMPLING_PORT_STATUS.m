function [sampling_port_status, return_code] = GET_SAMPLING_PORT_STATUS(sampling_port_id)
    sample = get_sample_by_id(sampling_port_id);
    if sample == []
        return_code = INVALID_PARAM;
        return;
    end

    sampling_port_status = sample.status;
    return_code = NO_ERROR;
end