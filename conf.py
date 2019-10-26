#! /usr/bin/env python3

with_hcoding = False
mstar_dir = './mxx'
arinc_struct_conf_path = "./mxx/arinc_struct.json"

cvt_file = [
    'create_process',
    'set_priority',
    'suspend_self',
    'suspend',
    'resume',
    "stop_self",
    "stop",
    "start",
    "lock_preemption",
    "unlock_preemption",
    "get_my_id",
    "get_process_id",
    "get_process_status"
]

inline_func = [
    'set_proc_waiting',
    'set_proc_dormant',
    'add_timer',
    'stop_timer'
]