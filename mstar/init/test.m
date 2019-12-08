clear;
init;

attr = new_proc_attr();
attr.name = "proc1";
CREATE_PROCESS(attr);

attr.name = "proc2";
CREATE_PROCESS(attr);

SET_PARTITION_MODE(NORMAL);
