def parse(in_str):
    from .lexer import LispLexer
    from .parser import LispParser

    lex = LispLexer()
    par = LispParser()

    toks = lex.tokenize(in_str)
    out = par.parse(toks)

    return out

def debug_parse(in_str):
    from .lexer import LispLexer
    from .parser import LispParser

    lex = LispLexer()
    par = LispParser()

    toks = lex.tokenize(in_str)
    par._lexer = lex
    out = par.parse(toks)

    ret = [out, par, lex, toks]

    return ret
