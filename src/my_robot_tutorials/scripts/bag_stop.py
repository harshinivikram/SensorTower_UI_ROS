import rosbag, rospy, rostopic
from std_msgs.msg import Bool,String,Int32

def callback_record_bag(msg):
	rospy.loginfo('msg recieved')
	rospy.loginfo(msg)

	bag.close
	msg.data = 0
	pub.Publish(msg)
	rospy.loginfo('executed bag close command')
if __name__ == '__main__':
	rospy.init_node('record_stop')

	sub = rospy.Subscriber('/bag/stop', Bool, callback_record_bag)

	pub = rospy.Publisher("/bag/record", Bool, queue_size=10)


	rospy.spin()






