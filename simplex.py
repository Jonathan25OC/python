import tkinter as tk
from tkinter import messagebox
from scipy.optimize import linprog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def resolver_simplex():
    try:
        c = list(map(float, entrada_c.get().split()))
        A = [list(map(float, row.split())) for row in entrada_A.get("1.0", tk.END).strip().split("\n")]
        b = list(map(float, entrada_b.get().split()))
        
        resultado = linprog(c, A_ub=A, b_ub=b, method='simplex')
        
        if resultado.success:
            messagebox.showinfo("Resultado", f"Valor óptimo: {resultado.fun}\nVariables: {resultado.x}")
            plot_graph(c, A, b, resultado.x)
        else:
            messagebox.showerror("Error", "No se encontró solución.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def plot_graph(c, A, b, optimal_solution):
    fig, ax = plt.subplots()

    # Configurar las restricciones como áreas sombreada
    x = [i for i in range(int(max(b)) + 1)]
    for i in range(len(A)):
        y = [(b[i] - A[i][0] * xi) / A[i][1] if A[i][1] != 0 else 0 for xi in x]
        ax.plot(x, y, label=f'Restricción {i+1}')

    # Dibujar la solución óptima
    ax.plot(optimal_solution[0], optimal_solution[1], 'ro', label='Solución Óptima')

    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.legend()
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, columnspan=2)

# Crear la ventana principal
root = tk.Tk()
root.title("Solucionador Método Simplex")

# Etiquetas y campos de entrada
tk.Label(root, text="Coeficientes de la Función Objetivo (c):").grid(row=0, column=0)
entrada_c = tk.Entry(root, width=50)
entrada_c.grid(row=0, column=1)

tk.Label(root, text="Coeficientes de las Restricciones (A):").grid(row=1, column=0)
entrada_A = tk.Text(root, height=10, width=50)
entrada_A.grid(row=1, column=1)

tk.Label(root, text="Límites de las Restricciones (b):").grid(row=2, column=0)
entrada_b = tk.Entry(root, width=50)
entrada_b.grid(row=2, column=1)

# Botón para resolver
boton_resolver = tk.Button(root, text="Resolver", command=resolver_simplex)
boton_resolver.grid(row=3, columnspan=2)

# Ejecutar la interfaz
root.mainloop()
