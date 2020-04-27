#!/usr/bin/env python3
import z3
from z3 import *
import sys
import random

z3._main_ctx = None
z3.main_ctx()
z3.set_param('smt.random_seed', random.SystemRandom().randint(0, sys.maxsize))

a = z3.Int('a')
b = z3.Int('b')
c = z3.Int('c')

f = z3.Function('f', IntSort(), IntSort())
s = z3.Solver()
# s.add(ForAll([a, b], (c == f(a+b)) == (c == a+f(b)) == (c == f(a)+b)))
s.add(ForAll([a, b], f(a+b)== a+f(b)))

x = z3.Int('x')
y = z3.Int('y')
s.add(f(x + y) != x + f(y))
print(s.check())

