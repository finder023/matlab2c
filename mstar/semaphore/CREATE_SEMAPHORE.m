function [semaphore_id, return_code] = CREATE_SEMAPHORE(semaphore_name, current_value, max_value, queuing_discipline)
    part = current.part;
    if part.sem_num >= MAX_NUMBER_OF_SEMAPHORES
        return_code = INVALID_CONFIG;
        return;
    end

    sem = get_sem_by_name(semaphore_name);
    if sem ~= []
        return_code = NO_ACTION;
        return;
    end

    if current_value > MAX_SEMAPHORE_VALUE
        return_code = INVALID_PARAM;
        return;
    end

    if max_value > MAX_SEMAPHORE_VALUE
        return_code = INVALID_PARAM;
        return;
    end

    if queuing_discipline ~= FIFO && queuing_discipline ~= PRIORITY
        return_code = INVALID_PARAM;
        return;
    end

    sem = alloc_sem();
    if sem == []
        return_code = INVALID_CONFIG;
        return;
    end

    strcpy(sem.sem_name, semaphore_name);
    semaphore_id = sem.sem_id;
    sem.sem_status.current_value = current_value;
    sem.sem_status.max_value = max_value;
    sem.sem_status.waiting_processes = 0;

    add_sem(part, sem);

    return_code = NO_ERROR;

end