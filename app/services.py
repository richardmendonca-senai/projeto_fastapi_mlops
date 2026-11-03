import joblib
import pandas as pd
from app.schemas import ImovelInput

_modelo_instancia = None

def carregar_modelo():
    """Carrega o artefato binário na memória RAM uma única vez."""
    global _modelo_instancia
    if _modelo_instancia is None:
        _modelo_instancia = joblib.load("models/modelo_imoveis.joblib")
        print("-> Modelo de Machine Learning carregado com sucesso na memória RAM.")

def modelo_esta_carregado() -> bool:
    """Verifica se o modelo reside na memória RAM."""
    return _modelo_instancia is not None

def executar_predicao(dados: ImovelInput) -> float:
    """Executa a inferência matemática a partir do esquema validado."""
    if not modelo_esta_carregado():
        raise RuntimeError("O modelo preditivo não está inicializado na memória RAM.")
    
    # Converte a entrada Pydantic em DataFrame mantendo os nomes das colunas esperados pelo Scikit-Learn
    df_input = pd.DataFrame([dados.model_dump()])
    
    # Realiza a previsão com o pipeline
    predicao = _modelo_instancia.predict(df_input)
    return float(predicao[0])