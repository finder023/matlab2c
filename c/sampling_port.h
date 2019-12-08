#ifndef __L_SAMPLING_PORT_H
#define __L_SAMPLING_PORT_H

void do_create_sampling_port( sampling_port_name_t name, message_size_t max_msg_size, port_direction_t port_direction, system_time_t refresh_period, sampling_port_id_t* sampling_port_id, return_code_t* return_code);

void do_get_sampling_port_id( sampling_port_name_t name, sampling_port_id_t* sampling_port_id, return_code_t* return_code);

void do_get_sampling_port_status( sampling_port_id_t sampling_port_id, sampling_port_status_t* sampling_port_status, return_code_t* return_code);

void do_read_sampling_message( sampling_port_id_t sampling_port_id, message_addr_t msg_addr, message_size_t* len, validity_t* validity, return_code_t* return_code);

void do_write_sampling_message( sampling_port_id_t sampling_port_id, message_addr_t msg_addr, message_size_t len, return_code_t* return_code);


#endif
