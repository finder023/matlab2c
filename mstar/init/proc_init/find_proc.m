function [proc] = find_proc(pid)
    global ProcessSet;
    for p = ProcessSet
        if p.pid == pid
            proc = p;
            return;
        end
    end
    proc = [];
end