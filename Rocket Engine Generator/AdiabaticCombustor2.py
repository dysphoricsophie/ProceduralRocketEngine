import csv
import numpy as np
from molmass import Formula
from AssholeKeggels import solver
########################################################################################################################
def findex(array, search):
    return array.index(search)
def interpolation(Hp_List, Hr):
    # Hp_List = [[Product Enthalpy, Temperature], [Product Enthalpy, Temperature] ...
    return Hp_List[0][1] + (Hr - Hp_List[0][0]) * ((Hp_List[1][1] - Hp_List[0][1]) / (Hp_List[1][0] - Hp_List[0][0]))
def check(string, sub_str):
    if string.find(sub_str) == -1:
        return False
    else:
        return True
def close(listh, num):
    a = min([i for i in listh if num < i])
    b = max([i for i in listh if num > i])
    return a, b
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
    Exhaust_List_L = ["Nitrogen Dioxide", "Carbon Dioxide", "Water Vapour", "Hydrogen Fluoride", "Nitrogen Fluoride", "Tetrafluorocarbon"]
    Prod_Enth = [-1, 1.289, -1, -1, -1, -1]

    Temperatures = []; Gas1 = []; Gas2 = []; Gas3 = []
    Gas4 = []; Gas5 = []; Gas6 = []; Gas7 = []
    Totality = [Temperatures, Gas1, Gas2, Gas3, Gas4, Gas5, Gas6, Gas7]
    with open('ProductEnthalpies.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            # Access data by column index (starting from 0)
            Temperatures.append(row[0])
            Gas1.append(row[1])
            Gas2.append(row[2])
            Gas3.append(row[3])
            Gas4.append(row[4])
            Gas5.append(row[5])
            Gas6.append(row[6])
            Gas7.append(row[7])

    indexA = -1; ProA = str(productsData[0][0])
    indexB = -1; ProB = str(productsData[0][1])
    heado = []; head = []
    for j in range(0, len(Totality)):
        heado.append(Totality[j][0])
    for x in heado:
        head.append(x.split("(")[1].strip(")"))

    for i in range(0, len(head)):
        if head[i] == ProA.strip(" "):
            indexA = i
        if head[i] == ProB.strip(" "):
            indexB = i
    print(f"Index 1 is {str(indexA)} --- Index 2 is {str(indexB)}")

    temp = 12
    print(f"Temperature: {Temperatures[temp]}K \n"
          f"{heado[indexA]} at {Temperatures[temp]}K: {Totality[indexA][temp]} kJ/mol \n"
          f"{heado[indexB]} at {Temperatures[temp]}K: {Totality[indexB][temp]} kJ/mol \n")

    Exh_A = Totality[indexA]
    Exh_B = Totality[indexB]
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
print(f"{Combust_Temp} \n{C_ExhaustVel} \n{OF_Ratio}")
########################################################################################################################
