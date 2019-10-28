converting sampling_port ...
	CREATE_SAMPLING_PORT -> 82.81 ms
	GET_SAMPLING_PORT_ID -> 4.09 ms
	READ_SAMPLING_MESSAGE -> 34.51 ms
	WRITE_SAMPLING_MESSAGE -> 7.74 ms
	GET_SAMPLING_PORT_STATUS -> 3.43 ms
converting buffer ...
	CREATE_BUFFER -> 17.09 ms
	GET_BUFFER_ID -> 3.23 ms
	RECEIVE_BUFFER -> 37.96 ms
	SEND_BUFFER -> 36.61 ms
	GET_BUFFER_STATUS -> 3.66 ms
converting event ...
	RESET_EVENT -> 4.65 ms
	WAIT_EVENT -> 13.25 ms
	GET_EVENT_STATUS -> 3.43 ms
	SET_EVENT -> 4.83 ms
	GET_EVENT_ID -> 3.01 ms
	CREATE_EVENT -> 8.49 ms
converting queuing_port ...
	CLEAR_QUEUING_PORT -> 6.43 ms
	GET_QUEUING_PORT_ID -> 3.00 ms
	CREATE_QUEUING_PORT -> 14.65 ms
	GET_QUEUING_PORT_STATUS -> 3.27 ms
	SEND_QUEUING_MESSAGE -> 27.42 ms
	RECEIVE_QUEUING_MESSAGE -> 27.68 ms
converting process ...
	RESUME -> 11.33 ms
	GET_PROCESS_STATUS -> 3.15 ms
	CREATE_PROCESS -> 28.54 ms
	STOP_SELF -> 1.45 ms
	LOCK_PREEMPTION -> 5.35 ms
	START -> 10.09 ms
	GET_MY_ID -> 1.64 ms
	SUSPEND_SELF -> 9.80 ms
	SUSPEND -> 8.79 ms
	STOP -> 5.30 ms
	SET_PRIORITY -> 6.16 ms
	GET_PROCESS_ID -> 3.52 ms
	UNLOCK_PREEMPTION -> 6.08 ms
converting partition ...
	GET_PARTITION_STATUS -> 1.90 ms
	SET_PARTITION_MODE -> 10.90 ms
converting semaphore ...
	GET_SEMAPHORE_ID -> 4.50 ms
	GET_SEMAPHORE_STATUS -> 8.54 ms
	SIGNAL_SEMAPHORE -> 12.52 ms
	WAIT_SEMAPHORE -> 16.10 ms
	CREATE_SEMAPHORE -> 13.89 ms
converting blackboard ...
	GET_BLACKBOARD_ID -> 4.30 ms
	CREATE_BLACKBOARD -> 10.95 ms
	DISPLAY_BLACKBOARD -> 10.22 ms
	READ_BLACKBOARD -> 17.80 ms
	CLEAR_BLACKBOARD -> 3.67 ms
	GET_BLACKBOARD_STATUS -> 3.24 ms


find . -name '*.m' | xargs cat | wc -l
1244

find . -name '*.c' | xargs cat | wc -l
1517