#ifndef __L_EVENT_H
#define __L_EVENT_H

void do_create_event( event_name_t event_name, event_id_t* event_id, return_code_t* return_code);

void do_get_event_id( event_name_t event_name, event_id_t* event_id, return_code_t* return_code);

void do_get_event_status( event_id_t event_id, event_status_t* event_status, return_code_t* return_code);

void do_reset_event( event_id_t event_id, return_code_t* return_code);

void do_set_event( event_id_t event_id, return_code_t* return_code);

void do_wait_event( event_id_t event_id, system_time_t time_out, return_code_t* return_code);


#endif
