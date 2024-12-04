from datetime import datetime

# Obtener la hora actual
hora_actual = datetime.now()

# Formatear la hora en un formato legible
hora_formateada = hora_actual.strftime("%H:%M:%S")

print("La hora exacta es:", hora_formateada)
