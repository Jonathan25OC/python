import turtle

# Configuración de la pantalla
pantalla = turtle.Screen()
pantalla.bgcolor("white")
pantalla.title("Dibujo de una Flor")

# Crear el objeto "tortuga"
flor = turtle.Turtle()
flor.shape("turtle")
flor.speed(10)

# Función para dibujar un pétalo
def dibujar_petalo():
    for _ in range(2):
        flor.circle(100, 60)  # Dibujar un arco
        flor.left(120)       # Girar para el siguiente arco

# Dibujar la flor completa
flor.color("red", "pink")  # Color de contorno y relleno
flor.begin_fill()

for _ in range(6):  # Dibujar 6 pétalos
    dibujar_petalo()
    flor.right(60)  # Girar para el siguiente pétalo

flor.end_fill()

# Dibujar el tallo
flor.color("green")
flor.right(90)
flor.pensize(5)
flor.forward(300)

# Finalizar
flor.hideturtle()
pantalla.mainloop()
