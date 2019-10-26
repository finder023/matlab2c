# DETAILS

## schedule 前后的资源处理

- 进程申请了资源，被挂起，由唤醒进程释放其资源和清除其标识，毕竟没法原子操作
- 数量统计，由同一个进程处理，谁改的数，谁再改回来

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

### set_proc_dormant

- `set_proc_dormant(proc)`
  
1. proc.status.process_state = DORMANT;
2. list_del_from run link
3. list_add_to dormant list

### wakeup waiting proc with flag waiting_state

- `wakeup_waiting_proc(flag)`

1. le = part->proc_set.next;
2. 循环查找flag
3. 这个比较烦，。。。

### add new semaphore to partition

- `add_sem(partition, sem)`
  
1. list_add
2. sem_num += 1

### select and del a proc from waiting_thread

- `select_waiting_proc(resources)`
  
1. save next list_elem
2. get proc by list_elem
3. list_del_init