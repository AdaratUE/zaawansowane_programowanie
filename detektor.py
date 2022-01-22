import cv2


def Detector(img, model):
    model.setInputSize(320, 320)
    model.setInputScale(1.0 / 127.5)
    model.setInputMean((127.5, 127.5, 127.5))
    model.setInputSwapRB(True)

    ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.5)
    counter = 0
    for ClassIndex, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
        if ClassIndex == 1:
            counter += 1
            cv2.rectangle(img, boxes, (255, 0, 0), 2)
            cv2.putText(img, str(counter), (boxes[0] + 10, boxes[1] + 40),
                        fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                        color=(0, 255, 0), thickness=3)

    cv2.putText(img, f'Total: {counter}', (40, 40), fontFace=cv2.FONT_HERSHEY_PLAIN,
                fontScale=2, color=(0, 0, 255), thickness=3)

    return img
