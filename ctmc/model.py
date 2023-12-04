from sage.all_cmdline import *   # import sage library
from ctmc.vars import *
from ctmc.generator import make_generator_matrix, find_steady_state_distribution


transition_matrix = Matrix([[0, k*gamm, omegaA*gamm, omegaB*gamm, 0, 0, 0, 0, 0],
                            [beta, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, k*gamm, 0, 0, omegaA*gamm, omegaB*gamm, 0, 0, 0],
                            [0, k*gamm, 0, 0, 0, omegaA*gamm, omegaB*gamm, 0, 0],
                            [beta, 0, 0, 0, 0, 0, 0, omegaA*gamm, 0],
                            [0, k*gamm, 0, 0, omegaA*gamm, 0, omegaB*gamm, 0, 0],
                            [beta, 0, 0, 0, 0, 0, 0, 0, omegaB*gamm],
                            [0, 0, beta, 0, omegaA*gamm, 0, 0, 0, 0],
                            [0, 0, 0, beta, 0, 0, omegaB*gamm, 0, 0]])

generator = make_generator_matrix(transition_matrix)

pi = find_steady_state_distribution(generator)
