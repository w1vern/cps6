



from solver.Chebyshev import solve_Chebyshev
from solver.Euler import solve_Euler


if __name__ == "__main__":
    #print(solve_Euler([1, -1, 2, -2], "x**2"))
    print(solve_Chebyshev(10))



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
