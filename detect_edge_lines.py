import cv2
import numpy as np

def detect_edge_lines(edge_image, min_line_length=30, max_line_gap=20, hough_thresh=80):
    # Detect straight line segments using Probabilistic Hough Transform
    lines = cv2.HoughLinesP(
        edge_image, rho=1, theta=np.pi/180,
        threshold=hough_thresh,
        minLineLength=min_line_length,
        maxLineGap=max_line_gap
    )
    if lines is not None:
        line_segments = [tuple(line[0]) for line in lines]
    else:
        line_segments = []
    return line_segments
