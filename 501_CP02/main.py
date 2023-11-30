import numpy as np
import matplotlib.pyplot as plt
import finite_difference as fd
from constants import *
from data import *
import plots
import analytical

""" r = np.linspace(1e-10,R, 10)
t = np.linspace(0,300, 10000)
T = fd.computeT(r,t)


plt.plot(r, T[:,9999])
plt.show() """

#Plotting and printing eigenvalues
eigenvalues = analytical.computeEigenvalues()
plots.eigenvalues()
#export.eigenvalues()


#Grid Refinment
fig_grid_ref, axs_grid_ref, axs_grid_ref_list = plots.six_subplots()
legend_grid = []
n_elements = 2
delta_r = 0
n_grid_trials = 5
delta_t = 0.005
t = np.linspace(0, t_max, int(t_max/delta_t) + 1)
T_converged = 0

for i in range(n_grid_trials):
    r = np.linspace(epilson, R, n_elements+1)
    delta_r = R/n_elements
    T_numerical = np.empty([len(r), len(t)])
    T_numerical = fd.computeT(r, t)
    
    #plot
    for j in range(len(timestamps)):
        axs_grid_ref_list[j].plot(r*m_to_cm, T_numerical[:,int(timestamps[j]/delta_t)])
    exp = i+2
    legend_grid.append("$\Delta$" + "r =" + "$2^{-}$" rf"$^{exp}$" + " (cm)")
    n_elements *= 2
    
plt.legend(legend_grid, loc = "center", bbox_to_anchor = (1.3, 1.6), fontsize = 15)
plt.savefig("grid_ref.png", bbox_inches='tight', dpi = 400)
plt.close()


#time step study
n_elements = 32
delta_r = R/n_elements
r = np.linspace(epilson, R, n_elements+1)

#final evaluation
delta_t = 0.005
t = np.linspace(0, t_max, int(t_max/delta_t) + 1)
T_numerical = np.empty([len(r), len(t)])
T_numerical = fd.computeT(r, t)
plots.T_numerical(r, T_numerical, delta_t)

""" #bad time step
plt.figure()
delta_t = 0.01
t = np.linspace(0, t_max, int(t_max/delta_t) + 1)
T_numerical = np.empty([len(r), len(t)])
T_numerical = fd.computeT(r, t)
plt.xlabel("r (cm)")
plt.ylabel("T(r,50) ($^oC$)")
plt.plot(r*m_to_cm, T_numerical[:, 5000])
plt.savefig("bad time_step.png", bbox_inches='tight', dpi = 400)
plt.close() """

#good time step
""" fig_time_step, axs_step, axs_time_step_list = plots.six_subplots()
legend_time_step = []
delta_t = 0.005

t = np.linspace(0, t_max, int(t_max/delta_t) + 1)
T_numerical = np.empty([len(r), len(t)])
T_numerical = fd.computeT(r, t)

#plot
for j in range(len(timestamps)):
    axs_time_step_list[j].plot(r*m_to_cm, T_numerical[:,int(timestamps[j]/delta_t)])
plt.savefig("time_step.png", bbox_inches='tight', dpi = 400)
plt.close() """


""" #final numerical evaluation
n_elements = 32
delta_r = R/n_elements
r = np.linspace(0, R, n_elements+1)
delta_t = 0.05
t = np.linspace(0, t_max, int(t_max/delta_t) + 1)
T_numerical = fd.computeT(r, t, delta_r, delta_t) """