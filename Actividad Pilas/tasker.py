tasks = []

def menu():
    while True:
        print("\n==== Tareas TASKER ===== \n Bienvenid@, por favor elige uno de los numeros segun la opcion: ")
        print("1. Agregar tarea (Push)")
        print("2. Marcar tarea como terminada (Pop)")
        print("3. Ver tarea actual (Peek)")
        print("4. Hay tareas pendientes? (isEmpty)")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            tarea = input("Escribe la tarea: ")
            tasks.append(tarea) # Operación PUSH
            print(f"Tarea '{tarea}' agregada a la cima.")

        elif opcion == "2":
            if len(tasks) > 0: # Verificar que este con datos
                eliminada = tasks.pop() # Operación POP
                print(f"¡Hecho! Tarea '{eliminada}' eliminada.")
            else:
                print("No hay tareas para eliminar. La pila está vacía.")

        elif opcion == "3":
            if len(tasks) > 0:
                # El índice [-1] en Python accede al último elemento
                print(f"La tarea en la cima es: {tasks[-1]}") # Operación PEEK
            else:
                print("La pila está vacía.")

        elif opcion == "4":
            if not tasks: # Operación isEmpty
                print("La pila está vacía. ¡Día libre!")
            else:
                print(f"Tienes {len(tasks)} tareas en la pila.")

        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


menu()