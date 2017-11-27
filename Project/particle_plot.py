import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib, time
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter
from function_list import *
from matplotlib import cm

P_MAX = 100
C1 = 2.05
C2 = 2.05
NFC = 5000
D = 2
e = int(sys.argv[1])
prefix = ""

class plot3dClass( object ):

    def __init__( self,x1, y1, X, Y, zs, Z):
        self.x1 = x1
        self.y1 = y1
        self.X = X
        self.Y = Y
        self.zs = zs
        self.Z = Z
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot( 111, projection='3d' )

        self.ax.w_zaxis.set_major_locator( LinearLocator( 10 ) )
        self.ax.w_zaxis.set_major_formatter( FormatStrFormatter( '%.03f' ) )
        self.surf = self.ax.plot_surface( 
            self.X, self.Y, self.Z, cmap=cm.coolwarm, alpha=0.5 )
        # plt.draw() maybe you want to see this frame?

    def drawNow( self, pop, h, pnum):
        plt.cla()
        self.surf = self.ax.plot_surface( 
            self.X, self.Y, self.Z, cmap=cm.coolwarm, alpha=0.5 )
        for x in range(pnum):
            self.ax.scatter(pop[x][0], pop[x][1], h[x], lw=5, color='green')
        plt.draw()
        self.fig.canvas.flush_events()                      # redraw the canvas

matplotlib.interactive(True)

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

x1 = y1 = np.arange(-10, 10, 0.05)
X, Y = np.meshgrid(x1,y1)
zs = np.array([eval([x1,y1],e) for x1,y1 in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)
p = plot3dClass(x1,y1,X,Y,zs,Z)

print "Init..."
start = time.time()
end = time.time() - start
W = 0.9
pop = np.random.uniform(-10.0, 10.0, (P_MAX, D))
vel = np.random.uniform(-1.0, 1.0, (P_MAX, D))
fness = [eval(pop[x],e) for x in range(P_MAX)]
gBest = np.random.uniform(0.0,0.0,(D))
for x in range(D):
    gBest[x] = pop[0][x]
fgBest = fness[0]
pBest = pop
fpBest = fness

for j in range(P_MAX):
    if(fness[j] < fgBest):
        fgBest = fness[j]
        for d in range(D):
                gBest[d] = pop[j][d]

for x in range(0, NFC/P_MAX * D):

    best = fness[0]
    end = time.time() - start
    
    W = 0.5 * (((NFC/P_MAX * D) - x * 1.0) / ((NFC/P_MAX) *D)) + 0.4

    for j in range(P_MAX):
        rho1 = np.random.rand()
        rho2 = np.random.rand()
        for d in range(D):

            print (str(gBest[d]))

            vel[j][d] = W * vel[j][d] + rho1 * C1 * (pBest[j][d] - pop[j][d]) + rho2 * C2 * (gBest[d] - pop[j][d])

            if((pop[j][d] + vel[j][d]) >= -10 and (pop[j][d] + vel[j][d]) <= 10):
                pop[j][d] = pop[j][d] + vel[j][d]
            elif((pop[j][d] + vel[j][d]) < -10):
                pop[j][d] = -10
                vel[j][d] = vel[j][d] * -1/2.0
            elif((pop[j][d] + vel[j][d]) > 10):
                pop[j][d] = 10
                vel[j][d] = vel[j][d] * -1/2.0

        fness[j] = eval(pop[j],e)

        if(fness[j] < fpBest[j]):
            fpBest[j] = fness[j]
            for d in range(D):
                pBest[j][d] = pop[j][d]

        if(fness[j] < fgBest):
            fgBest = fness[j]
            for d in range(D):
                gBest[d] = pop[j][d]

        if(fness[j] < best):
            best = fness[j]

    print("%3d  function: %s    time: %10.4f s %10.10f" % ((x * 1.0)/(NFC/P_MAX * D) * 100, prefix, end, best))

    #print best[x]
    if(x % 6 == 0):
        p.drawNow(pop,fness,P_MAX)
    if(x == 0):
        time.sleep(1)


                    

                
            

