function [pid, return_code] = CREATE_PROCESS(attr)
    proc = alloc_proc();
    if proc == []
        return_code = INVALID_CONFIG;
        return;
    end
    proc.status.attributes = attr;
    pid = proc.pid;
    return_code = NO_ERROR;
end

