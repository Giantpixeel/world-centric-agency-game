
import cv2
import mediapipe as mp

class PoseTracker:
    def __init__(self):
        self.pose = mp.solutions.pose.Pose(static_image_mode=False)

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.pose.process(rgb)
