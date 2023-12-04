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


def mEF_t(py):
    return k*gamm*(pi[0] + pi[2] + pi[3] + pi[5]) + gamm*(pi[1])


def mS1A_t(pi):
    return omegaA*gamm*(pi[0] + pi[3] + pi[4])


def mS1B_t(pi):
    return omegaB*gamm*(pi[0] + pi[2] + pi[6])


def mS2A_t(pi):
    return omegaA*gamm*(pi[2] + pi[5] + pi[7])

def mS2B_t(pi):
    return omegaB*gamm*(pi[3] + pi[5] + pi[8])


def raceA_t(pi):
    return k*gamm*(pi[2]*pA + pi[5]*pAB)

def raceB_t(pi):
    return k*gamm*(pi[3]*pB + pi[5]*pBA)

def race_fair_t(pi):
    return k*gamm*(pi[2]*(1-pA) + pi[3]*(1-pB) + pi[5]*(1-pAB-pBA))


def poolA_throughput(pi):
    return 2*mS2A_t(pi) + raceA_t(pi)

def poolB_throughput(pi):
    return 2*mS2B_t(pi) + raceB_t(pi)

def fair_throughput(pi):
    return k*gamm*pi[0] + gamm*(pi[1]) + race_fair_t(pi)


def total_throughput(pi):
    return poolA_throughput(pi) + poolB_throughput(pi) + fair_throughput(pi)


def poolA_revenue(pi):
    return poolA_throughput(pi) / (poolA_throughput(pi) + poolB_throughput(pi) + fair_throughput(pi))
