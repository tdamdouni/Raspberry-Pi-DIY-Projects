import cv2, os, time
from pantilthat import *

# Display size
FRAME_W = 180
FRAME_H = 90

# Motion params
PAN_INCREMENT = 2
TILT_INCREMENT = 5
HYSTERESIS = 0.2

forward = True

# Roam params
ROAM_START = 20
PAN_RANGE = (60,120) 
TILT_RANGE = (60,75) 

frames_since_face = 0

# Initial pan-tilt position
cam_pan = PAN_RANGE[0] 
cam_tilt = TILT_RANGE[0]

# Load the BCM V4l2 driver for /dev/video0
os.system('sudo modprobe bcm2835-v4l2')

# Set up the CascadeClassifier for face tracking
cascPath = '/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

# Set up the capture with our frame size
video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH,  FRAME_W)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_H)
time.sleep(2)

# Turn the camera to the start position
pan(cam_pan-90)
tilt(cam_tilt-90)

try:
    while video_capture.isOpened():
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        frame = cv2.flip(frame, -1)

        # Convert to greyscale for detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        # Do face detection
        faces = faceCascade.detectMultiScale(gray, 1.1, 3, 0, (10, 10))

        if len(faces) > 0:
            frames_since_face = 0
            for (x, y, w, h) in faces:
                
                # Draw a green rectangle around the face
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                # Get the center of the face
                x = x + (w/2)
                y = y + (h/2)

                # Correct relative to center of image
                turn_x = float(x - (FRAME_W/2))
                turn_y = float(y - (FRAME_H/2))

                # Convert to percentage offset
                turn_x /= float(FRAME_W/2)
                turn_y /= float(FRAME_H/2)

                # Scaleframes_since_face offset to degrees
                turn_x *= 2.5 # VFOV
                turn_y *= 2.5 # HFOV
                
                if abs(turn_x) > HYSTERESIS:
                    cam_pan  += -turn_x

                if abs(turn_y) > HYSTERESIS:
                    cam_tilt += turn_y

                # Clamp Pan/Tilt to 0 to 180 degrees
                cam_pan = max(0, min(180,cam_pan))
                cam_tilt = max(0, min(180,cam_tilt))

                # Update the servos
                pan(int(cam_pan-90))
                tilt(int(cam_tilt-90))

                # Exit after first face
                break
            
        else:
            frames_since_face = frames_since_face + 1

            if frames_since_face > ROAM_START:
                # Start roam
                if forward:
                    cam_pan = cam_pan + PAN_INCREMENT
                else:
                    cam_pan = cam_pan - PAN_INCREMENT

                if cam_pan < PAN_RANGE[0]:
                    forward = True
                    cam_tilt = cam_tilt + TILT_INCREMENT
                    cam_pan = PAN_RANGE[0]
                    
                elif cam_pan > PAN_RANGE[1]:
                    forward = False
                    cam_tilt = cam_tilt + TILT_INCREMENT
                    cam_pan = PAN_RANGE[1]
                    
                if cam_tilt > TILT_RANGE[1]:
                    cam_tilt = TILT_RANGE[0]

                # Update the servos
                pan(int(cam_pan-90))
                tilt(int(cam_tilt-90))

        print("%.2f %.2f" % (cam_pan-90, cam_tilt-90))            
        
        cv2.imshow("preview", frame)
        cv2.waitKey(20)                
        #cv2.imwrite("test.jpg", frame)
        
except:
    video_capture.release()
    cv2.destroyAllWindows()
