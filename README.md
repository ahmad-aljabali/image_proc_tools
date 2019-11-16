# image_proc_tools
collection of basic image processing functions and useful tools, based on OpenCV & ROS

| Name                     	| Inputs                                                                                                                                                                                                                  	| Outputs                                                                                                                                        	| Description                                                                                                                                      	|
|--------------------------	|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|------------------------------------------------------------------------------------------------------------------------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------	|
| color_mask               	| -frame: HSV image<br>-colors: Array of HSV ranges [[[Low],[Up]]]                                                                                                                                                        	| -mask.                                                                                                                                         	|                                                                                                                                                  	|
| mask_info                	| -mask.                                                                                                                                                                                                                  	| -approx: Array of simplified contours.<br>-bbox: Array of contour bounding boxes [x,y,w,h]<br>-centroids: Array of contour center points (x,y) 	|                                                                                                                                                  	|
| template_matcher         	| -frame: HSV image.<br>-template_path: file path for template image.<br>-confidence_thresh(def=0): 0-1.0 thresh hold for minimum acceptable match confidence.<br>-steps(def=5): number of different scales for matching. 	| -result: [x,y,w,h,confidence] of best match.                                                                                                   	|                                                                                                                                                  	|
| get_position             	| -world_pts: a map of world points in format world_pts[x_px][y_px]=[x_world,y_world,z_world]<br>-bbox(def=None): bounding box of region of intrest.<br>-input_mask(def=None): mask of region of interest.                	| -position: resulting average world position [x_world,y_world,z_world]                                                                          	|                                                                                                                                                  	|
| stereo_calibration       	|                                                                                                                                                                                                                         	|                                                                                                                                                	| file to save calibration result of stereo cam and it contains a description of the calibration matrices.                                         	|
| stereo_cam_processing    	| -world_pts: world_pts map from a ROS topic.<br>-image_rect_color: rectified image from a ROS topic.                                                                                                                     	|                                                                                                                                                	| a starting template for processing stereo camera output to be used with ROS stereo_image_proc.                                                   	|
| stereo_cam_ros_publisher 	| -stereo_calibration: a calibration file as described above.                                                                                                                                                             	| -world_pts: world_pts map published on a ROS topic.                                                                                            	| a publisher for stereo camera stream in the format expected by ROS stereo_image_proc, and it converts disparity map to world_pts and publish it. 	|
| FPS                      	|                                                                                                                                                                                                                         	|                                                                                                                                                	| simple fps counter object it prints fps in terminal on .update()                                                                                 	|
| custom_math_func         	|                                                                                                                                                                                                                         	|                                                                                                                                                	| a collection of usefull geometric functions, check file for details.                                                                             	|
| draw_shapes              	| -frame.<br>-draw_q: queue of shapes to be drawn, check file for dictionary format.                                                                                                                                      	|                                                                                                                                                	|                                                                                                                                                  	|
| screen_grab              	| -area: [x,y,w,h] of screen area to be grabbed as Opencv image.                                                                                                                                                          	| -frame.                                                                                                                                        	|                                                                                                                                                  	|
| threaded_video_stream    	| -src(def=0): video src.<br>-resolution(def=None): (w,h)<br>-fps(def=None)                                                                                                                                               	|                                                                                                                                                	| moves video capture to an independent thread for improved performance.                                                                           	|
