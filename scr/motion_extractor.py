
import numpy as np

class MotionExtractor:
    def __init__(self):
        self.prev = None

    def extract(self, landmarks, shape):
        h, w, _ = shape
        xs = [lm.x * w for lm in landmarks]
        ys = [lm.y * h for lm in landmarks]
        center = np.array([sum(xs)/len(xs), sum(ys)/len(ys)])
        if self.prev is None:
            self.prev = center
            return np.zeros(2)
        motion = center - self.prev
        self.prev = center
        return motion
