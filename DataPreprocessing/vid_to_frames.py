
import cv2
vidcap = cv2.VideoCapture('C:/Users/onyeo/Pictures/Planet9/output1.mp4')
success,image = vidcap.read()
count = 1
skip = 10
success = True
while success:
  if count%skip == 0:
    cv2.imwrite("C:/Users/onyeo/Pictures/Planet9/Pilot2data/Newframe%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
  