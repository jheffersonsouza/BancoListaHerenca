from .conta import Conta
from .registro import Registro


class Corrente(Conta):
    def __init__(self, nome: str, registro: Registro, saldo: float, limite: float, taxa_manutencao: float):
        super().__init__(nome, registro, saldo)
        self._limite = limite
        self._taxa_manutencao = taxa_manutencao

    def limiteDisponivel(self) -> float:
        return self._limite - self._saldo

    def cobrarTaxa(self):
        self._saldo -= self._taxa_manutencao
