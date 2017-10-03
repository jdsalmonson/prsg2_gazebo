#! /bin/bash

# Author: Jay Salmonson <jdsalmonson@gmail.com>
#
# Please remove the "Author" lines above and replace them
# with your own name if you copy and modify this script.

# PATH should only include /usr/* if it runs after the mountnfs.sh script
HOSTNAME=`/bin/hostname`
# PATH=/usr/local/bin:$PATH
# PYTHONPATH=/usr/local/lib/python2.7/site-packages:/usr/local/lib/python:$PYTHONPATH
# NAME=roscore
# DAEMON=/opt/ros/kinetic/bin/$NAME
# DAEMONUSER=mcp
# ROSCORE_LOG=/media/LOG/roscore.log
# ROSCORE_ERR=/media/LOG/roscore.err
export ROS_MASTER_URI=http://$HOSTNAME:11311
export ROS_IP=`hostname -I | cut -d' ' -f1`
# PIDDIR=/var/run/roscore
# PIDFILE=$PIDDIR/$NAME.pid
#. /opt/ros/kinetic/setup.sh
. $HOME/catkin_ws/devel/setup.bash
# date >> $ROSCORE_LOG
# date >> $ROSCORE_ERR
# echo $PATH >> $ROSCORE_LOG
# echo $PYTHONPATH >> $ROSCORE_LOG
# DESC="ROS core process"
# DAEMON_ARGS=""
# SCRIPTNAME=/etc/init.d/$NAME

# last line of /etc/sudoers removes need for password
#sudo modprobe --first-time i2c-dev

roslaunch prsg2_gazebo prsg2.launch
#roslaunch prsg2_gazebo prsg2_jointed_wheels.launch record_sensors:=false

