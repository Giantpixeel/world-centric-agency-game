
import csv, time

class Logger:
    def __init__(self, path):
        self.f = open(path, 'w', newline='')
        self.w = csv.writer(self.f)
        self.w.writerow(["time","dx","dy"])

    def log(self, motion):
        self.w.writerow([time.time(), motion[0], motion[1]])

    def close(self):
        self.f.close()
