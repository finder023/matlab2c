function [process_id, return_code]= GET_PROCESS_ID(process_name)
    proc = find_proc_name(process_name);
    if proc == []
        return_code = INVALID_CONFIG;
        return;
    end
    
    process_id = proc.pid;
    return_code = NO_ERROR;
    return;
end