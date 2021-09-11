import rosbag, rospy, rostopic
from std_msgs.msg import Bool,String,Int32
from sensor_msgs.msg import Imu
import message_filters

def callback_record_bag(msg ):
	rospy.loginfo('msg recieved')
	rospy.loginfo(msg)
	#print(type(msg))
	#extract = msg[0]
	#print(type(extract))
	#if msg==True:
	rospy.loginfo('Entered Loop')
	bag = rosbag.Bag('testwebui6.bag','w')
	print(Imu)

	s = String()
	s.data = 'foo'

	i = Int32()
	i.data = 42

	bag.write('/ovc/imu', Imu)
	bag.write('numbers', i)


if __name__ == '__main__':
	rospy.init_node('record_bag')

	sub1 = rospy.Subscriber('/bag/record', Bool, callback_record_bag)
	imu_sub = message_filters.Subscriber('/ovc/imu', Imu)
	vectornav_sub = message_filters.Subscriber('/ovc/vectornav', msg.sensor_msg.Imu)

	ts = message_filters.TimeSynchronizer([imu_sub, vectornav_sub], 10)
	ts.registerCallback(callback_record_bag)

	rospy.spin()






