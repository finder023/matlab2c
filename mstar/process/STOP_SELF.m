function  STOP_SELF()
    global current;

    proc = current;
    set_proc_dormant(proc);
    schedule();
    update_proc(current);
end