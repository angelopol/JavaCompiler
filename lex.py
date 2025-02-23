import ply.lex as lex
from tokens import get_all, get_token_patterns, get_token_functions
import tokens as tok

tokens = get_all()

for token in get_token_patterns(): 
    globals()[f't_{token[0]}'] = token[1]

for func in get_token_functions():
    globals()[f't_{func}'] = getattr(tok, f't_{func}')

def execute(data):
    result = []
    lexer = lex.lex()
    lexer.input(data)

    while True:
        token = lexer.token()
        if not token:
            break

        state = f"{token.lineno:<8} {token.type:<40} {token.value:<15} {token.lexpos:<10}\n"
        result.append(state)
    return result

