import customtkinter as ctk
from PIL import Image
import time
from calculator import Calculator
from file_system import File
from notepad import Notepad
from tareas import TaskManager
from recursos import Administrador
import subprocess
import webbrowser
class DeskPage(ctk.CTk):
    def __init__(self, username):
        super().__init__()
        ctk.set_appearance_mode("dark")  # Modo oscuro

        # Configuración de la ventana principal del escritorio
        self.title("Desk")
        self.geometry("1200x900")
        self.state('zoomed')

        # Colores personalizados
        self.configure(bg_color="#2D2D2D")  # Fondo oscuro

        # Inicializar el administrador de tareas
        self.task_manager = TaskManager()

        # Etiqueta de bienvenida con el usuario actual
        self.label = ctk.CTkLabel(
            self, text=f"Bienvenido al Escritorio, {username}",
            font=("Arial", 24, "bold"), text_color="#E9967A"
        )
        self.label.pack(pady=60)

        # Barra de tareas estilizada
        self.taskbar = ctk.CTkFrame(self, height=40, fg_color="#333333", corner_radius=10)
        self.taskbar.pack(side="bottom", fill="x", padx=10, pady=10)

        # Iconos de la barra de tareas con bordes redondeados y sombras
        self.add_taskbar_icon("calculadora.png", "Calculadora", self.on_calculator_click)
        self.add_taskbar_icon("tareas.png", "Administrador de Tareas", self.on_task_manager_click)
        self.add_taskbar_icon("notas.png", "Bloc de Notas", self.on_notepad_click)
        self.add_taskbar_icon("carpeta.png", "File system", self.on_file_click)
        self.add_taskbar_icon("cromo.png", "Google", self.on_chrome_click)
        self.add_taskbar_icon("whatsapp.png", "WhatsApp", self.on_whatsapp_click)
        self.add_taskbar_icon("memoria-ram.png", "Recursos", self.on_recursos_click)
        # self.add__icon("memoria-ram.png", "Cerrar", self.on_close_click)

        # Reloj en la barra de tareas
        self.clock_label = ctk.CTkLabel(
            self.taskbar, text="", font=("Arial", 14, "bold"), text_color="#FFFFFF"
        )
        self.clock_label.pack(side="right", padx=10)
        self.update_clock()

        # Mantener DeskPage siempre al fondo
        self.lower()
        self.bind("<FocusIn>", self.keep_desk_in_background)
    def on_chrome_click(self):
            self.lower()
       
            # Abre Google Chrome usando subprocess o webbrowser
            url = "https://www.google.com"  # Puedes reemplazar esto por cualquier URL
            try:
                # Usar subprocess para abrir Chrome (asegurándote de que esté instalado y en la ruta)
                subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe", url])
            except Exception as e:
                print(f"Error al intentar abrir Google Chrome: {e}")
            # calc = Calculator(self.on_google_close)
            self.task_manager.add_task("Chrome")
            # calc.protocol("WM_DELETE_WINDOW", lambda: self.on_window_close(calc, "Chrome"))
            # calc.mainloop()

    def on_whatsapp_click(self):
        self.lower()

        # URL de WhatsApp Web
        url = "https://web.whatsapp.com"  # Abre WhatsApp Web en Chrome
        try:
            # Usar subprocess para abrir WhatsApp Web en Google Chrome
            subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe", url])
        except Exception as e:
            print(f"Error al intentar abrir WhatsApp Web: {e}")
        self.task_manager.add_task("WhatsApp")
        
    def keep_desk_in_background(self, event=None):
        """Mantiene la ventana DeskPage en el fondo cada vez que recibe foco."""
        self.lower()

    def on_task_manager_click(self):
        print("Hiciste clic en el Administrador de Tareas")
        self.lower()
        self.task_manager.mainloop()

    def add_taskbar_icon(self, image_path, tooltip_text, command):
        # Iconos personalizados con bordes y sombras
        image = ctk.CTkImage(light_image=Image.open(image_path), size=(30, 30))
        button = ctk.CTkButton(
            self.taskbar, image=image, text="", width=40, height=40,
            fg_color="#4A4A4A", hover_color="#616161", corner_radius=8,
            command=command
        )
        button.pack(side="left", padx=8, pady=5)
    def on_close_click(self):
        print("Hiciste clic el admin de recursos")
        # self.lower()
        recursos = Administrador(self.on_recursos_close)
        self.task_manager.add_task("Bloc de Notas")
        recursos.protocol("WM_DELETE_WINDOW", lambda: self.on_window_close(recursos, "Admin de recursos"))
        recursos.mainloop()
        
    def on_calculator_click(self):
        print("Hiciste clic en la Calculadora")
        # self.lower()
        calc = Calculator(self.on_calculator_close)
        self.task_manager.add_task("Calculadora")
        calc.protocol("WM_DELETE_WINDOW", lambda: self.on_window_close(calc, "Calculadora"))
        calc.mainloop()

    def on_notepad_click(self):
        print("Hiciste clic en el Bloc de Notas")
        # self.lower()
        notepad = Notepad(self.on_notepad_close)
        self.task_manager.add_task("Bloc de Notas")
        notepad.protocol("WM_DELETE_WINDOW", lambda: self.on_window_close(notepad, "Bloc de Notas"))
        notepad.mainloop()

    def on_recursos_click(self):
        print("Hiciste clic el admin de recursos")
        # self.lower()
        recursos = Administrador(self.on_recursos_close)
        self.task_manager.add_task("Bloc de Notas")
        recursos.protocol("WM_DELETE_WINDOW", lambda: self.on_window_close(recursos, "Admin de recursos"))
        recursos.mainloop()
    def on_file_click(self):
        print("Hiciste clic en file")
        self.lower()
        file = File(self.on_file_close)
        self.task_manager.add_task("File system")
        file.protocol("WM_DELETE_WINDOW", lambda: self.on_window_close(file, "File system"))
        file.mainloop()

    def on_window_close(self, window, task_name):
        print(f"Cerrando {task_name}")
        self.task_manager.remove_task(task_name)
        window.destroy()

    def on_calculator_close(self):
        print("La calculadora ha sido cerrada.")

    def on_google_close(self):
        print("La ventana Google ha sido cerrada.")
        
    def on_notepad_close(self):
        print("El Bloc de Notas ha sido cerrado.")
    def on_recursos_close(self):
        print("El admin de recursos se cerró.")
        
    def on_file_close(self):
        print("El sistema de archivos ha sido cerrado.")
        
    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.configure(text=current_time)
        self.after(1000, self.update_clock)
