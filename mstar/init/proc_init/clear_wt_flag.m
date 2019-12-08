function [] = clear_wt_flag(proc, flag)
    global ProcessSet;
    res = ProcessSet(proc.pid+1).wait_state ~= flag;
    ProcessSet(proc.pid+1).wait_state = ProcessSet(proc.pid+1).wait_state(res);
    return;
end