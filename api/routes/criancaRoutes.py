from fastapi import APIRouter, HTTPException
from schema.crianca import CriancaCreate, CriancaOut
import service.crianca as service

router = APIRouter(prefix="/criancas", tags=["criancas"])

@router.post("", response_model=CriancaOut)
def criar(payload: CriancaCreate) -> CriancaOut:
    try:
        crianca = service.cadastrar_crianca(payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return CriancaOut(
        id=crianca.id,
        nome=crianca.nome,
        idade=crianca.idade,
        responsavel=crianca.responsavel,
    )
