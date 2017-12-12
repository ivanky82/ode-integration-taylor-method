import math as m
import numpy as np

def derivative(x):
	z = []
	for i in range(1,len(x)):
		z.append(i*x[i])
	z.append(0.0)	
	return z

def addpoli(x,y):
    z = []
    n1 = len(x)
    n2 = len(y)
    n = min(n1,n2)
    for k in range(0,n):
        z.append(x[k]+y[k])
    return z

def subtractpoli(x,y):
    z = []
    n1 = len(x)
    n2 = len(y)
    n = min(n1,n2)
    for k in range(0,n):
        z.append(x[k]-y[k])
    return z

def addconstantpoli(a,x):
    z = []
    n = len(x)
    for k in range(0,n):
        if k == 0:
            z.append(x[k]+a)
        else:
            z.append(x[k])
    return z

def multiplyconstantpoli(a,x):
    z = []
    n = len(x)
    for k in range(0,n):
        z.append(a*x[k])
    return z

def multiplypoli(x,y):
    z = []
    n1 = len(x)
    n2 = len(y)
    n = min(n1,n2)
    for k in range(0,n):
        temp = 0.0
        for j in range(0,k+1):
            temp = temp + x[j]*y[k-j]
        z.append(temp)
    return z

def divideconstantpoli(a,x):
    z = []
    n = len(x)
    for k in range(0,n):
        if x[k] == 0 :
            print("cannot input zero")
        elif k == 0 :
            z.append(a/float(x[k]))
        elif k == 1 :
            z.append(((-z[k-1]*x[k]))/float(x[k-1]))
        else :
            temp = 0.0
            for j in range(0,k):
                temp = temp + z[j]*x[k-j]
            z.append((-temp)/float(x[0]))
    return z

def dividepoli(x,y):
    z = []
    n1 = len(x)
    n2 = len(y)
    n = min(n1,n2)
    for k in range(0,n):
        if k == 0 :
            z.append(x[k]/float(y[k]))
        elif k == 1 :
            z.append((x[k]-(y[k]*z[k-1]))/float(y[0]))
        else :
            temp = 0.0
            for j in range(0,k):
                temp = temp + z[j]*y[k-j]
            z.append((x[k]-temp)/float(y[0]))
    return z

def exponentialpoli(x):
    z = []
    n = len(x)
    for k in range (0,n):
        if k == 0 :
            z.append(float(m.exp(x[k])))
        elif k == 1 :
            z.append(float(x[k]*z[k-1]))
        else :
            temp = 0.0
            for j in range(0,k):
                temp = temp + (k-j)*z[j]*x[k-j]
            z.append((temp)/float(k))
    return z

def exponentialpoli2(x):
	z = []
	n = len(x)
	dx = derivative(x)
	y = []
	z.append(m.exp(x[0]))
	y.append(z[0])
	for k in range(1,n):
		u = multiplypoli(dx,y)
		z.append(u[k-1]/float(k))
		y.append(z[k])
	return z

def sqrtpoli(x):
    z = []
    n = len(x)
    for k in range (0,n):
        if k == 0 :
            z.append(float(m.sqrt(x[0])))
        elif k == 1 :
            z.append((z[k-1]*x[k])/float(2*x[k-1]))
        else :
            temp1 = 0.0
            temp2 = 0.0
            for b in range(1,k):
                temp1 = temp1 + float(b*z[b]*2*x[k-b])
            for j in range(0,k):
                temp2 = temp2 + float((k-j)*z[j]*x[k-j])
            z.append(float(temp2-temp1)/float(2*k*x[0]))
    return z

def sqrtpoli2(x):
	z = []
	n = len(x)
	y = []
	dx = derivative(x)
	z.append(m.sqrt(x[0]))
	y.append(2*z[0])
	for k in range(1,n):
		u = dividepoli(dx,y)
		z.append(u[k-1]/float(k))
		y.append(2*z[k])
	return z


def integrate(F,y_init,t_init = 0.0 ,tStop = 0.4 ,h = 0.01 ):
    dim = len(y_init)
    y_sol = []
    for i in range(0,dim):
        y_sol.append([])
        y_sol[i].append(y_init[i])
    t_sol = []
    t_sol.append(t_init)
    t = t_init
        
    while t < tStop:
        y = []
        for i in range(0,dim):
            y.append([])
            y[i].append(y_sol[i][-1])
                
        for k in range(0,23):
            dy = F(y)
            for i in range(0,dim):
                y[i].append(dy[i][k]/float(k+1))
        n = len(y[0])
        for i in range(0,dim):
            temp = 0.0
            for j in range(0,n):
                temp = temp + y[i][j]*h**j
            y_sol[i].append(temp)
        t_sol.append(t+h)
        t = t + h
        
    return np.array(t_sol) ,np.transpose(np.array(y_sol))
