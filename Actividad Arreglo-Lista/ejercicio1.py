# 1. Función para crear una página (nodo doble)
def crear_pagina(url):
    return {
        "url": url,
        "siguiente": None,
        "anterior": None
    }

def visitar_pagina(actual, nueva_url):
    nueva = crear_pagina(nueva_url)
    if actual is not None:
        actual["siguiente"] = nueva  
        nueva["anterior"] = actual    
    return nueva  


historial_actual = crear_pagina("google.com")
print(f"Estoy en: {historial_actual['url']}")

historial_actual = visitar_pagina(historial_actual, "youtube.com")
print(f"Visitando: {historial_actual['url']}")

historial_actual = visitar_pagina(historial_actual, "github.com")
print(f"Visitando: {historial_actual['url']}")


def ir_atras(actual):
    if actual["anterior"] is not None:
        print(f"Retrocediendo a: {actual['anterior']['url']}")
        return actual["anterior"]
    else:
        print("No hay páginas atrás.")
        return actual

def ir_adelante(actual):
    if actual["siguiente"] is not None:
        print(f"Avanzando a: {actual['siguiente']['url']}")
        return actual["siguiente"]
    else:
        print("No hay páginas adelante.")
        return actual


# PROBANDO LA NAVEGACIÓN
print("\n--- PRUEBA DE BOTONES ---")
historial_actual = ir_atras(historial_actual)   
historial_actual = ir_atras(historial_actual)    
historial_actual = ir_adelante(historial_actual)