from schema.crianca import CriancaCreate
from domain.crianca import Crianca
from repositories.memory import db

def cadastrar_crianca(crianca: CriancaCreate) -> Crianca:
    novo_id = len(db.crianca_por_id) + 1
    nova_crianca = Crianca(
        id=novo_id,
        nome=crianca.nome,
        idade=crianca.idade,
        responsavel=crianca.responsavel,
    )
    db.crianca_por_id[novo_id] = nova_crianca
    return nova_crianca

def buscar_crianca_por_id(crianca_id: int) -> Crianca:
    return db.crianca_por_id.get(crianca_id)