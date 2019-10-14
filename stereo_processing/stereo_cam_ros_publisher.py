# this file is intended to be used with ROS stereo_image_proc
#!/usr/bin/env python
import cv2
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image, CameraInfo
#assuems a calibration result file in the format provided in this repository 
from stereo_calibration import *


rospy.init_node("stereo")
imgL_pub = rospy.Publisher("/stereo/left/image_raw",Image, queue_size=10)
imgR_pub = rospy.Publisher("/stereo/right/image_raw",Image, queue_size=10)
camL_pub = rospy.Publisher("/stereo/left/camera_info",CameraInfo, queue_size=10)
camR_pub = rospy.Publisher("/stereo/right/camera_info",CameraInfo, queue_size=10)


bridge = CvBridge()

cam_infoL = CameraInfo()
cam_infoL.height = CAMERA_HEIGHT
cam_infoL.width = CAMERA_WIDTH/2 #assuems both cameras are read in 1 frame 
cam_infoL.distortion_model = "plumb_bob"
cam_infoL.K = KL
cam_infoL.D = DL
cam_infoL.R = RL
cam_infoL.P = PL

cam_infoR = CameraInfo()
cam_infoR.height = CAMERA_HEIGHT
cam_infoR.width = CAMERA_WIDTH/2 #assuems both cameras are read in 1 frame 
cam_infoR.distortion_model = "plumb_bob"
cam_infoR.K = KR
cam_infoR.D = DR
cam_infoR.R = RR
cam_infoR.P = PR

cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)



while True:
    _,frame=cap.read()

    if frame != None:
        height, width, channels = frame.shape
        #assuems both cameras are read in 1 frame therefor seperate the camera frames
        frameL=frame[0:height,0:width/2]
        frameR=frame[0:height,width/2:width]

        imgL_pub.publish(bridge.cv2_to_imgmsg(frameL, "bgr8"))
        imgR_pub.publish(bridge.cv2_to_imgmsg(frameR, "bgr8"))

        camL_pub.publish(cam_infoL)
        camR_pub.publish(cam_infoR)

        cv2.imshow("frame", cv2.resize(frameL, (0,0), fx=0.1, fy=0.1))

        k=cv2.waitKey(1)
        if k== ord('q'):
            break
