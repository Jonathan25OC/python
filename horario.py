# Definimos el horario del alumno en un diccionario
horario = {
    "Lunes": [("Matemáticas", "08:00 - 09:30"), ("Historia", "10:00 - 11:30"), ("Física", "12:00 - 13:30")],
    "Martes": [("Química", "08:00 - 09:30"), ("Literatura", "10:00 - 11:30"), ("Educación Física", "12:00 - 13:30")],
    "Miércoles": [("Matemáticas", "08:00 - 09:30"), ("Biología", "10:00 - 11:30"), ("Arte", "12:00 - 13:30")],
    "Jueves": [("Historia", "08:00 - 09:30"), ("Física", "10:00 - 11:30"), ("Química", "12:00 - 13:30")],
    "Viernes": [("Literatura", "08:00 - 09:30"), ("Matemáticas", "10:00 - 11:30"), ("Inglés", "12:00 - 13:30")]
}

# Función para mostrar el horario de un día específico
def mostrar_horario_dia(dia):
    if dia in horario:
        print(f"Horario para {dia}:")
        for clase, horas in horario[dia]:
            print(f"  - {clase} ({horas})")
    else:
        print("Día no válido. Introduzca un día entre lunes y viernes.")

# Función para mostrar el horario completo de la semana
def mostrar_horario_completo():
    for dia, clases in horario.items():
        print(f"\nHorario para {dia}:")
        for clase, horas in clases:
            print(f"  - {clase} ({horas})")

# Menú para el usuario
while True:
    print("\n1. Mostrar horario completo")
    print("2. Mostrar horario de un día específico")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_horario_completo()
    elif opcion == "2":
        dia = input("Introduzca el día de la semana (Lunes, Martes, etc.): ").capitalize()
        mostrar_horario_dia(dia)
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")