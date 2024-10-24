import customtkinter as ctk

class Notepad(ctk.CTk):
    def __init__(self, on_close_callback):
        super().__init__()
        self.title("Bloc de Notas")
        self.geometry("600x400")  # Tamaño del bloc de notas
        # Guardar la función de cierre
        self.on_close_callback = on_close_callback

        # Crear un cuadro de texto
        self.text_area = ctk.CTkTextbox(self, width=580, height=350)
        self.text_area.pack(pady=10, padx=10)

        # Botones para guardar y limpiar
        self.save_button = ctk.CTkButton(self, text="Guardar", command=self.save_note)
        self.save_button.pack(side="left", padx=10, pady=5)

        self.clear_button = ctk.CTkButton(self, text="Limpiar", command=self.clear_note)
        self.clear_button.pack(side="right", padx=10, pady=5)

        # Llamar a la función de cerrar al cerrar la ventana
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def save_note(self):
        """
        Guarda el contenido del cuadro de texto en un archivo.
        """
        note_text = self.text_area.get("1.0", "end-1c")  # Obtiene todo el texto del bloc de notas
        with open("nota.txt", "w") as file:
            file.write(note_text)  # Guarda el texto en un archivo llamado nota.txt
        print("Nota guardada")

    def clear_note(self):
        """
        Limpia el cuadro de texto.
        """
        self.text_area.delete("1.0", "end")

    def on_close(self):
        """
        Maneja el evento de cierre de la ventana.
        Llama al callback proporcionado para notificar al TaskManager y luego destruye la ventana.
        """
        self.on_close_callback()  # Llama al callback para actualizar el TaskManager
        self.destroy()  # Cierra la ventana del bloc de notas
