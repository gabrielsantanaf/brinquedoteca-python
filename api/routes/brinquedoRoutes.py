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

@router.get("/{brinquedo_id}", response_model=BrinquedoOut)
def buscar(brinquedo_id: int) -> BrinquedoOut:
    brinquedo = service.buscar_brinquedo_por_id(brinquedo_id)
    if not brinquedo:
        raise HTTPException(status_code=404, detail="Brinquedo não encontrado")

    return BrinquedoOut(
        id=brinquedo.id,
        nome=brinquedo.nome,
        categoria=brinquedo.categoria,
        faixa_etaria=brinquedo.faixa_etaria,
        disponivel=brinquedo.disponivel,
    )
    
