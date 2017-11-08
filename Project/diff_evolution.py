import numpy as np
import sys
import time
from function_list import *

P_MAX = 100
CR = 0.9
F = 0.8
D = int(sys.argv[1])

pop = np.random.uniform(-10.0, 10.0, (P_MAX, D))
for x in range(0, 5000 * D):
    print x    
    pop_new = [[0.0 for i in range(D)] for k in range(P_MAX)]
    for j in range(P_MAX):
        a = 0
        b = 0
        c = 0
        mutated_v = [0.0 for i in range(D)]
        diff_v = [0.0 for i in range(D)]
        new_v = [0.0 for i in range(D)]
        while True:
            a = np.random.randint(0, P_MAX)
            if j != a:
                break
        while True:
            b = np.random.randint(0, P_MAX)
            if b != a and b != j:
                break
        while True:
            c = np.random.randint(0, P_MAX)
            if c != b and c != a and c != j:
                break

        for i in range(D):
            diff_v[i] = (pop[a][i] - pop[b][i]) * F
            mutated_v[i] = diff_v[i] + pop[c][i]

        for i in range(D):
            if np.random.random() < CR:
                new_v = mutated_v
            else:
                new_v[i] = pop[j][i]

        if(high_conditioned_elliptic(new_v) < high_conditioned_elliptic(pop[j])):
            pop_new[j] = new_v
        else:
            pop_new[j] = pop[j]
    
    for j in range(P_MAX):
        pop[j] = pop_new[j]

print pop