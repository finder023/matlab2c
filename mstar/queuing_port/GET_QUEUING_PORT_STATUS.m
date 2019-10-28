function [status, return_code] = GET_QUEUING_PORT_STATUS(id)
    queue = get_queue_by_id(id);
    if queue == []
        return_code = INVALID_CONFIG;
        return;
    end
    status = queue.status;
    return_code = NO_ERROR;
end