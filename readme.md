parse-lisp
==========

Parse lisp into python list-of-lists. Intended for use as part of a
larger tree-edit analysis project.

notes
-----

0. Originally based on code swiped from https://github.com/eignnx/lispish.

1. Long term probably not workable. Lisp has so much lisp-specific
   reader macro stuff that doing it yacc-style may not be feasible.
