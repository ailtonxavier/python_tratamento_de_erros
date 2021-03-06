from pprint import pprint


class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


class Conta_Corrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.saldo = 100
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero
        Conta_Corrente.total_contas_criadas += 1
        Conta_Corrente.taxa_operacao = 30 / Conta_Corrente.total_contas_criadas


    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)


    def sacar(self, valor):
        self.saldo -= valor


    def depositar(self, valor):
        self.saldo += valor


conta_corrente = Conta_Corrente(None, "00", "101")

