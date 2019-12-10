#!/usr/bin/env python3
# Standart, System and Third Party
import sys
import yaml

# ROS
import rospy

# Robonomics
from robonomics_msgs.msg import Offer
from ethereum_common.msg import Address, UInt256
from ipfs_common.msg import Multihash

def create_offer(fields: dict) -> Offer:
    rospy.loginfo("Creating an offer...")

    offer = Offer()
    offer.model = Multihash(fields["model"]["multihash"])
    offer.objective = Multihash(fields["objective"]["multihash"])
    offer.token = Address(fields["token"]["address"])
    offer.cost = UInt256(fields["cost"]["uint256"])
    offer.lighthouse = Address(fields["lighthouse"]["address"])
    offer.validator = Address(fields["validator"]["address"])
    offer.lighthouseFee = UInt256(fields["lighthouseFee"]["uint256"])
    offer.deadline = UInt256(fields["deadline"]["uint256"])

    rospy.loginfo(offer)
    return offer

if __name__ == "__main__":
    rospy.init_node("broadcast_offer_node")

    # Register a publisher
    offer_pub = rospy.Publisher("/liability/infochan/eth/signing/offer", Offer, queue_size=128)

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
            "lighthouseFee": {
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

    offer = create_offer(fields)    # put the fields into Offer structure

    rospy.sleep(2)                  # it's necessary to make sure ROS has registered the publisher
    offer_pub.publish(offer)
    rospy.loginfo("Published!")

    rospy.spin()                    # press Ctrl+C to exit

