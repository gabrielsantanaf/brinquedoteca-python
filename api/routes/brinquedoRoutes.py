from fastapi import APIRouter, HTTPException
from schema.brinquedo import BrinquedoCreate, BrinquedoOut
import service.brinquedo as service

router = APIRouter(prefix="/brinquedos", tags=["brinquedos"])

@router.post("", response_model=BrinquedoOut)
def criar(payload: BrinquedoCreate) -> BrinquedoOut:
    try:
        brinquedo = service.cadastrar_brinquedo(payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return BrinquedoOut(
        id=brinquedo.id,
        nome=brinquedo.nome,
        categoria=brinquedo.categoria,
        faixa_etaria=brinquedo.faixa_etaria,
        disponivel=brinquedo.disponivel,
    )
    
