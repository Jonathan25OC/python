import re

# Especificación de patrones para los tokens
token_specification = [
    ('NUMBER', r'\d+(\.\d*)?'),    # Números: enteros o decimales
    ('IDENTIFIER', r'[A-Za-z_]\w*'), # Identificadores: variables, nombres
    ('ASSIGN', r'='),             # Operador de asignación
    ('OPERATOR', r'[+\-*/]'),     # Operadores matemáticos
    ('NEWLINE', r'\n'),           # Nueva línea
    ('SKIP', r'[ \t]+'),          # Espacios o tabulaciones
    ('MISMATCH', r'.'),           # Cualquier otro carácter no esperado
]

# Compilar las expresiones regulares en un patrón global
token_re = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
tokenizer = re.compile(token_re)

# Función para extraer tokens y lexemas
def lex_analyze(code):
    tokens = []
    for match in tokenizer.finditer(code):
        kind = match.lastgroup  # Tipo de token
        lexeme = match.group()  # Lexema correspondiente
        if kind == 'SKIP':
            continue  # Ignorar espacios en blanco
        elif kind == 'MISMATCH':
            raise ValueError(f"Carácter inesperado: {lexeme}")
        tokens.append((kind, lexeme))
    return tokens

# Ejemplo de código fuente
code = """x = 42
y = x + 3.14
"""

# Analizar el código y extraer tokens y lexemas
tokens = lex_analyze(code)

# Mostrar los resultados
for token_type, lexeme in tokens:
    print(f"Token: {token_type}, Lexema: '{lexeme}'")
