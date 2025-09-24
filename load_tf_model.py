import tensorflow as tf

def load_model(model_path):
    """
    Load a TensorFlow saved model from disk.
    """
    model = tf.saved_model.load(model_path)
    return model
