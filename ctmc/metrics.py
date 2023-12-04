from sage.all_cmdline import *   # import sage library
from ctmc.vars import *


def mining_throughput(pi):
    return (
        k*gamm*(pi[0] + pi[2] + pi[3] + pi[5]) +
        gamm*(pi[1]) +
        2 * omegaA*gamm*(pi[2] + pi[5] + pi[7]) +
        2 * omegaB*gamm*(pi[3] + pi[5] + pi[8])
    )


def fair_verify(pi):
    return ((k-1)/k*pi[1] + pi[4] + pi[6] + pi[7] + pi[8])


def poolA_verify(pi):
    return (pi[1] + pi[6] + pi[8])


def poolB_verify(pi):
    return (pi[1] + pi[4] + pi[7])
