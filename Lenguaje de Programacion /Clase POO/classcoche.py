class coche:
    def __init__(self, marca, color): ## init es el constructor y self es la referencia al objeto
        self.marca = marca
        self.color = color
        
    def acelerar(self):
        print("El coche esta acelerando")

mi_coche = coche("Toyota","Rojo") # Definicion del objeto

print(mi_coche.marca)
print(mi_coche.color)

mi_coche.acelerar()