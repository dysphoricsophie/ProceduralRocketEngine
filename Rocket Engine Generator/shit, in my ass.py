from EqtnBalancer import solver

solver("H2 + F2 = HF")
solver("CH4 + F2 = CF2 + HF")
solver("C2H5OH + F2 = CO2 + HF + H2O")
print(solver("C2H5OH + F2 = CO2 + HF + H2O"))
solver("C6H5NH2 + F2 = CF2 + N2 + HF")
solver("CH3OH + F2 = CF2 + CO2 + HF")
solver("C12H26 + F2 = CF2 + HF")

solver("H2 + F2O2 = HF + H2O")
solver("C12H26 + F2O2 = CO2 + HF + H2O")

solver("C2H5OH + N2O4 = CO2 + N2 + H2O")
solver("C2H5OH + N2O4 = CO2 + N2 + H2O")
solver("C6H5NH2 + N2O4 = CO2 + H2O + N2")
solver("CH3OH + N2O4 = N2 + CO2 + H2O")
solver("C2H8N2 + N2O4 = CO2 + N2 + H2O")