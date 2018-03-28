import cv2
import numpy as np
import imutils
import mahotas as mh

img = cv2.imread('./images/pool-table-above-17031042.jpg', 0)
# img = (imc*255).astype(np.uint8)
cv2.imshow('window', img)
cv2.moveWindow('window', 80, 80)
cv2.waitKey(500)

# im2 = img[::2, ::2]
# im2 = mh.gaussian_filter(im2, 1.4)
# im2 = 255 - im2
# mean_filtered = mh.convolve(im2.astype(float), np.ones((9, 9))/81.)
# imc = im2 > mean_filtered - 4
# cv2.imshow('window', (imc*255).astype(np.uint8))
# cv2.waitKey(0)

img = cv2.medianBlur(img, 5)
cv2.imshow('window', img)
cv2.waitKey(500)

cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# cv2.imshow('window', cimg)
# cv2.waitKey(0)

# img = cv2.medianBlur(cimg, 7)
# th3 = cv2.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
#                             cv2.THRESH_BINARY, 11, 2)
cv2.imshow('window', img)
cv2.waitKey(500)

diameterBall = 15
radiusBall = int(round(diameterBall/2))
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, diameterBall*0.95,
                           minRadius=int(round(radiusBall*0.95)),
                           maxRadius=int(round(radiusBall*1.05)),
                           param1=120,
                           param2=10
                           )

#    param1=10, param2=1

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(cimg, (i[0], i[1]), 1, (0, 0, 255), 3)

    cv2.imshow('window', cimg)
    cv2.waitKey(2000)

cv2.destroyAllWindows()
