import customtkinter as ctk
import random

class TaskManager(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Administrador de Tareas")
        self.geometry("400x500")

        # Etiqueta de título
        self.title_label = ctk.CTkLabel(self, text="Administrador de Tareas", font=("Arial", 20))
        self.title_label.pack(pady=20)

        # Cuadro de lista de tareas (marco contenedor)
        self.task_frame = ctk.CTkFrame(self)
        self.task_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Lista para almacenar los procesos en ejecución
        self.processes = {}

        # Encabezado de la tabla
        self.update_task_list()

    def update_task_list(self):
        """
        Actualiza la lista de tareas, mostrando el nombre de la tarea, su ID y un botón para eliminarla.
        """
        # Limpiar el contenido del task_frame
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        # Agregar encabezado
        header = ctk.CTkLabel(self.task_frame, text=f"{'Tarea':<30}{'ID del Proceso':>20}", anchor="w")
        header.pack(fill="x", padx=5, pady=5)
        
        # Línea de separación
        separator = ctk.CTkLabel(self.task_frame, text="-"*60)
        separator.pack(fill="x", padx=5)

        # Agregar tareas
        for task_name, process_id in self.processes.items():
            task_container = ctk.CTkFrame(self.task_frame)
            task_container.pack(fill="x", pady=5)

            # Etiqueta para el nombre de la tarea y el ID del proceso
            task_label = ctk.CTkLabel(task_container, text=f"{task_name:<30} ID: {process_id}", anchor="w")
            task_label.pack(side="left", padx=5)

            # Botón para eliminar la tarea
            delete_button = ctk.CTkButton(task_container, text="Eliminar", width=10,
                                          command=lambda t=task_name: self.remove_task(t))
            delete_button.pack(side="right", padx=5)

    def add_task(self, task_name):
        """
        Agrega una tarea al administrador de tareas con un ID de proceso aleatorio.
        """
        process_id = random.randint(1000, 9999)  # Generar un ID de proceso aleatorio
        self.processes[task_name] = process_id  # Guardar el proceso en ejecución
        self.update_task_list()  # Actualizar la lista de tareas

    def remove_task(self, task_name):
        """
        Elimina una tarea del administrador de tareas.
        """
        if task_name in self.processes:
            self.processes.pop(task_name)  # Remover de la lista de procesos
            self.update_task_list()  # Actualizar la lista después de eliminar una tarea

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = TaskManager()
    app.add_task("Ejemplo de Tarea")
    app.mainloop()
