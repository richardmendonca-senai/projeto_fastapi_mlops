from fastapi import APIRouter, HTTPException, status
from app.services import modelo_esta_carregado

router = APIRouter(tags=["Monitoramento"])

@router.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    """Endpoint para checagem da integridade da API e presença do modelo em memória."""
    if not modelo_esta_carregado():
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Serviço ativo, mas o modelo não está carregado na memória RAM."
        )
    return {"status": "ok", "modelo_carregado": True}