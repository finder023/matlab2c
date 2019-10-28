function [event_status, return_code] = GET_EVENT_STATUS(event_id)
    event = get_event_by_id(event_id);
    if event == []
        return_code = INVALID_PARAM;
        return;
    end
    
    event_status = event.status;
    return_code = NO_ERROR;
end