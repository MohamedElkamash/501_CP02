import numpy as np
from constants import *
from scipy.optimize import fsolve
from scipy.special import jv
import scipy.integrate as integrate
import plots
import matplotlib.pyplot as plt
import csv


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
eigenvalues_guess = [477, 1094, 1715, 2338, 2960, 3582, 4205, 4828, 5451, 6074, 6694, 7320, 7944, 8567, 9190, 9814, 10438, 11061, 11685, 12309, 12933]

def eigenvaluesEquation(lamda):
    return lamda*jv(1,lamda*R) - h/k * jv(0,lamda*R)

def computeEigenvalues():
    eigenvalues = fsolve(eigenvaluesEquation, eigenvalues_guess)
    return eigenvalues

""" guess = np.linspace(0,20000,2001)
eigen = fsolve(eigenvaluesEquation, guess)
eigen_unique = np.unique(eigen)
print(eigen_unique) """


""" eigen = np.zeros(10000)
i = 0
for guess in range(0, 10000, 1):
    x = fsolve(eigenvaluesEquation, guess)
    if (np.abs(x - eigen[i])) > 1:
        eigen[i+1] = x
        i = i + 1

for j in range(len(eigen)):
    if eigen[j] > 0:
        print(eigen[j]) """

""" with open("eigenvalues.csv", 'r') as x:
    eigen = list(csv.reader(x, delimiter=",")) """
    
lamda = np.genfromtxt('1900EVs.csv', dtype=float, delimiter=',')
lamda = lamda[0:225]

#lamda = computeEigenvalues()
""" 
print(lamda)

x = np.linspace(9000,15000,1000)
y = eigenvaluesEquation(x)
plt.plot(x,y)
plt.xticks(np.arange(9000,15001, 1000))
plt.ylim(0,1000)
plt.show() """
n_terms = len(lamda)

def I_1():
    result = np.empty(len(lamda))
    for i in range(len(lamda)):
        result[i], error = integrate.quad(lambda r: r*jv(0,lamda[i]*r), 0, R)
    return result

def I_2():
    result = np.empty(len(lamda))
    for i in range(len(lamda)):
        result[i], error = integrate.quad(lambda r: r*(jv(0,lamda[i]*r))**2, 0, R)
    return result

def I_3():
    result = np.empty(len(lamda))
    for i in range(len(lamda)):
        result[i], error = integrate.quad(lambda r: r*jv(0,lamda[i]*r) * (q_0/(4*k) * (R**2 - r**2) + q_0*R/(2*h) + T_b0), 0, R)
    return result

def c_1():
    result = np.empty(len(lamda))
    for i in range(len(lamda)):
        result[i] = alpha*h*R*T_b0*jv(0,lamda[i]*R) / (2*k)
    return result

def c_2():
    result = np.empty(len(lamda))
    for i in range(len(lamda)):
        result[i] = alpha*q_0*I_1()[i] / (2*k)
    return result

def alpha_lamda_square():
    result = np.empty(len(lamda))
    for i in range(len(lamda)):
        result[i] = alpha*lamda[i]**2
    return result



