#!/usr/bin/env python3

import rospy

from  std_msgs.msg import String 

if __name__ == '__main__':
	rospy.init_node('Number_Publishing_Node')

	pub1 = rospy.Publisher('/number', String, queue_size = 20)

	rospy.loginfo('Number Publishing Node has started')

	rate = rospy.Rate(2)

	while not rospy.is_shutdown():

		i = 1
		while(i<=10):
			rospy.loginfo(i)
		i = i+ 1

		rate.sleep()

	rospy.loginfo('Number Publishing node has stopped')
