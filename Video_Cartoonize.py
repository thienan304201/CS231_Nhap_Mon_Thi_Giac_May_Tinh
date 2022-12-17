import cv2
import numpy as np
 
capture = cv2.VideoCapture('E:/CS231/CS231_Nhap_Mon_Thi_Giac_May_Tinh/nice ocean waves remix.mp4')

if (capture.isOpened()== False): 
  print("Error opening video stream or file")

else:
  # Get frame rate information
  # You can replace 5 with CAP_PROP_FPS as well, they are enumerations
  fps = capture.get(5)
  print('Frames per second : ', fps,'FPS')
 
  # Get frame count
  # You can replace 7 with CAP_PROP_FRAME_COUNT as well, they are enumerations
  frame_count = capture.get(7)
  print('Frame count : ', frame_count)

frameNr = 0
 
while (True):
 
  success, frame = capture.read()
 
  if not success:
    break

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  blur = cv2.medianBlur(gray, 5)
  edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 9, 9)
  
  color = cv2.bilateralFilter(frame, 9, 250, 250)
  cartoon = cv2.bitwise_and(color, color, mask=edges)

  cv2.imwrite(f'E:/CS231/CS231_Nhap_Mon_Thi_Giac_May_Tinh/frames_output/frame_{frameNr}.jpg', cartoon)
 
  frameNr = frameNr+1
 
capture.release()


img_array = []

for x in range (0, 867):
  img = cv2.imread('E:/CS231/CS231_Nhap_Mon_Thi_Giac_May_Tinh/frames_output/frame_{0}.jpg'.format(x))
  height, width, layers = img.shape
  size = (width,height)
  img_array.append(img)

video = cv2.VideoWriter('E:/CS231/CS231_Nhap_Mon_Thi_Giac_May_Tinh/output_vid.mp4',cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 30, size)
 
for i in range(len(img_array)):
    video.write(img_array[i])
video.release()

