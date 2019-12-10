#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ROS
import rospy
from std_msgs.msg import String

# Robonomics communication
from robonomics_msgs.msg import Demand, Result
from ipfs_common.msg import Multihash
from ipfs_common.ipfs_rosbag import IpfsRosBag

class WorkerNode:

    def __init__(self):
        rospy.init_node("worker_node")
        rospy.loginfo("Launching worker node...")

        rospy.Subscriber('/liability/infochan/incoming/demand', Demand, self.on_incoming_demand)

        self.result_publish = rospy.Publisher('/liability/infochan/eth/signing/result', Result, queue_size=128)

        rospy.loginfo("The node is launched")

    def on_incoming_demand(self, demand: Demand):
        rospy.loginfo("Incoming demand: {}".format(demand))
        if demand.model.multihash == rospy.get_param("~model"):
            self.send_result(demand)
        else:
            rospy.loginfo("Demand is not for me")

    def pack_result(self) -> Multihash:
        topics = {
                "/data": [
                    String("Hello from my sensor!")
                    ]
                }

        bag = IpfsRosBag(messages=topics)
        return bag.multihash

    def send_result(self, demand: Demand):
        rospy.loginfo("Collecting data...")

        res = Result()
        res.liability = demand.sender
        res.result = self.pack_result()
        res.success = True

        rospy.loginfo("Result: {}".format(res))
        self.result_publish.publish(res)

    def spin(self):
        rospy.spin()

if __name__ == "__main__":
    WorkerNode().spin()

