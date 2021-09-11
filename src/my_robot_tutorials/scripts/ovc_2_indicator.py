#!usr/bin/env/python3

if __name__ == '__main__':

	import rospy, rostopic
	from std_msgs.msg import Int32
	result = None
	TOPIC = '/ovc/right/image_raw'
	rospy.init_node('ovc_2_indicator')
	a=[]

	h = rostopic.ROSTopicHz(-1)
	s1 = rospy.Subscriber(TOPIC, rospy.AnyMsg, h.callback_hz, callback_args = TOPIC)
	rospy.sleep(1)
	a = h.get_hz(topic='/ovc/right/image_raw')
	b = a[0]
	print(b)
	if b>20:
		result=1
	else:
		result=0

	pub=rospy.Publisher('/ovc_2_status_topic', Int32, queue_size=10)

	rate = rospy.Rate(2)

	while not rospy.is_shutdown():
		msg = Int32()
		msg.data = result
		pub.publish(msg)
		rate.sleep()

