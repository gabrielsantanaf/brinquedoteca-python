from dataclasses import dataclass


@dataclass
class Brinquedo:
    id: int
    nome: str
    categoria: str
    faixa_etaria: str
    disponivel: bool = True
    