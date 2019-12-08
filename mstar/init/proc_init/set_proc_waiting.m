function [proc] = set_proc_waiting(proc, flag, resc)
    global WAITING;
    
    proc.status.process_state = WAITING;
    proc.wait_state = [proc.wait_state, flag];
end