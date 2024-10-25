import customtkinter as ctk
import json
import os
from desk_page import DeskPage  # Importar la nueva ventana

# Ruta del archivo JSON donde se almacenarán los usuarios
USER_DATA_FILE = "users.json"
import json
import os

USER_DATA_FILE = "users.json"

class LoginPage(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Login")
        self.geometry("1200x900")
     #   self.state('zoomed')

        # Crear un frame central para organizar los widgets
        self.frame = ctk.CTkFrame(self, corner_radius=10)
        self.frame.pack(pady=100, padx=100, fill="both", expand=True)

        # Etiqueta de título
        self.label = ctk.CTkLabel(self.frame, text="Iniciar Sesión", font=("Arial", 30))
        self.label.pack(pady=25)

        # Campo para ingresar el nombre de usuario
        self.username_entry = ctk.CTkEntry(self.frame, placeholder_text="Usuario", width=300)
        self.username_entry.pack(pady=15)

        # Campo para ingresar la contraseña
        self.password_entry = ctk.CTkEntry(self.frame, placeholder_text="Contraseña", show="*", width=300)
        self.password_entry.pack(pady=15)

        # Botón de login
        self.login_button = ctk.CTkButton(self.frame, text="Login", command=self.login)
        self.login_button.pack(pady=25)

        # Botón de registro
        self.register_button = ctk.CTkButton(self.frame, text="Registrarse", command=self.register_user)
        self.register_button.pack(pady=15)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Cargar los usuarios desde el archivo JSON
        users = self.load_users()

        # Verificar si el usuario existe y la contraseña coincide
        if username in users and users[username] == password:
            self.open_desk()
        else:
            print("Usuario o contraseña incorrectos")

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            print("El nombre de usuario y la contraseña no pueden estar vacíos")
            return

        # Cargar los usuarios existentes
        users = self.load_users()

        # Verificar si el usuario ya existe
        if username in users:
            print("El usuario ya existe")
            return

        # Agregar el nuevo usuario al diccionario
        users[username] = password

        # Guardar el nuevo usuario en el archivo JSON
        self.save_users(users)
        print("Usuario registrado exitosamente")

    def load_users(self):
        """Carga los usuarios desde el archivo JSON. Si el archivo no existe o está vacío, retorna un diccionario vacío."""
        if os.path.exists(USER_DATA_FILE):
            try:
                with open(USER_DATA_FILE, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                # Si el archivo está vacío o no es válido, retorna un diccionario vacío
                return {}
        return {}

    def save_users(self, users):
        """Guarda el diccionario de usuarios en el archivo JSON."""
        with open(USER_DATA_FILE, "w") as f:
            json.dump(users, f, indent=4)

    def open_desk(self):
        self.destroy()  # Cerrar la ventana actual (login)
        desk = DeskPage()  # Crear una nueva ventana de escritorio
        desk.mainloop()  # Iniciar la ventana de escritorio

# Ejemplo de uso
if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
