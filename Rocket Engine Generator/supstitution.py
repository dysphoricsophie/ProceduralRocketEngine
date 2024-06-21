import numpy as np
from scipy.interpolate import interp1d

CH4_data = np.loadtxt('data/ch4_janaf.txt',dtype='float', skiprows=3)
O2_data = np.loadtxt('data/o2_janaf.txt',dtype='float', skiprows=3)
CO2_data = np.loadtxt('data/co2_janaf.txt',dtype='float', skiprows=3)
H2O_data = np.loadtxt('data/h2o_janaf.txt',dtype='float', skiprows=3)

CH4_hf = np.interp(298.15, CH4_data[:, 0], CH4_data[:, 5])
O2_hf = np.interp(298.15, O2_data[:, 0], O2_data[:, 5])
CO2_hf = np.interp(298.15, CO2_data[:, 0], CO2_data[:, 5])
H2O_hf = np.interp(298.15, H2O_data[:, 0], H2O_data[:, 5])

co2_dh = interp1d(CO2_data[:,0], CO2_data[:,4])
h2o_dh = interp1d(H2O_data[:,0], H2O_data[:,4])
delta_h_f_o = 2 * H2O_hf + CO2_hf - CH4_hf - 2 * O2_hf
q_rxn = CH4_hf + 2 * O2_hf - CO2_hf - 2 * H2O_hf

temps = np.linspace(300,6000,100)
h_comb = np.zeros_like(temps)

for j, T in enumerate(temps):
    h_comb[j] = 2*h2o_dh(T) + co2_dh(T)

T_adiabatic = (np.interp(-delta_h_f_o, h_comb, temps))-273.15
T_kinetic = ((q_rxn*1000)/(64.22+(2*59.628)))+298.15
print(T_kinetic)
print(T_adiabatic)