import customtkinter as ctk
import random

class TaskManager(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Administrador de Tareas")
        self.geometry("600x400")  # Tamaño del administrador de tareas

        # Etiqueta de título
        self.title_label = ctk.CTkLabel(self, text="Administrador de Tareas", font=("Arial", 20))
        self.title_label.pack(pady=20)

        # Cuadro de lista de tareas (simulación de procesos)
        self.task_listbox = ctk.CTkTextbox(self, width=580, height=250)
        self.task_listbox.pack(pady=10, padx=10)

        # Lista para almacenar los procesos en ejecución
        self.processes = {}

    def add_task(self, task_name):
        """
        Agrega una tarea al administrador de tareas con un ID de proceso aleatorio.
        """
        process_id = random.randint(1000, 9999)  # Generar un ID de proceso aleatorio
        message = f"Ejecutando tarea: {task_name} con ID de proceso número {process_id}\n"
        self.task_listbox.insert("end", message)  # Añadir el mensaje a la lista de tareas
        self.processes[task_name] = process_id  # Guardar el proceso en ejecución

    def remove_task(self, task_name):
        """
        Elimina una tarea del administrador de tareas.
        """
        if task_name in self.processes:
            process_id = self.processes.pop(task_name)
            message = f"Finalizando tarea: {task_name} con ID de proceso número {process_id}\n"
            self.task_listbox.insert("end", message)  # Añadir el mensaje de finalización a la lista de tareas
