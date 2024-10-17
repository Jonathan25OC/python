import tkinter as tk

def click_button(value):
    current = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(tk.END, current + value)

def clear():
    entry_field.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry_field.get())
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, str(result))
    except:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Crear el campo de entrada
entry_field = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry_field.grid(row=0, column=0, columnspan=4)

# Crear los botones de la calculadora
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Colocar los botones en la ventana
row = 1
col = 0
for button in buttons:
    tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), command=lambda b=button: click_button(b) if b != '=' else calculate()).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Botón para limpiar el campo de entrada
tk.Button(root, text='C', width=5, height=2, font=('Arial', 18), command=clear).grid(row=row, column=col)

# Iniciar el bucle de la interfaz gráfica
root.mainloop()
