import cv2

def detect_edges(gray_image, canny_thresh1=50, canny_thresh2=150):
    # Detect edges in the grayscale image using Canny edge detection
    edges = cv2.Canny(gray_image, canny_thresh1, canny_thresh2)
    return edges
