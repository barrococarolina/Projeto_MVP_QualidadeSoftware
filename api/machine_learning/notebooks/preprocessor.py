# api/machine_learning/preprocessor.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def clean_and_encode(df: pd.DataFrame):
    """
    Limpa, codifica e prepara o dataset para treino de modelo.
    Retorna features e target separados.
    """
    df = df.copy()

    # Alvo (nota final)
    target = df['G3']
    df = df.drop(columns=['G3'])

    # Colunas categóricas
    cat_cols = df.select_dtypes(include='object').columns
    df[cat_cols] = df[cat_cols].astype('category')

    # One-hot encoding
    df_encoded = pd.get_dummies(df, drop_first=True)

    return df_encoded, target

