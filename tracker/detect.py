import cv2
import numpy as np

cap = cv2.VideoCapture(0)
counter = 0
while(1):

    # Take each frame
    _, frame = cap.read()
    simg = cv2.blur(frame, (5,5))
    simg = cv2.GaussianBlur(simg,(5,5),0)
    simg = cv2.medianBlur(simg,5)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(simg, cv2.COLOR_BGR2HSV)

    # define range of purple color in HSV
    lower_blue = np.array([120, 80, 80], dtype=np.uint8)
    upper_blue = np.array([150, 255, 255], dtype=np.uint8)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(simg,simg, mask= mask)

    # cv2.imshow('simg',simg)
    # cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    counter = counter+1
    print 'Frame Number: ',counter
    if counter == 100:
        break

    width = res[1].size
    height = res.size / width
    width = width/3
    number_matches = 0
    print height, width
    sum_x = 0
    sum_y = 0
    for i in range(height-1):
        for j in range(width-1):
            if res[i][j][0] >0:
                sum_x = sum_x + i
                sum_y = sum_y + j
                number_matches = number_matches + 1
    if number_matches <100:
        continue

    print 'Number of matches = ',number_matches
    Mean_x = sum_x/number_matches
    Mean_y = sum_y/number_matches
    print 'Mean_x, Mean_y= ',Mean_x, Mean_y

cv2.destroyAllWindows()