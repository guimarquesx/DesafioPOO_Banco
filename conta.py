from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia}\nNúmero: {self.numero}\nSaldo:{self.saldo}')
    
    # Sacar need to be in ContaPoupanca and ContaCorrente
    @abstractmethod
    def sacar(self): 
        pass
    

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        
        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo, limite=100):
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()