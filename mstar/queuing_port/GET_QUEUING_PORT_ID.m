function [id, return_code] = GET_QUEUING_PORT_ID(name)
    queue = get_queue_by_name(name);
    if queue == []
        return_code = INVALID_CONFIG;
        return;
    end
    id = queue.id;
    return_code = NO_ERROR;
end