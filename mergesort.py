def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    # Dividir la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])

    # Mezclar las mitades ordenadas
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    # Comparar elementos y agregarlos en orden
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar los elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# Ejemplo de uso
mi_lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", mi_lista)
print("Lista ordenada:", merge_sort(mi_lista))
