function [blackboard_status, return_code] = GET_BLACKBOARD_STATUS(blackboard_id)
    bboard = get_blackboard_by_id(blackboard_id); 
    if bboard == []
        return_code = INVALID_PARAM;
        return;
    end

    blackboard_status = bboard.status;
    return_code = NO_ERROR;
end