import numpy
import matplotlib.pyplot as plt

# To define the range of equivalence ratio (0.1,0.2,0.3.....2.0)
i = numpy.linspace(0.1, 2.0, 200)
e_r = i  # e_r represents range of equivalence ratio

def h(T, co_effs):  # Function to calculate enthalpy of all reactants and products
    R = 8.314  # J/mol-K
    a1 = co_effs[0]
    a2 = co_effs[1]
    a3 = co_effs[2]
    a4 = co_effs[3]
    a5 = co_effs[4]
    a6 = co_effs[5]
    return (a1 + a2 * T / 2 + a3 * pow(T, 2) / 3 + a4 * pow(T, 3) / 4 + a5 * pow(T, 4) / 5 + a6 / T) * R * T

# Low temperature coefficients (Reactants) at STP condition
CH4_coeffs_l = [5.14987613E+00, -1.36709788E-02, 4.91800599E-05, -4.84743026E-08, 1.66693956E-11, -1.02466476E+04, -4.64130376E+00]
O2_coeffs_l = [3.78245636E+00, -2.99673416E-03, 9.84730201E-06, -9.68129509E-09, 3.24372837E-12, -1.06394356E+03, 3.65767573E+00]
N2_coeffs_l = [0.03298677E+02, 0.14082404E-02, -0.03963222E-04, 0.05641515E-07, -0.02444854E-10, -0.10208999E+04, 0.03950372E+02]

# High temperature coefficients	(Products)
N2_coeffs_h = [0.02926640E+02, 0.14879768E-02, -0.05684760E-05, 0.10097038E-09, -0.06753351E-13, -0.09227977E+04, 0.05980528E+02]
CO2_coeffs_h = [3.85746029E+00, 4.41437026E-03, -2.21481404E-06, 5.23490188E-10, -4.72084164E-14, -4.87591660E+04, 2.27163806E+00]
H2O_coeffs_h = [3.03399249E+00, 2.17691804E-03, -1.64072518E-07, -9.70419870E-11, 1.68200992E-14, -3.00042971E+04, 4.96677010E+00]
CO_coeffs_h = [2.71518561E+00, 2.06252743E-03, -9.98825771E-07, 2.30053008E-10, -2.03647716E-14, -1.41518724E+04, 7.81868772E+00]
O2_coeffs_h = [3.28253784E+00, 1.48308754E-03, -7.57966669E-07, 2.09470555E-10, -2.16717794E-14, -1.08845772E+03, 5.45323129E+00]

def f(T, e_r):
    # To calculate enathlpy of reactants and products and to perform root finding problem
    # For calculation of enthalpy of Products in Jouls

    R = 8.314  # J/mol-K
    h_N2_p = h(T, N2_coeffs_h)  # J/Mol-K
    h_CO2_p = h(T, CO2_coeffs_h)  # J/Mol-K
    h_H2O_p = h(T, H2O_coeffs_h)  # J/Mol-K
    h_CO_p = h(T, CO_coeffs_h)  # J/Mol-K
    h_O2_p = h(T, O2_coeffs_h)  # J/Mol-K

    if e_r > 1:  # Conditional loop based on equivalence ratio enthalpy of products will be find out
        H_products = ((4 / e_r) - 3) * h_CO2_p + (4 - (4 / e_r)) * h_CO_p + 2 * h_H2O_p + (7.52 / e_r) * h_N2_p  # Enthalpy in J basis
        N_products = (((4 / e_r) - 3) + 2 + (4 - 4 / e_r) + (7.52 / e_r)) * R * T
    else:
        H_products = h_CO2_p + ((2 / e_r) - 2) * h_O2_p + 2 * h_H2O_p + (7.52 / e_r) * h_N2_p  # Enthalpy in J basis
        N_products = (((2 / e_r) - 2) + 3 + (7.52 / e_r)) * R * T

    # For calculation of enthalpy of Reactants in Jouls
    Tstd = 298.15  # in K at STP condition
    h_CH4_r = h(Tstd, CH4_coeffs_l)  # J/Mol-K
    h_O2_r = h(Tstd, O2_coeffs_l)  # J/Mol-K
    h_N2_r = h(Tstd, N2_coeffs_l)  # J/Mol-K

    H_reactants = h_CH4_r + (2 / e_r) * h_O2_r + ((2 / e_r) * 3.76) * h_N2_r  # Enthalpy in J basis
    N_reactants = (1 + (2 / e_r) + ((2 / e_r) * 3.76)) * R * Tstd

    return (H_reactants - H_products) - (N_reactants - N_products)

def fprime(T, e_r):
    # To define numerical derivative of function (forward-differencing)
    return (f(T + 1e-6, e_r) - f(T, e_r)) / 1e-6

# Using Newton-Raphson to solve iteratively
tol = 1e-3
alpha = 0.9
Temp = [] # Defined arrays to store the values of temperature

for j in e_r:  # Loop to perform a root-finding procedure for all values of equivalence ratio between 0.1 to 2
    T_guess = 1500
    while (abs(f(T_guess, j)) > tol):
        T_guess = T_guess - alpha * (
        (f(T_guess, j) / fprime(T_guess, j)))  # N-R iteration formula for getting better estimate of true root
    Temp.append(T_guess)

plt.plot(e_r, Temp, color='red')
plt.xlabel('Equivalence ratio (e_r)')
plt.ylabel('Adiabatic Flame temperature (K)')
plt.title('Equivalence Ratio VS Adiabatic Flame temperature for CH4')

plt.grid('on')
plt.show()