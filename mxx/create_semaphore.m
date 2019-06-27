function  [semaphore_id,return_code] = create_semphore( semaphore_name,current_value,max_value,queuing_discipline )

    global sem_record;
    global sem_num;

    if sem_num >= MAX_NUMBER_OF_SEMAPHORES
        return_code = INVALID_CONFIG;
        return;
    end

    sem = get_sem_by_name(semaphore_name);
    if sem == [] 
        return_code = INVALID_PARAM;
        return;
    end

    if (current_value > MAX_SEMPHORE_VALUE)
        return_code = INVALID_PARAM;
        return;
    end

    if queuing_discipline ~= FIFO && queuing_discipline ~= PRIORITY
        return_code = INVALID_PARAM;
        return;
    end

    nsem = sem_alloc();
    semaphore_id = nsem.sem_id;
    nsem.sem_status.current_value = current_value;
    nsem.sem_status.max_value = max_value;
    nsem.sem_status.waiting_process = 0;
    
    sem_record{nsem.sem_id, 1} = nsem;
    sem_num = sem_num + 1;
    return_code = NO_ERROR;

    return;

end
