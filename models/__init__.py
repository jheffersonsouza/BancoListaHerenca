class Registro:
    def __init__(self, agencia: str, conta: str):
        self._agencia = agencia
        self._conta = conta

    def getAgencia(self):
        return self._agencia

    def getConta(self):
        return self._conta


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


class Digital(Conta):
    def __init__(self, nome: str, registro: Registro, saldo: float):
        super().__init__(nome, registro, saldo)


class Corrente(Conta):
    def __init__(self, nome: str, registro: Registro, saldo: float, limite: float, taxa_manutencao: float):
        super().__init__(nome, registro, saldo)
        self._limite = limite
        self._taxa_manutencao = taxa_manutencao

    def limiteDisponivel(self) -> float:
        return self._limite - self._saldo

    def cobrarTaxa(self):
        self._saldo -= self._taxa_manutencao


class Poupanca(Conta):
    def __init__(self, nome: str, registro: Registro, saldo: float, taxa_rendimento: float):
        super().__init__(nome, registro, saldo)
        self._taxa_rendimento = taxa_rendimento

    def calcularRendimento(self) -> float:
        return self._saldo * self._taxa_rendimento

    def aplicarRendimento(self):
        self._saldo += self.calcularRendimento()


class Banco:
    def __init__(self, contas: list):
        self._contas = contas

    def cadastrar(self, conta: Conta):
        self._contas.append(conta)

    def procurarConta(self, registro: Registro):
        for conta in self._contas:
            if conta.getAgencia() == registro.getAgencia() and conta.getConta() == registro.getConta():
                return conta
        return None

    def transferir(self, origem: Conta, destino: Conta, valor: float):
        origem.debitar(valor)
        destino.creditar(valor)

    def listarContas(self):
        return self._contas
