class ContaBancaria():
    #Documentação da classe
    """
    Cria uma conta bancária e permite fazer saques e depositos 
    """

    def __init__(self, id, titular, saldo = 0):
        
        #Atributos de instância
        self.id = id
        self.titular = titular
        self.saldo = saldo
        
    #Métodos de instância
        
    def depositar(self, valor = 0):
        self.saldo += valor
        
    def sacar(self, valor = 0):
        self.saldo -= valor
        
    def mostrarSaldo(self):
        return  (
                f"Id......: {self.id}\n"
                f"Titular.: {self.titular}\n"
                f"Saldo...: R${self.saldo:,.2f}\n"
                )
        

conta1 = ContaBancaria(123456, "Eduardo Bougo", 1000)

print(conta1.mostrarSaldo())

conta1.depositar(200)
print(conta1.mostrarSaldo())

conta1.sacar(600)
print(conta1.mostrarSaldo())
