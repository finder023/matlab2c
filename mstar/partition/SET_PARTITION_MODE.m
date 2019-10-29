function [return_code] = SET_PARTITION_MODE(mode)
    proc = current;
    part = current.part;
    if mode >= 4
        return_code = INVALID_PARAM;
        return;
    end
    
    if part.status.operating_mode == NORMAL && mode == NORMAL
        return_code = NO_ACTION;
        return;
    end

    if part.status.operating_mode == COLD_START && mode == WARM_START
        return_code = INVALID_MODE;
        return;
    end

    part.status.operating_mode = mode;

    if mode == IDLE
        part.scheduling = 0;
    end

    if mode == NORMAL
        wakeup_waiting_proc(WT_PNORMAL, []);
        part.scheduling = 1;
        if part.first_run == 0
            part.first_run = 1;
        end
        part.status.lock_level = 0;
    end
    return_code = NO_ERROR;

end