from fastapi import APIRouter, HTTPException, status
from app.schemas import ImovelInput, ImovelOutput
from app.services import executar_predicao

router = APIRouter(tags=["Inferência"])

@router.post("/v1/predict", response_model=ImovelOutput, status_code=status.HTTP_200_OK)
def predict_preco(dados: ImovelInput):
    """Endpoint para realizar a previsão do preço de um imóvel."""
    try:
        preco = executar_predicao(dados)
        return ImovelOutput(preco_estimado=round(preco, 2), status="sucesso")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro interno no servidor ao processar inferência: {str(e)}"
        )