import cv2
import numpy as np
import matplotlib.pyplot as plt

print(cv2.__version__)

# Threshold to detect objects
thres = 0.5

# Capture video from the default camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Load class names
classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Load the model configuration and weights
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
WeightsPath = 'frozen_inference_graph.pb'

# Setup the detection model
net = cv2.dnn.DetectionModel(WeightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

img_counter = 0

while True:
    success, img = cap.read()  # Read frame from camera
    if not success:
        break

    # Perform object detection
    classIds, confs, bbox = net.detect(img, confThreshold=thres)
    
    # If objects are detected, draw bounding boxes and labels
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), color=(0, 255, 0), thickness=2)
            cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(img, str(round(confidence * 100, 2)) + '%', (box[0] + 10, box[1] + 60),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    # Instead of using cv2.imshow(), use matplotlib to display the image
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Turn off axis
    plt.show()

    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # ESC key to exit
        print("Escape hit, closing...")
        break
    elif k == 32:  # SPACE key to capture image
        img_name = f"opencv_frame_{img_counter}.png"
        cv2.imwrite(img_name, img)
        print(f"{img_name} written!")
        img_counter += 1

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
