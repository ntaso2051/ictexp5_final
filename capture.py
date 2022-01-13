import cv2
import os

capture = cv2.VideoCapture(0)
if capture.isOpened() is False:
  raise IOError

while(True):
  try:
    ret, frame = capture.read()
    if ret is False:
      raise IOError
    cv2.imshow('frame',frame)
    cv2.imwrite('/home/pi/final/temp.jpg', frame)
    cv2.waitKey(1)
  except KeyboardInterrupt:
    break

capture.release()
cv2.destroyAllWindows()
