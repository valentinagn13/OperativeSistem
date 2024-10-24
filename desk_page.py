import customtkinter as ctk
from PIL import Image  # Necesario para manejar las imágenes
import time
from calculator import Calculator  # Importa la clase Calculator
from file_system import File  # Importa la clase Calculator

from notepad import Notepad  # Importa el bloc de notas
from tareas import TaskManager  # Importa el administrador de tareas
class DeskPage(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal del escritorio
        self.title("Desk")
        self.geometry("800x600")  # Puedes ajustar el tamaño si lo deseas
        self.state('zoomed')  # Pantalla completa

        # Inicializar el administrador de tareas
        self.task_manager = TaskManager()

        # Etiqueta de bienvenida
        self.label = ctk.CTkLabel(self, text="Bienvenido al Escritorio", font=("Arial", 30))
        self.label.pack(pady=100)

        # Barra de tareas en la parte inferior
        self.taskbar = ctk.CTkFrame(self, height=40)
        self.taskbar.pack(side="bottom", fill="x")

        # Iconos de la barra de tareas (ejemplo con 3 iconos)
        self.add_taskbar_icon("archivo.png", "Calculadora", self.on_calculator_click)
        self.add_taskbar_icon("tareas.png", "Administrador de Tareas", self.on_task_manager_click)
        self.add_taskbar_icon("notas.png", "Bloc de Notas", self.on_notepad_click)
        self.add_taskbar_icon("carpeta.png", "File system", self.on_file_click)

        # Reloj en la barra de tareas
        self.clock_label = ctk.CTkLabel(self.taskbar, text="", font=("Arial", 12))
        self.clock_label.pack(side="right", padx=10)
        self.update_clock()
        
    def on_task_manager_click(self):
            print("Hiciste clic en el Administrador de Tareas")
            # Aquí puedes crear y mostrar la ventana del administrador de tareas
            # Por ejemplo:
            self.task_manager.mainloop()  # Asegúrate de que TaskManager tenga un método show()


    def add_taskbar_icon(self, image_path, tooltip_text, command):
        image = ctk.CTkImage(light_image=Image.open(image_path), size=(30, 30))
        button = ctk.CTkButton(self.taskbar, image=image, text="", width=40, command=command)
        button.pack(side="left", padx=5)

    def on_calculator_click(self):
        print("Hiciste clic en la Calculadora")
        calc = Calculator(self.on_calculator_close)  # Aquí se pasa el callback
        self.task_manager.add_task("Calculadora")
        calc.protocol("WM_DELETE_WINDOW", lambda: self.on_window_close(calc, "Calculadora"))
        calc.mainloop()

    def on_notepad_click(self):
        print("Hiciste clic en el Bloc de Notas")
        notepad = Notepad(self.on_notepad_close)
        self.task_manager.add_task("Bloc de Notas")
        notepad.protocol("WM_DELETE_WINDOW", lambda: self.on_window_close(notepad, "Bloc de Notas"))
        notepad.mainloop()

    def on_file_click(self):
        print("Hiciste clic en file")
        file = File(self.on_file_close)
        self.task_manager.add_task("File system")
        file.protocol("WM_DELETE_WINDOW", lambda: self.on_window_close(file, "Bloc de Notas"))
        file.mainloop()



    def on_window_close(self, window, task_name):
        print(f"Cerrando {task_name}")
        self.task_manager.remove_task(task_name)
        window.destroy()

    def on_calculator_close(self):
        print("La calculadora ha sido cerrada.")
        
    def on_notepad_close(self):
        print("La calculadora ha sido cerrada.")
        
    def on_file_close(self):
        print("La calculadora ha sido cerrada.")
        
    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.configure(text=current_time)
        self.after(1000, self.update_clock)
