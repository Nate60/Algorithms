import numpy as np
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from function_list import *
from matplotlib import cm

P_MAX = 100
NFC = 5000
CR = 0.9
F = 0.8
D = int(sys.argv[1])
e = int(sys.argv[2])
prefix = ""

def graph(x,y,z, fcn):
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    x1 = y1 = np.arange(-10, 10, 0.05)
    X, Y = np.meshgrid(x1,y1)
    zs = np.array([eval([x1,y1],fcn) for x1,y1 in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha=0.5)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    ax.scatter(x, y, z, lw=5, color='green')
    plt.show()

def eval(xinputs, E):
    global prefix
    if(E == 0):
        prefix = "elliptic"
        return high_conditioned_elliptic(xinputs)
    elif(E == 1):
        prefix = "cigar"
        return bent_cigar(xinputs)
    elif(E == 2):
        prefix = "discus"
        return discus(xinputs)
    elif(E == 3):
        prefix = "rosen"
        return rosenbrock(xinputs)
    elif(E == 4):
        prefix = "ackley"
        return ackley(xinputs)
    elif(E == 5):
        prefix = "weier"
        return weierstrass(xinputs)
    elif(E == 6):
        prefix = "grie"
        return griewank(xinputs)
    elif(E == 7):
        prefix = "rast"
        return rastrigin(xinputs)
    elif(E == 8):
        prefix = "katsuura"
        return katsuura(xinputs)
print "Init..."

#for r in range(1, 52):
pop = np.random.uniform(-10.0, 10.0, (P_MAX, D))
for x in range(0, NFC/P_MAX * D):
    print("%5.4f function: %s" % ((x * 1.0)/((NFC/P_MAX) * D) * 100, prefix))
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
            if (np.random.random() < CR) and (mutated_v[i] <= 10) and (mutated_v[i] >= -10):
                new_v[i] = mutated_v[i]
            else:
                new_v[i] = pop[j][i]

        if(eval(new_v,e) < eval(pop[j],e)):
            pop_new[j] = new_v
        else:
            pop_new[j] = pop[j]

    for j in range(P_MAX):
        pop[j] = pop_new[j]


    out_file = open(str(D) + "_" + prefix + "_de_points"  + ".csv","w")
    full_output = pop.tolist()
    for line in full_output:
        out_file.write(str(line)[1:-1] + ', ' + str(eval(line,e)) + "\n")
    out_file.close()
print str(pop[0][0]) + "," + str(pop[0][1]) + "," + str(eval(pop[0],e))
graph(pop[0][0], pop[0][1], eval(pop[0],e), e)