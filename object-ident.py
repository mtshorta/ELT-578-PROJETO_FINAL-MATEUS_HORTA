import cv2
import os

# ---------------- CONFIG ----------------
THRESH = 0.45
NMS = 0.2
ALLOWED_CLASSES = ["dog"]
# ----------------------------------------

# Base directory (folder where this file lives)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load COCO class names
classFile = os.path.join(BASE_DIR, "coco.names")
with open(classFile, "rt") as f:
    classNames = f.read().strip().split("\n")

# Model files
configPath = os.path.join(BASE_DIR, "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt")
weightsPath = os.path.join(BASE_DIR, "frozen_inference_graph.pb")

# Load model
net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


def getObjects(img, thres, nms, draw=True, objects=None):
    if objects is None:
        objects = classNames

    classIds, confs, bbox = net.detect(
        img,
        confThreshold=thres,
        nmsThreshold=nms
    )

    objectInfo = []

    if len(classIds) != 0:
        for classId, confidence, box in zip(
            classIds.flatten(),
            confs.flatten(),
            bbox
        ):
            className = classNames[classId - 1]

            if className in objects:
                objectInfo.append([box, className, float(confidence)])

                if draw:
                    x, y, w, h = box
                    cv2.rectangle(
                        img,
                        (x, y),
                        (x + w, y + h),
                        (0, 255, 0),
                        2
                    )

                    label = f"{className.upper()} {confidence*100:.1f}%"
                    cv2.putText(
                        img,
                        label,
                        (x, max(30, y - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 0),
                        2
                    )

    return img, objectInfo


if __name__ == "__main__":

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        success, img = cap.read()
        if not success:
            break

        result, objectInfo = getObjects(
            img,
            THRESH,
            NMS,
            objects=ALLOWED_CLASSES
        )

        cv2.imshow("Humans & Dogs Only", result)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
