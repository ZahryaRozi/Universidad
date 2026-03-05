class Persona: #Definicion de Clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print("Hola, mucho gusto, me llamo", self.nombre)
    
# definicion del objeto

p1 = Persona("Miguel", 25)

p1.saludar()