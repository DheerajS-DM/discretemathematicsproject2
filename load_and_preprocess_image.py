import cv2
import numpy as np

def load_and_preprocess_image(image_path):
    # Load image in color
    img = cv2.imread(image_path)
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian Blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Increase contrast by histogram equalization
    contrast_enhanced = cv2.equalizeHist(blur)
    
    return img, contrast_enhanced
