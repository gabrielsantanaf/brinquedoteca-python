from domain.brinquedo import Brinquedo
from repositories.memory import db

def cadastrar_brinquedo(brinquedo: Brinquedo) -> Brinquedo:
    novo_id = len(db.brinquedo_por_id) + 1
    novo_brinquedo = Brinquedo(
        id=novo_id,
        nome=brinquedo.nome,
        categoria=brinquedo.categoria,
        faixa_etaria=brinquedo.faixa_etaria,
        disponivel=brinquedo.disponivel,
    )
    db.brinquedo_por_id[novo_id] = novo_brinquedo
    return novo_brinquedo

def buscar_brinquedo_por_id(brinquedo_id: int) -> Brinquedo:
    return db.brinquedo_por_id.get(brinquedo_id)