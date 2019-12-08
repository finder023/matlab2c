function [] = set_wt_flag(proc, flag)
    global ProcessSet;
    if ismember(flag, ProcessSet(proc.pid+1).wait_state)
        return
    end
    ProcessSet(proc.pid+1).wait_state = [ProcessSet(proc.pid+1).wait_state, flag];
    return;
end