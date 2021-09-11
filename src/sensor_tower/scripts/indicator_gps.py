#!/usr/bin/env python3
import roslib
roslib.load_manifest('ssnode')
import rospy
import roslib.message
import rosgraph
import rostopic
from rostopic import ROSTopicHz
from rosgraph.impl import graph

topic = '/ovc/imu'

def myhz(topic, window_size=-1, filter_expr=None):
	rospy.loginfo("check if roscore is up")

	while not rospy.is_shutdown():
       # thegraph();
       # ros::sleep(10);
            return
	rospy.init_node("myname", anonymous=True)
	rospy.loginfo("registered node name")
	rt = ROSTopicHz(window_size, filter_expr=filter_expr)

# have to subscribe with topic_type
	sub = rospy.Subscriber(topic, rospy.AnyMsg, rt.callback_hz)
	print("subscribed to [%s]"%topic)
	while not rospy.is_shutdown():
		rospy.loginfo(rt.times)

if __name__ == '__main__':
	try:
	#mygraph()
		myhz("sometopic")
	except rospy.ROSInterruptException: pass
