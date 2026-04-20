from dataclasses import dataclass
from domain.enums import status_emprestimo


@dataclass
class Emprestimo:
    id: int
    crianca_id: int
    brinquedo_id: int
    data_emprestimo: str
    data_devolucao: str = None
    status: status_emprestimo = status_emprestimo.EMPRESTADO