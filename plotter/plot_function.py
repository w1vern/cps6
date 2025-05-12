
import os
from uuid import uuid4
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.core.expr import Expr
from .config import Config


def plot_function(f: Expr,
                  x_range: tuple[float, float] = Config.x_range,
                  num_points: int = Config.num_points
                  ) -> str:
    x = sp.symbols('x')
    new_f = f.subs(
        {sym: 1 for sym in f.free_symbols if sym.name.startswith('C_')})
    f_lambdified = sp.lambdify(x, new_f, 'numpy')

    x_vals = np.linspace(x_range[0], x_range[1], num_points)
    y_vals = f_lambdified(x_vals)

    plt.figure()
    plt.plot(x_vals, y_vals, label="f(x)")
    plt.title("График функции")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)

    file_path = os.path.join(Config.output_dir, f"function.png")
    plt.savefig(file_path)
    plt.close()
    return file_path
