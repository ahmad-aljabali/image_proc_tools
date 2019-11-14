import cv2
from threading import Thread


class threadedVideoStream(object):
    def __init__(self, src=0, resolution=None, fps=None):
        self.stream = cv2.VideoCapture(src)
        if resolution != None:
            self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
            self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])
        if fps !=None:
            self.stream.set(cv2.CAP_PROP_FPS, fps)
        (self.grabbed, self.frame) = self.stream.read()

        # thread stop flag
        self.stopped = False

        # start the thread to read frames from the video stream
        t = Thread(target=self.update, name="VideoStream", args=())
        t.daemon = True
        t.start()

    def update(self):
        while self.stopped == False:
            (self.grabbed, self.frame) = self.stream.read()


    def read(self):
        return (self.grabbed, self.frame)

    def release(self):
        self.stopped = True
        self.stream.release()
