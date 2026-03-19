import cv2
import numpy as np

# TODO (Oppong): Mirror the exact preprocessing pipeline from the published research
# Resize, normalize, and format image for model input

def preprocess(image_bytes: bytes) -> np.ndarray:
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    return img
