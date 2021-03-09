#! /usr/bin/env python
# BEGIN ALL
#! /usr/bin/env python
import rospy

import time
import actionlib
import random
# BEGIN PART_1
from casestudy2.msg import AveAction, AveGoal, AveResult, AveFeedback
# END PART_1

def do_calculator(goal):
    start_time = time.time()
  
    result = AveResult()
    feedback = AveFeedback()
    result.average_five = 0
    result.circles = 0.0
    count = 0.0
    array = []
    
    while  result.average_five < goal.threshold:
        
        feedback.random_number = random.randint(0,100)
        array. append(feedback.random_number)
        count += 1
        if count % 5 == 0:
            result.average_five = sum(array[-5:]) / 5.0
        if count % 60 == 0:
            feedback.average_minute = sum(array[-60:]) / 60.0
     
        server.publish_feedback(feedback)
        time.sleep(0.995)

    if count < 60:
        feedback.average_minute = sum(array) / len(array)
    else:
        feedback.average_minute = sum(array[-60:]) / 60
    server.publish_feedback(feedback)
    # BEGIN PART_8
    result = AveResult()
    result.average_five = sum(array[-5:]) / 5
    result.circles = count / 60.0
    # server.set_succeeded(result, "Exit calculator because five consecutive readings is 60 or above")
    server.set_aborted(result, "Exit calculator because five consecutive readings is 60 or above")
    print (time.time() - start_time)

rospy.init_node('Sensor')
server = actionlib.SimpleActionServer('reading', AveAction, do_calculator, False)
server.start()
rospy.spin()
# END ALL
