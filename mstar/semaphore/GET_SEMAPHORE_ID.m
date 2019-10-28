function [semaphore_id, return_code] = GET_SEMAPHORE_ID(semaphore_name)
    sem = get_sem_by_name(semaphore_name);
    if sem == []
        return_code = INVALID_CONFIG;
        return;
    end
    
    semaphore_id = sem.sem_id;
    return_code = NO_ERROR;
end