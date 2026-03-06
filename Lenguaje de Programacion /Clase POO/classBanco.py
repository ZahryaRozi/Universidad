'''
Crear una cuenta bancaria
Atributos (titular, saldo, cantidadDepositar)
Metodos (depositar() y mostrar_saldo())
'''

class cuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
     
    def mostrar_saldo(self):
        print("Su saldo es: ", self.saldo)
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        

cuenta1 = cuentaBancaria("Carlos", 100)
cuenta1.depositar(50)
cuenta1.mostrar_saldo