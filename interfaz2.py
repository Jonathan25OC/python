import re
import tkinter as tk
from tkinter import messagebox

# Definimos los patrones para los diferentes tokens
token_patterns = [
    (r'\d+', 'NUMBER'),          # Números
    (r'[a-zA-Z_]\w*', 'IDENTIFIER'),  # Identificadores
    (r'\+', 'PLUS'),             # Operador +
    (r'-', 'MINUS'),             # Operador -
    (r'\*', 'MULTIPLY'),         # Operador *
    (r'/', 'DIVIDE'),            # Operador /
    (r'=', 'ASSIGN'),            # Operador de asignación =
    (r'\(', 'LPAREN'),           # Paréntesis izquierdo
    (r'\)', 'RPAREN'),           # Paréntesis derecho
    (r'\s+', None),              # Espacios en blanco (ignorar)
]

# Función para tokenizar una entrada
def tokenize(text):
    tokens = []
    pos = 0
    while pos < len(text):
        match = None
        for pattern, token_type in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(text, pos)
            if match:
                lexeme = match.group(0)
                if token_type:  # Ignorar tokens sin tipo (como espacios)
                    tokens.append((token_type, lexeme))
                pos = match.end()
                break
        if not match:
            raise SyntaxError(f"Token no reconocido en la posición {pos}: '{text[pos]}'")
    return tokens

# Función para procesar el código ingresado y mostrar tokens generados
def process_input():
    code = code_input.get("1.0", tk.END).strip()  # Obtener texto del área de entrada
    if not code:
        messagebox.showwarning("Advertencia", "Por favor, ingrese código para analizar.")
        return
    
    try:
        tokens = tokenize(code)
        # Generar la salida como si se ejecutara el código
        exec_output = []
        exec_locals = {}
        try:
            exec(code, {}, exec_locals)
            exec_output.append(f"Salida del código ejecutado:\n{exec_locals}")
        except Exception as e:
            exec_output.append(f"Error al ejecutar el código:\n{str(e)}")
        
        # Mostrar tokens generados
        token_output = "Tokens generados:\n"
        for token_type, lexeme in tokens:
            token_output += f"Token: {token_type}, Lexema: {lexeme}\n"
        
        # Mostrar todo en el área de resultados
        result_output.delete("1.0", tk.END)
        result_output.insert(tk.END, token_output + "\n" + "\n".join(exec_output))
    except SyntaxError as e:
        messagebox.showerror("Error de Sintaxis", str(e))

# Crear la ventana principal
root = tk.Tk()
root.title("Tokenizador y Ejecutador de Código")

# Crear y ubicar los widgets
tk.Label(root, text="Ingrese el código:").pack(anchor="w", padx=10, pady=5)
code_input = tk.Text(root, height=10, width=50)
code_input.pack(padx=10, pady=5)

tk.Button(root, text="Analizar y Ejecutar", command=process_input).pack(pady=5)

tk.Label(root, text="Resultados:").pack(anchor="w", padx=10, pady=5)
result_output = tk.Text(root, height=15, width=50, state="normal")
result_output.pack(padx=10, pady=5)

# Iniciar la aplicación
root.mainloop()
