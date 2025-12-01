# BancoListaHerenca

## Descrição
Este projeto é uma simulação simples de um sistema bancário desenvolvido em Python. O objetivo principal é demonstrar conceitos de Programação Orientada a Objetos (POO).

## Estrutura do Projeto

A estrutura de arquivos do projeto está organizada da seguinte maneira:

```
BancoListaHerenca/
├── main.py              # Ponto de entrada da aplicação. Contém o código de exemplo para execução.
├── models/              # Pacote contendo as definições das classes (Modelos)
│   ├── __init__.py      # Inicializador do pacote, expondo as classes principais
│   ├── conta.py         # Definição da classe base 'Conta'
│   ├── corrente.py      # Definição da classe 'Corrente' (herda de Conta)
│   ├── poupanca.py      # Definição da classe 'Poupanca' (herda de Conta)
│   ├── digital.py       # Definição da classe 'Digital' (herda de Conta)
│   └── registro.py      # Definição da classe auxiliar 'Registro' (dados da conta)
└── README.md            # Documentação do projeto
```

## Como Executar

Siga os passos abaixo para rodar o projeto em sua máquina local:

**Executar a Aplicação**:
    ```bash
    python main.py
    ```
    *(Nota: Em alguns sistemas, pode ser necessário usar `python3 main.py`)*