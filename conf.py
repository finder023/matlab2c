#! /usr/bin/env python3

with_hcoding = False
mstar_dir = './mstar'
arinc_struct_conf_path = "./mstar/arinc_struct.json"

cvt_file = [
#    # process
#    'create_process',
#    'set_priority',
#    'suspend_self',
#    'suspend',
#    'resume',
#    "stop_self",
#    "stop",
#    "start",
#    "lock_preemption",
#    "unlock_preemption",
#    "get_my_id",
#    "get_process_id",
#    "get_process_status"
#
#    # partitioin
#    "get_partition_status",
#    "set_partition_mode"
#
#    # semaphore
#    "create_semaphore",
#    "wait_semaphore",
#    'signal_semaphore'
#    'get_semaphore_id',
#    'get_semaphore_status'
#
#    # event
#    'create_event',
#    "set_event",
#    "reset_event",
#    "wait_event",
#    "get_event_id",
#    "get_event_status"

#    # blackboard
#    'create_blackboard',
#    'display_blackboard',
#    'read_blackboard',
#    'clear_blackboard',
#    'get_blackboard_id',
#    'get_blackboard_status'
]

inline_func = [
    'set_proc_waiting',
    'set_proc_dormant',
    'add_timer',
    'stop_timer',
    "wakeup_waiting_proc",
    'add_sem',
    'select_waiting_proc',
    'add_event',
    'stop_all_timer'
]