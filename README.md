# API Preditiva de Precificação de Imóveis (MLOps com FastAPI)

Este projeto consiste na implementação de uma API RESTful de alta performance e baixa latência para estimativa de preços de imóveis no município de King County (EUA). A solução disponibiliza um pipeline de Machine Learning treinado como um microsserviço assíncrono em produção, utilizando **FastAPI**, **Pydantic** e práticas modernas de **MLOps**.

---

## 1. Origem do Modelo e Problema de Negócio
- **Problema de Negócio:** Estimativa contínua do valor de mercado de imóveis (`price` em USD) com base em características estruturais e de localização.
- **Origem (Opção A):** Reaproveitamento e aprimoramento do modelo desenvolvido no Módulo 1 (dataset *King County House Sales* / `kc_house_data.csv`).
- **Algoritmo:** Pipeline Scikit-Learn composto por imputação de nulos (`SimpleImputer`), padronização de escalas (`StandardScaler`) e regressão com `RandomForestRegressor`.

### Métricas Alcançadas pelo Modelo (Fase 1)
- **R² Score:** ~0.86 (Explica ~86% da variância dos preços)
- **RMSE (Root Mean Squared Error):** ~\$125,000.00

---

## 2. Tecnologias Utilizadas
- **Linguagem:** Python 3.12+
- **Framework Web:** FastAPI (Arquitetura assíncrona ASGI)
- **Servidor ASGI:** Uvicorn
- **Validação de Dados:** Pydantic v2 (Classes BaseModel e Field)
- **Machine Learning:** Scikit-Learn, Pandas, NumPy, Joblib

---

## 3. Arquitetura Modular do Projeto (Fase 2)

O projeto adota uma arquitetura em camadas desacopladas:

```text
projeto_fastapi_mlops/
├── data/
│   └── kc_house_data.csv          # Base de dados (caminho relativo)
├── models/
│   └── modelo_imoveis.joblib      # Artefato do pipeline serializado
├── app/
│   ├── __init__.py
│   ├── main.py                    # Ponto de entrada e gerenciamento de Lifespan
│   ├── schemas.py                 # Esquemas de validação Pydantic
│   ├── services.py                # Camada de inferência e gestão da RAM
│   └── routers/
│       ├── __init__.py
│       ├── health.py              # Endpoint GET /health
│       └── predict.py             # Endpoint POST /v1/predict
├── requirements.txt               # Dependências do projeto
└── README.md                      # Documentação técnica
```

---

## 4. Ciclo de Vida e Inicialização (Lifespan - Fase 3)
A aplicação utiliza a diretiva `@asynccontextmanager` (`lifespan`) no FastAPI para carregar o arquivo binário `.joblib` **uma única vez na memória RAM durante a inicialização do servidor**. Não há leitura do disco a cada requisição de inferência, garantindo máxima performance de I/O e eliminando latências desnecessárias.

---

## 5. Instruções de Instalação e Execução

### Pré-requisitos
- Python 3.10+ e Git instalados.

### Passo a Passo
1. **Clonar o repositório:**
   ```bash
   git clone [suspicious link removed]
   cd projeto_fastapi_mlops
   ```

2. **Criar e ativar o ambiente virtual:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar as dependências do projeto:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Iniciar o servidor de produção local:**
   ```bash
   uvicorn app.main:app --reload
   ```
   O servidor estará ativo em: `http://127.0.0.1:8000`

---

## 6. Documentação dos Endpoints (Swagger UI)

Acesse a interface interativa do Swagger em: **[suspicious link removed]**

### 1. Monitoramento de Saúde (`GET /health`)
- **Descrição:** Verifica a integridade da aplicação e se o modelo reside na memória RAM.
- **Resposta de Sucesso (200 OK):**
  ```json
  {
    "status": "ok",
    "modelo_carregado": true
  }
  ```

### 2. Inferência Preditiva (`POST /v1/predict`)
- **Descrição:** Executa a previsão do preço do imóvel a partir dos atributos validados.
- **Exemplo de Payload de Entrada (JSON):**
  ```json
  {
    "sqft_living": 2000,
    "bedrooms": 3,
    "bathrooms": 2.5,
    "floors": 2.0,
    "waterfront": 0,
    "zipcode": 98178
  }
  ```
- **Resposta de Sucesso (200 OK):**
  ```json
  {
    "preco_estimado": 485920.50,
    "status": "sucesso"
  }
  ```
- **Tratamento de Erros e Validação Estrita (422 Unprocessable Entity):**
  Envios com tipos de dados inválidos ou fora das restrições de negócio no Pydantic (`Field`) são interceptados automaticamente, retornando HTTP 422 antes de atingir o modelo preditivo.

---

## 7. Links das Evidências de Entrega
- **Repositório GitHub:** `[suspicious link removed]`
- **Vídeo de Demonstração (Google Drive):** `[Insira aqui o link público do seu vídeo no Google Drive]`