function [process_id, return_code] = GET_MY_ID()
    global current;
    global NO_ERROR;

    process_id = current.pid;
    return_code = NO_ERROR; 
end