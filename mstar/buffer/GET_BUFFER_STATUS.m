function [buffer_status, return_code] = GET_BUFFER_STATUS(buffer_id)
    buffer = get_buffer_by_id(buffer_id);
    if buffer == []
        return_code = INVALID_PARAM;
        return;
    end
    buffer_status = buffer.status;
    return_code = NO_ERROR; 
end