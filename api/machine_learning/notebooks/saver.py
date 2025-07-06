# api/machine_learning/saver.py

import joblib
import os

OUTPUT_DIR = "api/machine_learning/models"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_all(model, scaler):
    """Salva modelo e scaler treinados."""
    joblib.dump(model, os.path.join(OUTPUT_DIR, "model.pkl"))
    joblib.dump(scaler, os.path.join(OUTPUT_DIR, "scaler.pkl"))

