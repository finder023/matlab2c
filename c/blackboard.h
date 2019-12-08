#ifndef __L_BLACKBOARD_H
#define __L_BLACKBOARD_H

void do_clear_blackboard( blackboard_id_t blackboard_id, return_code_t* return_code);

void do_create_blackboard( blackboard_name_t blackboard_name, message_size_t max_message_size, blackboard_id_t* blackboard_id, return_code_t* return_code);

void do_display_blackboard( blackboard_id_t blackboard_id, message_addr_t message_addr, message_size_t len, return_code_t* return_code);

void do_get_blackboard_id( blackboard_name_t blackboard_name, blackboard_id_t* blackboard_id, return_code_t* return_code);

void do_get_blackboard_status( blackboard_id_t blackboard_id, blackboard_status_t* blackboard_status, return_code_t* return_code);

void do_read_blackboard( blackboard_id_t blackboard_id, system_time_t time_out, message_addr_t message_addr, message_size_t* len, return_code_t* return_code);


#endif
