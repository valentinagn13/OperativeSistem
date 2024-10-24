import customtkinter as ctk

class Calculator(ctk.CTk):
    def __init__(self, on_close_callback):
        super().__init__()
        self.title("Calculadora")
        self.geometry("300x400")  # Tamaño de la calculadora

        self.expression = ""
        self.input_text = ctk.StringVar()
        # Guardar la función de cierre
        self.on_close_callback = on_close_callback

        # Crear pantalla de la calculadora
        self.display = ctk.CTkEntry(self, textvariable=self.input_text, width=280, font=("Arial", 20), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        # Botones de la calculadora
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = ctk.CTkButton(self, text=text, width=60, height=60, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        # Botón para borrar (Clear)
        clear_button = ctk.CTkButton(self, text='C', width=60, height=60, command=self.clear_expression)
        clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Llamar a la función de cerrar al cerrar la ventana
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_button_click(self, char):
        """
        Maneja los eventos de clic en los botones de la calculadora.
        """
        if char == '=':
            self.calculate()
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

    def calculate(self):
        """
        Evalúa la expresión ingresada y muestra el resultado.
        """
        try:
            result = str(eval(self.expression))  # Calcula el resultado de la expresión
            self.input_text.set(result)  # Muestra el resultado
            self.expression = result  # Guarda el resultado para futuros cálculos
        except:
            self.input_text.set("Error")
            self.expression = ""

    def clear_expression(self):
        """
        Limpia la pantalla de la calculadora.
        """
        self.expression = ""
        self.input_text.set("")

    def on_close(self):
        """
        Maneja el evento de cierre de la ventana.
        Llama al callback proporcionado para notificar al TaskManager y luego destruye la ventana.
        """
        self.on_close_callback()  # Llama al callback para actualizar el TaskManager
        self.destroy()  # Cierra la ventana de la calculadora
