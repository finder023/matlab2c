typedef void process_attr_

void do_create_process(
        process_attr_t *attr, 
        process_id_t *pid, 
        return_code_t *return_code){
    struct porc_struct *proc = alloc_proc();
    if (proc == NULL) {
        *return_code = INVALID_CONFIG;
        return;
    }
    proc->status.attributes = *attr;
    *pid = proc->pid;
    *return_code = NO_ERROR;
}