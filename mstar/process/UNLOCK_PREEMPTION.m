function [lock_level, return_code] = UNLOCK_PREEMPTION()
    global current;
    global NORMAL;
    global NO_ACTION;
    global NO_ERROR;
    
    part = current.part;
    if part.status.operating_mode ~= NORMAL || part.status.lock_level == 0
        return_code = NO_ACTION;
        return;
    end
    
    part.status.lock_level = part.status.lock_level - 1;
    if part.status.lock_level == 0
        lock_level = 0;
        schedule();
    end
    lock_level = part.status.lock_level;
    update_proc(proc);
    return_code = NO_ERROR;
end