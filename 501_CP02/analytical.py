import numpy as np
from constants import *
from scipy.optimize import fsolve
from scipy.special import jv
import scipy.integrate as integrate
import plots
import matplotlib.pyplot as plt

#mesh
n_points = 100
r = np.linspace(0, R, n_points)

#time axis
n_time_points = 100
t_max = 200 #s
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
""" plots.T_ss(r, T_ss)
plots.q(t,q,m)
plots.T_b(t, T_b, m) """

#initial guess of the first 10 eigenvalues
eigenvalues_guess = [477, 1094, 1715, 2338, 2960, 3582, 4205, 4828, 5451, 6074]

def eigenvaluesEquation(lamda):
    return lamda*jv(1,lamda*R) - h/k * jv(0,lamda*R)

def computeEigenvalues():
    eigenvalues = fsolve(eigenvaluesEquation, eigenvalues_guess)
    return eigenvalues

eigenvalues = computeEigenvalues()
lamda = eigenvalues[0:10]

""" x = np.linspace(0, 7000, 1000)
y = eigenvaluesEquation(x)
plots.eigenvalues(x,y) """

def c_1():
    return 2*lamda**2 / (R**2 * (jv(0,lamda*R))**2 * (h/k + lamda**2))

def c_2():
    result = np.empty(len(lamda))
    for i in range(len(lamda)):
        result[i], error = integrate.quad(lambda r: r*jv(0,lamda[i]*r)*(q_0/(4*k) * (R**2 - r**2) + q_0*R/(2*h) + T_b0), 0, R)
    return result

def c_3():
    result = np.empty(len(lamda))
    for i in range(len(lamda)):
        result[i], error = integrate.quad(lambda r: r*(jv(0,lamda[i]*r))**2 * 2*lamda[i]**2 / (R**2 * (jv(0,lamda[i]*R))**2 * (h/k + lamda[i]**2))  , 0, R)
    return result

def c_4():
    return alpha*h*R*jv(0,lamda*R)*T_b0/(2*k)

def c_5():
    result = np.empty(len(lamda))
    for i in range(len(lamda)):
        result[i], error = integrate.quad(lambda r: r*jv(0,lamda[i]*r)*alpha*q_0 / (2*k), 0, R)
    return result

def c_6():
    return alpha*lamda**2

def computeT():
    c1 = c_1()
    c2 = c_2()
    c3 = c_3()
    c4 = c_4()
    c5 = c_5()
    c6 = c_6()

    T = np.zeros((len(r), len(t)))

    n_terms = 10
    sum = np.zeros(len(r))

    for j in range(len(r)):
        for k in range(len(t)):
            for i in range(n_terms):
                T[j,k] = T[j,k] + c1[i]*jv(0,r[j]) * (c2[i]/c3[i] * np.exp(-c6[i]*t[k]) + c4[i]*(m[1]-c6[i]*(1+np.exp(-m[1]*t[k]))-(m[1]-2*c6[i])*np.exp(-c6[i]*t[k]))/(m[1]*c6[i]-c6[i]**2) + c5[i]*(eta[1]-c6[i]*(1+np.exp(-eta[1]*t[k]))-(eta[1]-2*c6[i])*np.exp(-c6[i]*t[k]))/(eta[1]*c6[i]-c6[i]**2))
    return T

T = computeT()
plt.plot(r,T[:,99])
plt.show()

