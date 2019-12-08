function [res] = test_wt_flag(proc, flag)
    global ProcessSet;
    res = ismember(flag, ProcessSet(proc.pid+1).wait_state);
    return;
end