function [blackboard_id, return_code] = GET_BLACKBOARD_ID(blackboard_name)
    bboard = get_blackboard_by_name(blackboard_name); 
    if bboard == []
        return_code = INVALID_PARAM;
        return;
    end

    blackboard_id = bboard.id;
    return_code = NO_ERROR;
end