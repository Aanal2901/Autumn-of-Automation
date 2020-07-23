
import cv2
#filepath = input("Enter filepath: ")
filepath = "C://Users//Aanal Sonara//Downloads//red-blue.jpeg"
img = cv2.imread(filepath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh, _ = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
img_rev = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("red to blue", img_rev)
cv2.imshow("grayscale", gray)
cv2.imshow("black and white", thresh)
cv2.waitKey(10000)
cv2.destroyAllWindows()