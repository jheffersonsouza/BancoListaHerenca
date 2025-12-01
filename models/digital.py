from .conta import Conta
from .registro import Registro


class Digital(Conta):
    def __init__(self, nome: str, registro: Registro, saldo: float):
        super().__init__(nome, registro, saldo)
