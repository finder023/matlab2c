function [buffer_id, return_code] = GET_BUFFER_ID(buffer_name)
    buffer = get_buffer_by_name(buffer_name);
    if buffer == []
        return_code = INVALID_CONFIG;
        return;
    end
    buffer_id = buffer.id;
    return_code = NO_ERROR; 
end