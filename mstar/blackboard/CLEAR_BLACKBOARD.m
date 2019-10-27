function [return_code] = CLEAR_BLACKBOARD(blackboard_id)
    bboard = get_blackboard_by_id(blackboard_id);
    if bboard == []
        return_code = INVALID_PARAM;
        return;
    end
    
    bboard.status.empty_indicator = EMPTY;
    return_code = NO_ERROR;
end