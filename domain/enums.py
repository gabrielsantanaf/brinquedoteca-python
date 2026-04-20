from enum import Enum

class Status (str, Enum):
    DISPONIVEL = "Disponível"
    EMPRESTADO = "Emprestado"