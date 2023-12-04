from sage.all_cmdline import *   # import sage library


def make_generator_matrix(tr_m):
    rows, cols = tr_m.dimensions()
    assert rows == cols

    g = Matrix(tr_m)

    for i in range(rows):
        g[i, i] = -sum(*tr_m[i, :])

    return g


def find_steady_state_distribution(gen_m):
    rows, cols = gen_m.dimensions()
    assert rows == cols

    gen_m = gen_m.T

    for i in range(cols):
        gen_m[-1, i] = 1

    b = zero_vector(cols)
    b[-1] = 1

    return gen_m.solve_right(b)
