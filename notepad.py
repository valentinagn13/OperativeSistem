import customtkinter as ctk
import google.generativeai as genai

# Configuración de la API de Google
genai.configure(api_key="apy_key")
model = genai.GenerativeModel("gemini-1.5-flash")

class Notepad(ctk.CTk):
    def __init__(self, on_close_callback):
        super().__init__()
        self.title("Bloc de Notas")
        self.geometry("600x600")  # Tamaño del bloc de notas
        self.on_close_callback = on_close_callback

        # Crear un cuadro de texto
        self.text_area = ctk.CTkTextbox(self, width=580, height=250)
        self.text_area.pack(pady=10, padx=10)

        # Botones para guardar y limpiar
        self.save_button = ctk.CTkButton(self, text="Guardar", command=self.save_note)
        self.save_button.pack(side="left", padx=10, pady=5)

        self.clear_button = ctk.CTkButton(self, text="Limpiar", command=self.clear_note)
        self.clear_button.pack(side="right", padx=10, pady=5)

        # Botón para interactuar con la API
        self.ask_button = ctk.CTkButton(self, text="Preguntar a la IA", command=self.ask_ai)
        self.ask_button.pack(pady=10)

        # Input para la pregunta
        self.question_input = ctk.CTkEntry(self, width=580)
        self.question_input.pack(pady=10)
        # Llamar a la función de cerrar al cerrar la ventana
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def save_note(self):
        """Guarda el contenido del cuadro de texto en un archivo."""
        note_text = self.text_area.get("1.0", "end-1c")  # Obtiene todo el texto del bloc de notas
        with open("nota.txt", "w") as file:
            file.write(note_text)  # Guarda el texto en un archivo llamado nota.txt
        print("Nota guardada")

    def clear_note(self):
        """Limpia el cuadro de texto."""
        self.text_area.delete("1.0", "end")

    def ask_ai(self):
        """Hace una pregunta a la API de IA y muestra la respuesta en el text_area."""
        question = self.question_input.get()  # Obtiene la pregunta del input
        if question:  # Si la pregunta no está vacía
            response = model.generate_content(question)  # Llama a la API con la pregunta
            self.text_area.insert("end", f"\nRespuesta: {response.text}\n\n")  # Inserta la pregunta y la respuesta en el text_area
        else:
            self.response_label.configure(text="Por favor ingresa una pregunta.")  # Mensaje de error si la pregunta está vacía

    def on_close(self):
        """Maneja el evento de cierre de la ventana."""
        self.on_close_callback()  # Llama al callback para actualizar el TaskManager
        self.destroy()  # Cierra la ventana del bloc de notas
