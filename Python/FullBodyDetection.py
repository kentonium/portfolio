from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

#declare the capture
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('PersonTracker.avi',fourcc, 20.0, (640,480))

#initialize HOG descriptor aka person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

#loop for the video
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret==True:
        
        body_cascade = cv2.CascadeClassifier('C:\EhEye\XMLFiles\haarcascade_fullbody.xml')

        bodies = body_cascade.detectMultiScale(frame, 1.3, 5)

        (rects, weights) = hog.detectMultiScale(frame, winStride=(4, 4),
                                                padding=(8, 8), scale=1.05)
        #draw the original bound boxing
        for(x, y, w, h) in rects:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            
        #apply non-maxima suppression using a big overlap threshhold to
        #maintain overlapping boxes that contain people
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        #draw the box
        for (x,y,w,h) in bodies:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        #display video     
        cv2.imshow('frame',frame)
        
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished

out.release()
cap.release()
cv2.destroyAllWindows()
