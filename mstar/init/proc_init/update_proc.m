function [] = update_proc(proc)
    global ProcessSet;

    for p = ProcessSet
        if p.pid == proc.pid
            ProcessSet(p.pid+1) = proc;
            break;
        end
    end
end