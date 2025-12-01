from .conta import Conta
from .registro import Registro


class Poupanca(Conta):
    def __init__(self, nome: str, registro: Registro, saldo: float, taxa_rendimento: float):
        super().__init__(nome, registro, saldo)
        self._taxa_rendimento = taxa_rendimento

    def calcularRendimento(self) -> float:
        return self._saldo * self._taxa_rendimento

    def aplicarRendimento(self):
        self._saldo += self.calcularRendimento()
