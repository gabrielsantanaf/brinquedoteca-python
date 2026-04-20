from schema.emprestimo import EmprestimoCreate
from domain.emprestimo import Emprestimo
from repositories.memory import db

def criar_emprestimo(emprestimo: EmprestimoCreate) -> Emprestimo:
    novo_id = len(db.emprestimos_por_id) + 1
    novo_emprestimo = Emprestimo(
        id=novo_id,
        crianca_id=emprestimo.crianca_id,
        brinquedo_id=emprestimo.brinquedo_id,
        data_emprestimo=emprestimo.data_emprestimo,
        data_devolucao=emprestimo.data_devolucao,
        status=emprestimo.status
    )
    db.emprestimos_por_id[novo_id] = novo_emprestimo
    return novo_emprestimo
