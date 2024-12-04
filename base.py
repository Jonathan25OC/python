import sqlite3

# Crear/Conectar a la base de datos
# Si la base de datos no existe, se creará automáticamente.
conexion = sqlite3.connect('mi_base_de_datos.db')

# Crear un cursor
cursor = conexion.cursor()

# Crear una tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER,
        correo TEXT
    )
''')

# Confirmar cambios
conexion.commit()

# Insertar datos en la tabla
cursor.execute('''
    INSERT INTO usuarios (nombre, edad, correo)
    VALUES ('Juan Perez', 30, 'juan.perez@example.com')
''')

# Insertar múltiples registros
usuarios = [
    ('Ana López', 25, 'ana.lopez@example.com'),
    ('Carlos García', 40, 'carlos.garcia@example.com'),
    ('María Fernández', 35, 'maria.fernandez@example.com')
]
cursor.executemany('''
    INSERT INTO usuarios (nombre, edad, correo)
    VALUES (?, ?, ?)
''', usuarios)

# Confirmar cambios
conexion.commit()

# Consultar datos
cursor.execute('SELECT * FROM usuarios')
usuarios_registrados = cursor.fetchall()

# Imprimir los resultados
print("Usuarios registrados:")
for usuario in usuarios_registrados:
    print(usuario)

# Cerrar la conexión
conexion.close()
