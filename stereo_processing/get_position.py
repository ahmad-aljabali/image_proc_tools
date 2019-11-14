import cv2
import numpy as np

# this function takes world_pts, bounding box*[x,y,width,hight] and/or mask* (* = optional input)
def get_position(world_pts, bbox=None, input_mask=None):

    mask1 = np.zeros((height,width), np.uint8)
    mask2 = np.zeros((height,width), np.uint8)
    # use provided roi formats
    if input_mask != None:
        mask1 = input_mask
    if bbox != None:
        height, width, _ = world_pts.shape
        mask2[int(bbox[1]):int(bbox[1]) + int(bbox[3]),int(bbox[0]):int(bbox[0]) + int(bbox[2])]=(1)

    # mask out missing values from world_pts
    mask3 = cv2.inRange(world_pts, np.array([0,0,0]), np.array([50,50,50]))

    # combine masks
    mask = cv2.bitwise_and(mask1, mask2)
    mask = cv2.bitwise_and(mask, mask3)

    # average the world points to optain average position (Xavg,Yavg,Zavg)
    position = cv2.mean(world_pts, mask)
    return position
