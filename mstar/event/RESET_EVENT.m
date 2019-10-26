function [return_code] = RESET_EVENT(event_id)
    event = get_event_by_id(event_id);
    if event == []
        return_code = INVALID_PARAM;
        return;
    end
    
    event.status.event_state = DOWN;
    return_code = NO_ERROR;
end