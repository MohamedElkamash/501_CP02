import numpy as np
from constants import *
import plots

#mesh
n_points = 100
r = np.linspace(0, R, n_points)

#time axis
n_time_points = 1000
t_max = 300 #s
t = np.linspace(0, t_max, n_time_points)

#steady state temperature
T_ss = q_0/(4*k) * (R**2 - r**2) + q_0*R/(2*h) + T_b0

#heat generation and fluid temperature
q = np.empty((len(m), len(t)))
T_b = np.empty((len(m), len(t)))

for i in range(len(m)):
    q[i,:] = q_0/2 * (1 + np.exp(-m[i]*t))
    T_b[i,:] = T_b0/2 * (1 + np.exp(-m[i]*t))

#plots
plots.T_ss(r, T_ss)
plots.q(t,q,m)
plots.T_b(t, T_b, m)
