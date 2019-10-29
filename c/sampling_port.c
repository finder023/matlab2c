void do_create_sampling_port( sampling_port_name_t name, message_size_t max_msg_size, port_direction_t port_direction, system_time_t refresh_period, sampling_port_id_t* sampling_port_id, return_code_t* return_code) {

    if ( nr_sampling_port >= MAX_NUMBER_OF_SAMPLING_PORTS ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    sampling_port_t* sample = get_sample_by_name(name);
    partition_t* part = current->part;
    if ( max_msg_size <= 0 ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    if ( port_direction != SOURCE && port_direction != DESTINATION ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    if ( refresh_period >= MAX_TIME_OUT ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    if ( part->status.operating_mode == NORMAL ) {
        *return_code = INVALID_MODE;
        return;
    }
    sample = alloc_sampling_port(max_msg_size);
    if ( sample == NULL ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    sample->status.max_message_size = max_msg_size;
    sample->status.port_direction = port_direction;
    sample->status.refresh_period = refresh_period;
    strcpy(sample->name, name);
    *return_code = NO_ERROR;
}

void do_get_sampling_port_id( sampling_port_name_t name, sampling_port_id_t* sampling_port_id, return_code_t* return_code) {

    sampling_port_t* sample = get_sample_by_name(name);
    if ( sample == NULL ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    *sampling_port_id = sample->id;
    *return_code = NO_ERROR;
}

void do_read_sampling_message( sampling_port_id_t sampling_port_id, message_addr_t msg_addr, message_size_t* len, validity_t* validity, return_code_t* return_code) {

    sampling_port_t* sample = get_sample_by_id(sampling_port_id);
    if ( sample == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( sample->length == 0 ) {
        *len = 0;
        *validity = INVALID;
        *return_code = NO_ACTION;
    }
    else {
        memcpy(msg_addr, sample->buff, sample->length);
        *len = sample->length;
        if ( sample->status.last_msg_validity == VALID ) {
            *validity = VALID;
        }
        else {
            *validity = INVALID;
        }
        *return_code = NO_ERROR;
    }
    if ( ticks - sample->last_time_stamp > sample->status.refresh_period ) {
        sample->status.last_msg_validity = INVALID;
    }
    else {
        sample->status.last_msg_validity = VALID;
    }
    *return_code = NO_ERROR;
}

void do_write_sampling_message( sampling_port_id_t sampling_port_id, message_addr_t msg_addr, message_size_t len, return_code_t* return_code) {

    sampling_port_t* sample = get_sample_by_id(sampling_port_id);
    if ( sample == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    if ( len > sample->status.max_message_size ) {
        *return_code = INVALID_CONFIG;
        return;
    }
    if ( len <= 0 ) {
        *return_code = INVALID_PARAM;
        return;
    }
    memcpy(sample->buff, msg_addr, len);
    sample->length = len;
    sample->last_time_stamp = ticks;
    *return_code = NO_ERROR;
}

void do_get_sampling_port_status( sampling_port_id_t sampling_port_id, sampling_port_status_t* sampling_port_status, return_code_t* return_code) {

    sampling_port_t* sample = get_sample_by_id(sampling_port_id);
    if ( sample == NULL ) {
        *return_code = INVALID_PARAM;
        return;
    }
    *sampling_port_status = sample->status;
    *return_code = NO_ERROR;
}

