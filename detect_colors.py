# import required libraries
import numpy as np
import cv2

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--a", default=1, type=int, help="This is the 'a' variable")
parser.add_argument("--color", 
                    choices=["red", "green", "blue"],
                    required=True, type=str, help="Color to detect")

args = parser.parse_args()

color_to_detect = args.color

if color_to_detect == "red":
    low_val = np.array([161, 155, 84])
    high_val = np.array([179, 255, 255])
elif color_to_detect == "blue":
    low_val = np.array([94, 80, 2])
    high_val = np.array([126, 255, 255])
elif color_to_detect == "green":
    low_val = np.array([25, 52, 72])
    high_val = np.array([102, 255, 255])
else:
    # every color except white
    low_val = np.array([0, 42, 0])
    high_val = np.array([179, 255, 255])




# create the camera object
cam = cv2.VideoCapture(0)

while (True):
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)    
    # create a mask that is in the range of green 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    image_mask = cv2.inRange(hsv, low_val, high_val)
    output = cv2.bitwise_and(frame, frame, mask = image_mask)
    
    # display both the original feed and the detected (green)
    cv2.imshow('Original', frame)
    cv2.imshow('Output', output)
    
    # break out of 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# cleanup
cv2.destroyAllWindows()
cam.release()