from models import Registro, Conta, Digital, Corrente, Poupanca, Banco


if __name__ == "__main__":
    reg1 = Registro("000-1", "1234-1")
    reg2 = Registro("001", "5678-3")
    reg3 = Registro("002", "9012-4")

    digital = Digital("João Digital", reg1, 1000.0)
    corrente = Corrente("Maria Corrente", reg2, 2000.0, 5000.0, 20.0)
    poupanca = Poupanca("Pedro Poupança", reg3, 3000.0, 0.01)

    banco = Banco([])
    banco.cadastrar(digital)
    banco.cadastrar(corrente)
    banco.cadastrar(poupanca)

    print(f"Saldo inicial conta digital: {digital.getSaldo()}")
    print(f"Saldo inicial conta corrente: {corrente.getSaldo()}")
    print(f"Saldo inicial conta poupança: {poupanca.getSaldo()}")

    banco.transferir(digital, corrente, 500.0)
    print(f"\nApós transferência de 500:")
    print(f"Novo saldo conta digital: {digital.getSaldo()}")
    print(f"Novo saldo conta corrente: {corrente.getSaldo()}")

