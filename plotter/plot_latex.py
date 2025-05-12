
import os
from uuid import uuid4
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.core.expr import Expr
from .config import Config

def plot_latex(f: Expr) -> str:
    fig, ax = plt.subplots()
    ax.axis("off")
    ax.text(0.5, 0.5, f"${sp.latex(f)}$", fontsize=20, ha='center', va='center')

    file_path = os.path.join(Config.output_dir, f"latex.png")
    plt.savefig(file_path, bbox_inches='tight')
    plt.close()
    return file_path