import customtkinter as ctk
import psutil
import time
import threading
from tkinter import ttk

class Administrador(ctk.CTk):
    def __init__(self, on_close_callback):
        super().__init__()
        self.title("Administrador de Recursos")
        self.geometry("600x600")  # Tamaño de la ventana
        self.on_close_callback = on_close_callback

        # Crear un Frame para contener la tabla
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(pady=10, padx=10, expand=True, fill="both")

        # Crear la tabla (Treeview)
        self.tree = ttk.Treeview(self.table_frame, columns=("Parametro", "Valor"), show="headings", height=15)
        self.tree.pack(fill="both", expand=True)

        # Definir las columnas de la tabla
        self.tree.heading("Parametro", text="Parámetro")
        self.tree.heading("Valor", text="Valor")
        self.tree.column("Parametro", width=200, anchor="w")
        self.tree.column("Valor", width=300, anchor="w")

        # Crear un botón para actualizar la información
        self.refresh_button = ctk.CTkButton(self, text="Actualizar Información", command=self.update_info)
        self.refresh_button.pack(pady=5)

        # Crear un botón para limpiar la tabla
        self.clear_button = ctk.CTkButton(self, text="Limpiar", command=self.clear_table)
        self.clear_button.pack(pady=5)

        # Llamar a la función de cerrar al cerrar la ventana
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # Actualizar la información del sistema cada cierto intervalo
        self.update_info_thread = threading.Thread(target=self.auto_update_info)
        self.update_info_thread.daemon = True
        self.update_info_thread.start()

    def get_system_info(self):
        """Obtiene la información del sistema utilizando psutil."""
        info = []

        # Información sobre la CPU
        info.append(("Total de núcleos", psutil.cpu_count(logical=False)))
        info.append(("Núcleos lógicos", psutil.cpu_count(logical=True)))
        info.append(("Uso de la CPU (%)", psutil.cpu_percent(interval=1)))
        info.append(("Uso de la CPU por núcleo", str(psutil.cpu_percent(interval=1, percpu=True))))

        # Información sobre la memoria RAM
        memory = psutil.virtual_memory()
        info.append(("Memoria Total (GB)", f"{memory.total / (1024 ** 3):.2f}"))
        info.append(("Memoria Usada (GB)", f"{memory.used / (1024 ** 3):.2f}"))
        info.append(("Memoria Libre (GB)", f"{memory.available / (1024 ** 3):.2f}"))
        info.append(("Uso de Memoria (%)", memory.percent))

        # Información sobre el disco
        disk = psutil.disk_usage('/')
        info.append(("Espacio Total (GB)", f"{disk.total / (1024 ** 3):.2f}"))
        info.append(("Espacio Usado (GB)", f"{disk.used / (1024 ** 3):.2f}"))
        info.append(("Espacio Libre (GB)", f"{disk.free / (1024 ** 3):.2f}"))
        info.append(("Uso del Disco (%)", disk.percent))

        # Información sobre la red
        net_io = psutil.net_io_counters()
        info.append(("Bytes Enviados (MB)", f"{net_io.bytes_sent / (1024 ** 2):.2f}"))
        info.append(("Bytes Recibidos (MB)", f"{net_io.bytes_recv / (1024 ** 2):.2f}"))
        info.append(("Paquetes Enviados", net_io.packets_sent))
        info.append(("Paquetes Recibidos", net_io.packets_recv))

        return info

    def update_info(self):
        """Actualiza la información del sistema manualmente."""
        # Obtener la información
        info = self.get_system_info()

        # Limpiar la tabla antes de agregar nueva información
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insertar la nueva información en la tabla
        for param, value in info:
            self.tree.insert("", "end", values=(param, value))

    def auto_update_info(self):
        """Actualiza la información del sistema automáticamente cada 5 segundos."""
        while True:
            time.sleep(5)
            self.update_info()

    def clear_table(self):
        """Limpia la tabla."""
        for row in self.tree.get_children():
            self.tree.delete(row)

    def on_close(self):
        """Maneja el evento de cierre de la ventana."""
        self.on_close_callback()  # Llama al callback para actualizar el TaskManager
        self.destroy()  # Cierra la ventana del Administrador de Recursos

# Crear una función para manejar el cierre de la ventana
def on_close_callback():
    print("La ventana ha sido cerrada.")

# Crear y ejecutar la ventana de la aplicación
if __name__ == "__main__":
    app = Administrador(on_close_callback)
    app.mainloop()
