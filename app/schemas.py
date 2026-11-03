from pydantic import BaseModel, Field

class ImovelInput(BaseModel):
    sqft_living: int = Field(..., gt=0, description="Área construída em pés quadrados (ex: 2000)")
    bedrooms: int = Field(..., ge=1, le=15, description="Quantidade de quartos (1 a 15)")
    bathrooms: float = Field(..., gt=0.0, description="Quantidade de banheiros (ex: 2.5)")
    floors: float = Field(..., gt=0.0, le=4.0, description="Número de andares (1.0 a 4.0)")
    waterfront: int = Field(0, ge=0, le=1, description="Vista para a água (0 = Não, 1 = Sim)")
    zipcode: int = Field(..., description="Código postal da região do imóvel")

    model_config = {
        "json_schema_extra": {
            "example": {
                "sqft_living": 2000,
                "bedrooms": 3,
                "bathrooms": 2.5,
                "floors": 2.0,
                "waterfront": 0,
                "zipcode": 98178
            }
        }
    }

class ImovelOutput(BaseModel):
    preco_estimado: float = Field(..., description="Valor predito do imóvel em USD")
    status: str = Field("sucesso", description="Status da inferência")