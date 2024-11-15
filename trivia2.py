# Lista de preguntas, cada una con opciones y respuesta correcta
trivia = [
    {"pregunta": "¿Cuál es la capital de Francia?", "opciones": ["a) Madrid", "b) Roma", "c) París"], "respuesta": "c"},
    {"pregunta": "¿En qué continente se encuentra Egipto?", "opciones": ["a) Asia", "b) África", "c) Europa"], "respuesta": "b"},
    {"pregunta": "¿Cuál es el metal más común en la corteza terrestre?", "opciones": ["a) Aluminio", "b) Hierro", "c) Cobre"], "respuesta": "a"},
]

# Variables de puntuación y respuestas correctas
puntaje = 0
correctas = 0

print("¡Bienvenido a la trivia de conocimientos generales!\n")

# Bucle a través de las preguntas
for index, item in enumerate(trivia, start=1):
    print(f"Pregunta {index}: {item['pregunta']}")
    for opcion in item["opciones"]:
        print(opcion)
    
    respuesta_usuario = input("Tu respuesta (a/b/c): ").strip().lower()

    # Verificar si la respuesta es correcta
    if respuesta_usuario == item["respuesta"]:
        print("¡Respuesta correcta!")
        puntaje += 10
        correctas += 1
    else:
        print(f"Incorrecto. La respuesta correcta es '{item['respuesta']}'.")

    print()  # Espacio entre preguntas

# Mostrar el resultado final
print("¡Has terminado la trivia!")
print(f"Respondiste correctamente {correctas} de {len(trivia)} preguntas.")
print(f"Tu puntaje total es: {puntaje} puntos.")
