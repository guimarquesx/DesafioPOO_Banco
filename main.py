"""
Exercício para estudo sobre Polimorfismo, Herança, Encapsulamento, Abstração e Getters.
Criação de um sistema bancário que tem clientes, contas e um banco;
O objetivo é que o cliente tenha uma conta (corrente ou poupança) e que 
possa sacar/depositar nessa conta;
Contas correntes tem um limite extra;
O banco será responsável por autenticar o cliente e as contas;
Só é possível sacar mediante a autenticação do banco.
"""

from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Guilherme', 24)
cliente2 = Cliente('Lucas', 18)
cliente3 = Cliente('Caio', 40)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 254137, 0)
conta3 = ContaPoupanca(3333, 254138, 0)

cliente1.inserir_numero(conta1)
cliente2.inserir_numero(conta2)
cliente3.inserir_numero(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_numero(conta1.numero)

banco.inserir_cliente(cliente2)
banco.inserir_numero(conta2.numero)

banco.inserir_cliente(cliente3)
banco.inserir_numero(conta3.numero)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(0)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado.')

print('####################')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado.')

print('####################')

if banco.autenticar(cliente3):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado.')