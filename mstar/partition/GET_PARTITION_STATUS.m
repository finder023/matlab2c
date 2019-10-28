function [status, return_code] = GET_PARTITION_STATUS()
    part = current.part;
    status = part.status;
    return_code = NO_ERROR;
end