#Inputs
R = 0.005   #m
k = 2       #W m^-1 K^-1
h = 45000   #W m^-2 K-2
T_b0 = 300  #degC
T_max = 700 #degC
rho = 10750 #kg m^-3
Cp = 311    #J kg^-1 K^-1

alpha = k/(rho*Cp)

#steady state heat generation
q_0 = (T_max - T_b0) / (R**2/(4*k) + R/(2*h))

#time constants
m = [0.015, 0.020, 0.025]

eta = [0.015, 0.020, 0.025]

#conversions
m_to_cm = 100



