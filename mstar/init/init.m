% global
global NO_ERROR;
NO_ERROR = 0;

global NO_ACTION;
NO_ACTION = 1;

global NOT_AVAILABLE;
NOT_AVAILABLE = 2;

global INVALID_PARAM;
INVALID_PARAM = 3;

global INVALID_CONFIG;
INVALID_CONFIG = 4;

global INVALID_MODE;
INVALID_MODE = 5;

global TIMED_OUT;
TIMED_OUT = 6;

global MAX_TIMED_OUT;
MAX_TIMED_OUT = 1000;

global INFINITE_TIME_VALUE
INFINITE_TIME_VALUE = -1;

% partition
global NORMAL;
NORMAL = 1;

global IDLE;
IDLE = 0;

global WARM_START;
WARM_START = 2;

global COLD_START;
COLD_START = 3;


% process
global MAX_NUMBER_OF_PROCESSES;
MAX_NUMBER_OF_PROCESSES = 128;

global MAX_STACK_SIZE;
MAX_STACK_SIZE = 4096 * 100;

global MAX_PRIORITY_VALUE;
MAX_PRIORITY_VALUE = 128;

global MAX_PROC_PERIOD;
MAX_PROC_PERIOD = 1000;

global MAX_TIME_CAPA;
MAX_TIME_CAPA = 1000;


global DORMANT;
DORMANT = 0;

global READY;
READY = 1;

global WAITING;
WAITING = 2;

global RUNNING;
RUNNING = 3;

global ProcessSet;
ProcessSet = [];

global ReadyProcessSet;
ReadyProcessSet = [];

global PartitionSet;
PartitionSet = [];

global WT_SUSPEND;
WT_SUSPEND = 1;

global WT_TIMER;
WT_TIMER = 2;


global PREEMPTION
PREEMPTION = 1;

global current;
current = alloc_proc();
current.status.attributes.name = "init";
current.status.process_state = RUNNING;
current.part = new_partition();
 
current.part.status.operating_mode = COLD_START;
%PartitionSet = [PartitionSet, current.part];
ProcessSet = [ProcessSet, current];

