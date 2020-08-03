#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
import numpy as np

x = 0
y = 0
z = 0
yaw = 0

def pose_callback(pose_msg):

    global x, y, z, yaw
    x = pose_msg.x
    y = pose_msg.y
    yaw = pose_msg.theta

def move(speed, d, is_forward):
    vel = Twist()

    x0 = x
    y0 = y
    if is_forward:
    	vel.linear.x = speed
    else:
	vel.linear.x = -abs(speed)
    dist_moved = 0.0
    loop_rate = rospy.Rate(10)

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    while True:

        pub.publish(vel)
        loop_rate.sleep()

        dist_moved = dist_moved + abs(0.5 * math.sqrt((x - x0)**2 + (y - y0)**2))


        if dist_moved > d:

            break

    vel.linear.x = 0
    pub.publish(velocity_message)

def rotate(speed,angle,clockwise):
        angular_speed = speed*2*np.pi/360
        relative_angle = angle*2*np.pi/360
	global yaw
	vel_msg = Twist() 
    	vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0

	theta0=yaw
	if clockwise:
        	vel_msg.angular.z = -abs(angular_speed)
        else:
        	vel_msg.angular.z = abs(angular_speed)
	rate=rospy.Rate(10)
	cmd_vel_topic='/turtle1/cmd_vel'
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    # Setting the current time for distance calculation
        t0 = rospy.Time.now().to_sec()
        current_angle = 0.0

        while True:

		pub.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		current_angle = angular_speed*(t1-t0)
		rate.sleep()
		if (current_angle>relative_angle):

			break


        vel_msg.angular.z = 0
        pub.publish(vel_msg)
	

def main():
        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        cmd_vel_topic = '/turtle1/cmd_vel'
        pub = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        position_topic = '/turtle1/pose'
        sub = rospy.Subscriber(position_topic, Pose, pose_callback)

        time.sleep(2)
	rotate(20,60,0)
        move(1.0, 15.0,1)
	rotate(30,120,1)
	move(1.0,15.0,1)
	move(1.0,3.0,0)
	rotate(20,120,1)
	move(1.0,5.0,1)
        time.sleep(2)

        rospy.spin()
if __name__ == '__main__':
    try:
    	main()
    except rospy.ROSInterruptException:
    	pass