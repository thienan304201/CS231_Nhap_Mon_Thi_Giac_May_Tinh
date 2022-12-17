# import cv2
 
# capture = cv2.VideoCapture('E:/CS231/CS231_Nhap_Mon_Thi_Giac_May_Tinh/Normal_Ocean_Wave.mp4')
 
# frameNr = 0
 
# while (True):
 
#     success, frame = capture.read()
 
#     if success:
#         cv2.imwrite(f'E:\CS231\CS231_Nhap_Mon_Thi_Giac_May_Tinh\frames_output\frame_{frameNr}.jpg', frame)
 
#     else:
#         break
 
#     frameNr = frameNr+1
 
# capture.release()


import cv2
import numpy as np
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('Normal_Ocean_Wave.mp4')
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
 
    # Display the resulting frame
    cv2.imshow('Frame',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()