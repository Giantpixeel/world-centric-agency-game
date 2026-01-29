
import cv2
import numpy as np

class Renderer:
    def __init__(self, w=640, h=480):
        self.w, self.h = w, h
        self.offset = np.zeros(2)

    def render(self, motion):
        self.offset += motion
        canvas = np.zeros((self.h, self.w, 3), dtype=np.uint8)
        cx, cy = int(self.w/2 + self.offset[0]), int(self.h/2 + self.offset[1])
        cv2.circle(canvas, (cx, cy), 40, (255,255,255), -1)
        return canvas
