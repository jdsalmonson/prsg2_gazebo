# testbag.py - script to open and plot contents of a ROS bag from the PRSG2
# Jay Salmonson
# 8/8/2017

import rosbag
import numpy as np

bagfile = "/tmp/prsg2-base-sensors_2017-10-02-22-01-25.bag"

bag = rosbag.Bag(bagfile)
#topic, msg, t = bag.read_messages(topics=['/arduino/sensor/battery_voltage']).next()

#: read bag data

odom_angz = []
odom_linx = []
tm_odom = []
for _, msg, t in bag.read_messages(topics=['/odom']):
    if msg.twist.twist.linear.z <> 0. or msg.twist.twist.linear.y <> 0.:
        print(msg.twist.twist)
    odom_angz.append(msg.twist.twist.angular.z)
    odom_linx.append(msg.twist.twist.linear.x)
    tm_odom.append(msg.header.stamp.to_nsec())

#get a time zero:
tm0 = tm_odom[0]

cmdvel_angz = []
cmdvel_linx = []
tm_cmdvel = []
for _, msg, msg_tm in bag.read_messages(topics=['/cmd_vel']):
    if msg.linear.z <> 0. or msg.linear.y <> 0.:
        print(msg.twist.twist)
    cmdvel_angz.append(msg.angular.z)
    cmdvel_linx.append(msg.linear.x)
    tm_cmdvel.append(msg_tm.to_nsec())

bag.close()

#: plot data
from pylab import plt

f, (ax4) = plt.subplots(1, sharex=True)
ax4.plot((np.array(tm_odom)-tm0)/1.e9, np.array(odom_linx), 'g-', label="odom.linear.x")
ax4.plot((np.array(tm_odom)-tm0)/1.e9, np.array(odom_angz), 'm-', label="odom.angular.z")
ax4.plot((np.array(tm_cmdvel)-tm0)/1.e9, np.array(cmdvel_linx), 'c-', label="cmd_vel.linear.x")
ax4.plot((np.array(tm_cmdvel)-tm0)/1.e9, np.array(cmdvel_angz), 'y-', label="cmd_vel.angular.z")
ax4.legend(frameon=True, framealpha=0.5)
ax4.set_xlabel("time [s]")
f.subplots_adjust(hspace=0)
plt.show()

