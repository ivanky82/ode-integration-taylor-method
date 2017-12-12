from mytaylor import *
import matplotlib.pyplot as plt
import numpy as np
import math as m

#define your function here
def fun(y):
    z = subtractpoli(y[0],multiplypoli(y[0],y[0])) #dy/dt = y-y^2
    return [z]

y_init = [0.5]
t_init = 0
h = 0.1
tStop = 1.0
T, Y = integrate(fun,y_init,t_init,tStop,h)

#real solution computation
real_sol = []
for t in T:
	temp = m.exp(t)/(m.exp(t)+1.0)
	real_sol.append(temp)
print Y
print real_sol
#plotting the error versus time
real_sol = np.array(real_sol)
error = Y[:,0]-real_sol
#plt.plot(T[:],error[:])
#plt.show()
