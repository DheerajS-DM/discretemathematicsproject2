from select_file_dialog import select_image_file
from load_tf_model import load_model
from preprocess_image import preprocess_image
from run_inference import run_inference
from parse_keypoints import parse_keypoints
from build_graph_from_keypoints import build_graph_from_keypoints
from analyze_graph_structure import analyze_graph_structure

def main():
    # Select bridge image file
    image_path = select_image_file()
    if not image_path:
        print("No file selected. Exiting.")
        return
    print(f"Selected image: {image_path}")

    # Load TensorFlow keypoint detection model
    model_path = "path_to_your_saved_model"  # Set this appropriately
    model = load_model(model_path)

    # Preprocess image to model input format
    input_size = (256, 256)  # Example input size; adjust to your model
    input_tensor, original_img = preprocess_image(image_path, input_size)

    # Run inference
    outputs = run_inference(model, input_tensor)

    # Parse keypoints from model output, scaled to original image size
    keypoints = parse_keypoints(outputs, original_img.shape, input_size)
    if not keypoints:
        print("No keypoints detected. Exiting.")
        return

    # Define edges (connections between keypoints)
    # This must be provided based on your bridge structure or predicted
    # Example: simple chain connection (replace with actual edges)
    edges = [(0, 1), (1, 2), (2, 3), (3, 4)]

    # Build graph from detected keypoints and edges
    G = build_graph_from_keypoints(keypoints, edges)

    # Analyze graph connectivity and weak points
    analyze_graph_structure(G)

if __name__ == "__main__":
    main()
