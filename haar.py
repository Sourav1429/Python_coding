import cv2
import numpy as np
face_cascade=cv2.CascadeClassifier("D://datasets//haar//haarcascade_frontalface_default.xml")
img=cv2.imread("D://datasets//Sourav//sourav1.jpg",1)
img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
faces=face_cascade.detectMultiScale(img,scaleFactor=1.05)
print(type(faces))
print(faces)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,245,0),3)
face_cascade=cv2.CascadeClassifier("D://datasets//haar//haarcascade_lefteye_2splits.xml")
faces=face_cascade.detectMultiScale(img,scaleFactor=1.05)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
cv2.startWindowThread()
cv2.namedWindow("Image")
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
