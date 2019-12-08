#ifndef __L_BUFFER_H
#define __L_BUFFER_H

void do_create_buffer( buffer_name_t buffer_name, message_size_t max_message_size, message_range_t max_nb_message, queuing_discipline_t queuing_discipline, buffer_id_t* buffer_id, return_code_t* return_code);

void do_get_buffer_id( buffer_name_t buffer_name, buffer_id_t* buffer_id, return_code_t* return_code);

void do_get_buffer_status( buffer_id_t buffer_id, buffer_status_t* buffer_status, return_code_t* return_code);

void do_receive_buffer( buffer_id_t buffer_id, system_time_t time_out, message_addr_t message_addr, message_size_t* len, return_code_t* return_code);

void do_send_buffer( buffer_id_t buffer_id, message_addr_t message_addr, message_size_t len, system_time_t time_out, return_code_t* return_code);


#endif
