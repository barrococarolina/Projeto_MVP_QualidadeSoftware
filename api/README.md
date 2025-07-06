# MVP Sprint: Qualidade de Software, Segurança e Sistemas Inteligentes

## 1. Introdução
Este projeto é parte integrante da Sprint **Qualidade de Software, Segurança e Sistemas Inteligentes** do curso de Engenharia de Software da PUC-Rio. O MVP é composto de um Back-End, com um modelo de machine learning treinado, e de um Front-End.

>O projeto desenvolvido visa prever a *nota final (G3)* de estudantes com base em dados demográficos, escolares e sociais, usando um modelo de regressão treinado com os datasets de Matemática e Português.

## 2.Back-end
- app.py
- machine_learning:
    - data
    - models
    - notebooks
    - pipeline
    - scalers
- schemas
    - __ init __.py
    - error_schema.py 
    - predicao_schema.py
    - schema.py 
- utils
    - pre_processamento.py
    - utils.py
- requirements.txt

## 3. Como Rodar

### 3.1. Pré-requisitos

- Recomenda-se o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

- Faz-se necessária a instalação de todas as dependências/bibliotecas listadas no arquivo requirements.txt:
```
    (env)$ pip install -r requirements.txt
```
- Se receber o erro Failed to build greenlet, rodar:
pip install --only-binary :all: greenlet
pip install --only-binary :all: Flask-SQLAlchemy

- Install: 
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)


### 3. Rodar com Docker Compose

```bash
docker-compose up --build
```

A API estará disponível em: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Exemplo de Requisição

### Endpoint: `POST /predict`

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "school": "GP", "sex": "F", "age": 17, "address": "U", "famsize": "GT3", "Pstatus": "T",
    "Medu": 4, "Fedu": 4, "Mjob": "teacher", "Fjob": "teacher", "reason": "course", "guardian": "mother",
    "traveltime": 1, "studytime": 2, "failures": 0, "schoolsup": "no", "famsup": "yes", "paid": "no",
    "activities": "yes", "nursery": "yes", "higher": "yes", "internet": "yes", "romantic": "no",
    "famrel": 4, "freetime": 3, "goout": 4, "Dalc": 1, "Walc": 1, "health": 5, "absences": 2,
    "G1": 15, "G2": 14, "subject": "mat"
  }'
```

### Resposta esperada:
```json
{
  "predicted_G3": 15.12
}
```

##  Modelo

- Tipo: Regressão (`RandomForestRegressor`)
- Input: Dados do aluno + notas anteriores (`G1`, `G2`)
- Output: Nota final prevista (`G3`)