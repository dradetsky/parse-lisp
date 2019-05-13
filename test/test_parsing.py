import pytest

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

def test_parse_symbol():
    inp = 'foo'
    out = parse(inp)
    assert out == 'foo'

    inp = 'foo:bar'
    out = parse(inp)
    assert out == 'foo:bar'

def test_empty():
    inp = '()'
    out = parse(inp)
    assert out == []

    inp = '(())'
    out = parse(inp)
    assert out == [[]]

def test_space():
    inp = '(a  b)'
    out = parse(inp)
    assert out == ['a', 'b']

    inp = ' (a b)'
    out = parse(inp)
    assert out == ['a', 'b']

    inp = '( a b)'
    out = parse(inp)
    assert out == ['a', 'b']

    inp = '(a b )'
    out = parse(inp)
    assert out == ['a', 'b']

    inp = ' ( a b ) '
    out = parse(inp)
    assert out == ['a', 'b']

    inp = ' ( a  b ) '
    out = parse(inp)
    assert out == ['a', 'b']

    inp = '(a\nb\n) '
    out = parse(inp)
    assert out == ['a', 'b']

    inp = '((a)\n(b)\n) '
    out = parse(inp)
    assert out == [['a'], ['b']]

def test_invalid():
    inp = ')(lulz (a b)'
    out = parse(inp)
    assert out == None


def test_block_comment():
    inp = '#| lulz |# (a b)'
    out = parse(inp)
    assert out == ['a', 'b']

    inp = '#| )(lulz |# (a b)'
    out = parse(inp)
    assert out == ['a', 'b']

    inp = '(a b) #| lulz |#'
    out = parse(inp)
    assert out == ['a', 'b']

    inp = '((a b) #| lulz |# (a b))'
    out = parse(inp)
    assert out == [['a', 'b'], ['a', 'b']]


def test_multiline_block_comment():
    inp = '''#|
 lulz
|# (a b)'''
    out = parse(inp)
    assert out == ['a', 'b']

def test_sharp_plusminus():
    inp = '#+sbcl "sb-posix"'
    out = parse(inp)
    assert out == ['sharpsign-plus', 'sbcl', '"sb-posix"']

    inp = '#+(and linux (not asdf3)) "uiop"'
    out = parse(inp)
    assert out == ['sharpsign-plus',
                   ['and', 'linux', ['not', 'asdf3']],
                   '"uiop"']

    # inp = '#+sbcl "sb-concurrency"'

    inp = '#-sbcl "cl-speedy-queue"'
    out = parse(inp)
    assert out == ['sharpsign-minus', 'sbcl', '"cl-speedy-queue"']
