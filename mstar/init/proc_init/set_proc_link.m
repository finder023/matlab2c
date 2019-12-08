function [] = set_proc_link(proc)
    global ProcessSet;
    ProcessSet = [ProcessSet, proc];
    return;
end