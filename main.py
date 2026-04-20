#import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Request

from api.routes.criancaRoutes import router as criancas_router
from api.routes.brinquedoRoutes import router as brinquedo_router

app = FastAPI(
                title="Projeto Lanchonete", 
                description="API para gerenciamento de clientes e produtos da lanchonete", 
                version="1.0.0"
            )

# Tratamento global de erros do tipo ValueError, retornando status 400 com a mensagem de erro
@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )

app.include_router(criancas_router)
app.include_router(brinquedo_router)