import random

def generar_correo(nombre, apellido, dominio='ejemplo.com'):
    # Genera un correo electrónico usando el nombre y apellido
    correo = f"{nombre}.{apellido}@{dominio}".lower()
    return correo

def generar_correos(nombres, apellidos, cantidad=5, dominio='ejemplo.com'):
    correos_generados = set()  # Usar un conjunto para evitar duplicados

    while len(correos_generados) < cantidad:
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        correo = generar_correo(nombre, apellido, dominio)
        correos_generados.add(correo)

    return list(correos_generados)

# Listas de nombres y apellidos
nombres = ['Juan', 'Ana', 'Pedro', 'Laura', 'Carlos', 'Marta']
apellidos = ['Gomez', 'Perez', 'Lopez', 'Martinez', 'Sanchez', 'Rodriguez']

# Generar correos
cantidad_deseada = 5
correos = generar_correos(nombres, apellidos, cantidad=cantidad_deseada)

# Imprimir los correos generados
for correo in correos:
    print(correo)