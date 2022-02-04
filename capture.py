import cv2
import os
import requests

def notification(person):
    url = "https://notify-api.line.me/api/notify"
    token = "Input Your Token"
    headers = {"Authorization" : "Bearer "+ token}
    if person == 1:
        message = str(person) + "person"
    if person > 1:
        message = str(person) + "persons"
    payload = {"message": message}
    r = requests.post(url, headers = headers, params=payload)

# notification(5) # test

global hog
face_cascade = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades, 'haarcascade_upperbody.xml'))
pnum = 0

def draw_rectangle(img, rects):
    for x,y,w,h in rects:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)
capture = cv2.VideoCapture(0)
if capture.isOpened() is False:
  raise IOError

while(True):
  try:
    ret, frame = capture.read()
    if ret is False:
      raise IOError
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        face = frame[y:y+h, x:x+w]
        face_gray = gray[y:y+h,x:x+w]
        cv2.putText(frame, 'Face Detet', (20,50), cv2.FONT_HERSHEY_SIMPLEX,1.2, (0,0,200),2,cv2.LINE_AA)
    if len(faces)>0 and pnum != len(faces):
        print(len(faces))
        notification(len(faces))
        pnum = len(faces)
    else:
        pnum = 0
    cv2.imshow('frame',frame)
    cv2.imwrite('/home/pi/final/temp.jpg', frame)
    cv2.waitKey(1)
  except KeyboardInterrupt:
    break

capture.release()
cv2.destroyAllWindows()
