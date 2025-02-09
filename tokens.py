def get_reserved():
    return (
        'INCLUDE',
        'USING',
        'NAMESPACE',
        'STD',
        'COUT',
        'CIN',
        'GET',
        'RETURN',
        'VOID',
        'INT',
        'ENDL',
    )

def get_math():
    return (
        'SUMA',
        'RESTA',
        'MULT',
        'DIV',
        'POTENCIA',
        'MODULO',
        'MINUSMINUS',
        'PLUSPLUS',
    )

def get_conditions():
    return (
        'SI',
        'SINO',
    )

def get_loops():
    return (
        'MIENTRAS',
        'PARA',
    )

def get_logic():
    return (
        'AND',
        'OR',
        'NOT',
        'IGUAL',
        'DIFERENTE',
        'MAYOR',
        'MENOR',
        'MENORQUE',
        'MAYORQUE',
        'MAYORIGUAL',
        'MENORIGUAL',
        'DISTINTO',
    )

def get_others():
    return (
        'NUMERAL',
        'PARIZQ',
        'PARDER',
        'CORIZQ',
        'CORDER',
        'LLAIZQ',
        'LLADER',
        'PUNTOCOMA',
        'COMA',
        'COMDOB',
        'MAYORDER',
        'MAYORIZQ',
    )

def get_sintax():
    return (
        'IDENTIFICADOR',
        'ENTERO',
        'ASIGNAR',
        'CADENA'
    )

def get_all():
    return get_reserved() + get_math() + get_conditions() + get_loops() + get_logic() + get_others() + get_sintax()

def get_token_patterns():
    return [
        ['SUMA', r'\+'],
        ['RESTA', r'-'],
        ['MINUSMINUS', r'\-\-'],
        ['MULT', r'\*'],
        ['DIV', r'/'],
        ['MODULO', r'\%'],
        ['POTENCIA', r'(\*{2} | \^)'],
        ['ASIGNAR', r'='],
        ['AND', r'\&\&'],
        ['OR', r'\|{2}'],
        ['NOT', r'\!'],
        ['MENORQUE', r'<'],
        ['MAYORQUE', r'>'],
        ['PUNTOCOMA', ';'],
        ['COMA', r','],
        ['PARIZQ', r'\('],
        ['PARDER', r'\)'],
        ['CORIZQ', r'\['],
        ['CORDER', r'\]'],
        ['LLAIZQ', r'{'],
        ['LLADER', r'}'],
        ['COMDOB', r'\"'],
        ['ignore', ' \t']
    ]

def get_token_functions():
    return [
        'INCLUDE', 'USING', 'NAMESPACE', 'STD', 'COUT', 'CIN', 'GET', 'ENDL',
        'SINO', 'SI', 'RETURN', 'VOID', 'MIENTRAS', 'PARA', 'ENTERO', 'IDENTIFICADOR',
        'CADENA', 'NUMERAL', 'PLUSPLUS', 'MENORIGUAL', 'MAYORIGUAL', 'IGUAL', 'MAYORDER',
        'MAYORIZQ', 'DISTINTO', 'newline', 'comments', 'comments_ONELine', 'error'
    ]

def t_INCLUDE(t):
    r'include'
    return t

def t_USING(t):
    r'using'
    return t

def t_NAMESPACE(t):
    r'namespace'
    return t

def t_STD(t):
    r'std'
    return t

def t_COUT(t):
    r'cout'
    return t

def t_CIN(t):
    r'cin'
    return t

def t_GET(t):
    r'get'
    return t

def t_ENDL(t):
    r'endl'
    return t

def t_SINO(t):
    r'else'
    return t

def t_SI(t):
    r'if'
    return t

def t_RETURN(t):
   r'return'
   return t

def t_VOID(t):
   r'void'
   return t

def t_MIENTRAS(t):
    r'while'
    return t

def t_PARA(t):
    r'for'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

def t_CADENA(t):
   r'\"?(\w+ \ *\w*\d* \ *)\"?'
   return t

def t_NUMERAL(t):
    r'\#'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_MENORIGUAL(t):
    r'<='
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'=='
    return t

def t_MAYORDER(t):
    r'<<'
    return t

def t_MAYORIZQ(t):
    r'>>'
    return t

def t_DISTINTO(t):
    r'!='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Multiline comment")

def t_comments_ONELine(t):
    r'\/\/(.)*\n'
    t.lexer.lineno += 1
    print("One line comment")

def t_error(t):
    print("Not valid token, Line: {:4} Value: {:16} Position: {:4}".format(str(t.lineno), str(t.value), str(t.lexpos)))
    t.lexer.skip(1)