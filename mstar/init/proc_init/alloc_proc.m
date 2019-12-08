function [proc] = alloc_proc()
    proc = [];
    global ProcessSet;
    proc.status = new_proc_status();
    proc.timer = [];
    proc.part = [];
    proc.pid = length(ProcessSet);
    proc.wait_state = [];
    proc.time_slice = 0;
    return;
end