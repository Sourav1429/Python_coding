'''import cv2
import numpy as np
import os

def frames_to_video(inputpath,outputpath,fps):
    image_array=[]
    fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
    out = cv2.VideoWriter(outputpath,fourcc, fps, (640,480))
    for i in range(len(image_array)):
        out.write(image_array[i])
    out.release()

fps = 29

init_path="F://music//scenki//bso//bso//normal_hungama//y2mate.com - Babuji Zara Dheere Chalo Lyric Video - Dum_Vivek Oberoi_Sukhwinder Singh, Sonu Kakkar_VEDZxXP88lU_360p.mp4"
final_path="Babuji_inv1.avi"
frames_to_video(init_path,final_path,fps)

Playing a video'''

import numpy as np
import cv2 as cv
init_path="F://music//scenki//bso//bso//normal_hungama//y2mate.com - Babuji Zara Dheere Chalo Lyric Video - Dum_Vivek Oberoi_Sukhwinder Singh, Sonu Kakkar_VEDZxXP88lU_360p.mp4"
final_path="Babuji_inv1.avi"
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
cap = cv.VideoCapture(init_path)
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv.flip(frame, 1)
    out.write(frame)
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
out.release()
cv.destroyAllWindows()
