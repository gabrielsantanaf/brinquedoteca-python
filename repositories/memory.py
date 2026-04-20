from typing import Dict
from domain.crianca import Crianca
from domain.brinquedo import Brinquedo

class MemoryDB:
    def __init__(self):
        self.crianca_por_id: Dict[int, Crianca] = {}
        self.brinquedo_por_id: Dict[int, Brinquedo] = {}

db = MemoryDB()