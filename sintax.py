import ply.yacc as yacc
import tokens as tok
from tokens import get_all, get_token_patterns, get_token_functions
import ply.lex as lex

# resultado del análisis
resultado_gramatica = []

# Definir los tokens para el parser
tokens = get_all()

for token in get_token_patterns(): 
    globals()[f't_{token[0]}'] = token[1]

for func in get_token_functions():
    globals()[f't_{func}'] = getattr(tok, f't_{func}')

# Precedencia de operadores
precedence = (
    ('right', 'ASSIGN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS'),
)

# Diccionario para almacenar variables
nombres = {}

# Reglas de la gramática
def p_program(t):
    'program : declaraciones'
    t[0] = t[1]

def p_declaraciones_lista(t):
    '''
    declaraciones : declaraciones declaracion
                  | declaracion
    '''
    if len(t) == 3:
        t[0] = t[1] + [t[2]]
    else:
        t[0] = [t[1]]

def p_declaracion_variable(t):
    'declaracion : tipo IDENTIFICADOR ASSIGN expresion SEMICOLON'
    nombres[t[2]] = t[4]
    t[0] = f"Declaración de variable: {t[2]} = {t[4]}"

def p_declaracion_asignacion(t):
    'declaracion : IDENTIFICADOR ASSIGN expresion SEMICOLON'
    nombres[t[1]] = t[3]
    t[0] = f"Asignación: {t[1]} = {t[3]}"

def p_declaracion_if(t):
    '''
    declaracion : IF LPAREN expresion RPAREN bloque
                | IF LPAREN expresion RPAREN bloque ELSE bloque
    '''
    if len(t) == 6:
        t[0] = f"IF({t[3]}) {t[5]}"
    else:
        t[0] = f"IF({t[3]}) {t[5]} ELSE {t[7]}"

def p_declaracion_while(t):
    'declaracion : WHILE LPAREN expresion RPAREN bloque'
    t[0] = f"WHILE({t[3]}) {t[5]}"

def p_bloque(t):
    '''
    bloque : LBRACE declaraciones RBRACE
           | LBRACE RBRACE
    '''
    if len(t) == 3:
        t[0] = "{}"
    else:
        t[0] = f"{{ {t[2]} }}"

def p_tipo(t):
    '''
    tipo : INT
         | FLOAT
         | BOOLEAN
         | CHAR
         | STRING
    '''
    t[0] = t[1]

def p_expresion_operaciones(t):
    '''
    expresion : expresion PLUS expresion
              | expresion MINUS expresion
              | expresion MULT expresion
              | expresion DIV expresion
    '''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]

def p_expresion_uminus(t):
    'expresion : MINUS expresion %prec UMINUS'
    t[0] = -t[2]

def p_expresion_grupo(t):
    'expresion : LPAREN expresion RPAREN'
    t[0] = t[2]

def p_expresion_literal(t):
    '''
    expresion : ENTERO
              | FLOAT_LITERAL
              | CADENA
    '''
    t[0] = t[1]

def p_expresion_nombre(t):
    'expresion : IDENTIFICADOR'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print(f"Nombre desconocido '{t[1]}'")
        t[0] = 0

def p_expresion_comparacion(t):
    '''
    expresion : expresion EQUALS expresion
    '''
    t[0] = t[1] == t[3]

def p_declaracion_incremento(t):
    'declaracion : IDENTIFICADOR INCREMENT SEMICOLON'
    if t[1] in nombres:
        nombres[t[1]] += 1  # Incrementar el valor de la variable en el diccionario
        t[0] = f"Incremento: {t[1]}++"
    else:
        print(f"Error: La variable '{t[1]}' no está definida.")
        t[0] = f"Error: Incremento fallido para '{t[1]}'"

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = f"Sintax error of type {t.type} in the value {t.value}"
        print(resultado)
    else:
        resultado = "Sintax error in empty input"
        print(resultado)
    resultado_gramatica.append(resultado)

# Instanciar el analizador sintáctico
parser = yacc.yacc()

# Función para probar el análisis sintáctico
def execute_sintax(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    gram = parser.parse(data, lexer=lex.lex())  # Procesar todo el código como un bloque
    if gram:
        if isinstance(gram, list):  # Si el resultado es una lista, extiende el resultado
            resultado_gramatica.extend(gram)
        else:  # Si no es una lista, simplemente añádelo
            resultado_gramatica.append(str(gram))

    # Mostrar cada elemento del resultado en una nueva línea
    print("Result:")
    for item in resultado_gramatica:
        print(f" - {item}")
    
    return resultado_gramatica

if __name__ == '__main__':
    while True:
        try:
            s = input('Ingresa dato >>> ')
        except EOFError:
            break
        if not s:
            continue
        execute_sintax(s)