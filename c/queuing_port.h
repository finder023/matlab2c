#ifndef __L_QUEUING_PORT_H
#define __L_QUEUING_PORT_H

void do_clear_queuing_port( queuing_port_id_t id, return_code_t* return_code);

void do_create_queuing_port( queuing_port_name_t name, message_size_t max_msg_size, message_range_t max_nb_msg, port_direction_t port_direction, queuing_discipline_t queuing_discipline, queuing_port_id_t* id, return_code_t* return_code);

void do_get_queuing_port_id( queuing_port_name_t name, queuing_port_id_t* id, return_code_t* return_code);

void do_get_queuing_port_status( queuing_port_id_t id, queuing_port_status_t* status, return_code_t* return_code);

void do_receive_queuing_message( queuing_port_id_t id, system_time_t time_out, message_addr_t message_addr, message_size_t* len, return_code_t* return_code);

void do_send_queuing_message( queuing_port_id_t id, message_addr_t msg_addr, message_size_t len, system_time_t time_out, return_code_t* return_code);


#endif
