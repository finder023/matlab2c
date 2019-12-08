function [attr] = new_proc_attr()
    attr.period = -1;
    attr.time_capacity = 0;
    attr.entry_point = [];
    attr.stack_size = 0;
    attr.base_priority = 0;
    attr.deadline = 0;
    attr.name = "proc";
end