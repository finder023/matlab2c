function [] = stop_timer(proc)
    global ProcessSet;
    ProcessSet(proc.pid+1).timer = [];
    return;
end