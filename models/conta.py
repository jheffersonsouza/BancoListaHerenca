from .registro import Registro


class Conta:
    def __init__(self, nome: str, registro: Registro, saldo: float):
        self._nome = nome
        self._registro = registro
        self._saldo = saldo

    def getSaldo(self) -> float:
        return self._saldo

    def creditar(self, valor: float):
        self._saldo += valor

    def debitar(self, valor: float):
        self._saldo -= valor
