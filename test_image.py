#import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

#initilaize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

#allow the camera to warm up
time.sleep(0.1)

#grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

#display the image on screen and wait for a key press
cv2.imshow("Image", image)
cv2.waitKey(0)
