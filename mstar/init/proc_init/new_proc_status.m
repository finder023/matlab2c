function [status] = new_proc_status()
    global DORMANT;
    status.attributes = new_proc_attr();
    status.process_state = DORMANT;
    status.current_priority = status.attributes.base_priority;
    status.deadline_time = 0;
end