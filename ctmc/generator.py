from sage.all_cmdline import *   # import sage library


def make_generator_matrix(m):
    rows, _ = m.dimensions()
    g = Matrix(m)

    for i in range(rows):
        g[i, i] = -sum(*m[i, :])

    return g


k, gamm, beta, omegaA, omegaB = var('k γ β ωA ωB')

transition = Matrix([[0, k*gamm, omegaA*gamm, omegaB*gamm, 0, 0, 0, 0, 0],
                     [beta, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, k*gamm, 0, 0, omegaA*gamm, omegaB*gamm, 0, 0, 0],
                     [0, k*gamm, 0, 0, 0, omegaA*gamm, omegaB*gamm, 0, 0],
                     [beta, 0, 0, 0, 0, 0, 0, omegaA*gamm, 0],
                     [0, k*gamm, 0, 0, omegaA*gamm, 0, omegaB*gamm, 0, 0],
                     [beta, 0, 0, 0, 0, 0, 0, 0, omegaB*gamm],
                     [0, 0, beta, 0, omegaA*gamm, 0, 0, 0, 0],
                     [0, 0, 0, beta, 0, 0, omegaB*gamm, 0, 0]])

rows, cols = transition.dimensions()

generator = make_generator_matrix(transition)

g = generator.T

for i in range(cols):
    g[-1, i] = 1

pi = g.solve_right(vector([0, 0, 0, 0, 0, 0, 0, 0, 1]))
                           
# print(pi)
