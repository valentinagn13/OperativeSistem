import os
import customtkinter as ctk
import pygame  # Importar pygame para la reproducción de audio

class File(ctk.CTk):
    def __init__(self, on_close_callback):
        super().__init__()
        self.on_close_callback = on_close_callback
        
        # Inicializar pygame para reproducción de música
        pygame.mixer.init()

        # Leer el nombre del usuario desde session.json
        user_name = self.load_session()
        self.title(f"Explorador de Archivos de {user_name}")  # Personalizar el título
        self.geometry("800x400")  # Tamaño del explorador de archivos
        
        # Crear un marco para las carpetas (lado izquierdo)
        self.left_frame = ctk.CTkFrame(self)
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)

        # Crear un marco para mostrar los archivos (lado derecho)
        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Listado de carpetas
        self.folders = ["Fotos", "Proyectos", "Descargas", "Musica"]

        # Rutas a las carpetas
        self.photo_folder_path = "photo_folder"
        self.project_folder_path = "project_folder"
        self.download_folder_path = "download_folder"
        self.music_folder_path = "music_folder"


        # Agregar botones para cada carpeta en el lado izquierdo
        for folder in self.folders:
            button = ctk.CTkButton(self.left_frame, text=folder, command=lambda f=folder: self.open_folder(f))
            button.pack(pady=5, fill="x")

        # Crear un área de texto para mostrar archivos en el lado derecho
        self.text_area = ctk.CTkTextbox(self.right_frame, width=380, height=350)
        self.text_area.pack(pady=10, padx=10, fill="both", expand=True)

        # Llamar a la función de cerrar al cerrar la ventana
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_session(self):
        """
        Carga el nombre del usuario desde el archivo session.json.
        Si el archivo no existe o está vacío, devuelve un valor predeterminado.
        """
        session_file = "session.json"
        default_name = "Usuario"
        if os.path.exists(session_file):
            try:
                with open(session_file, "r") as file:
                    data = file.read().strip()  # Leer la palabra y quitar espacios
                    if data:  # Asegurarse de que no esté vacío
                        return data
            except Exception as e:
                print(f"Error al leer el archivo session.json: {e}")
        return default_name

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
        elif folder_name == "Musica":
            self.show_music_folder()
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

    def show_music_folder(self):
        """
        Muestra los archivos dentro de la carpeta música y agrega un botón para reproducir cada canción.
        """
        if not os.path.exists(self.music_folder_path):
            self.text_area.insert(ctk.END, f"La carpeta '{self.music_folder_path}' no existe.\n")
            return

        # Obtener todos los archivos en la carpeta
        files = os.listdir(self.music_folder_path)
        print(f"los archivos de canciones: {files}")
        self.show_files_in_folder(self.music_folder_path, "Musica")

        if files:
            self.text_area.insert(ctk.END, f"Archivos en '{self.music_folder_path}':\n\n")
            for file in files:
                if file.endswith(".mp3"):  # Solo mostrar archivos de audio
                    # Crear un botón para reproducir cada archivo
                    button = ctk.CTkButton(self.right_frame, text=f"Reproducir {file}", 
                                           command=lambda f=file: self.play_music(f))
                    button.pack(pady=5, fill="x")
        else:
            self.text_area.insert(ctk.END, f"No hay archivos en la carpeta '{self.music_folder_path}'.")

    def play_music(self, file_name):
        """
        Reproduce la música seleccionada.
        """
        song_path = os.path.join(self.music_folder_path, file_name)
        
        if os.path.exists(song_path):
            pygame.mixer.music.load(song_path)  # Cargar la canción
            pygame.mixer.music.play()  # Reproducirla
            self.text_area.insert(ctk.END, f"Reproduciendo: {file_name}\n")
        else:
            self.text_area.insert(ctk.END, f"No se pudo encontrar el archivo: {file_name}\n")

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
if __name__ == "__main__":
    app = File(on_close_callback)
    app.mainloop()