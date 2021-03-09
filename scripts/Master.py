#! /usr/bin/env python
# BEGIN ALL
#! /usr/bin/env python
import rospy
from std_msgs.msg import Float32

def callback(data):
    print ("receive the averge value of readings in the past one minute:", data.data)
rospy.init_node('Master')
sub = rospy.Subscriber('counter', Float32, callback)
rospy.spin()

