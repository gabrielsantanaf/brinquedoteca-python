from enum import Enum

class status_emprestimo (str, Enum):
    DEVOLVIDO = "devolvido"
    EMPRESTADO = "emprestado"