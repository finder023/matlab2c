function  [semaphore_id_ptr,return_code_ptr] = create_semphore( semaphore_name,current_value,max_value,queuing_discipline )

    global sem_record;

    if sem_num >= MAX_NUMBER_OF_SEMAPHORES
        return_code_ptr = INVALID_CONFIG;
        return;
    end

    sem = get_sem_by_name(semaphore_name);
    if sem != NULL
        return_code_ptr = INVALID_PARAM;
        return;
    end

    if (current_value > MAX_SEMPHORE_VALUE)
        return_code_ptr = INVALID_PARAM;
        return;
    end

    if queuing_discipline != FIFO && queuing_discipline != PRIORITY
        return_code_ptr = INVALID_PARAM;
        return;
    end

    sem_ptr = [];
    sem_init(sem_ptr);
    semaphore_id_ptr = sem_id_generator();
    sem_ptr.sem_id = semaphore_id_ptr;
    sem_ptr.sem_status.current_value = current_value;
    sem_ptr.sem_status.max_value = max_value;
    sem_ptr.sem_status.waiting_process = 0;

    
    sem_record[sem_ptr.sem_id] = sem_ptr;  

    return_code_ptr = NO_ERROR;

end
