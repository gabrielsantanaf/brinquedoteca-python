from typing import Dict
from domain.crianca import Crianca
from domain.brinquedo import Brinquedo
from domain.emprestimo import Emprestimo

class MemoryDB:
    def __init__(self):
        self.crianca_por_id: Dict[int, Crianca] = {}
        self.brinquedo_por_id: Dict[int, Brinquedo] = {}
        self.emprestimos_por_id: Dict[int, Emprestimo] = {}

db = MemoryDB()