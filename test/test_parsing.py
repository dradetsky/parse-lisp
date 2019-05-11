from parse_lisp import parse

def test_parse_num():
    inp = '3'
    out = parse(inp)
    assert out == '3'

def test_parse_list():
    inp = '(a b)'
    out = parse(inp)
    assert out == ['a', 'b']

    inp = '(a b c d e f g)'
    out = parse(inp)
    assert out == ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def test_parse_quote():
    inp = "'(a b)"
    out = parse(inp)
    assert out == ['quote', ['a', 'b']]
