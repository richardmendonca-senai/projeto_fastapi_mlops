from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.services import carregar_modelo
from app.routers import health, predict

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicialização: carrega o modelo na RAM uma única vez
    carregar_modelo()
    yield
    # Encerramento do servidor

app = FastAPI(
    title="API Preditiva de Precificação de Imóveis",
    description="API RESTful para estimativa de preços de imóveis construída com FastAPI, Pydantic e Scikit-Learn.",
    version="1.0.0",
    lifespan=lifespan
)

# Inclusão das rotas modularizadas
app.include_router(health.router)
app.include_router(predict.router)