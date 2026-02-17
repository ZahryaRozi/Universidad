def inicializar_inventario(cantidad):
    return [0.0] * cantidad

def registrar_precio(inventario, id_producto, precio):
    if id_producto >= 0 and id_producto < len(inventario):
        inventario[id_producto] = precio
    return inventario

def consultar_precio(inventario, id_producto):
    if id_producto >= 0 and id_producto < len(inventario):
        return inventario[id_producto]
    return None

# --- PRUEBA DEL SISTEMA ---

precios = inicializar_inventario(500)

precios = registrar_precio(precios, 10, 25.50)
precios = registrar_precio(precios, 450, 120.99)
precios = registrar_precio(precios, 0, 5.00)

id_a_buscar = 450
precio_encontrado = consultar_precio(precios, id_a_buscar)

if precio_encontrado is not None:
    print(f"El precio del producto con ID {id_a_buscar} es: ${precio_encontrado}")
else:
    print("ID de producto no válido.")