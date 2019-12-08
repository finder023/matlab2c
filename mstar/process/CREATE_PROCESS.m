function [pid, return_code] = CREATE_PROCESS(attr)
    global current;
    global INVALID_CONFIG;
    global NO_ACTION;
    global MAX_STACK_SIZE;
    global INVALID_PARAM;
    global MAX_PRIORITY_VALUE;
    global MAX_PROC_PERIOD;
    global MAX_TIME_CAPA;
    global NORMAL;
    global INVALID_MODE;
    global DORMANT;
    global NO_ERROR;
    
    pid = -1;
    part = current.part;
    if valid_nr_proc() == 0
        return_code = INVALID_CONFIG;
        return;
    end

    if ~isequal(find_proc_name(attr.name), [])
        return_code = NO_ACTION;
        return;
    end

    if attr.stack_size > MAX_STACK_SIZE
        return_code = INVALID_PARAM;
        return;
    end

    if attr.base_priority > MAX_PRIORITY_VALUE
        return_code = INVALID_PARAM;
        return;
    end

    if attr.period > MAX_PROC_PERIOD
        return_code = INVALID_PARAM;
        return;
    end

    if attr.time_capacity > MAX_TIME_CAPA
        return_code = INVALID_PARAM;
        return;
    end

    if part.status.operating_mode == NORMAL
        return_code = INVALID_MODE;
        return;
    end

    proc = alloc_proc();

    if isequal(proc, [])
        return_code = INVALID_CONFIG;
        return;
    end

    proc.status.attributes = attr;
    proc.part = current.part;

    if setup_ustack(proc) ~= 0
        return_code = INVALID_CONFIG;
        return;
    end

    if setup_kstack(proc) ~= 0
        return_code = INVALID_CONFIG;
        return;
    end

    init_proc_context(proc);
    set_mm(proc);
    proc.status.process_state = DORMANT;
    pid = proc.pid;
    set_proc_link(proc);
    return_code = NO_ERROR;
    return;
end