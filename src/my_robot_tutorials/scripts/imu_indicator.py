#!usr/bin/env/python3


if __name__ == '__main__':


	import rospy, rostopic
	from std_msgs.msg import Float32,Bool,Int32
	result = None
	TOPIC = '/ovc/imu'
	rospy.init_node('imu_indicator')
	rospy.loginfo('imu status node started')
	a=[]

	h = rostopic.ROSTopicHz(-1)
	s1 = rospy.Subscriber(TOPIC, rospy.AnyMsg, h.callback_hz, callback_args= TOPIC)
	rospy.sleep(1)
	a = h.get_hz(topic='/ovc/imu')
	b = a[0]
	if b>50:
		result=1
	else:
		result=0
	#print (a)
	#print (b)
	#print (type(b))


	pub =rospy.Publisher('/imu_status_topic_1', Int32, queue_size=10)

	rate = rospy.Rate(2)

	while not rospy.is_shutdown():
		msg = Int32()
		msg.data = result
		pub.publish(msg)
		rate.sleep()
	rospy.loginfo('imu_status  node was stopped')


