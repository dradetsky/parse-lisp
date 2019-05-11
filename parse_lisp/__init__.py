def parse(in_str):
    from .lexer import LispLexer
    from .parser import LispParser

    lex = LispLexer()
    par = LispParser()

    toks = lex.tokenize(in_str)
    out = par.parse(toks)

    return out
