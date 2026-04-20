from dataclasses import dataclass
from domain.enums import status


@dataclass
class Emprestimo:
    id: int
    crianca_id: int
    brinquedo_id: int
    data_emprestimo: str
    data_devolucao: str = None
    status: status = status.DISPONIVEL