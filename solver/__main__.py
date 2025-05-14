

from solver.Chebyshev import solve_Chebyshev
from solver.Euler import find_a_t, solve_Euler
from plotter import plot_function, plot_latex


if __name__ == "__main__":
    #euler_ans = solve_Euler([1, -1, 2, -2], "x**3")
    #chebyshev_ans = solve_Chebyshev(10)

    #plot_function(euler_ans)
    #plot_function(chebyshev_ans)

    #plot_latex(euler_ans)
    #plot_latex(chebyshev_ans)
    def find_coefs(n: int):
        first = find_a_t([1.] * (n+1))
        second = [0] + find_a_t([1.] * (n))
        return [first[i] - second[i] for i in range(len(first)-1)]
    for i in range(1, 6):
        print(find_coefs(i))
    print(find_a_t([1,1,1,1,1,1]))
   


