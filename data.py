# Importar bibliotecas necesarias
import pandas as pd

# Cargar el dataset (en este caso, un archivo CSV)
# Puedes usar un archivo que tengas, por ejemplo 'data.csv'
file_path = 'data.csv'  # Cambia esto por la ruta de tu archivo
data = pd.read_csv(file_path)

# Explorar los datos
print("Primeras 5 filas del dataset:")
print(data.head())  # Muestra las primeras 5 filas

print("\nResumen estadístico:")
print(data.describe())  # Resumen estadístico de las columnas numéricas

print("\nInformación general del dataset:")
print(data.info())  # Información general sobre el dataset

# Análisis simple: promedio de una columna (ejemplo: 'age')
if 'age' in data.columns:
    promedio_edad = data['age'].mean()
    print(f"\nEl promedio de edad es: {promedio_edad}")

# Filtrar datos (ejemplo: registros donde 'age' > 30)
if 'age' in data.columns:
    mayores_30 = data[data['age'] > 30]
    print(f"\nRegistros con edad mayor a 30:\n{mayores_30}")

# Guardar un subconjunto del dataset filtrado
output_path = 'filtered_data.csv'
if 'age' in data.columns:
    mayores_30.to_csv(output_path, index=False)
    print(f"\nDatos filtrados guardados en {output_path}")
