function [proc] = find_proc_name(name)
    global ProcessSet;
    for p = ProcessSet
        if p.status.attributes.name == name
            proc = p;
            return;
        end
    end
    proc = [];
end