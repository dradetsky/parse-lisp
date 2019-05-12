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
