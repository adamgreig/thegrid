"""
tracking.py

Person detection and tracking.
"""

import logging
from multiprocessing import Process

from .cv import get_centroids

logger = logging.getLogger(__name__)

try:
    import cv2
except ImportError:
    logger.warning("Could not import cv2, continuing with no tracking")
    cv2 = None


def start_tracking(shared_dict):
    logger.info("Tracking starting up")
    while True:
        shared_dict['centroids'] = get_centroids()


class Tracking:
    def __init__(self, shared_dict):
        self.process = Process(
            target=start_tracking, args=(shared_dict,))
        self.process.daemon = True
        self.process.start()
        self.data = shared_dict

    def stop(self):
        self.process.terminate()
        self.process.join()

    def __del__(self):
        self.stop()
