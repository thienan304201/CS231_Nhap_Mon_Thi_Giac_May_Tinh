import cv2

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Check if camera opened successfully
if (webcam.isOpened() == False):
    print("Error opening video stream or file")

# Read the video
while(webcam.isOpened()):
    # Capture frame-by-frame
    ret, frame = webcam.read()
    if ret == True:
        frame = cv2.flip(frame, 1) # Flip mirror
        color = cv2.bilateralFilter(frame, 9, 9, 7)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.medianBlur(gray, 7)
        edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
        frame_edge = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
        cartoon = cv2.bitwise_and(color, frame_edge)
        # Display the resulting frame
        cv2.imshow('Cartoonized', cartoon)
        # Press q on keyboard to  exit
        if cv2.waitKey(25) == ord('q'):
            break
            # Press s on keyboard to save a screenshot
        elif cv2.waitKey(25) == ord('s'):
            cv2.imwrite('screenshot.png', cartoon)

# When everything done, release the video capture object
webcam.release()

# Closes all the frames
cv2.destroyAllWindows()