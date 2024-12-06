import customtkinter as ctk
import math

class Calculator(ctk.CTk):
    def __init__(self, on_close_callback):
        super().__init__()
        
        # Configuración de apariencia
        ctk.set_appearance_mode("dark")  # Modo oscuro
        ctk.set_default_color_theme("blue")  # Tema de color predeterminado
        
        self.title("Calculadora Científica")
        self.geometry("400x500") 
        
        # Variables de estado
        self.expression = ""
        self.input_text = ctk.StringVar()
        self.on_close_callback = on_close_callback
        
        # Configuración de fuentes
        title_font = ("Arial", 20, "bold")
        display_font = ("Consolas", 24)
        button_font = ("Arial", 16)
        
        # Título de la calculadora
        self.title_label = ctk.CTkLabel(self, text="Calculadora Científica", font=title_font)
        self.title_label.grid(row=0, column=0, columnspan=5, pady=(10, 20))
        
        # Pantalla de la calculadora 
        self.display = ctk.CTkEntry(
            self, 
            textvariable=self.input_text, 
            width=380, 
            font=display_font, 
            justify='right',
            state="readonly"  # Hace que no se pueda editar directamente
        )
        self.display.grid(row=1, column=0, columnspan=5, padx=10, pady=10)
        
        # Definir botones científicos y estándar
        scientific_buttons = [
            # Fila científica 1
            ('sin', 2, 0), ('cos', 2, 1), ('tan', 2, 2), ('log', 2, 3), ('ln', 2, 4),
            
            # Fila científica 2
            ('^2', 3, 0), ('√', 3, 1), ('π', 3, 2), ('e', 3, 3), ('!', 3, 4),
            
            # Números y operadores base
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('/', 4, 3), ('C', 4, 4),
            ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('*', 5, 3), ('(', 5, 4),
            ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('-', 6, 3), (')', 6, 4),
            ('0', 7, 0), ('.', 7, 1), ('+', 7, 2), ('=', 7, 3), ('Ans', 7, 4)
        ]
        
        #  botones
        for (text, row, col) in scientific_buttons:
            button = ctk.CTkButton(
                self, 
                text=text, 
                width=70, 
                height=50, 
                font=button_font,
                command=lambda t=text: self.on_button_click(t)
            )
            button.grid(row=row, column=col, padx=3, pady=3)
        
        # Configuración de cierre
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Variable para guardar respuesta anterior
        self.last_answer = None

    def on_button_click(self, char):
        """Maneja los eventos de clic de los botones."""
        if char == '=':
            self.calculate()
        elif char == 'C':
            self.clear_expression()
        elif char == 'Ans' and self.last_answer is not None:
            self.expression += str(self.last_answer)
            self.input_text.set(self.expression)
        else:
            # Mapeo de funciones científicas
            scientific_map = {
                'sin': 'math.sin(',
                'cos': 'math.cos(',
                'tan': 'math.tan(',
                'log': 'math.log10(',
                'ln': 'math.log(',
                '^3': '**3',
                '√': 'math.sqrt(',
                'π': 'math.pi',
                'e': 'math.e',
                '!': 'math.factorial(',
            }
            
            # Procesar funciones científicas
            if char in scientific_map:
                self.expression += scientific_map[char]
                self.input_text.set(self.expression)
            else:
                self.expression += str(char)
                self.input_text.set(self.expression)

    def calculate(self):
        """Evalúa la expresión con manejo de errores."""
        try:
            # Completar paréntesis abiertos
            while self.expression.count('(') > self.expression.count(')'):
                self.expression += ')'
            
            # Reemplazar factorial con llamada a math.factorial
            while '!' in self.expression:
                self.expression = self.expression.replace('!', ')')
                
            # Calcular resultado
            result = eval(self.expression)
            
            # Formatear resultado para evitar notación científica
            if abs(result) < 1e-4 or abs(result) > 1e6:
                formatted_result = f"{result:.6e}"
            else:
                formatted_result = f"{result:.6f}".rstrip('0').rstrip('.')
            
            self.input_text.set(formatted_result)
            self.last_answer = result
            self.expression = formatted_result
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""

    def clear_expression(self):
        """Limpia la pantalla de la calculadora."""
        self.expression = ""
        self.input_text.set("")
        self.last_answer = None

    def on_close(self):
        """Maneja el evento de cierre de la ventana."""
        self.on_close_callback()
        self.destroy()

if __name__ == "__main__":
    def close_callback():
        print("Calculadora cerrada")
    
    calculator = Calculator(close_callback)
    calculator.mainloop()