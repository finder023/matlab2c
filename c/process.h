#ifndef __L_PROCESS_H
#define __L_PROCESS_H

void do_create_process( process_attribute_t* attr, process_id_t* pid, return_code_t* return_code);

void do_get_my_id( process_id_t* process_id, return_code_t* return_code);

void do_get_process_id( process_name_t process_name, process_id_t* process_id, return_code_t* return_code);

void do_get_process_status( process_id_t process_id, process_status_t* process_status, return_code_t* return_code);

void do_lock_preemption( lock_level_t* lock_level, return_code_t* return_code);

void do_resume( process_id_t process_id, return_code_t* return_code);

void do_set_priority( process_id_t process_id, priority_t priority, return_code_t* return_code);

void do_start( process_id_t process_id, return_code_t* return_code);

void do_stop( process_id_t process_id, return_code_t* return_code);

void do_stop_self( );

void do_suspend( process_id_t process_id, return_code_t* return_code);

void do_suspend_self( system_time_t time_out, return_code_t* return_code);

void do_unlock_preemption( lock_level_t* lock_level, return_code_t* return_code);


#endif
