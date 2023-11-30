import numpy as np
from constants import *
from scipy.optimize import fsolve
from scipy.special import jv
import scipy.integrate as integrate
import plots
import matplotlib.pyplot as plt
import csv
from data import *
import finite_difference as fd

#mesh
n_points = 100
r = np.linspace(0, R, n_points)

#time axis
n_time_points = 100
t_max = 300 #s
t = np.linspace(0, t_max, n_time_points)
delta_t = t_max/(n_time_points-1)



#steady state temperature
T_ss_a = q_0/(4*k) * (R**2 - r**2) + q_0*R/(2*h) + T_b0

#heat generation and fluid temperature
q = np.empty((len(m), len(t)))
T_b = np.empty((len(m), len(t)))

for i in range(len(m)):
    q[i,:] = q_0/2 * (1 + np.exp(-m[i]*t))
    T_b[i,:] = T_b0/2 * (1 + np.exp(-m[i]*t))


#initial guess of the first 10 eigenvalues
eigenvalues_guess = [477, 1094, 1715, 2338, 2960, 3582, 4205, 4828, 5451, 6074, 6694, 7320, 7944, 8567, 9190, 9814, 10438, 11061, 11685, 12309, 12933]

def eigenvaluesEquation(lamda):
    return lamda*jv(1,lamda*R) - h/k * jv(0,lamda*R)

def computeEigenvalues():
    eigenvalues = fsolve(eigenvaluesEquation, eigenvalues_guess)
    return eigenvalues

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

def computeT():
    I1 = I_1()
    I2 = I_2()
    I3 = I_3()
    c1 = c_1()
    c2 = c_2()
    a = alpha_lamda_square()

    T = np.zeros((n_points, n_time_points))

    for i in range(n_terms):
        for j in range(n_points):
            for k in range(n_time_points):
            
                n1 = m[1] - a[i] + (2*a[i] - m[1]) * np.exp(-a[i]*t[k]) - a[i] * np.exp(-m[1]*t[k])
                n2 = eta[1] - a[i] + (2*a[i] - eta[1]) * np.exp(-a[i]*t[k]) - a[i] * np.exp(-eta[1]*t[k])
                d1 = a[i] * (m[1] - a[i])
                d2 = a[i] * (eta[1] - a[i])
                
                T[j,k] = T[j,k] + jv(0,lamda[i]*r[j]) / I2[i] * (I3[i] * np.exp(-a[i]*t[k]) + c1[i] * n1/d1 + c2[i] * n2/d2)
    return T

def computeTsplit():
    I2 = I_2()
    I3 = I_3()
    c1 = c_1()
    c2 = c_2()
    a = alpha_lamda_square()

    T = np.zeros((n_points, n_time_points))

    for i in range(n_terms):
        for j in range(n_points):
            for k in range(n_time_points):
                T[j,k] = T[j,k] + I3[i] / (2*I2[i]) * jv(0,lamda[i]*r[j]) * np.exp(-a[i]*t[k])
    
    for j in range(n_points):
        for k in range(n_time_points):
            T[j,k] = T_ss_a[j]/2 + T[j,k]
    return T



""" 
plt.plot(r,T[:,399])
plt.show() """

fig, ax, axs_list = plots.six_subplots()
legend = []
lamda_all = np.genfromtxt('1900EVs.csv', dtype=float, delimiter=',')

#n_terms_array = [2, 10, 20, 30, 40, 50, 100]

lamda = lamda_all[0:200]
n_terms = len(lamda)


T_anal = computeT()
plots.analytical(r,T_anal,delta_t)
#T_split = computeTsplit()

""" #time step study
n_elements = 32
delta_r = R/n_elements
r_num = np.linspace(epilson, R, n_elements+1)
delta_t_num = 0.005
t_num = np.linspace(0, t_max, int(t_max/delta_t_num) + 1)

#final evaluation

T_numerical = np.empty([len(r_num), len(t_num)])
T_numerical = fd.computeT(r_num, t_num)


fig, ax, axs_list = plots.six_subplots()


for j in range(len(timestamps)):
    axs_list[j].plot(r*m_to_cm, T_anal[:,int(timestamps[j]/delta_t)])
    axs_list[j].plot(r_num*m_to_cm, T_numerical[:,int(timestamps[j]/delta_t_num)])
    #axs_list[j].plot(r*m_to_cm, T_split[:,int(timestamps[j]/delta_t)])


        
legend = ["$T_{analytical}$", "$T_{numerical}$"]
plt.legend(legend, loc = "center", bbox_to_anchor = (1.3, 1.6), fontsize = 15)


plt.savefig("final_comparison.png", bbox_inches='tight', dpi = 400)
plt.close()   """