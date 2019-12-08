function [status] = new_part_status()
    status.period = -1;
    status.duration = 0;
    status.identifier = 0;
    status.lock_level = 0;
    status.operating_mode = 0;
    status.start_condition = 0;
    return;
end