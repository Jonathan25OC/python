import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
file_path = 'sales.csv'  # Cambia esto por la ruta de tu archivo
data = pd.read_csv(file_path)

# Convertir la columna 'date' a formato de fecha
data['date'] = pd.to_datetime(data['date'])

# Verificar los datos cargados
print("Primeras filas del dataset:")
print(data.head())

# Agrupar las ventas por mes (análisis temporal)
data['month'] = data['date'].dt.to_period('M')  # Extraer año-mes
sales_by_month = data.groupby('month')['sales'].sum()

# Mostrar las ventas agrupadas
print("\nVentas totales por mes:")
print(sales_by_month)

# Graficar las ventas por mes
plt.figure(figsize=(10, 6))
sales_by_month.plot(kind='bar', color='skyblue')
plt.title('Ventas Totales por Mes', fontsize=16)
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Ventas Totales', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
