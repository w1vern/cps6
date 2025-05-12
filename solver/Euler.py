import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.core.expr import Expr

from solver.print import md_print

t = sp.Symbol('t')
x = sp.Symbol('x')


def stirling_first_kind(n: int) -> list[list[int]]:
    s = [[0] * (n + 1) for _ in range(n + 1)]
    s[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            s[i][j] = s[i - 1][j - 1] - (i - 1) * s[i - 1][j]
    return s


s_size = 10
s = stirling_first_kind(s_size)


def find_a_t(a_x: list[float]) -> list[float]:
    n = len(a_x) - 1
    A = [0.] * (n + 1)
    for j in range(n + 1):
        for i in range(n - j + 1):
            A[j] += a_x[i] * s[n - i][j]
    return A[::-1]


def find_Y(a_t: list[float]) -> Expr:
    roots = np.roots(a_t)
    roots = [np.round(root.real, 2) + 1j * np.round(root.imag, 2)
             for root in roots if isinstance(root, np.complex128)]
    roots = [root.real for root in roots if isinstance(
        root, np.complex128) and abs(root.imag) < 0.01]
    real: dict[float, int] = {}
    complex: dict[tuple[float, float], int] = {}
    for root in roots:
        if isinstance(root, np.float64):
            if float(root) in real:
                real[root] += 1
            else:
                real[root] = 1
        elif isinstance(root, np.complex128):
            tmp_tuple = root.real, abs(root.imag)
            if tmp_tuple in complex:
                complex[tmp_tuple] += 1
            else:
                complex[tmp_tuple] = 1
        else:
            raise Exception(
                f"wrong type definition. Current type: {type(root)}")
    f_real_part = sp.S(0)

    C_index = 1

    for key, value in real.items():
        for i in range(value):
            C = sp.Symbol(f'C_{C_index}')
            C_index += 1
            f_real_part += C * t**i * sp.exp(key*t)

    f_complex_part = sp.S(0)
    C_index = 1

    for (re, im), value in complex.items():
        for i in range(value//2):
            C1 = sp.Symbol(f'C_{C_index}')
            C2 = sp.Symbol(f'C_{C_index+1}')
            C_index += 2
            f_complex_part += t**i * \
                sp.exp(t*re) * (C1 * sp.cos(t*im) + C2 * sp.sin(t*im))

    Y = f_real_part + f_complex_part
    return Y


def find_y_with_tilde(f_t: Expr, Y: Expr) -> Expr:
    t = sp.Symbol('t')
    y = sp.Function('y')

    constants = sorted([s for s in Y.free_symbols if s.name.startswith('C')],
                       key=lambda s: s.name)
    base_solutions = []
    for c in constants:
        subs = {k: 0 for k in constants}
        subs[c] = 1
        base_solutions.append(sp.simplify(Y.subs(subs)))

    n = len(base_solutions)
    phi = base_solutions
    u_prime = [sp.Function(f'u{i + 1}')(t).diff(t) for i in range(n)]

    system = []
    for k in range(n - 1):
        row = sum(u_prime[i] * phi[i].diff(t, k) for i in range(n))
        system.append(sp.Eq(row, 0))

    row = sum(u_prime[i] * phi[i].diff(t, n - 1) for i in range(n))
    system.append(sp.Eq(row, f_t))

    u_prime_syms = [sp.Symbol(f'du{i+1}') for i in range(n)]
    system_subs = [eq.lhs.subs({u_prime[i]: u_prime_syms[i]
                               for i in range(n)}) - eq.rhs for eq in system]
    sol = sp.linsolve(system_subs, *u_prime_syms)
    if not sol:
        raise ValueError(
            "Не удалось найти частное решение: система несовместна.")
    sol = list(sol)[0]

    u_funcs = [sp.integrate(sol[i], t) for i in range(n)]
    yp = sum(u_funcs[i] * phi[i] for i in range(n))

    for s in yp.free_symbols:
        if s.name.startswith('tau'):
            yp = yp.subs(s, 0)

    def remove_projection(yp: Expr, phi: list[Expr]) -> Expr:
        coeffs = sp.symbols(f'_a0:{len(phi)}')
        lin_comb = sum(coeffs[i] * phi[i] for i in range(len(phi)))
        eq = sp.expand(yp - lin_comb)

        try:
            sol = sp.solve(eq, coeffs, dict=True)
        except Exception:
            sol = []

        if not sol:
            return sp.simplify(yp)

        lin_part = sum(sol[0][coeffs[i]] * phi[i] for i in range(len(phi)))
        return sp.simplify(yp - lin_part)

    # yp = remove_projection(yp, phi)
    return yp


def find_y(a_t: list[float], f_t: Expr) -> Expr:
    Y = find_Y(a_t)
    y_with_tilde = find_y_with_tilde(f_t, Y)
    return Y + y_with_tilde


def find_closest_common_ancestor(cls1, cls2):
    mro1 = type(cls1).__mro__
    mro2 = type(cls2).__mro__

    for parent in mro1:
        if parent in mro2:
            return parent
    return None


def clean_expr(expr):
    """Очистка выражения:
       - убирает множители 1 и 1.0
       - приводит степени с .0 к целым
       - заменяет десятичные дроби на рациональные (если точные)
    """

    if isinstance(expr, sp.Symbol):
        return expr

    if isinstance(expr, sp.Number):
        if expr == int(expr):
            return sp.Integer(int(expr))
        else:
            return sp.nsimplify(expr, rational=True, tolerance=1e-10)

    if isinstance(expr, sp.Pow):
        base = clean_expr(expr.base)
        exp = clean_expr(expr.exp)
        if exp.is_Float and exp == int(exp):
            exp = int(exp)
        return base**exp

    if isinstance(expr, sp.Mul):
        coeff, rest = expr.as_coeff_Mul()
        rest_clean = clean_expr(rest)
        if coeff == 1 or coeff == 1.0:
            return rest_clean
        if isinstance(coeff, sp.Float) and coeff == int(coeff):
            coeff = sp.Integer(int(coeff))
        elif isinstance(coeff, sp.Float):
            numer, denom = coeff.as_integer_ratio()
            if denom < 100:
                coeff = sp.Rational(numer, denom)
        return coeff * rest_clean

    if isinstance(expr, sp.Add):
        return sp.Add(*[clean_expr(arg) for arg in expr.args])

    if isinstance(expr, sp.Basic):
        return expr.func(*[clean_expr(arg) for arg in expr.args])

    return expr


def solve_Euler(a_x: list[float], f_x: str) -> Expr:
    a_t = find_a_t(a_x)
    sp_f_x = sp.sympify(f_x)
    x_expr = sp.exp(t)
    t_expr = sp.ln(x)
    sp_f_t = sp_f_x.subs(x, x_expr)
    if not isinstance(sp_f_t, Expr):
        raise Exception("need to fix this possibility")
    y_t = find_y(a_t, sp_f_t)
    y_x = y_t.subs(t, t_expr)
    y_x = sp.simplify(y_x)

    # y_x = clean_expr(y_x)

    # md_text = sp.latex(y_x)
    # md_print(md_text)

    return y_x
