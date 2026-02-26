def crear_caracter(valor):
    return {
        "valor": valor,
        "siguiente": None
    }

def insertar_despues_de(nodo_anterior, letra):
    nuevo_nodo = crear_caracter(letra)
    if nodo_anterior is not None:
        nuevo_nodo["siguiente"] = nodo_anterior["siguiente"]
        nodo_anterior["siguiente"] = nuevo_nodo
    return nuevo_nodo

def mostrar_texto(cabeza):
    actual = cabeza
    resultado = ""
    while actual is not None:
        resultado += actual["valor"]
        actual = actual["siguiente"]
    print(f"Texto actual: {resultado}")

# --- PRUEBA DEL EDITOR ---

# Creamos la palabra "Hola" (H -> o -> l -> a)
parrafo = crear_caracter("H")
n2 = insertar_despues_de(parrafo, "o")
n3 = insertar_despues_de(n2, "l")
n4 = insertar_despues_de(n3, "a")

mostrar_texto(parrafo)

# Insertamos un guion medio entre la 'o' y la 'l'
insertar_despues_de(n2, "-")

mostrar_texto(parrafo)