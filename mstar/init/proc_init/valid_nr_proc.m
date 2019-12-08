function [res] =  valid_nr_proc()
    global ProcessSet;
    global MAX_NUMBER_OF_PROCESSES;
    res = 1;
    if length(ProcessSet) >= MAX_NUMBER_OF_PROCESSES
        res = 0;
    end
end