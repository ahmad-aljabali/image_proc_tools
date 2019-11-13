#!/usr/bin/env python
# this script is intended for use with ros "stereo_image_proc"
import cv2
import rospy

from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError
from stereo_msgs.msg import DisparityImage


def process():
    global color_availability,hsv
    color_availability = False
    hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

    #put processing code from here


    #to here

    cv2.imshow('depth', depth)
    cv2.imshow('color', color)
    k = cv2.waitKey(1)
    if k==ord('q'):
        pass


def depthCB(data):
    global depth
    depth = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
    if color_availability:
        process()


def colorCB(data):
    global color_availability, color
    color = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
    color_availability = True



global bridge, depth, color, color_availability
bridge = CvBridge()
color_availability = False
depth = None
color = None
hsv = None

rospy.init_node("stereo_processing")

rospy.Subscriber("/stereo/world_pts", Image, depthCB)
rospy.Subscriber("/stereo/left/image_rect_color", Image, colorCB)


rospy.spin()
