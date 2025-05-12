
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.core.expr import Expr


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
    roots = [np.round(root.real, 2) + 1j * np.round(root.imag, 2) for root in roots if isinstance(root, np.complex128)]
    roots = [root.real for root in roots if isinstance(root, np.complex128) and abs(root.imag) < 0.01]
    print(roots)
    real: dict[float, int] = {}
    complex: dict[tuple[float, float], int] = {}
    for root in roots:
        if isinstance(root, np.float64):
            if float(root) in real:
                real[root] += 1
            else:
                real[root] = 1
        elif isinstance(root, np.complex128):
            t = root.real, abs(root.imag)
            if t in complex:
                complex[t] += 1
            else:
                complex[t] = 1
        else:
            raise Exception(f"wrong type definition. Current type: {type(root)}")
    print(real)
    print(complex)
    f_real_part = sp.S(0)
    t = sp.Symbol('t')
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


def find_y_with_tilde(a_t: list[float], f_t: Expr) -> Expr:
    def get_root_multiplicity(a_t: list[float], lam: float) -> int:
        """Возвращает кратность корня lam в характеристическом уравнении."""
        roots = np.roots(a_t)
        count = sum(1 for r in roots if np.isclose(r.real, lam, atol=1e-2))
        return count
    def adjust_rhs_if_needed(f_t: Expr, a_t: list[float]) -> Expr:
        """Модифицирует f_t, если она совпадает по виду с решением однородного уравнения."""
        t = sp.Symbol('t')
        # Попробуем угадать вид f_t: exp(lambda * t)
        if f_t.func == sp.exp:
            lam = f_t.args[0].as_coeff_mul(t)[0]
            multiplicity = get_root_multiplicity(a_t, float(lam))
            if multiplicity > 0:
                return t**multiplicity * f_t
        return f_t
    #f_t = adjust_rhs_if_needed(f_t, a_t)
    t = sp.Symbol('t')
    y = sp.Function('y')

    order = len(a_t) - 1
    ode_lhs = sum(
        a_t[i] * y(t).diff(t, order - i)
        for i in range(len(a_t))
    )

    sol = sp.dsolve(sp.Eq(ode_lhs, f_t), y(t), hint='undetermined_coefficients')
    yp = sol.rhs

    consts = [sym for sym in yp.free_symbols if sym.name.startswith('C')]
    yp_part = yp.subs({c: 0 for c in consts})
    return sp.simplify(yp_part)


def find_y(a_t: list[float], f_t: Expr) -> Expr:
    return find_Y(a_t) + find_y_with_tilde(a_t, f_t)  # type: ignore


def find_closest_common_ancestor(cls1, cls2):
    mro1 = type(cls1).__mro__
    mro2 = type(cls2).__mro__

    for parent in mro1:
        if parent in mro2:
            return parent
    return None


def solve(a_x: list[float], f_x: str) -> str:
    x = sp.Symbol('x')
    t = sp.Symbol('t')
    a_t = find_a_t(a_x)
    print(a_t)
    print(find_Y(a_t))
    sp_f_x = sp.sympify(f_x)
    x_expr = sp.exp(t)
    t_expr = sp.ln(x)
    sp_f_t = sp_f_x.subs(x, x_expr)
    print(sp_f_t)
    if not isinstance(sp_f_t, Expr):
        raise Exception("need to fix this possibility")
    y_t = find_y(a_t, sp_f_t)
    print(y_t)
    y_x = y_t.subs(t, t_expr)
    print(y_x)

    return ""


""" x = sp.Symbol('x')
    y = sp.cos(x)
    f = sp.lambdify(x, y, modules=['numpy'])

    x_vals = np.arange(-1, 1.01, 0.01)

    y_vals = f(x_vals)

    plt.plot(x_vals, y_vals, label='cos(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show() """

if __name__ == "__main__":
    solve([1, -1, 2, -2], "x")