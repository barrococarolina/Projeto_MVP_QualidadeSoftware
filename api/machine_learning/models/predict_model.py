from api.services.model_loader import load_model
from api.schemas.predict_input import PredictInput
import pandas as pd

model = load_model()

def predict_grade(data: PredictInput) -> float:
    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)[0]
    return round(float(prediction), 2)