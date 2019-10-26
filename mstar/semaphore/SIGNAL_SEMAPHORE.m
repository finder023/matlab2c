function [return_code] = SIGNAL_SEMAPHORE(semaphore_id)
    sem = get_sem_by_id(semaphore_id);
    if sem == []
        return_code = INVALID_PARAM;
        return;
    end

    if sem.sem_status.current_value == sem.sem_status.max_value
        return_code = NO_ACTION;
        return;
    end

    if sem.sem_status.waiting_processes == 0
        sem.sem_status.current_value = sem.sem_status.current_value + 1;
        return_code = NO_ERROR;
    else
        proc = select_waiting_proc(sem);
        if test_wt_flag(proc, WT_TIMER) ~= 0
            stop_timer(proc);
        end
        clear_wt_flag(proc, WT_KSEM);
        if test_wt_flag(proc, WT_SUSPEND) == 0
            wakeup_proc(proc);
            if PREEMPTION ~= 0
                schedule();
            end
        end
        return_code = NO_ERROR;
    end

end