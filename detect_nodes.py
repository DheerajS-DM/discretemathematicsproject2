import cv2
import numpy as np

def detect_nodes(gray_image, max_corners=50, quality_level=0.5, min_distance=20):
    # Detect corners in the grayscale image (nodes/joints)
    corners = cv2.goodFeaturesToTrack(
        gray_image, maxCorners=max_corners,
        qualityLevel=quality_level, minDistance=min_distance
    )
    if corners is not None:
        nodes = [tuple(pt[0]) for pt in corners.astype(int)]
    else:
        nodes = []
    return nodes
