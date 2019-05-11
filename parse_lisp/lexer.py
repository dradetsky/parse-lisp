from sly import Lexer

class LispLexer(Lexer):
    tokens = {
        LPAREN,
        RPAREN,
        NUMBER,
        SYMBOL,
        SEP
    }

    LPAREN = r'\('
    RPAREN = r'\)'
    NUMBER = r'-?((\.\d+)|(\d+\.\d*)|(\d+))'
    SYMBOL = r"[a-zA-Z_\-+*\/=<>][\w\-=><]*['!?]*"
    SEP = r'\s'
