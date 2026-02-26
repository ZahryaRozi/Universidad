def crear_cliente(nombre):
    return {
        "nombre": nombre,
        "siguiente": None
    }

def llegar_a_fila(cabeza, nombre):
    nuevo_cliente = crear_cliente(nombre)
    if cabeza is None:
        return nuevo_cliente
    
    actual = cabeza
    while actual["siguiente"] is not None:
        actual = actual["siguiente"]
    
    actual["siguiente"] = nuevo_cliente
    return cabeza

def atender_cliente(cabeza):
    if cabeza is None:
        print("La fila está vacía.")
        return None
    
    print(f"Atendiendo a: {cabeza['nombre']}")
    nueva_cabeza = cabeza["siguiente"]
    return nueva_cabeza

def ver_fila(cabeza):
    actual = cabeza
    print("ESTADO DE LA FILA:")
    while actual is not None:
        print(f"[{actual['nombre']}]", end=" -> ")
        actual = actual["siguiente"]
    print("FIN")

# --- PRUEBA DEL SISTEMA (FIFO) ---

fila = None

fila = llegar_a_fila(fila, "Doña María")
fila = llegar_a_fila(fila, "Don Pedro")
fila = llegar_a_fila(fila, "Juan")

ver_fila(fila)

fila = atender_cliente(fila)
fila = atender_cliente(fila)

ver_fila(fila)