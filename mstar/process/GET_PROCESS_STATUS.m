function [process_status, return_code] = GET_PROCESS_STATUS(process_id)
    global INVALID_PARAM;
    global NO_ERROR;

    proc = find_proc(process_id);
    if isequal(proc, [])
        return_code = INVALID_PARAM;
        return;
    end
    
    process_status = proc.status;
    return_code = NO_ERROR;
end