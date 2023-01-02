import cv2

# specify the URL of the IP camera
#url = "http://username:password@IP_ADDRESS:PORT/video.mjpg"
url ="http://192.168.0.2:8080/video"

# open the video stream
cap = cv2.VideoCapture(url)

# check if the video stream is opened successfully
if not cap.isOpened():
  print("Error opening video stream")

# loop through the frames of the video
while True:
  # read the frame
  ret, frame = cap.read()

  # check if the frame is empty
  if not ret:
    print("Error reading frame")
    break

  # display the frame
  cv2.imshow("Frame", frame)

  # check if the user pressed the "q" key
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# release the video stream and close all windows
cap.release()
cv2.destroyAllWindows()
