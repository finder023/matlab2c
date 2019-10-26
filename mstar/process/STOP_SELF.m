function  STOP_SELF()
    proc = current;
    set_proc_dormant(proc);
    schedule();
end