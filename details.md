# DETAILS

## special inline

对于一下具有固定套路的操作，比如，挂起当前进程，添加timer，可以在matlab中使用小函数来实现，在转换的过程中，不能照着转，需要转换成一个程序块。下面先做些总结，然后给出matlab函数名

## process

### set process waiting

- `set_proc_waiting(proc, flag, [])`

1. proc->state = WAITING
2. list_del_init(&proc->run_link)
3. set_wt_flag()

### add timer

- `add_timer(proc, time_out)`

1. alloc_timer
2. timer_init
3. set_wt_flag
4. add_timer
5. current->timer = timer;

### stop timer

- `stop_timer(proc)`

1. del_timer
2. clear_wt_flag
3. free_timer
4. proc->timer == NULL