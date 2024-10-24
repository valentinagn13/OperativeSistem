import os
import customtkinter as ctk

class File(ctk.CTk):
    def __init__(self, on_close_callback):
        super().__init__()
        self.title("Explorador de Archivos")
        self.geometry("800x400")  # Tamaño del explorador de archivos
        # Guardar la función de cierre
        self.on_close_callback = on_close_callback

        # Crear un marco para las carpetas (lado izquierdo)
        self.left_frame = ctk.CTkFrame(self)
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)

        # Crear un marco para mostrar los archivos (lado derecho)
        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Listado de carpetas
        self.folders = ["Fotos", "Proyectos", "Descargas", "Música"]

        # Rutas a las carpetas (asegúrate de que existan en tu proyecto)
        self.photo_folder_path = "photo_folder"
        self.project_folder_path = "project_folder"
        self.download_folder_path = "download_folder"

        # Agregar botones para cada carpeta en el lado izquierdo
        for folder in self.folders:
            button = ctk.CTkButton(self.left_frame, text=folder, command=lambda f=folder: self.open_folder(f))
            button.pack(pady=5, fill="x")

        # Crear un área de texto para mostrar archivos en el lado derecho
        self.text_area = ctk.CTkTextbox(self.right_frame, width=380, height=350)
        self.text_area.pack(pady=10, padx=10, fill="both", expand=True)

        # Llamar a la función de cerrar al cerrar la ventana
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def open_folder(self, folder_name):
        """
        Maneja el evento de clic en una carpeta.
        Muestra los archivos dentro de la carpeta seleccionada en el área de texto.
        """
        # Limpiar el área de texto
        self.text_area.delete('1.0', ctk.END)

        if folder_name == "Fotos":
            self.show_photo_folder()
        elif folder_name == "Descargas":
            self.show_download_folder()
        elif folder_name == "Proyectos":
            self.show_project_folder()
        else:
            # Manejar otras carpetas (por ejemplo, "Música")
            self.text_area.insert(ctk.END, f"No hay archivos para mostrar en '{folder_name}'.")

    def show_photo_folder(self):
        """
        Muestra los archivos dentro de la carpeta photo_folder.
        """
        self.show_files_in_folder(self.photo_folder_path, "Fotos")

    def show_download_folder(self):
        """
        Muestra los archivos dentro de la carpeta download_folder.
        """
        self.show_files_in_folder(self.download_folder_path, "Descargas")

    def show_project_folder(self):
        """
        Muestra los archivos dentro de la carpeta project_folder.
        """
        self.show_files_in_folder(self.project_folder_path, "Proyectos")

    def show_files_in_folder(self, folder_path, folder_name):
        """
        Función genérica para mostrar archivos dentro de una carpeta.
        """
        if not os.path.exists(folder_path):
            self.text_area.insert(ctk.END, f"La carpeta '{folder_name}' no existe.\n")
            return

        # Obtener todos los archivos en la carpeta
        files = os.listdir(folder_path)

        if files:
            self.text_area.insert(ctk.END, f"Archivos en '{folder_name}':\n\n")
            for file in files:
                self.text_area.insert(ctk.END, f"- {file}\n")
        else:
            self.text_area.insert(ctk.END, f"No hay archivos en la carpeta '{folder_name}'.")

    def on_close(self):
        """
        Maneja el evento de cierre de la ventana.
        Llama al callback proporcionado para notificar al TaskManager y luego destruye la ventana.
        """
        self.on_close_callback()  # Llama al callback para actualizar el TaskManager
        self.destroy()  # Cierra la ventana del explorador de archivos

# Ejemplo de uso
if __name__ == "__main__":
    def on_close():
        print("Cerrando el explorador de archivos.")

    app = File(on_close)
    app.mainloop()
