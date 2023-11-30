from constants import *
import matplotlib.pyplot as plt
import numpy as np

def computeT(r, t):
    
    #mesh and step sizes
    del_r = R/(len(r)-1)
    del_t = max(t)/(len(t)-1)
    
    #heat generation and fluid temperature
    q   = np.empty(len(t))
    T_b = np.empty(len(t))
    q   = q_0/2  * (1 + np.exp(-m[1]*t))
    T_b = T_b0/2 * (1 + np.exp(-m[1]*t))

    #define temperature matrix
    T = np.empty((len(r), len(t)))
    #apply initial condition
    T[:,0] = q_0/(4*k) * (R**2 - r**2) + q_0*R/(2*h) + T_b0

    for j in range(1, len(t)):

        #update boundary at r = 0
        T[0,j] = T[0,j-1] + 2*alpha*del_t/del_r**2 * (T[1,j-1] - T[0,j-1]) + alpha*del_t/k * q[j-1]

        #update interior points
        for i in range(1, len(r)-1):
            T[i,j] = T[i,j-1] + alpha*del_t/del_r**2 * (T[i+1, j-1] - 2*T[i,j-1] + T[i-1,j-1]) + alpha*del_t/(2*r[i]*del_r) * (T[i+1,j-1] - T[i-1,j-1]) + alpha*del_t/k * q[j-1]
        
        #update boundary at r = R
        I = len(r) - 1
        T[I,j] = T[I,j-1] + 2*alpha*del_t/del_r**2 * (T[I-1,j-1] - T[I,j-1]) - alpha*del_t*h/k * (2/del_r + 1/r[I]) * (T[I,j-1] - T_b[j-1]) + alpha*del_t/k * q[j-1]
    
    return T