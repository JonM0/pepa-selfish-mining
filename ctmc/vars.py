from sage.all_cmdline import *   # import sage library

k, gamm, beta, omegaA, omegaB = var('k γ β ωA ωB')

pA, pB = var('pA pB')
pAB, pBA = var('pAB pBA')


par = {k: 100, gamm: 0.00083, beta: 0.314, omegaA: 60, omegaB: 40}
