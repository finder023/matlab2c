function [sampling_port_id, return_code] = GET_SAMPLING_PORT_ID(name)
    sample = get_sample_by_name(name);
    if sample == []
        return_code = INVALID_CONFIG;
        return;
    end

    sampling_port_id = sample.id;
    return_code = NO_ERROR;
end