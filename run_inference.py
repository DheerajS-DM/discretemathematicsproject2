def run_inference(model, input_tensor):
    """
    Run model inference on the input_tensor.
    Returns the raw outputs.
    """
    # For TF2 saved model, use __call__ method on the inference function 
    result = model(input_tensor)
    return result
