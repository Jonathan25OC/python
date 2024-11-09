# Agenda en Python
agenda = {}

def agregar_evento():
    fecha = input("Ingrese la fecha del evento (formato DD/MM/AAAA): ")
    evento = input("Ingrese la descripción del evento: ")
    if fecha in agenda:
        agenda[fecha].append(evento)
    else:
        agenda[fecha] = [evento]
    print("Evento agregado correctamente.\n")

def ver_eventos():
    if agenda:
        print("Agenda:")
        for fecha, eventos in agenda.items():
            print(f"{fecha}:")
            for evento in eventos:
                print(f"  - {evento}")
    else:
        print("La agenda está vacía.\n")

def eliminar_evento():
    fecha = input("Ingrese la fecha del evento a eliminar (formato DD/MM/AAAA): ")
    if fecha in agenda:
        print(f"Eventos para {fecha}:")
        for idx, evento in enumerate(agenda[fecha], start=1):
            print(f"{idx}. {evento}")
        try:
            evento_idx = int(input("Ingrese el número del evento que desea eliminar: "))
            if 1 <= evento_idx <= len(agenda[fecha]):
                eliminado = agenda[fecha].pop(evento_idx - 1)
                print(f"Evento '{eliminado}' eliminado.\n")
                if not agenda[fecha]:  # Elimina la fecha si no quedan eventos
                    del agenda[fecha]
            else:
                print("Número de evento no válido.\n")
        except ValueError:
            print("Entrada no válida.\n")
    else:
        print("No hay eventos para esa fecha.\n")

def menu():
    while True:
        print("Seleccione una opción:")
        print("1. Agregar evento")
        print("2. Ver eventos")
        print("3. Eliminar evento")
        print("4. Salir")
        opcion = input("Opción: ")
        
        if opcion == "1":
            agregar_evento()
        elif opcion == "2":
            ver_eventos()
        elif opcion == "3":
            eliminar_evento()
        elif opcion == "4":
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")

# Ejecutar la agenda
menu()
