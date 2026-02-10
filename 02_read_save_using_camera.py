import cv2

cap = cv2.VideoCapture(r"D:\Learning Notes and code\Opencv\opencv-4.x\samples\data\vtest.avi")  # 0 is the default camera
# cap = cv2.VideoCapture('myfile.mp4')  # to read a video file instead of camera
# For camera feed, you can use cap = cv2.VideoCapture(0) for the default camera or cap = cv2.VideoCapture(1) for the second camera if you have multiple cameras connected. For video files, provide the path to the video file as shown above.

#save a frame 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(r"D:\Learning Notes and code\Opencv\images\output.avi", fourcc, 20.0, (768, 576))  # Assuming fixed frame size

while True:
    ret, frame = cap.read()  # ret is a boolean indicating if the frame was read successfully
    if not ret:
        print("Failed to grab frame")
        break
    # width & height of the frame
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(f"Frame dimensions: {width} x {height}")
    out.write(frame)  # Save the frame to the output file
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    # cv2.imshow("Camera Feed", frame) # To display the original color feed
    cv2.imshow("Grayscale Feed", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break
cap.release()
out.release()
cv2.destroyAllWindows()


# # Read and display video file in grayscale
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret:
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         cv2.imshow('frame', gray)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
# cap.release()
# cv2.destroyAllWindows()

