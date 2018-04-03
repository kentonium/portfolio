import numpy as np
import cv2

#Little program demonstrating general OpenCV functionality using haar cascade

cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2(1000, 75, True)  

# Define the codec and create VideoWriter object for recording video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('faceTracker.avi',fourcc, 20.0, (640,480))

count = 0

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret==True:

        #read in the cascade
        body_cascade = cv2.CascadeClassifier('C:\EhEye\XMLFiles\haarcascade_frontalface.xml')

        #Smooth to get rid of false positives
        gray = cv2.GaussianBlur(frame, (15, 15), 0)

        #Convert the image to grayscale.
        cv.CvtColor(color_image, grey_image, cv.CV_RGB2GRAY)

        # scale input image for faster processing
        cv.Resize(gray, small_img, cv.CV_INTER_LINEAR)

        #grab all instances of a face
        heads = body_cascade.detectMultiScale(frame, 1.3, 5)

        #draw a recrangle around the face
        for (x,y,w,h) in heads:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        #show the frame
        cv2.imshow('frame',frame)

        #save the frame to folder as video
        out.write(frame)

        #press q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
out.release()
cap.release()
cv2.destroyAllWindows()
