import random
import string

def generar_contrasena(longitud=12):
    # Definir los caracteres que se utilizarán para generar la contraseña
    letras_minusculas = string.ascii_lowercase
    letras_mayusculas = string.ascii_uppercase
    digitos = string.digits
    caracteres_especiales = string.punctuation
    
    # Combinar todos los caracteres
    todos_los_caracteres = letras_minusculas + letras_mayusculas + digitos + caracteres_especiales
    
    # Asegurarse de que la contraseña contenga al menos un carácter de cada tipo
    contrasena = [
        random.choice(letras_minusculas),
        random.choice(letras_mayusculas),
        random.choice(digitos),
        random.choice(caracteres_especiales)
    ]
    
    # Completar la contraseña con caracteres aleatorios hasta alcanzar la longitud deseada
    contrasena += random.choices(todos_los_caracteres, k=longitud - 4)
    
    # Mezclar los caracteres para evitar patrones predecibles
    random.shuffle(contrasena)
    
    # Convertir la lista de caracteres en una cadena
    return ''.join(contrasena)

# Solicitar al usuario la longitud de la contraseña
longitud_deseada = int(input("Ingrese la longitud deseada para la contraseña: "))
contrasena_generada = generar_contrasena(longitud_deseada)

# Imprimir la contraseña generada
print(f"Contraseña generada: {contrasena_generada}")