
import numpy as np

class WorldModel:
    def __init__(self, mode="neutral"):
        self.mode = mode

    def transform(self, motion):
        if self.mode == "neutral":
            return motion
        if self.mode == "heavy":
            return motion * 0.4
        if self.mode == "distorted":
            return np.array([motion[1], -motion[0]]) * 1.2
        return motion
