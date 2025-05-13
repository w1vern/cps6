
import os
import sympy as sp
import matplotlib.pyplot as plt
from sympy.core.expr import Expr
from .config import Config

def plot_latex(f: Expr, is_dark: bool = False) -> str:
    fig, ax = plt.subplots(figsize=(0.5,0.1), dpi=300)
    ax.axis("off")
    ax.text(0.5, 0.5, f"$f(x)={sp.latex(f)}$", fontsize=15, ha='center', va='center', color='white' if is_dark else 'black')

    file_path = os.path.join(Config.output_dir, f"latex.svg")
    plt.savefig(file_path, bbox_inches='tight', transparent=True)
    plt.close()
    return file_path
