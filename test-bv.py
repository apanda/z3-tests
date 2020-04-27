#!/usr/bin/env python3
import z3
from z3 import *
import sys
import random

z3._main_ctx = None
z3.main_ctx()
z3.set_param('smt.random_seed', random.SystemRandom().randint(0, sys.maxsize))

a = z3.BitVec('a', 8)
b = z3.BitVec('b', 8)

f = z3.Function('f', BitVecSort(8), BitVecSort(8))
s = z3.Solver()
s.add(ForAll([a, b], f(a*b)== a*f(b)))

x = z3.BitVec('x', 8)
y = z3.BitVec('y', 8)
z = z3.BitVec('z', 8)
s.add(f(x * y * z) != x * f(y * z))
print(s.check())

