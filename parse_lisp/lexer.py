from sly import Lexer

class LispLexer(Lexer):
    tokens = {
        QUOTE,
        LPAREN,
        RPAREN,
        NUMBER,
        SYMBOL,
        STRING,

        SHARPPLUS,
        SHARPMINUS,
        SHARPDOT,
        SHARPBSHARP,
        SHARPBSLASH,
        SHARPPAREN,
        SHARPQUOTE,
        SHARPCOLON,
        SHARPO,
        SHARPP,

        BACKQUOTE,
        COMMAAMP,
        COMMA,

        EXTRA_CHAR,
    }

    ignore = ' \t'
    ignore_comment = r';.*'

    QUOTE = r"'"
    LPAREN = r'\('
    RPAREN = r'\)'
    NUMBER = r'-?((\.\d+)|(\d+\.\d*)|(\d+))'
    SYMBOL = r"[a-zA-Z_\-+*\/=<>:.&%][.\w\-\+=><:%]*['!?]*"
    STRING = r'"[^"]*"'
    BACKQUOTE = r'`'
    COMMAAMP = r',@'
    COMMA = r','


    SHARPPLUS = r'#\+'
    SHARPMINUS = r'#\-'
    SHARPDOT = r'#\.'
    SHARPBSHARP = r'#\\#'
    SHARPBSLASH = r'#\\'
    SHARPPAREN = r'#\('
    SHARPQUOTE = r"#'"
    SHARPCOLON = r'#:'
    SHARPO = r'#o'
    SHARPP = r'#p'

    EXTRA_CHAR = r'[\?]'

    @_(r'#\|')
    def begin_comment(self, t):
        end_idx = self.text.find('|#', self.index)
        if end_idx == -1:
            raise ValueError('unclosed block comment')
        self.index = end_idx + 2
