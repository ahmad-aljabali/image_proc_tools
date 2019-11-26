#!/usr/bin/env python
import cv2
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image, CameraInfo

cam_name = 'stereo'

def process():
    global color_availability,hsv
    # reset the flag
    color_availability = False
    hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

    # start processing


    # end processing

    cv2.imshow('world_pts', world_pts)
    cv2.imshow('color', color)
    k = cv2.waitKey(1)
    if k==ord('q'):
        pass


def world_ptsCB(data):
    global world_pts
    world_pts = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
    # check flag to insure both frame & world_pts are available pefore processing
    if color_availability:
        process()


def colorCB(data):
    global color, color_availability
    color = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
    # set flag
    color_availability = True



global bridge, world_pts, color, color_availability
bridge = CvBridge()
color_availability = False
world_pts = None
color = None
hsv = None

# init ros node & subscribers
rospy.init_node(cam_name + "_processing")
rospy.Subscriber("/" + cam_name + "/world_pts", Image, world_ptsCB)
rospy.Subscriber("/" + cam_name + "/left/image_rect_color", Image, colorCB)


rospy.spin()
