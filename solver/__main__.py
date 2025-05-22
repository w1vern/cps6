

from solver.Chebyshev import solve_Chebyshev
from solver.Euler import find_a_t, solve_Euler
from plotter import plot_function, plot_latex


if __name__ == "__main__":
    #euler_ans = solve_Euler([1, -1, 2, -2], "x**3")
    chebyshev_ans = solve_Chebyshev(0)

    #plot_function(euler_ans)
    plot_function(chebyshev_ans)

    #plot_latex(euler_ans)
    #plot_latex(chebyshev_ans)

   


