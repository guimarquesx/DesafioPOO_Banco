class Banco:
    def __init__(self):
        self.agencias = []
        self.numeros = []
        self.clientes = []

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def inserir_numero(self, numero):
        self.numeros.append(numero)

    def autenticar(self, cliente):
        if cliente.nome not in self.clientes:
            return False

        if cliente.numero not in self.numeros:
            return False

        if cliente.conta.agencia not in self.agencias:
            return False

        return True
