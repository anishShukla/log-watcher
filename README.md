log-watcher
===========

log-watcher is python script to verify debug print/ message sequence in a continuously generated log file.
#Log - Watcher 1.0

This script I am using to verify my test cases on the basis of call flow.
In the logs we have agreed on protocol which clearly defines the sequence 
which we verify with this script and say if the test case has passed.

CONFIGURATION:-

In the file find these lines.
 
tests={
    'test1':{
        'callFlow':[
            "This is first line for test1",
            "This is second line for test1",
            "This is third line for test1"
        ]
    },
    'test2':{
        'callFlow':[
            "This is first line for test2",
            "This is second line for test2",
            "This is third line for test2"
        ]
    }
} 

So, 'tests' is a dictionary containing all the test cases as you can see. Just add the 'callFlow' 
in the sequence that is supposed to happen.

GLOBAL VARIABLES:-

'BREAK_TIME' : program will keep trying to read line from log file . If it does not find any update on file for 
few seconds defined by 'BREAK_TIME' it will halt the execution.

RUN:-
run the command with log file as argument.

$python log-watcher.py log.txt
