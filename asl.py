import cv2

cap = cv2.VideoCapture(5)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 576)
# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# print(f"Camera resolution: {width}x{height}")
if not cap.isOpened():
    print("Could not open video device")
else:
    print("Video device opened successfully")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Could not read frame from video device")
            break
        cv2.imshow('OpenCV Feed', frame)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
