from sly import Parser

from .lexer import LispLexer


class LispParser(Parser):
    tokens = LispLexer.tokens

    # sexp = atom
    #      | (sexp_seq)
    @_('atom')
    def sexp(self, p):
        return p.atom

    @_('LPAREN sexp_seq RPAREN')
    def sexp(self, p):
        return p.sexp_seq

    # sexp_seq = sexp
    #          | sexp sexp_seq
    @_('sexp')
    def sexp_seq(self, p):
        return [p.sexp]

    @_('sexp SEP sexp_seq')
    def sexp_seq(self, p):
        return [p.sexp] + p.sexp_seq

    # atom = number
    #      | symbol
    @_('NUMBER')
    def atom(self, p):
        return p.NUMBER

    @_('SYMBOL')
    def atom(self, p):
        return p.SYMBOL
