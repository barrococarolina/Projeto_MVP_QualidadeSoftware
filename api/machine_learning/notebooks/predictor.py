# api/machine_learning/predictor.py

import joblib
import pandas as pd
from pathlib import Path

MODEL_DIR = Path("api/machine_learning/models")
model = joblib.load(MODEL_DIR / "model.pkl")
scaler = joblib.load(MODEL_DIR / "scaler.pkl")

def predict_from_input(input_data: pd.DataFrame) -> float:
    """
    Recebe um DataFrame com um único registro (com mesmas features do treino)
    e retorna a predição do modelo treinado.
    """
    X_scaled = scaler.transform(input_data)
    prediction = model.predict(X_scaled)
    return prediction[0]
