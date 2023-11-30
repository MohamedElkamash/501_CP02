import matplotlib.pyplot as plt
import numpy as np
from constants import *
from data import timestamps

def T_ss(r, T_ss):
    fig, ax = plt.subplots()
    ax.set_xlabel("r (cm)", fontsize = 11)
    ax.set_ylabel("$T_{ss} \; (^{\degree}C)$", fontsize = 11)
    ax.set_xticks(np.arange(0, R * m_to_cm + 1, 0.1))
    ax.set_yticks(np.arange(300, max(T_ss) + 101, 100))
    ax.set_xlim(0, R * m_to_cm)
    ax.set_ylim(300, max(T_ss)+100)
    ax.plot(r * m_to_cm, T_ss)
    plt.savefig("T_ss.png", bbox_inches='tight', dpi = 400)

def q(t, q, m):
    fig, ax = plt.subplots()
    ax.set_xlabel("t (s)", fontsize = 11)
    ax.set_ylabel("$q \; (W/m^{3})$", fontsize = 11)
    ax.set_xlim(0, max(t))
    ax.set_xticks(np.arange(0, max(t) + 1, 50))
    ax.set_yticks(np.arange(0.6e8, 1.3e8 +1, 0.1e8))
    ax.set_ylim(0.6e8, 1.3e8)
    legend = []
    for i in range(len(m)):
        ax.plot(t, q[i, :])
        legend.append("m = " + "{:.3f}".format(m[i]) + " $s^{-1}$")
    plt.legend(legend)
    plt.savefig("q.png", bbox_inches='tight', dpi = 400)

def T_b(t, T_b, m):
    fig, ax = plt.subplots()
    ax.set_xlabel("t (s)", fontsize = 11)
    ax.set_ylabel("$T_{b} \; (^{\degree}C)$", fontsize = 11)
    ax.set_yticks(np.arange(150, 301, 25))
    ax.set_ylim(150, 300)
    ax.set_xlim(0, max(t))
    ax.set_xticks(np.arange(0, max(t) + 1, 50))
    legend = []
    for i in range(len(m)):
        ax.plot(t, T_b[i, :])
        legend.append("m = " + "{:.3f}".format(m[i]) + " $s^{-1}$")
    plt.legend(legend)
    plt.savefig("T_b.png", bbox_inches='tight', dpi = 400)

def eigenvalues(x,y):
    fig_eigen, ax_eigen = plt.subplots()
    ax_eigen.set_xlabel("$\lambda (m^{-1})$", fontsize = 11)
    ax_eigen.set_ylabel("$\lambda J_{1} (\lambda R)$ - " + r"$\frac{h}{k}$" + "$ \; J_{0} (\lambda R)$", fontsize = 11)
    ax_eigen.set_xticks(np.arange(0,6301,1000))
    ax_eigen.set_yticks(np.arange(-25000,10001,10000))
    ax_eigen.set_xlim(0,6300)
    ax_eigen.set_ylim(-25000,10000)
    ax_eigen.tick_params(axis = 'both', labelsize = 11)
    ax_eigen.plot(x,y)
    ax_eigen.axhline(0, color = 'r')
    plt.savefig("Eigenvalues.png", bbox_inches='tight', dpi = 400)
    plt.close()

def T_numerical(r, T_numerical, delta_t):
    fig_analytical, ax = plt.subplots()
    ax.set_xlabel("r (cm)", fontsize = 11)
    ax.set_ylabel('T(r,t) ($^oC$)', fontsize = 11)
    ax.set_xticks(np.arange(0,R * m_to_cm + 1,0.1))
    ax.set_yticks(np.arange(100,701,100))
    ax.set_xlim(0,0.5)
    ax.set_ylim(100,700)
    ax.tick_params(axis = 'both', labelsize = 11)
    legend = []
    for i in range(len(timestamps)):
        ax.plot(r*m_to_cm, T_numerical[:,int(timestamps[i]/delta_t)])
        legend.append("t = " + str(int(timestamps[i])) + "s")
    plt.legend(legend)
    plt.savefig("Numerical.png", bbox_inches='tight', dpi = 400)
    plt.close()

def six_subplots():
    fig_T, axs = plt.subplots(3,2, figsize = (12.0,12.0))
    axs_list = [axs[0,0], axs[0,1], axs[1,0], axs[1,1], axs[2,0], axs[2,1]]
    plt.setp(axs, xlabel="r (cm)", xticks=np.arange(0,R * m_to_cm + 1,0.1), yticks=np.arange(0,801,100), xlim=(0,0.5), ylim=(0,800))
    legend_T_analytical_individual = []
    for i in range(len(timestamps)):
        plt.setp(axs_list[i], ylabel = "T(r," + str(int(timestamps[i])) + ") ($^oC$)")
    return fig_T, axs, axs_list

def T_ss_1_and_2(r, T_ss, T_ss_split):
    fig, ax = plt.subplots()
    ax.set_xlabel("r (cm)", fontsize = 11)
    ax.set_ylabel("$T(r) \; (^{\degree}C)$", fontsize = 11)
    ax.set_xticks(np.arange(0, R * m_to_cm + 1, 0.1))
    ax.set_yticks(np.arange(100, max(T_ss) + 101, 100))
    ax.set_xlim(0, R * m_to_cm)
    ax.set_ylim(100, max(T_ss)+100)
    ax.plot(r * m_to_cm, T_ss)
    ax.plot(r*m_to_cm, T_ss_split)
    legend = ["$T_{i}$", "$T_{ss}$"]
    plt.legend(legend)
    plt.savefig("T_ss_comparison.png", bbox_inches='tight', dpi = 400)

def analytical(r, T, delta_t):
    fig_analytical, ax = plt.subplots()
    ax.set_xlabel("r (cm)", fontsize = 11)
    ax.set_ylabel('$T(r,t) \; (^{\degree}C)$', fontsize = 11)
    ax.set_xticks(np.arange(0, R * m_to_cm + 1, 0.1))
    ax.set_yticks(np.arange(100, 801, 100))
    ax.set_xlim(0, R * m_to_cm)
    ax.set_ylim(100, 800)
    ax.tick_params(axis = 'both', labelsize = 11)
    legend_T_analytical = []
    for i in range(len(timestamps)):
        ax.plot(r*m_to_cm, T[:,int(timestamps[i]/delta_t)])
        legend_T_analytical.append("t = " + str(int(timestamps[i])) + "s")
    plt.legend(legend_T_analytical)
    plt.savefig("analytical_all2.png", bbox_inches='tight', dpi = 400)
    plt.close()




