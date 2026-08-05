import cv2 as cv 
import numpy as np

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Problem in opening the Video ")
    exit()

while True: 
    ret, frame = cap.read()

    if not ret : 
        print("Could not read the Frame !")
        break
    width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)


    cv.imshow(f"Video({width} x({height})) ", frame)
    new_height = frame.shape[0]//2
    new_width = frame.shape[1]//2
    small_frame = np.zeros((new_height, new_width, 3), dtype=np.uint8)


    for row in range(0,height,2):
        for col in range(0,width,2):
            row_blue = frame.shape[row+1]
            



    print(frame[0, 4, 0])
    print(frame[4,4])

    if cv.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()