from sly import Lexer

class LispLexer(Lexer):
    tokens = {
        QUOTE,
        LPAREN,
        RPAREN,
        NUMBER,
        SYMBOL,
        STRING,
    }

    ignore = ' \t'
    ignore_newline = r'\n'
    ignore_comment = r';.*'

    QUOTE = r"'"
    LPAREN = r'\('
    RPAREN = r'\)'
    NUMBER = r'-?((\.\d+)|(\d+\.\d*)|(\d+))'
    SYMBOL = r"[a-zA-Z_\-+*\/=<>:.][.\w\-=><:]*['!?]*"
    STRING = r'"[^"]*"'

    @_(r'#\|')
    def begin_comment(self, t):
        end_idx = self.text.find('|#', self.index)
        if end_idx == -1:
            raise ValueError('unclosed block comment')
        self.index = end_idx + 2
