import tkinter as tk
from tkinter import messagebox

class CuestionarioApp:
    def __init__(self, master):
        self.master = master
        master.title("Cuestionario: Sistemas Expertos")
        master.geometry("700x500")
        master.configure(bg="#f0f0f0") 

        self.preguntas_data = [
            {
                "pregunta": "1. Rol principal de un Sistema Experto:",
                "opciones": [
                    "a) Reemplazar por completo a los expertos humanos en la toma de decisiones.",
                    "b) Seguir procedimientos algorítmicos complejos definidos por el desarrollador.",
                    "c) Emular (imitar) las actividades humanas que requieren pensamiento, habilidades y experiencia acumulada.",
                    "d) Generar programas de software convencional con alta eficiencia económica."
                ],
                "respuesta_correcta_idx": 2 # Opción 'c'
            },
            {
                "pregunta": "2. ¿Cuál de los siguientes triadas representa los componentes esenciales de un Sistema Experto?",
                "opciones": [
                    "a) Base de Datos, Modelo de Datos y Servidor.",
                    "b) Base de Conocimientos (BC), Motor de Inferencia (MI) e Interfaz Inteligente (II).",
                    "c) Software convencional, Hardware y Periféricos.",
                    "d) Ingeniero del Conocimiento, Experto del Dominio y Usuario Final."
                ],
                "respuesta_correcta_idx": 1 # Opción 'b'
            },
            {
                "pregunta": "3. El conocimiento que se basa en reglas prácticas o 'reglas de oro' que un experto utiliza para resolver problemas se denomina:",
                "opciones": [
                    "a) Conocimiento Factual.",
                    "b) Conocimiento Algorítmico.",
                    "c) Conocimiento Heurístico.",
                    "d) Conocimiento Estructurado."
                ],
                "respuesta_correcta_idx": 2 # Opción 'c'
            },
            {
                "pregunta": "4. El mecanismo de inferencia que comienza con los datos conocidos y procede 'hacia adelante' para deducir una conclusión ('¿Qué puede suceder después?') se conoce como :",
                "opciones": [
                    "a) Encadenamiento Hacia Adelante (Forward Chaining).",
                    "b) Encadenamiento Hacia Atrás (Backward Chaining).",
                    "c) Inferencia Declarativa.",
                    "d) Inferencia Iterativa."
                ],
                "respuesta_correcta_idx": 0 # Opción 'a'
            },
            {
                "pregunta": "5. ¿Qué mecanismo de inferencia es más apropiado cuando el sistema comienza con una hipótesis o un objetivo y busca la evidencia necesaria para probarlo ('¿Por qué sucedió esto?')?",
                "opciones": [
                    "a) Encadenamiento Lógico.",
                    "b) Encadenamiento Hacia Adelante.",
                    "c) Encadenamiento Hacia Atrás (Backward Chaining).",
                    "d) Razonamiento Heurístico."
                ],
                "respuesta_correcta_idx": 2 # Opción 'c'
            },
            {
                "pregunta": "6. La etapa del desarrollo de un Sistema Experto que es ampliamente considerada como el 'cuello de botella' debido a la dificultad de capturar y explicitar el conocimiento tácito de los especialistas es:",
                "opciones": [
                    "a) Identificación.",
                    "b) Adquisición de Conocimiento.",
                    "c) Implementación.",
                    "d) Formalización."
                ],
                "respuesta_correcta_idx": 1 # Opción 'b'
            },
            {
                "pregunta": "7. ¿Cuál es la responsabilidad principal del Ingeniero del Conocimiento (IC) en el equipo de desarrollo de un SE?",
                "opciones": [
                    "a) Proporcionar la experiencia profunda del dominio a ser capturada.",
                    "b) Garantizar la disponibilidad del hardware y software.",
                    "c) Diseñar, construir y probar el SE, incluyendo la estructuración del conocimiento.",
                    "d) Ser el usuario final que evaluará la satisfacción del sistema."
                ],
                "respuesta_correcta_idx": 2 # Opción 'c'
            },
            {
                "pregunta": "8. Un requisito crítico para que el desarrollo de un Sistema Experto sea viable es:",
                "opciones": [
                    "a) Que el problema sea tan amplio que cubra muchas áreas temáticas.",
                    "b) Que el experto del dominio sea reacio a participar en el proyecto.",
                    "c) La existencia de un experto del dominio reconocido, dispuesto y capaz de comunicar su conocimiento.",
                    "d) Que el desarrollo se base en un proceso lineal no iterativo."
                ],
                "respuesta_correcta_idx": 2 # Opción 'c'
            },
            {
                "pregunta": "9. La actividad de 'Verificación' durante la etapa de Pruebas se enfoca en:",
                "opciones": [
                    "a) Asegurar que el sistema cumple con los requisitos del usuario.",
                    "b) Demostrar la consistencia y corrección del software.",
                    "c) Determinar la disponibilidad de recursos humanos y económicos.",
                    "d) Seleccionar el mecanismo de representación de conocimiento más eficiente."
                ],
                "respuesta_correcta_idx": 1 # Opción 'b'
            },
            {
                "pregunta": "10. La etapa de 'Formalización' en la metodología de desarrollo de un SE implica principalmente:",
                "opciones": [
                    "a) La captura inicial de la experiencia mediante entrevistas.",
                    "b) La planificación de los recursos y la identificación de las fuentes de conocimiento.",
                    "c) La selección del método de representación del conocimiento (ej. reglas, frames) y la definición de la inferencia lógica.",
                    "d) El análisis de conceptos básicos y sus relaciones."
                ],
                "respuesta_correcta_idx": 2 # Opción 'c'
            },
        ]

        self.pregunta_actual_idx = 0
        self.puntuacion = 0
        self.total_preguntas = len(self.preguntas_data)
        self.respuesta_seleccionada = tk.IntVar(master, value=-1)

        self.frame_bienvenida = tk.Frame(master, bg="#f0f0f0")
        self.crear_pantalla_bienvenida()

    def crear_pantalla_bienvenida(self):
        
        for widget in self.master.winfo_children():
            widget.pack_forget()
            
        self.frame_bienvenida.pack(expand=True, fill="both")
        
        label_titulo = tk.Label(self.frame_bienvenida, text="Bienvenido al Cuestionario de Sistemas Expertos", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#004d40")
        label_titulo.pack(pady=50, padx=20)

        label_creditos = tk.Label(self.frame_bienvenida, text="Hecho por:\nJuan Martinez y Daniela Rodriguez", font=("Arial", 14), bg="#f0f0f0", fg="#333333")
        label_creditos.pack(pady=20, padx=20)

        boton_inicio = tk.Button(self.frame_bienvenida, text="Iniciar Cuestionario", command=self.cargar_interfaz_cuestionario, font=("Arial", 16, "bold"), bg="#4CAF50", fg="white",  padx=20, pady=10, relief=tk.RAISED)
        boton_inicio.pack(pady=40)

    def cargar_interfaz_cuestionario(self):
        """Oculta la bienvenida y construye la interfaz principal del cuestionario."""
        
        self.frame_bienvenida.pack_forget()

        self.frame_pregunta = tk.Frame(self.master, padx=10, pady=10, bg="#ffffff", relief=tk.GROOVE, borderwidth=2)
        
        self.frame_pregunta.pack(pady=20, padx=20, fill="x")

        self.label_pregunta = tk.Label(self.frame_pregunta, text="", wraplength=650, justify=tk.LEFT, font=("Arial", 14, "bold"), bg="#ffffff", fg="#333333")
        
        self.label_pregunta.pack(pady=10, padx=10, fill="x")

        self.frame_opciones = tk.Frame(self.master, padx=10, pady=10, bg="#f0f0f0")
        
        self.frame_opciones.pack(padx=20, fill="x")

        self.radio_buttons = []

        self.boton_verificar = tk.Button(self.master, text="Verificar Respuesta", command=self.verificar_respuesta, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
        
        self.boton_verificar.pack(pady=20)

        self.label_puntuacion = tk.Label(self.master, text=f"Puntuación: 0 / {self.total_preguntas}", font=("Arial", 12), bg="#f0f0f0", fg="#555555")
        
        self.label_puntuacion.pack(pady=5)
        
        # Inicia el cuestionario
        self.cargar_pregunta()

    def cargar_pregunta(self):
        if self.pregunta_actual_idx < self.total_preguntas:
            pregunta_actual = self.preguntas_data[self.pregunta_actual_idx]
            
            # 1. Actualizar el Label de la Pregunta
            self.label_pregunta.config(text=pregunta_actual["pregunta"])
            
            # 2. Eliminar botones anteriores si existen
            for rb in self.radio_buttons:
                rb.destroy()
            self.radio_buttons = []
            
            self.respuesta_seleccionada.set(-1) # Restablecer la selección
            for i, opcion in enumerate(pregunta_actual["opciones"]):
                rb = tk.Radiobutton(self.frame_opciones, text=opcion, variable=self.respuesta_seleccionada,
   value=i, font=("Arial", 12), justify=tk.LEFT, anchor="w",
   bg="#f0f0f0", fg="#000000", selectcolor="#E0E0E0")
                rb.pack(anchor="w", pady=5, fill="x")
                self.radio_buttons.append(rb)
            
            self.boton_verificar.config(text="Verificar Respuesta", command=self.verificar_respuesta)
        else:
            self.mostrar_resultado_final()

    def verificar_respuesta(self):
        """Verifica la respuesta """
        respuesta_usuario_idx = self.respuesta_seleccionada.get()
        
        if respuesta_usuario_idx == -1:
            messagebox.showwarning("Atención", "Por favor, selecciona una opción antes de verificar.")
            return

        pregunta_actual = self.preguntas_data[self.pregunta_actual_idx]
        correcta_idx = pregunta_actual["respuesta_correcta_idx"]

        # Compara la respuesta
        es_correcta = (respuesta_usuario_idx == correcta_idx)
        
        if es_correcta:
            self.puntuacion += 1
            feedback_msg = "¡Correcto!"
            self.radio_buttons[correcta_idx].config(fg="#006400", bg="#D4EDDA") 
        else:
            feedback_msg = "Incorrecto."
            self.radio_buttons[respuesta_usuario_idx].config(fg="#8B0000", bg="#F8D7DA")
            self.radio_buttons[correcta_idx].config(fg="#006400", bg="#D4EDDA")
            
        for rb in self.radio_buttons:
            rb.config(state=tk.DISABLED)

        # Actualizar puntuación
        self.label_puntuacion.config(text=f"Puntuación: {self.puntuacion} / {self.total_preguntas}")
        
        messagebox.showinfo("Resultado", feedback_msg)

        # Prepara siguiente pregunta
        self.pregunta_actual_idx += 1
        self.boton_verificar.config(text="Siguiente Pregunta", command=self.cargar_pregunta)


    def mostrar_resultado_final(self):
        
        self.boton_verificar.pack_forget() 
        
        resultado_final = f"¡Cuestionario Terminado! \nTu Puntuación Final es: {self.puntuacion} de {self.total_preguntas}"
        
        messagebox.showinfo("Fin del Cuestionario", resultado_final)
        
        # Limpiar y mostrar el resultado
        self.frame_pregunta.pack_forget()
        self.frame_opciones.pack_forget()
        self.label_puntuacion.config(text=resultado_final, font=("Arial", 16, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    app = CuestionarioApp(root)
    root.mainloop()