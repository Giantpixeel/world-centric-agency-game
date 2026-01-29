
import cv2
from src.pose_tracker import PoseTracker
from src.motion_extractor import MotionExtractor
from src.world_models import WorldModel
from src.renderer import Renderer
from src.logger import Logger

cap = cv2.VideoCapture(0)
tracker = PoseTracker()
motion_extractor = MotionExtractor()
world = WorldModel(mode="neutral")  # neutral | heavy | distorted
renderer = Renderer()
logger = Logger("logs.csv")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = tracker.process(frame)
    if results.pose_landmarks:
        motion = motion_extractor.extract(results.pose_landmarks.landmark, frame.shape)
        motion = world.transform(motion)
        logger.log(motion)
    else:
        motion = [0,0]
    out = renderer.render(motion)
    cv2.imshow("World-Centric Agency", out)
    if cv2.waitKey(1) == 27:
        break

logger.close()
cap.release()
cv2.destroyAllWindows()
