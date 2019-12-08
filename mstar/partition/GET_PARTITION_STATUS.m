function [status, return_code] = GET_PARTITION_STATUS()
    global current;
    global NO_ERROR;
    part = current.part;
    status = part.status;
    return_code = NO_ERROR;
end