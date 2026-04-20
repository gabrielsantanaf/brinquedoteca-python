from pydantic import BaseModel

class EmprestimoCreate(BaseModel):
    crianca_id: int
    brinquedo_id: int
    data_emprestimo: str
    data_devolucao: str = None
    status: str = "emprestado"

class EmprestimoOut(BaseModel):
    id: int
    crianca_id: int
    brinquedo_id: int
    data_emprestimo: str
    data_devolucao: str = None
    status: str = "emprestado"