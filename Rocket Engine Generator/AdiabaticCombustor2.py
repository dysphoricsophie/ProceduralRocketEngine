import csv

import numpy as np
from molmass import Formula
from ChumChildren import solver
########################################################################################################################
def findex(array, search):
    return array.index(search)
def split(txt, sep):
    return txt.split(sep)
def closest_value(input_list, input_value):
    arr = np.asarray(input_list)
    i = (np.abs(arr - input_value)).argmin()
    return arr[i]
def equationizer(equation):
    splitted = split(equation, "=")

    lhs = splitted[0]
    reactants = split(lhs, "+")
    reactantA = reactants[0]
    rA_Exponent = split(reactantA,"|")[0]
    reactantA = split(reactantA,"|")[1]
    reactantB = reactants[1]
    rB_Exponent = split(reactantB,"|")[0]
    reactantB = split(reactantB,"|")[1]

    rhs = splitted[1]
    products = split(rhs, "+")
    prodExponents, prodList = [], []
    for i in products:
        stuff = split(i,"|")
        prodExponents.append(stuff[0])
        prodList.append(stuff[1])
    return [[reactantA, rA_Exponent], [reactantB, rB_Exponent]], [prodList, prodExponents]
def exponentF(oxid, fuel):
    Reactants, fuel_ListSample = [], []
    match oxid:
        case "O2 (Oxygen)":
            fuel_ListSample = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                               "C6H5NH2 (Aniline)", "NH3 (Ammonia)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                               "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
            Reactants = [solver("H2 + O2 = H2O"),
                         solver("CH4 + O2 = CO2 + H2O"),
                         solver("C2H5OH + O2 = CO2 + H2O"),
                         solver("C2H5OH + O2 = CO2 + H2O"),
                         solver("C6H7N + O2 = CO2 + H2O + NO2"),
                         solver("NH3 + O2 = H2O + NO2"),
                         solver("CH6N2 + O2 = H2O + NO2 + CO2"),
                         solver("N2H4 + O2 = H2O + NO2"),
                         solver("CH4O + O2 = H2O + CO2"),
                         solver("C12H26 + O2 = H2O + CO2")]
    reaction = equationizer(Reactants[fuel_ListSample.index(fuel)])
    return reaction
def calculate(reaction):
    Oxid_List = ["O2", "F2", "F2O2", "N2O4", "H2O2-95[H2O-05]", "H2O2-85[H2O-15]", "O3", "HNO3-80[N2O4-20]",
                 "HNO3-73[N2O4-27]", "N2O"]
    Oxi_Enth = [0, 0, 0, -19.56, -205.3, -195.6, -132.2, -142.95, -132.16]

    Fuel_List = ["H2", "CH4", "C2H5OH-95[H2O-05]", "C2H5OH-75[H2O-25]", "C6H5NH2", "NH3", "C2H8N2", "CH6N2", "N2H4",
                 "CH3OH", "C12H26", "CH6N2-50[N2H4-50]", "CH6N2-75[N2H4-25]"]
    Fuel_Enth = [0, -74.65, -277.51, -277.07, 83.2, -46.05, 84.9, 94.5, 95.35, -210.5, -290.675, 94.925, 94.7125]
    reacA1 = reaction[0][0][0].strip()
    reacB1 = reaction[0][1][0].strip()
    reacAE = reaction[0][0][1].strip()
    reacBE = reaction[0][1][1].strip()

    Hr = (float(reacBE) * Oxi_Enth[findex(Oxid_List, reacB1)]) + (float(reacAE) * Fuel_Enth[findex(Fuel_List, reacA1)])
    OF = (float(reacBE)*Formula(reacB1).mass)/(float(reacAE)*Formula(reacA1).mass)

    productsData, Hp, combust_temp = reaction[1], 0, 0
    Exhaust_List = ["NO2", "CO2", "H2O", "HF", "NF2", "CF4"]
    Exhaust_List = ["Nitrogen Dioxide", "Carbon Dioxide", "Water Vapour", "Hydrogen Fluoride", "Nitrogen Fluoride", "Tetrafluorocarbon"]
    Prod_Enth = [-1, 1.289, -1, -1, -1, -1]

    Totality = []
    Temperatures = []
    Methane = []
    Carbon_Dioxide = []
    Carbon_Monoxide = []
    Diatomic_Oxygen = []
    Gaseous_Water = []
    Diatomic_Hydrogen = []
    Hydroxyl_Ion = []
    with open('ProductEnthalpies.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            # Access data by column index (starting from 0)
            Temperatures.append(row[0])
            Methane.append(row[1])
            Carbon_Dioxide.append(row[2])
            Carbon_Monoxide.append(row[3])
            Diatomic_Oxygen.append(row[4])
            Gaseous_Water.append(row[5])
            Diatomic_Hydrogen.append(row[6])
            Hydroxyl_Ion.append(row[7])

    temp = 12
    print(f"Temperature: {Temperatures[temp]}K \n"
          f"Water Vapour at {Temperatures[temp]}K: {Gaseous_Water[temp]} kJ/mol \n"
          f"Carbon Dioxide at {Temperatures[temp]}K: {Carbon_Dioxide[temp]} kJ/mol \n")

    for x in productsData:
        pass
    while Hp != Hr:
        pass
    #Characteristic Exhaust Velocity
    ExhaustVel = 0
    combust_temp = 0
    return combust_temp, ExhaustVel, OF
########################################################################################################################
Oxidizer = "O2 (Oxygen)"
Fuel = "C12H26 (n-Dodecane)"
Combust_Temp = calculate(exponentF(Oxidizer, Fuel))[0]
C_ExhaustVel = calculate(exponentF(Oxidizer, Fuel))[1]
OF_Ratio = calculate(exponentF(Oxidizer, Fuel))[2]
########################################################################################################################
