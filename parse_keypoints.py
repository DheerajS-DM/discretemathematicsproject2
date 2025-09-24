import numpy as np

def parse_keypoints(outputs, original_image_shape, input_size):
    """
    Parse the output tensors to extract keypoint coordinates scaled back
    to the original image dimensions.
    Example assumes output format contains 'keypoints' as normalized coords.
    """
    # Example: output tensor 'keypoints' shape [1, num_points, 2], normalized 0-1
    keypoints = outputs['keypoints'][0].numpy()  # shape (num_points, 2)
    
    height, width = original_image_shape[:2]
    input_width, input_height = input_size
    
    # Scale keypoints to original image size
    keypoints[:, 0] *= width      # x-coords
    keypoints[:, 1] *= height     # y-coords
    
    # Convert to list of (x, y) tuples int
    points = [(int(x), int(y)) for x, y in keypoints]
    return points
