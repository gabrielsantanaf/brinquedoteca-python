from pydantic import BaseModel

class BrinquedoCreate(BaseModel):
    nome: str
    categoria: str
    faixa_etaria: str
    disponivel: bool = True

class BrinquedoOut(BaseModel):
    id: int
    nome: str
    categoria: str
    faixa_etaria: str
    disponivel: bool = True