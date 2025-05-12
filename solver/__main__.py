

from solver.Chebyshev import solve_Chebyshev
from solver.Euler import solve_Euler
from plotter import plot_function, plot_latex


if __name__ == "__main__":
    euler_ans = solve_Euler([1, -1, 2, -2], "x**3")
    #chebyshev_ans = solve_Chebyshev(10)

    plot_function(euler_ans)
    #plot_function(chebyshev_ans)

    plot_latex(euler_ans)
    #plot_latex(chebyshev_ans)




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
