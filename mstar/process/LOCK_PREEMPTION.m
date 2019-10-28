function [lock_level, return_code] = lock_preemption()
    part = current.part;
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
    return_code = NO_ERROR;
end