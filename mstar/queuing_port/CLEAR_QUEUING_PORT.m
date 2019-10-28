function [return_code] = CLEAR_QUEUING_PORT(id)
    queue = get_queue_by_id(id);
    if queue == []
        return_code = INVALID_PARAM;
        return;
    end
    
    if queue.status.port_direction ~= DESTINATION
        return_code = INVALID_MODE;
        return;
    end

    clear_message_set(queue);
    queue.status.nb_message = 0;
    return_code = NO_ERROR;
end