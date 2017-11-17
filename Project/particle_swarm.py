import numpy as np
import sys
from time import time
from function_list import *

P_MAX = 100
C1 = 2.05
C2 = 2.05
NFC = 5000
D = int(sys.argv[1])
prefix = ""

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
    else:
        prefix = "katsuura"
        return katsuura(xinputs)
print "Init..."
start = time()
end = time() - start
for e in range(0, 9):
    avg = np.random.uniform(0.0,0.0,(NFC/P_MAX*D))
    for r in range(1, 52):
        W = 0.9
        pop = np.random.uniform(-10.0, 10.0, (P_MAX, D))
        vel = np.random.uniform(-1.0, 1.0, (P_MAX, D))
        fness = [eval(pop[x],e) for x in range(P_MAX)]
        best = [fness[0] for x in range(NFC/P_MAX * D)]
        gBest = pop[0]
        fgBest = fness[0]
        pBest = pop
        fpBest = fness
        
        for j in range(P_MAX):
            if(fness[j] < fgBest):
                fgBest = fness[j]
                for d in range(D):
                        gBest[d] = pop[j][d]

        for x in range(0, NFC/P_MAX * D):
            end = time() - start
            
            print("%3d  iteration: %3d  function: %s    time: %10.4f s" % ((x * 1.0)/(NFC/P_MAX * D) * 100, r, prefix, end))
            W = W * (((NFC/P_MAX * D) - x * 1.0) / ((NFC/P_MAX) *D))

            for j in range(P_MAX):
                for d in range(D):
                    rho1 = np.random.rand()
                    rho2 = np.random.rand()
                    vel[j][d] = W * vel[j][d] + rho1 * C1 * (pBest[j][d] - pop[j][d]) + rho2 * C2 * (gBest[d] - pop[j][d])
                    if((pop[j][d] + vel[j][d]) >= -10 and (pop[j][d] + vel[j][d]) <= 10):
                        pop[j][d] = pop[j][d] + vel[j][d]
                    elif((pop[j][d] + vel[j][d]) < -10):
                        pop[j][d] = -10
                        vel[j][d] = vel[j][d] * -1
                    elif((pop[j][d] + vel[j][d]) > 10):
                        pop[j][d] = 10
                        vel[j][d] = vel[j][d] * -1

                fness[j] = eval(pop[j],e)

                if(fness[j] < fpBest[j]):
                    fpBest[j] = fness[j]
                    for d in range(D):
                        pBest[j][d] = pop[j][d]

                if(fness[j] < fgBest):
                    fgBest = fness[j]
                    for d in range(D):
                        gBest[d] = pop[j][d]

                if(fness[j] < best[x]):
                    best[x] = fness[j]

            #print best[x]
            avg[x] += best[x]

        out_file = open("data/" + str(D) + "_" + prefix + "_pso_points" + str(r) + ".csv","w")
        full_output = pop.tolist()
        for line in full_output:
            out_file.write(str(line)[1:-1] + ', ' + str(eval(line,e)) + "\n")
        out_file.close()
        for x in range (NFC/P_MAX*D):
            avg[x] = avg[x]/51.0
    
    plot_file = open("plots/" + str(D) + "_" + prefix + "_pso_plot" + ".csv","w")
    for line in avg:
        plot_file.write(str(line) + "\n")
    plot_file.close()


                    

                
            

