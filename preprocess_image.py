import cv2
import numpy as np

def preprocess_image(image_path, input_size):
    """
    Load and preprocess image for TensorFlow model input.
    - Resize to model's expected input size.
    - Convert to RGB.
    - Normalize pixel values.
    """
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, input_size)
    img_normalized = img_resized / 255.0  # normalize to 0-1
    
    # Expand dims to add batch size
    input_tensor = np.expand_dims(img_normalized, axis=0).astype(np.float32)
    return input_tensor, img
