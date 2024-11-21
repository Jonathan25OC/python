import re

# Definimos los patrones para los diferentes tokens
token_patterns = [
    (r'\d+', 'NUMBER'),          # Números
    (r'[a-zA-Z_]\w*', 'IDENTIFIER'),  # Identificadores
    (r'\+', 'PLUS'),             # Operador +
    (r'-', 'MINUS'),             # Operador -
    (r'\*', 'MULTIPLY'),         # Operador *
    (r'/', 'DIVIDE'),            # Operador /
    (r'=', 'ASSIGN'),            # Operador de asignación =
    (r'\(', 'LPAREN'),           # Paréntesis izquierdo
    (r'\)', 'RPAREN'),           # Paréntesis derecho
    (r'\s+', None),              # Espacios en blanco (ignorar)
]

# Función para tokenizar una entrada
def tokenize(text):
    tokens = []
    pos = 0
    while pos < len(text):
        match = None
        for pattern, token_type in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(text, pos)
            if match:
                lexeme = match.group(0)
                if token_type:  # Ignorar tokens sin tipo (como espacios)
                    tokens.append((token_type, lexeme))
                pos = match.end()
                break
        if not match:
            raise SyntaxError(f"Token no reconocido en la posición {pos}: '{text[pos]}'")
    return tokens

# Ejemplo de uso
code = "x = 42 + (y - 5) * 2"
tokens = tokenize(code)
for token_type, lexeme in tokens:
    print(f"Token: {token_type}, Lexema: {lexeme}")
