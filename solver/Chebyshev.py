import sympy as sp
import matplotlib.pyplot as plt
from sympy.core.expr import Expr

from solver.print import md_print

x = sp.Symbol('x')
t = sp.Symbol('t')


def T(n: int) -> Expr:
    if n < 0:
        raise Exception("n must be positive")
    if n == 0:
        return sp.Integer(1)
    if n == 1:
        return t
    return sp.simplify(2 * t * T(n-1) - T(n-2))


def U(n: int) -> Expr:
    if n < -1:
        raise Exception("n must be positive")
    if n == -1:
        return sp.Integer(0)
    if n == 0:
        return sp.Integer(1)
    if n == 1:
        return 2 * t
    return 2 * t * U(n-1) - U(n-2)


def N(n: int) -> Expr:
    return sp.simplify(sp.sqrt(1 - t**2) * U(n-1))


def solve_Chebyshev(n: float) -> str:

    x_expr = sp.cos(t)
    t_expr = sp.acos(x)
    C_1 = sp.Symbol('C_1')
    C_2 = sp.Symbol('C_2')
    y_t = C_1 * sp.cos(n * t) + C_2 * sp.sin(n * t)
    if n.is_integer():
        y_x = T(int(n)) + N(int(n))
    else:
        y_x = y_t.subs(t, t_expr)
    #y_x = sp.simplify(y_x)
    md_text = y_x._repr_latex_()
    md_print(md_text)
    return md_text
