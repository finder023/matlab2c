function [] = update_part(part)
    global PartitionSet;
    global ProcessSet;
    global current;
    
    index = 0;
    for p = PartitionSet
        index = index + 1;
        if p.status.identifier == part.status.identifier
            PartitionSet(index) = part;
            for proc = ProcessSet
                if proc.part.status.identifier == part.status.identifier
                    ProcessSet(proc.pid+1).part = part;
                end
            end
            break;
        end
    end
end