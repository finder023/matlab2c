#ifndef __L_SEMAPHORE_H
#define __L_SEMAPHORE_H

void do_create_semaphore( semaphore_name_t semaphore_name, semaphore_value_t current_value, semaphore_value_t max_value, queuing_discipline_t queuing_discipline, semaphore_id_t* semaphore_id, return_code_t* return_code);

void do_get_semaphore_id( semaphore_name_t semaphore_name, semaphore_id_t* semaphore_id, return_code_t* return_code);

void do_get_semaphore_status( semaphore_id_t semaphore_id, semaphore_status_t* semaphore_status, return_code_t* return_code);

void do_signal_semaphore( semaphore_id_t semaphore_id, return_code_t* return_code);

void do_wait_semaphore( semaphore_id_t semaphore_id, system_time_t time_out, return_code_t* return_code);


#endif
