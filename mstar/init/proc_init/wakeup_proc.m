function [proc] = wakeup_proc(proc)
    global ProcessSet;
    global READY;
    
    proc.status.process_state = READY;
   
end