import numpy as np

def high_conditioned_elliptic(xvec):
    total = 0.0
    for dx in range(0, xvec.__len__()):
        total += 10 **(6 *(dx /(xvec.__len__() - 1)))* xvec[dx] * xvec[dx]
    return total

def bent_cigar(xvec):
    total = 0.0
    for dx in range(1, xvec.__len__()):
        total += xvec[dx] ** 2
    total = total * (10 ** 6)
    total += xvec[0]
    return total

def discus(xvec):
    total = 0.0
    for dx in range(1, xvec.__len__()):
        total += xvec[dx] ** 2
    total += (10 ** 6) * xvec[0]
    return total

def rosenbrock(xvec):
    total = 0.0
    for dx in range(0, xvec.__len__() - 1):
        total += 100 *(xvec[dx] ** 2 - xvec[dx + 1]) ** 2 + (xvec[dx] - 1) ** 2
    return total

def ackley(xvec):
    total_a = 0.0
    total_b = 0.0
    for dx in range(0, xvec.__len__()):
        total_a += xvec[dx] ** 2
        total_b += np.cos(2 * np.pi * xvec[dx])
    total_a = -1 * np.exp(-0.2 * np.sqrt(1 / xvec.__len__() * total_a)) - np.exp(1)
    return total_a

def weierstrass(xvec):
    total_a = 0.0
    total_b = 0.0
    total_c = 0.0
    for dx in range(0, xvec.__len__()):
        for kx in range(0, 21):
            total_a += 0.5 ** kx * np.cos(2 * np.pi * 3 ** kx *(xvec[dx] + 0.5))
            total_c += 0.5 ** kx * np.cos(2 * np.pi * 3 ** kx * 0.5)
        total_b += total_a
        total_a = 0
    total_b = total_b - xvec.__len__() * total_c
    return total_b

def griewank(xvec):
    total_a = 0.0
    total_b = 0.0
    for dx in range(0, xvec.__len__()):
        total_b += (xvec[dx] ** 2)/ 4000
        total_a *= np.cos(xvec[dx] / np.sqrt(dx + 1))
    total_a = total_b - total_a + 1
    return total_a

def rastrigin(xvec):
    total = 0.0
    for dx in range(0, xvec.__len__()):
        total += (xvec[dx] ** 2) - 10 * np.cos(2 * np.pi * xvec[dx]) + 10
    return total

def katsuura(xvec):
    total_a = 0.0
    total_b = 0.0
    for dx in range(0, xvec.__len__()):
        for i in range(1, 33):
            total_a += np.abs(2 ** i * xvec[dx] - np.round(2 ** i * xvec[dx]))/ (2 ** i)
        total_b *= (1 + (dx + 1) * total_a) ** (10 / (xvec.__len__() ** 1.2))
        total_a = 0
    total_b = 10 / (xvec.__len__() ** 2) * total_b - 10 / (xvec.__len__() ** 2)
    return total_b
