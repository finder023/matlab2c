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

    sem_ptr = sem_alloc();
    semaphore_id = sem_ptr.sem_id;
    sem_ptr.sem_status.current_value = current_value;
    sem_ptr.sem_status.max_value = max_value;
    sem_ptr.sem_status.waiting_process = 0;

    
    sem_record{sem_ptr.sem_id, 1} = sem_ptr;
    sem_num = sem_num + 1;
    return_code = NO_ERROR;

    return;

end
