import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
# Asegúrate de reemplazar 'datos_clima.csv' con la ruta de tu archivo CSV.
# El archivo debe tener columnas como 'Fecha', 'Temperatura', 'Humedad', 'Precipitaciones'.
archivo = 'archivo.csv'
datos = pd.read_csv(archivo)

# Convertir la columna de fecha a tipo datetime
datos['Fecha'] = pd.to_datetime(datos['Fecha'])

# Crear columnas adicionales para análisis
datos['Año'] = datos['Fecha'].dt.year
datos['Mes'] = datos['Fecha'].dt.month

# Resumen estadístico
print("Resumen de datos climáticos:")
print(datos.describe())

# Visualización de tendencias
plt.figure(figsize=(10, 6))
sns.lineplot(data=datos, x='Fecha', y='Temperatura', label='Temperatura')
sns.lineplot(data=datos, x='Fecha', y='Humedad', label='Humedad')
plt.title('Tendencias de Temperatura y Humedad')
plt.xlabel('Fecha')
plt.ylabel('Valores')
plt.legend()
plt.show()

# Análisis de precipitaciones por año
precipitaciones_por_año = datos.groupby('Año')['Precipitaciones'].sum()
plt.figure(figsize=(10, 6))
precipitaciones_por_año.plot(kind='bar', color='skyblue')
plt.title('Precipitaciones Totales por Año')
plt.xlabel('Año')
plt.ylabel('Precipitaciones (mm)')
plt.show()

# Correlación entre variables
correlacion = datos[['Temperatura', 'Humedad', 'Precipitaciones']].corr()
print("Matriz de correlación:")
print(correlacion)

# Visualización de la matriz de correlación
plt.figure(figsize=(8, 6))
sns.heatmap(correlacion, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlación')
plt.show()
