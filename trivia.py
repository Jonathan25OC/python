import random

# Lista de preguntas de trivia con respuestas
preguntas = [
    {
        "pregunta": "¿Cuál es la capital de Francia?",
        "opciones": ["A) Madrid", "B) Roma", "C) París", "D) Berlín"],
        "respuesta": "C"
    },
    {
        "pregunta": "¿Quién escribió 'Cien años de soledad'?",
        "opciones": ["A) Gabriel García Márquez", "B) Mario Vargas Llosa", "C) Jorge Luis Borges", "D) Isabel Allende"],
        "respuesta": "A"
    },
    {
        "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": ["A) Tierra", "B) Júpiter", "C) Marte", "D) Saturno"],
        "respuesta": "B"
    },
    {
        "pregunta": "¿En qué año llegó el hombre a la luna?",
        "opciones": ["A) 1959", "B) 1965", "C) 1969", "D) 1972"],
        "respuesta": "C"
    },
    {
        "pregunta": "¿Cuál es el océano más grande del mundo?",
        "opciones": ["A) Atlántico", "B) Índico", "C) Ártico", "D) Pacífico"],
        "respuesta": "D"
    }
]

# Función para hacer la trivia
def hacer_trivia(preguntas):
    puntuacion = 0
    print("¡Bienvenido a la Trivia!\n")

    # Mezclar preguntas para que el orden sea aleatorio
    preguntas_aleatorias = random.sample(preguntas, len(preguntas))
    
    # Iterar sobre cada pregunta
    for i, pregunta in enumerate(preguntas_aleatorias, 1):
        print(f"Pregunta {i}: {pregunta['pregunta']}")
        
        # Mostrar opciones
        for opcion in pregunta["opciones"]:
            print(opcion)
        
        # Pedir respuesta al usuario
        respuesta_usuario = input("Tu respuesta (A, B, C, D): ").upper()
        
        # Verificar respuesta
        if respuesta_usuario == pregunta["respuesta"]:
            print("¡Correcto!\n")
            puntuacion += 1
        else:
            print(f"Incorrecto. La respuesta correcta era {pregunta['respuesta']}.\n")

    # Mostrar puntuación final
    print(f"Has terminado la trivia. Tu puntuación final es {puntuacion} de {len(preguntas)}.")

# Ejecutar la trivia
hacer_trivia(preguntas)