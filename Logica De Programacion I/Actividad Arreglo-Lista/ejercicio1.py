def crear_nodo(url):
    return {
        "url": url,
        "siguiente": None,
        "anterior": None
    }

def visitar_pagina(actual, nueva_url):
    nuevo_nodo = crear_nodo(nueva_url)
    if actual is not None:
        actual["siguiente"] = nuevo_nodo
        nuevo_nodo["anterior"] = actual
    return nuevo_nodo

def ir_atras(actual):
    if actual is not None and actual["anterior"] is not None:
        actual = actual["anterior"]
    return actual

def ir_adelante(actual):
    if actual is not None and actual["siguiente"] is not None:
        actual = actual["siguiente"]
    return actual

# --- PRUEBA DEL PROGRAMA ---

mi_navegador = None

mi_navegador = visitar_pagina(mi_navegador, "google.com")
mi_navegador = visitar_pagina(mi_navegador, "youtube.com")
mi_navegador = visitar_pagina(mi_navegador, "github.com")

print(f"Página actual: {mi_navegador['url']}")

mi_navegador = ir_atras(mi_navegador)
print(f"Tras ir atrás: {mi_navegador['url']}")

mi_navegador = ir_adelante(mi_navegador)
print(f"Tras ir adelante: {mi_navegador['url']}")