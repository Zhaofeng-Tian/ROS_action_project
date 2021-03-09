#! /usr/bin/env python
# BEGIN ALL
#! /usr/bin/env python
import rospy

import time
import actionlib
from casestudy2.msg import AveAction, AveGoal, AveResult, AveFeedback
from std_msgs.msg import Float32

trigger_value = 0.0

def feedback_cb(feedback):
    print('[Feedback] Random number is: %f'%(feedback.random_number))
    global trigger_value
    if feedback.average_minute != trigger_value:
        print('[Feedback] Average value of readings in the past one minute: %f'%(feedback.average_minute))
        pub.publish(feedback.average_minute)
        trigger_value = feedback.average_minute

rospy.init_node('Receiver')
pub = rospy.Publisher('counter', Float32, queue_size = 10)
client = actionlib.SimpleActionClient('reading', AveAction)
client.wait_for_server()

goal = AveGoal()
goal.threshold = 70.0

client.send_goal(goal, feedback_cb=feedback_cb)
client.wait_for_result()

print('[Result] State: %d'%(client.get_state()))
print('[Result] Status: %s'%(client.get_goal_status_text()))
print('[Result] The average value of last five consecutive readings: %f'%(client.get_result().average_five))
print('[Result] How many minutes have past: %d'%(client.get_result().circles))

