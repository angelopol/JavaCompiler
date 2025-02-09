def get_reserved():
    return (
        'ABSTRACT',
        'ASSERT',
        'BOOLEAN',
        'BREAK',
        'BYTE',
        'CATCH',
        'CHAR',
        'CLASS',
        'CONST',
        'CONTINUE',
        'DOUBLE',
        'ENUM',
        'EXTENDS',
        'FINAL',
        'FINALLY',
        'FLOAT',
        'GOTO',
        'IMPLEMENTS',
        'IMPORT',
        'INSTANCEOF',
        'INT',
        'INTERFACE',
        'LONG',
        'NATIVE',
        'NEW',
        'PACKAGE',
        'PRIVATE',
        'PROTECTED',
        'PUBLIC',
        'RETURN',
        'SHORT',
        'STATIC',
        'STRICTFP',
        'STRING',
        'SUPER',
        'SYNCHRONIZED',
        'THIS',
        'THROW',
        'THROWS',
        'TRANSIENT',
        'TRY',
        'VOID',
        'VOLATILE',
    )

def get_math():
    return (
        'PLUS',       # +
        'MINUS',      # -
        'MULT',       # *
        'DIV',        # /
        'MOD',        # %
        'INCREMENT',  # ++
        'DECREMENT',  # --
    )

def get_conditions():
    return (
        'IF',
        'ELSE',
        'SWITCH',
        'CASE',
        'DEFAULT',
    )

def get_loops():
    return (
        'FOR',
        'WHILE',
        'DO',
    )

def get_logic():
    return (
        'AND',        # &&
        'OR',         # ||
        'NOT',        # !
    )

def get_others():
    return (
        'ASSIGN',     # =
    )

def get_sintax():
    return (
        'LESS_THAN',  # <
        'GREATER_THAN', # >
        'SEMICOLON',  # ;
        'COMMA',      # ,
        'LPAREN',     # (
        'RPAREN',     # )
        'LBRACKET',   # [
        'RBRACKET',   # ]
        'LBRACE',     # {
        'RBRACE',     # }
        'DOUBLE_QUOTE', # "
        'IDENTIFICADOR',
        'ENTERO',
        'CADENA'

    )

def get_all():
    return get_reserved() + get_math() + get_conditions() + get_loops() + get_logic() + get_others() + get_sintax()

def get_token_patterns():
    return [
        ['PLUS', r'\+'],
        ['MINUS', r'-'],
        ['INCREMENT', r'\+\+'],
        ['DECREMENT', r'--'],
        ['MULT', r'\*'],
        ['DIV', r'/'],
        ['MOD', r'%'],
        ['ASSIGN', r'='],
        ['AND', r'&&'],
        ['OR', r'\|\|'],
        ['NOT', r'!'],
        ['LESS_THAN', r'<'],
        ['GREATER_THAN', r'>'],
        ['SEMICOLON', r';'],
        ['COMMA', r','],
        ['LPAREN', r'\('],
        ['RPAREN', r'\)'],
        ['LBRACKET', r'\['],
        ['RBRACKET', r'\]'],
        ['LBRACE', r'\{'],
        ['RBRACE', r'\}'],
        ['DOUBLE_QUOTE', r'\"'],
        ['ignore', ' \t']
    ]

def get_token_functions():
    return [
        'ABSTRACT', 'ASSERT', 'BOOLEAN', 'BREAK', 'BYTE', 'CASE', 'CATCH', 'CHAR', 'CLASS', 'CONST', 'CONTINUE', 
        'DEFAULT', 'DO', 'DOUBLE', 'ELSE', 'ENUM', 'EXTENDS', 'FINAL', 'FINALLY', 'FLOAT', 'FOR', 'ENTERO',
        'CADENA', 'GOTO', 'IF', 'IMPLEMENTS', 'IMPORT', 'INSTANCEOF', 'INT', 'INTERFACE', 'LONG', 'NATIVE', 'NEW', 'PACKAGE', 'PRIVATE', 
        'PROTECTED', 'PUBLIC', 'RETURN', 'SHORT', 'STATIC', 'STRICTFP', 'STRING','SUPER', 'SWITCH', 'SYNCHRONIZED', 'THIS', 
        'THROW', 'THROWS', 'TRANSIENT', 'TRY', 'VOID', 'VOLATILE', 'WHILE', 'newline', 'IDENTIFICADOR', 'comments', 'comments_ONELine', 
        'error'
    ]

def t_ABSTRACT(t):
    r'abstract'
    return t

def t_ASSERT(t):
    r'assert'
    return t

def t_BOOLEAN(t):
    r'boolean'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_BYTE(t):
    r'byte'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_CHAR(t):
    r'char'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_CONST(t):
    r'const'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_DO(t):
    r'do'
    return t

def t_DOUBLE(t):
    r'double'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ENUM(t):
    r'enum'
    return t

def t_EXTENDS(t):
    r'extends'
    return t

def t_FINAL(t):
    r'final'
    return t

def t_FINALLY(t):
    r'finally'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_FOR(t):
    r'for'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_CADENA(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

def t_GOTO(t):
    r'goto'
    return t

def t_IF(t):
    r'if'
    return t

def t_IMPLEMENTS(t):
    r'implements'
    return t

def t_IMPORT(t):
    r'import'
    return t

def t_INSTANCEOF(t):
    r'instanceof'
    return t

def t_INT(t):
    r'int'
    return t

def t_INTERFACE(t):
    r'interface'
    return t

def t_LONG(t):
    r'long'
    return t

def t_NATIVE(t):
    r'native'
    return t

def t_NEW(t):
    r'new'
    return t

def t_PACKAGE(t):
    r'package'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_PROTECTED(t):
    r'protected'
    return t

def t_PUBLIC(t):
    r'public'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_SHORT(t):
    r'short'
    return t

def t_STATIC(t):
    r'static'
    return t

def t_STRICTFP(t):
    r'strictfp'
    return t

def t_STRING(t):
    r'String'
    return t

def t_SUPER(t):
    r'super'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_SYNCHRONIZED(t):
    r'synchronized'
    return t

def t_THIS(t):
    r'this'
    return t

def t_THROW(t):
    r'throw'
    return t

def t_THROWS(t):
    r'throws'
    return t

def t_TRANSIENT(t):
    r'transient'
    return t

def t_TRY(t):
    r'try'
    return t

def t_VOID(t):
    r'void'
    return t

def t_VOLATILE(t):
    r'volatile'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

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