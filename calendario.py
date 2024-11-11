import calendar
from datetime import datetime

def mostrar_calendario(mes=None):
    año_actual = datetime.now().year
    print(f"Calendario del año {año_actual}\n")

    # Si se especifica un mes, mostramos solo ese mes; de lo contrario, mostramos el año completo
    if mes:
        print(calendar.month(año_actual, mes))
    else:
        print(calendar.TextCalendar().formatyear(año_actual))

# Ejemplo de uso
mostrar_calendario()       # Muestra el calendario del año completo
mostrar_calendario(11)     # Muestra solo el mes de noviembre
