import cv2
import numpy as np

# TODO (Oppong): Original training script from published research
# Dataset: 3,243 images across disease classes
# Target accuracy: 99.4%

# Steps:
# 1. Load images from dataset/
# 2. Preprocess with OpenCV
# 3. Train model
# 4. Save model to backend/app/ml/model/

DATASET_PATH = "./dataset"
MODEL_OUTPUT  = "../backend/app/ml/model/plant_disease.pkl"
