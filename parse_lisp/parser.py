from sly import Parser

from .lexer import LispLexer


class LispParser(Parser):
    debugfile = '.parser.out'

    tokens = LispLexer.tokens

    # sexp = atom
    #      | 'sexp
    #      | (sexp_seq)
    @_('atom')
    def sexp(self, p):
        return p.atom

    @_('QUOTE sexp')
    def sexp(self, p):
        return ['quote', p.sexp]

    @_('LPAREN sexp_seq RPAREN')
    def sexp(self, p):
        return p.sexp_seq

    @_('rmac')
    def sexp(self, p):
        return p.rmac

    @_('SHARPPLUS sexp sexp')
    def rmac(self, p):
        return ['sharpsign-plus', p.sexp0, p.sexp1]

    @_('SHARPMINUS sexp sexp')
    def rmac(self, p):
        return ['sharpsign-minus', p.sexp0, p.sexp1]

    @_('SHARPDOT sexp')
    def rmac(self, p):
        return ['sharpsign-dot', p.sexp]

    # XXX i'm not using #\ correctly, maybe doesn't matter right now
    @_('SHARPBSLASH SYMBOL')
    def rmac(self, p):
        return ['sharpsign-backslash', p.SYMBOL]

    @_('SHARPBSLASH NUMBER')
    def rmac(self, p):
        return ['sharpsign-backslash', p.NUMBER]

    @_('SHARPBSLASH EXTRA_CHAR')
    def rmac(self, p):
        return ['sharpsign-backslash', p.EXTRA_CHAR]

    # XXX ugly special case b/c other attempts breaking the block
    # comment ignoring fn; precedence rules?
    @_('SHARPBSHARP')
    def rmac(self, p):
        return ['sharpsign-backslash', '#']

    @_('SHARPPAREN sexp_seq RPAREN')
    def rmac(self, p):
        return ['sharpsign-vector', p.sexp_seq]

    @_('SHARPQUOTE sexp')
    def rmac(self, p):
        return ['sharpsign-quote', p.sexp]

    @_('SHARPCOLON SYMBOL')
    def rmac(self, p):
        return ['sharpsign-colon', p.SYMBOL]

    @_('SHARPO NUMBER')
    def rmac(self, p):
        return ['sharpsign-o', p.NUMBER]

    @_('SHARPP STRING')
    def rmac(self, p):
        return ['sharpsign-o', p.STRING]

    @_('BACKQUOTE sexp')
    def rmac(self, p):
        return ['backquote', p.sexp]

    @_('COMMA sexp')
    def rmac(self, p):
        return ['comma', p.sexp]

    @_('COMMAAMP sexp')
    def rmac(self, p):
        return ['comma-amp', p.sexp]

    @_('sexp sexp_seq')
    def sexp_seq(self, p):
        return [p.sexp] + p.sexp_seq

    @_('empty')
    def sexp_seq(self, p):
        return []

    @_('')
    def empty(self, p):
        pass

    # atom = number
    #      | symbol
    #      | string
    @_('NUMBER')
    def atom(self, p):
        return p.NUMBER

    @_('SYMBOL')
    def atom(self, p):
        return p.SYMBOL

    @_('STRING')
    def atom(self, p):
        return p.STRING
