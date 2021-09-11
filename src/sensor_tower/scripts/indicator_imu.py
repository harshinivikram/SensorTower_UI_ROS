#!usr/bin/env python3

if __name__ == '__main__':

	import rospy, rostopic
	
	from std_msgs.msg import String

	TOPIC = '/ovc/imu'
	rospy.init_node('indicator_imu_node')
	a=[]

	h = rostopic.ROSTopicHz(-1)
	#print(h)
	s1 = rospy.Subscriber(TOPIC, rospy.AnyMsg, h.callback_hz, callback_args=TOPIC)
	rospy.sleep(1)	
	a = h.get_hz(topic='/ovc/imu')
	b = a[0]
	print (a)
	print (b)

	pub = rospy.Publisher("/imu_status_topic", String, queue_size=10)

	rate = rospy.Rate(1)

	while not rospy.is_shutdown():
		msg = String
		msg.data = 'test'
		pub.publish(msg)
		rate.sleep()
	rospy.loginfo('imu_status_node_1 has stopped')
