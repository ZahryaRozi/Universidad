print("===== Consulta Descuento ===== \nBy:Juan Martinez \n")

# Registro

name = str(input("Bienvenid@ usuario!! \nPor favor ingrese su nombre: "))
cnsmo = float(input(f"Hola, {name}! Cual es tu consumo mensual? (En kWh): "))

# Condiciones y Operacion

while cnsmo < 0:
    print(f"\n Uy! Parece que ingresaste un valor invalido. Tu consumo no puede ser menor a 0!!")
    cnsmo = float(input(f"Por favor, nuevamente: Cual es tu consumo mensual? (En kWh): "))

if cnsmo <= 100:
    valkWh = 450
elif cnsmo <= 300:
    valkWh = 600
else:
    valkWh = 800

totalCnsmo = cnsmo * valkWh

if totalCnsmo > 200000:
    desc = True
    totalCnsmo = totalCnsmo * 0.05
else:
    desc = False


# Salida
print(f"\nListo, {name}. El programa esta procesando tu solicitud. \n\n== Consulta Finalizada ==")

print(f"Nombre consultante: {name} \nConsumo Registrado: {cnsmo}")

if desc:
    print(f"Descuento: APLICA \nValor antes de Descuento: {totalCnsmo} \nDescuento realizado: 5%")
else:
    print(f"Descuento: NO APLICA")

print(f"Total a pagar: {totalCnsmo}")

# Espacio despues (para que la terminal se vea bonita :D)
print("")
