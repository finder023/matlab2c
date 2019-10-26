function [event_id, return_code] = GET_EVENT_ID(event_name)
    event = get_event_by_name(event_name);
    if event == []
        return_code = INVALID_CONFIG;
        return;
    end
    
    event_id = event.event_id;
    return_code = NO_ERROR;
end