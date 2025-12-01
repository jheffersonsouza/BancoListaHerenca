class Registro:
    def __init__(self, agencia: str, conta: str):
        self._agencia = agencia
        self._conta = conta

    def getAgencia(self):
        return self._agencia

    def getConta(self):
        return self._conta
