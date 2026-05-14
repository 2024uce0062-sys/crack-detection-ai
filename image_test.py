import cv2
img = cv2.imread("test.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
_, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE
)

for contour in contours:

    area = cv2.contourArea(contour)
    if 100 < area < 5000 :

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            img,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )
cv2.imshow("Crack Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()