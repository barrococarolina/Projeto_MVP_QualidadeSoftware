from flask import Flask, request, jsonify
import joblib
from schemas import *
from utils.pre_processamento import preparar_data_frame
from pydantic import ValidationError

app = Flask(__name__)

# Carrega o modelo treinado
modelo = joblib.load("ml_model/pipeline.pkl")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Previsão de Notas de Alunos está no ar!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Validar e converter os dados usando Pydantic
        dados = PredicaoSchema(**request.json)
    except ValidationError as e:
        return jsonify(ErrorSchema(mensagem="Erro de validação", detalhes=e.errors()).dict()), 400

    # Pré-processar dados
    dados_processados = preparar_data_frame(dados.dict())

    # Fazer a previsão
    resultado = modelo.predict(dados_processados)[0]

    return jsonify({"predicted_G3": round(float(resultado), 2)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)