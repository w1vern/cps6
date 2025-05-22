
import sympy as sp
from sympy.core.expr import Expr


x = sp.Symbol('x')


def T(n: int) -> Expr:
    if n == 0:
        return sp.Integer(1)
    if n == 1:
        return x
    return sp.simplify(2 * x * T(n-1) - T(n-2))


def U(n: int) -> Expr:
    if n == 0:
        return sp.Integer(1)
    if n == 1:
        return 2 * x
    return 2 * x * U(n-1) - U(n-2)


def N(n: int) -> Expr:
    if n == 0:
        U_n = sp.Integer(0)
    else:
        U_n = U(n-1)
    return sp.simplify(sp.sqrt(1 - x**2) * U_n)


def solve_Chebyshev(n: float) -> Expr:
    if n.is_integer():
        y_x = T(abs(int(n))) + N(abs(int(n)))
    else:
        t = sp.Symbol('t')
        C_1 = sp.Symbol('C_1')
        C_2 = sp.Symbol('C_2')
        t_expr = sp.acos(x)
        y_t = C_1 * sp.cos(n * t) + C_2 * sp.sin(n * t)
        y_x = y_t.subs(t, t_expr)
    # y_x = sp.simplify(y_x)

    # md_text = y_x._repr_latex_()
    # md_print(md_text)

    return y_x
