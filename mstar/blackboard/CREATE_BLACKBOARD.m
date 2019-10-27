function [blackboard_id, return_code] = CREATE_BLACKBOARD(blackboard_name, max_message_size)
    part = current.part;
    if part.blackboard_num >= MAX_NUMBER_OF_BLACKBOARDS
        return_code = INVALID_CONFIG;
        return;
    end

    blackboard = get_blackboard_by_name(blackboard_name);
    if blackboard ~= []
        return_code = NO_ACTION;
        return;
    end

    if max_message_size <= 0
        return_code = INVALID_PARAM;
        return;
    end

    if part.status.operating_mode == NORMAL
        return_code = INVALID_MODE;
        return;
    end

    blackboard = alloc_blackboard(max_message_size);
    if blackboard == []
        return_code = INVALID_CONFIG;
        return;
    end

    blackboard.status.max_message_size = max_message_size;
    blackboard.status.waiting_processes = 0;
    strcpy(blackboard.name, blackboard_name);
    add_blackboard(part, blackboard); 
    blackboard_id = blackboard.id;
    return_code = NO_ERROR;
end