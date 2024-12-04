# Crear un array (lista) en Python
mi_array = [1, 2, 3, 4, 5]

# Imprimir el array
print("Array original:", mi_array)

# Acceder a elementos por índice
print("Elemento en el índice 2:", mi_array[2])

# Modificar un elemento en el array
mi_array[3] = 10
print("Array después de modificar el índice 3:", mi_array)

# Agregar un elemento al final del array
mi_array.append(6)
print("Array después de agregar un elemento:", mi_array)

# Eliminar un elemento por valor
mi_array.remove(2)
print("Array después de eliminar el valor 2:", mi_array)

# Eliminar un elemento por índice
del mi_array[1]
print("Array después de eliminar el elemento en el índice 1:", mi_array)

# Longitud del array
print("Longitud del array:", len(mi_array))

# Iterar a través del array
print("Elementos del array:")
for elem in mi_array:
    print(elem)
