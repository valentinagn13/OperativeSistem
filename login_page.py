import customtkinter as ctk
import json
import os
from desk_page import DeskPage
from file_system import File  # Importar la nueva ventana

# Ruta del archivo JSON donde se almacenarán los usuarios
USER_DATA_FILE = "users.json"
USER_DIRECTORY = "usuarios"  # Carpeta base donde se guardarán las carpetas de los usuarios
USER_DATA_SESSION="session.json"  #PARA GUARDAR EL USUSARIO Q HIZO LOGIN
class LoginPage(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("SISTEMA OPERATIVO POLAR")
        self.geometry("1500x700")
        self.configure(fg_color="#2b2b2b")  # Fondo oscuro

        # Crear un frame central estilizado para organizar los widgets
        self.frame = ctk.CTkFrame(self, corner_radius=20, fg_color="#3c3c3c")
        self.frame.pack(pady=50, padx=50, fill="both", expand=True)

        # Etiqueta de título con estilo
        self.label = ctk.CTkLabel(self.frame, text="Iniciar Sesión", font=("Arial", 30, "bold"), text_color="white")
        self.label.pack(pady=(20, 10))

        # Campo para ingresar el nombre de usuario con estilo
        self.username_entry = ctk.CTkEntry(self.frame, placeholder_text="Usuario", width=300, height=40, corner_radius=10, border_width=2)
        self.username_entry.pack(pady=15)

        # Campo para ingresar la contraseña con estilo
        self.password_entry = ctk.CTkEntry(self.frame, placeholder_text="Contraseña", show="*", width=300, height=40, corner_radius=10, border_width=2)
        self.password_entry.pack(pady=15)

        # Botón de login estilizado
        self.login_button = ctk.CTkButton(self.frame, text="Login", command=self.login, corner_radius=10, height=40, fg_color="#1f6aa5", hover_color="#164f7d")
        self.login_button.pack(pady=25)

        # Botón de registro estilizado
        self.register_button = ctk.CTkButton(self.frame, text="Registrarse", command=self.register_user, corner_radius=10, height=40, fg_color="#5c5c5c", hover_color="#4b4b4b")
        self.register_button.pack(pady=15)

        # Etiqueta para mensajes de estado
        self.message_label = ctk.CTkLabel(self.frame, text="", font=("Arial", 14), text_color="red")
        self.message_label.pack(pady=10)

        # Variable para guardar el usuario actual
        self.actualUser = None  # Inicializa ActualUser

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Cargar los usuarios desde el archivo JSON
        users = self.load_users()

        # Verificar si el usuario existe y la contraseña coincide
        if username in users and users[username] == password:
            self.actualUser = username  # Guardar el usuario actual
            self.message_label.configure(text="Inicio de sesión exitoso", text_color="green")
            self.after(950, self.open_desk)  # Abrir el escritorio después de un breve retraso
            self.save_session_user(username) #GUARDAR QUE USUARIO HIZO SESSION

        else:
            self.message_label.configure(text="Usuario o contraseña incorrectos", text_color="red")


    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            self.message_label.configure(text="El nombre de usuario y la contraseña no pueden estar vacíos", text_color="red")
            return

        # Cargar los usuarios existentes
        users = self.load_users()

        # Verificar si el usuario ya existe
        if username in users:
            self.message_label.configure(text="El usuario ya existe", text_color="red")
            return

        # Agregar el nuevo usuario al diccionario
        users[username] = password

        # Guardar el nuevo usuario en el archivo JSON
        self.save_users(users)

        # Crear carpeta del usuario y subcarpetas predeterminadas
        self.crear_estructura_directorios(username)

        self.message_label.configure(text=f"Usuario {username} registrado exitosamente", text_color="green")

    def crear_estructura_directorios(self, username):
        """Crea una carpeta con el nombre del usuario y algunas subcarpetas dentro (imagenes, documentos, descargas)."""
        try:
            ruta_usuario = os.path.join(USER_DIRECTORY, username)
            os.makedirs(ruta_usuario, exist_ok=True)
            subcarpetas = ["imagenes", "documentos", "descargas"]
            for carpeta in subcarpetas:
                os.makedirs(os.path.join(ruta_usuario, carpeta), exist_ok=True)
        except Exception as e:
            self.message_label.configure(text=f"Error al crear carpetas para {username}: {e}", text_color="red")

    def load_users(self):
        """Carga los usuarios desde el archivo JSON. Si el archivo no existe o está vacío, retorna un diccionario vacío."""
        if os.path.exists(USER_DATA_FILE):
            try:
                with open(USER_DATA_FILE, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_users(self, users):
        """Guarda el diccionario de usuarios en el archivo JSON."""
        with open(USER_DATA_FILE, "w") as f:
            json.dump(users, f, indent=4)
            
    def save_session_user(self, users):
        """Guarda el diccionario dEL USER en el archivo JSON."""
        with open(USER_DATA_SESSION, "w") as f:
            json.dump(users, f, indent=4)
            
    def open_desk(self):
        self.destroy()  # Cerrar la ventana actual (login)
        desk = DeskPage(self.actualUser)  # Crear una nueva ventana de escritorio pasando el usuario actual
        desk.mainloop()
        file = File(self.actualUser)

# Ejemplo de uso
if __name__ == "__main__":
    if not os.path.exists(USER_DIRECTORY):
        os.makedirs(USER_DIRECTORY)
    app = LoginPage()
    app.mainloop()
