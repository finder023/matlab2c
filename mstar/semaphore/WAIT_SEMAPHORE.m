function [return_code] = WAIT_SEMAPHORE(semaphore_id, time_out)
    proc = current;
    sem = get_sem_by_id(semaphore_id);
    if sem == []
        return_code = INVALID_PARAM;
        return;
    end

    if time_out > MAX_TIME_OUT
        return_code = INVALID_PARAM;
        return;
    end

    if sem.sem_status.current_value > 0
        sem.sem_status.current_value = sem.sem_status.current_value - 1;
        return_code = NO_ERROR;
    elseif time_out == 0
        return_code = NOT_AVAILABLE;
        return;
    elseif PREEMPTION == 0
        return_code = INVALID_MODE;
        return;
    elseif time_out == INFINITE_TIME_VALUE
        set_proc_waiting(proc, WT_KSEM, sem);
        sem.sem_status.waiting_processes = sem.sem_status.waiting_processes + 1;
        schedule();
        sem.sem_status.waiting_processes = sem.sem_status.waiting_processes - 1;
        return_code = NO_ERROR;
        return;
    else
        add_timer(proc, time_out);
        set_proc_waiting(proc, WT_KSEM, sem);
        sem.sem_status.waiting_processes = sem.sem_status.waiting_processes + 1;
        schedule();
        sem.sem_status.waiting_processes = sem.sem_status.waiting_processes - 1;
        if proc.timer == []
            return_code = TIMED_OUT;
        else
            proc.timer = [];
            return_code = NO_ERROR;
        end
        return;
    end
end