#! /usr/bin/env python

import rospy 
import math
from converter.msg import roll_yaw_pitch, quaternion
from math import atan2
import numpy as np

global euler
def rotation(msg):
	global x, y, z, w
	x = msg.x
	y = msg.y
	z = msg.z
	w = msg.w

	sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x**2 + y**2)
    roll = np.arctan2(sinr_cosp, cosr_cosp)

    sinp = 2 * (w * y - z * x)
    pitch = np.where(np.abs(sinp) >= 1,
                     np.sign(sinp) * np.pi / 2,
                     np.arcsin(sinp))

    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y**2 + z**2)
    yaw = np.arctan2(siny_cosp, cosy_cosp)

    euler = [roll, pitch, yaw]
    return euler

def main():
	rospy.init_node("my_converter")

	sub = rospy.Subscriber("topic1", quaternion, rotation)
	pub = rospy.Publisher("topic2", roll_yaw_pitch, queue_size = 2)

	r = rospy.Rate(1)
	msg_value = roll_yaw_pitch()
	while not rospy.is_shutdown():

		msg_value.roll = euler[0]
		msg_value.pitch = euler[1]
		msg_value.yaw = euler[2]

		pub.publish(msg)

		r.sleep()
