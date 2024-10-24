import customtkinter as ctk
from desk_page import DeskPage  # Importar la nueva ventana

class LoginPage(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Login")
        self.geometry("800x600")  # Puedes ajustar el tamaño si lo deseas
        self.state('zoomed')  # Pantalla completa

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

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Aquí puedes agregar validación para el login
        if username == "1" and password == "1":  # Ejemplo simple de validación
            self.open_desk()
        else:
            print("Usuario o contraseña incorrectos")

    def open_desk(self):
        self.destroy()  # Cerrar la ventana actual (login)
        desk = DeskPage()  # Crear una nueva ventana de escritorio
        desk.mainloop()  # Iniciar la ventana de escritorio
