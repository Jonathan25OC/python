def generar_curp(apellido_paterno, apellido_materno, nombre, fecha_nacimiento, sexo, estado_nacimiento):
    # Diccionario para los códigos de estado
    estados = {
        "AGU": "Aguascalientes", "BCN": "Baja California", "BCS": "Baja California Sur",
        "CAM": "Campeche", "CHP": "Chiapas", "CHH": "Chihuahua", "COA": "Coahuila",
        "COL": "Colima", "DUR": "Durango", "GUA": "Guanajuato", "GRO": "Guerrero",
        "HID": "Hidalgo", "JAL": "Jalisco", "MEX": "Estado de México", "MIC": "Michoacán",
        "Mor": "Morelos", "NAY": "Nayarit", "NLE": "Nuevo León", "OAX": "Oaxaca",
        "PUE": "Puebla", "QUE": "Querétaro", "ROO": "Quintana Roo", "SLP": "San Luis Potosí",
        "SIN": "Sinaloa", "SON": "Sonora", "TAB": "Tabasco", "TAM": "Tamaulipas",
        "TLX": "Tlaxcala", "VER": "Veracruz", "YUC": "Yucatán", "ZAC": "Zacatecas"
    }

    # Obtener la primera letra del apellido paterno
    primer_letra_apellido_paterno = apellido_paterno[0].upper()
    
    # Obtener la primera vocal del apellido paterno
    for letra in apellido_paterno[1:]:
        if letra in 'AEIOU':
            primera_vocal_apellido_paterno = letra.upper()
            break
    else:
        primera_vocal_apellido_paterno = 'X'  # En caso de que no haya vocal

    # Obtener la primera letra del apellido materno
    primer_letra_apellido_materno = apellido_materno[0].upper()

    # Obtener la primera letra del nombre
    primer_letra_nombre = nombre[0].upper()

    # Obtener la fecha en el formato aammdd
    año = fecha_nacimiento[2:4]  # Dos últimos dígitos del año
    mes = fecha_nacimiento[5:7]   # Mes
    dia = fecha_nacimiento[8:10]   # Día

    # Sexo
    if sexo.lower() == 'm':
        sexo = 'H'  # Hombre
    else:
        sexo = 'M'  # Mujer

    # Obtener el código de estado
    codigo_estado = ''
    for clave, valor in estados.items():
        if valor.lower() == estado_nacimiento.lower():
            codigo_estado = clave
            break
    else:
        raise ValueError("Estado no válido.")

    # Generar la CURP
    curp = (primer_letra_apellido_paterno + primera_vocal_apellido_paterno +
            primer_letra_apellido_materno + primer_letra_nombre +
            año + mes + dia + sexo + codigo_estado)

    return curp


# Ejemplo de uso
apellido_paterno = "García"
apellido_materno = "López"
nombre = "Juan"
fecha_nacimiento = "1990-05-15"  # Formato: aaaa-mm-dd
sexo = "M"  # "M" para masculino, "F" para femenino
estado_nacimiento = "Jalisco"

curp_generada = generar_curp(apellido_paterno, apellido_materno, nombre, fecha_nacimiento, sexo, estado_nacimiento)
print(f"La CURP generada es: {curp_generada}")
