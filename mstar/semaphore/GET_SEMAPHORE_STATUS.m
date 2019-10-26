function [semaphore_status, return_code] = GET_SEMAPHORE_STATUS(semaphore_id)
    sem = get_sem_by_id(semaphore_id);
    if sem == []
        return_code = INVALID_PARAM;
        return;
    end
    
    semaphore_status = sem.sem_status;
    return_code = NO_ERROR;
end