#!usr/bin/env/python3

if __name__ == '__main__':

	import rospy, rostopic, shutil
	from std_msgs.msg import Float32

	path = "/home/vikramha/Desktop/Kumar_Lab/field_exp_2021-06-30-00-45-30.bag"
	stat = shutil.disk_usage(path)
	free = round( stat[2]/1000000000,2)

	rospy.init_node('stats_space')
	pub = rospy.Publisher('/stats/space_topic',Float32, queue_size=10)

	rate = rospy.Rate(2)


	while not rospy.is_shutdown():
		msg = Float32()
		msg.data= free
		pub.publish(msg)
		rate.sleep()

