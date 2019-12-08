function [proc] = set_proc_dormant(proc)
    global ProcessSet;
    global DORMANT;
    proc.status.process_state = DORMANT;
end