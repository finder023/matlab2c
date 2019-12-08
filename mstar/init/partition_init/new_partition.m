function [part] = new_partition()
    global PartitionSet;
    part.status = new_part_status();
    part.first_run = 0;
    part.scheduling = 0;
    PartitionSet = [PartitionSet, part];
    return;
end