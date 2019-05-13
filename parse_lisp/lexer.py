import re

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

    @_(r'"')
    def STRING(self, t):
        begin_idx = self.index - 1
        search_text = self.text[begin_idx:]

        end_match = re.search(r'[^\\]"', search_text)
        if not end_match:
            raise ValueError('cannot find closing quote')

        end_idx = end_match.end(0)
        val = search_text[0:end_idx]

        t.value = val
        self.index += (end_idx - 1)
        return t

    @_(r'#\|')
    def begin_comment(self, t):
        end_idx = self.text.find('|#', self.index)
        if end_idx == -1:
            raise ValueError('unclosed block comment')
        self.index = end_idx + 2
