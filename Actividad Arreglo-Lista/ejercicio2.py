def actualizar_leaderboard(top_10, nuevo_puntaje):
    if len(top_10) < 10 or nuevo_puntaje > top_10[-1]:
        top_10.append(nuevo_puntaje)
        top_10.sort(reverse=True)
        
        if len(top_10) > 10:
            top_10.pop()
            
    return top_10

def mostrar_leaderboard(lista):
    print("--- TOP 10 JUGADORES ---")
    for i in range(len(lista)):
        print(f"{i + 1}. Puntaje: {lista[i]}")

# --- PRUEBA DEL PROGRAMA ---

leaderboard = [950, 880, 720, 610, 550, 420, 330, 210, 150, 100]

mostrar_leaderboard(leaderboard)

print("\nNueva partida terminada: 500 puntos")
leaderboard = actualizar_leaderboard(leaderboard, 500)

mostrar_leaderboard(leaderboard)