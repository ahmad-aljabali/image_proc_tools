# this is intended for use with ros "stereo_image_proc"
#!/usr/bin/env python
import cv2
import rospy

from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError
from stereo_msgs.msg import DisparityImage
#define or import Q (reprojection matrix for the stereo camera) 


def process():
    global color_availability, hsv
    color_availability = False

    cv2.imshow('depth', depth)

    cv2.imshow('color', color)
    cv2.waitKey(1)


def depthCB(data):
    global depth
    disp_real = bridge.imgmsg_to_cv2(data.image, desired_encoding="passthrough")
    depth = cv2.reprojectImageTo3D(disp_real, Q, handleMissingValues=True)
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

rospy.Subscriber("/stereo/disparity", DisparityImage, depthCB)
rospy.Subscriber("/stereo/left/image_rect_color", Image, colorCB)


rospy.spin()
