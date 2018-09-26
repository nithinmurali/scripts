#!/bin/bash

# script to startAUV IITB vision module

#echo $1
if [ "$1"  = "kill" ]; then
    echo "killing all"
    pkill -f load_video
    pkill -f vision
    pkill -f roscore
    exit 0
fi

if [ !`rostopic list 2> /dev/null` ]; then
    roscore &> /dev/null &
    sleep 3
else
    echo "ros already running"
fi

rosrun auv_vision vision &
sleep 3

rosrun auv_utils load_video /bottom_camera/image_raw ~/dev/auv/data/AUV-IITB_Vision_TestVideo_Database/pool_IITB/marker_task_2013.avi 15 bottom_camera 

