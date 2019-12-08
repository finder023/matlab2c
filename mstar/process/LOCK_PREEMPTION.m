function [lock_level, return_code] = LOCK_PREEMPTION()
    global current;
    global NORMAL;
    global NO_ACTION;
    global MAX_LOCK_LEVEL;
    global INVALID_CONFIG;
    global NO_ERROR;
    
    part = current.part;
    lock_level = -1;
    if part.status.operating_mode ~= NORMAL
        return_code = NO_ACTION;
        return;
    end
    
    if part.status.lock_level > MAX_LOCK_LEVEL
        return_code = INVALID_CONFIG;
        return;
    end

    part.status.lock_level = part.status.lock_level + 1;
    lock_level = part.status.lock_level;
    update_part(part);
    return_code = NO_ERROR;
end