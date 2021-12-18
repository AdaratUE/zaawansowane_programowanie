import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


img1 = cv2.imread('Images/dahl.jpg')
img2 = cv2.imread('Images/mickiewicz.jp')
img3 = cv2.imread('Images/paint.png')
img4 = cv2.imread('Images/shutter.png')
img5 = cv2.imread('Images/social.jpg')

print(pytesseract.image_to_string(img5))


