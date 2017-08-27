from __future__ import print_function
import time
import threading
import cv2
import cv2.cv as cv
import Image
import StringIO

import config as cfg

    
def init_camera():
    try:
        # camera setup
        camera = cv2.VideoCapture(cfg.video_src)
        camera.set(cv.CV_CAP_PROP_FRAME_WIDTH, float(cfg.width))
        camera.set(cv.CV_CAP_PROP_FRAME_HEIGHT, float(cfg.height))
        return True, camera
    except:
        return False, False
        
def single_frame():
    sbuffer = StringIO.StringIO()
    camtest = False
    while camtest == False:
        camtest, rawimg = cfg.camera.read()
    if cfg.cv_hflip:
        rawimg = cv2.flip(rawimg, 1)
    if cfg.cv_vflip:
        rawimg = cv2.flip(rawimg, 0)
    imgRGB=cv2.cvtColor(rawimg, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(imgRGB)
    img.save(sbuffer, 'JPEG')
    return sbuffer.getvalue()

class Camera(object):
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera
    
    def initialize(self):
        if Camera.thread is None:
            # start background frame thread
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()
            # wait until frames start to be available
            while self.frame is None:
                time.sleep(0)

    def get_frame(self):
        Camera.last_access = time.time()
        self.initialize()
        return self.frame

    @classmethod
    def _thread(cls):
        # frame grabber loop
        while cfg.camera_active:
            sbuffer = StringIO.StringIO()
            camtest = False
            while camtest == False:
                camtest, rawimg = cfg.camera.read()
            if cfg.cv_hflip:
                rawimg = cv2.flip(rawimg, 1)
            if cfg.cv_vflip:
                rawimg = cv2.flip(rawimg, 0)
            imgRGB=cv2.cvtColor(rawimg, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(imgRGB)
            img.save(sbuffer, 'JPEG')
            cls.frame = sbuffer.getvalue()
            # if there hasn't been any clients asking for frames in
            # the last 10 seconds stop the thread
            if time.time() - cls.last_access > 10:
                break
                
