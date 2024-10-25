import customtkinter as ctk
import random
import customtkinter as ctk
import random

class TaskManager(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Administrador de Tareas")
        self.geometry("300x400")  # Tamaño del administrador de tareas

        # Etiqueta de título
        self.title_label = ctk.CTkLabel(self, text="Administrador de Tareas", font=("Arial", 20))
        self.title_label.pack(pady=20)

        # Cuadro de lista de tareas (simulación de procesos)
        self.task_listbox = ctk.CTkTextbox(self, width=580, height=250)
        self.task_listbox.pack(pady=10, padx=10)

        # Lista para almacenar los procesos en ejecución
        self.processes = {}

        # Encabezado de la tabla
        self.update_task_listbox_header()

    def update_task_listbox_header(self):
        """
        Actualiza el encabezado del cuadro de lista de tareas para mostrar los nombres de las columnas.
        """
        self.task_listbox.delete("1.0", "end")  # Limpiar el cuadro de texto
        header = f"{'Tarea':<40}{'ID del Proceso':>20}\n"
        self.task_listbox.insert("end", header)
        self.task_listbox.insert("end", "-"*60 + "\n")

    def update_task_list(self):
        """
        Actualiza el cuadro de lista de tareas con el formato de tabla.
        """
        self.update_task_listbox_header()  # Restablecer el encabezado antes de listar los procesos
        for task_name, process_id in self.processes.items():
            task_row = f"{task_name:<40}{process_id:>20}\n"  # Formato de tabla
            self.task_listbox.insert("end", task_row)

    def add_task(self, task_name):
        """
        Agrega una tarea al administrador de tareas con un ID de proceso aleatorio.
        """
        process_id = random.randint(1000, 9999)  # Generar un ID de proceso aleatorio
        self.processes[task_name] = process_id  # Guardar el proceso en ejecución
        self.update_task_list()  # Actualizar la lista de tareas formateada

    def remove_task(self, task_name):
        """
        Elimina una tarea del administrador de tareas.
        """
        if task_name in self.processes:
            process_id = self.processes.pop(task_name)
            self.update_task_list()  # Actualizar la lista de tareas después de eliminar una
