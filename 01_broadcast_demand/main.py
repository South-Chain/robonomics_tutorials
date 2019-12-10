#!/usr/bin/env python3
# Standart, System and Third Party
import sys
import yaml

# ROS
import rospy

# Robonomics
from robonomics_msgs.msg import Demand
from ethereum_common.msg import Address, UInt256
from ipfs_common.msg import Multihash

def create_demand(fields: dict) -> Demand:
    rospy.loginfo("Creating an demand...")

    demand = Demand()
    demand.model = Multihash(fields["model"]["multihash"])
    demand.objective = Multihash(fields["objective"]["multihash"])
    demand.token = Address(fields["token"]["address"])
    demand.cost = UInt256(fields["cost"]["uint256"])
    demand.lighthouse = Address(fields["lighthouse"]["address"])
    demand.validator = Address(fields["validator"]["address"])
    demand.validatorFee = UInt256(fields["validatorFee"]["uint256"])
    demand.deadline = UInt256(fields["deadline"]["uint256"])

    rospy.loginfo(demand)
    return demand

if __name__ == "__main__":
    rospy.init_node("broadcast_demand_node")

    # Register a publisher
    demand_pub = rospy.Publisher("/liability/infochan/eth/signing/demand", Demand, queue_size=128)

    # Default fields
    fields = {
            "model": {
                "multihash": "Qmbb8qcoEAbXWzFnzRf8NRbTNuJvWEXtZoH2L1LjnFtjbs"
                },
            "objective": {
                "multihash": "QmfC29P969647p1W8E19FwXcoL6TJV78U12zXMogo4jjvY"
                },
            "token": {
                "address": "xrt.5.robonomics.eth"
                },
            "cost": {
                "uint256": "0"
                },
            "validator": {
                "address": "0x0000000000000000000000000000000000000000"
                },
            "lighthouse": {
                "address": "airalab.lighthouse.5.robonomics.eth"
                },
            "validatorFee": {
                "uint256": "0"
                },
            "deadline": {
                "uint256": "9999999"
                }
            }

    # You can specify *.yaml file with the fields
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            fields = yaml.load(f, Loader=yaml.FullLoader)

    demand = create_demand(fields)      # put the fields into Demand structure

    rospy.sleep(2)                      # it's necessary to make sure ROS has registered the publisher
    demand_pub.publish(demand)
    rospy.loginfo("Published!")

    rospy.spin()                        # press Ctrl+C to exit

