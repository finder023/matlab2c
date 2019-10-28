function [event_id, return_code] = CREATE_EVENT(event_name)
    part = current.part;
    if part.event_num > MAX_NUMBER_OF_EVENTS
        return_code = INVALID_CONFIG;
        return;
    end
    
    event = get_event_by_name(event_name);
    if event ~= []
        return_code = NO_ACTION;
        return;
    end

    if part.status.operating_mode == NORMAL
        return_code = INVALID_MODE;
        return;
    end

    event = alloc_event();
    if event == []
        return_code = INVALID_CONFIG;
        return;
    end

    event_id = event.event_id;
    strcpy(event.event_name, event_name);
    add_event(part, event);
    return_code = NO_ERROR;
end