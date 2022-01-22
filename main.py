import glob
import time
import cv2
import imutils
from detektor import Detector

frozen_model = "frozen_inference_graph.pb"
config_file = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
model = cv2.dnn_DetectionModel(frozen_model, config_file)

for filename in glob.glob('photos/*.jpg'):
    img = cv2.imread(filename)
    img = imutils.resize(img, width=600)
    start = time.time()
    img = Detector(img, model)
    end = time.time()
    cv2.imshow(f"Wynik {filename}", img)
    print(round(end - start, 2))
    cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
