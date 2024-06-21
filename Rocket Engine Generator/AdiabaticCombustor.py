import numpy as np
from Final_EquationBalancer import *

def findex(array, search): return array.index(search)

def split(txt, sep): return txt.split(sep)

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

def exponentF(fuel, oxid):
    Reactants, fuel_ListSample = [], []
    match oxid:
        case "O2 (Oxygen)":
            fuel_ListSample = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                               "C6H5NH2 (Aniline)", "NH3 (Ammonia)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                               "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
            Reactants = [solver("H2 + O2 = H2O"),
                         solver("CH4 + O2 = CO2 + H2O"),
                         solver("C2H6O + O2 = CO2 + H2O"),
                         solver("C2H6O + O2 = CO2 + H2O"),
                         solver("C6H7N + O2 = CO2 + H2O + NO2"),
                         solver("NH3 + O2 = H2O + NO2"),
                         solver("CH6N2 + O2 = H2O + NO2 + CO2"),
                         solver("N2H4 + O2 = H2O + NO2"),
                         solver("CH4O + O2 = H2O + CO2"),
                         solver("C12H26 + O2 = H2O + CO2")]
        case "F2 (Fluorine)":
            fuel_ListSample = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                               "C6H5NH2 (Aniline)", "NH3 (Ammonia)", "C2H8N2 (UnsymmetricalDimethylHydrazine)",
                               "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)",
                               "C12H26 (n-Dodecane)"]
            Reactants = [solver("H2 + F2 = HF"),
                         solver("CH4 + F2 = CF4 + HF"),
                         solver("C2H5OH + F2 = CF4 + HF + CO2"),
                         solver("C2H5OH + F2 = CF4 + HF + CO2"),
                         solver("C6H5NH2 + F2 = C6F5NH2 + HF"),
                         solver("NH3 + F2 = NF3 + HF"),
                         solver("C2H8N2 + F2 = N2F4 + HF + CF4"),
                         solver("CH6N2 + F2 = C2F6 + HF + N2"),
                         solver("N2H4 + F2 = N2F4 + HF"),
                         solver("CH3OH + F2 = CF4 + HF + H2O"),
                         solver("C12H26 + F2 = CF4 + HF")]
        case "F2O2 (Perfluorine Peroxide)":
            fuel_ListSample = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                               "C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                               "CH6N2 (MonomethylHydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)",
                               "N2H4 (Hydrazine)"]
            Reactants = [solver("H2 + F2O2 = H2O + F2"),
                         solver("CH4 + F2O2 = CO2 + 2HF + H2O"),
                         solver("C2H5OH + F2O2 = CO2 + H2O + HF"),
                         solver("C2H5OH + F2O2 = CO2 + H2O + HF"),
                         solver("C6H5NH2 + F2O2 = C6H4N2O + HF + H2O"),
                         solver("(CH6N2-75/N2O4-25) + F2O2 = "),
                         solver("(CH6N2-50/N2O4-50) + F2O2 = "),
                         solver("CH6N2 + F2O2 = CO2 + 4HF + 2H2O + N2"),
                         solver("CH3OH + F2O2 = CO2 + HF + H2O"),
                         solver("C12H26 + F2O2 = CO2 + HF + H2O"),
                         solver("N2H4 + F2O2 = N2 + HF + H2O")]
        case "O3 (Ozone)":
            fuel_ListSample = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                               "C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                               "CH6N2 (MonomethylHydrazine)", "C12H26 (n-Dodecane)", "CH3OH (Methanol)",
                               "N2H4 (Hydrazine)", "NH3 (Ammonia)"]
            Reactants = [solver("H2 + O3 = H2O"),
                         solver("CH4 + O3 = CO2 + H2O"),
                         solver("(C2H5OH-95/H2O-05) + O3 = CO2 + H2O"),
                         solver("(C2H5OH-75/H2O-25) + O3 = CO2 + H2O"),
                         solver("C6H5NH2 + O3 = CO2 + H2O + NO2"),
                         solver("(CH6N2-75/N2O4-25) + O3 = H2O + CO2 + NO2"),
                         solver("(CH6N2-50/N2O4-50) + O3 = H2O + CO2 + NO2"),
                         solver("CH6N2 + O3 = H2O + CO2 + NO2"),
                         solver("C12H26 + O3 = H2O + CO2"),
                         solver("CH3OH + O3 = H2O + CO2"),
                         solver("N2H4 + O3 = H2O + NO2"),
                         solver("NH3 + O3 = H2O + NO2")]
        case "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)" | "AK20I: 80% HNO3 + 20% N2O4 (Nitric Acid)" |\
             "AK20K: 80% HNO3 + 20% N2O4 (Nitric Acid)":
            fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                               "CH3OH(Methanol) 95%"]
            Reactants = ["H2 + HNO3-80[N2O4-20] = ",
                         "C2H5OH-95[H2O-05] + HNO3-80[N2O4-20] = ",
                         "CH6N2 + HNO3-80[N2O4-20] = ",
                         "N2H4 + HNO3-80[N2O4-20] = ",
                         "CH3OH + HNO3-80[N2O4-20] = "]
        case "AK27I: 73% HNO3 + 27% N2O4 (Nitric Acid)" | "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)":
            fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                               "CH3OH (Methanol)"]
            Reactants = ["HNO3-73[N2O4-27] + H2" "",
                         "HNO3-73[N2O4-27] + C2H5OH-95[H2O-05]" "",
                         "HNO3-73[N2O4-27] + CH6N2" "",
                         "HNO3-73[N2O4-27] + N2H4" "",
                         "HNO3-73[N2O4-27] + CH3OH" ""]
        case "N2O4 (Nitrogen Tetroxide)":
            fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                               "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                               "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)",
                               "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
            Reactants = ["N2O4 + H2" "",
                         "N2O4 + C2H5OH-95[H2O-05]" "",
                         "N2O4 + C2H5OH-75[H2O-25]" "",
                         "N2O4 + C6H5NH2" "",
                         "N2O4 + CH6N2-75[N2H4-25]" "",
                         "N2O4 + CH6N2-50[N2H4-50]" "",
                         "N2O4 + C2H8N2" "",
                         "N2O4 + CH6N2" "",
                         "N2O4 + N2H4" "",
                         "N2O4 + CH3OH" "",
                         "N2O4 + C12H26" ""]
        case "N2O (Nitrous Oxide)":
            fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                               "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                               "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)",
                               "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
            Reactants = ["N2O + H2" "",
                         "N2O + C2H5OH-95[H2O-05]" "",
                         "N2O + C2H5OH-75[H2O-25]" "",
                         "N2O + C6H5NH2" " ",
                         "N2O + CH6N2-75[N2H4-25]" "",
                         "N2O + CH6N2-50[N2H4-50]" "",
                         "N2O + C2H8N2" "",
                         "N2O + CH6N2 " "",
                         "N2O + N2H4" "",
                         "N2O + CH3OH" "",
                         "N2O + C12H26" ""]
        case "H2O2 (Hydrogen Peroxide) 85%":
            fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                               "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                               "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)",
                               "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
            Reactants = ["H2O2-85[H2O-15] + H2" "",
                         "H2O2-85[H2O-15] + C2H5OH-95[H2O-05]" "",
                         "H2O2-85[H2O-15] + C2H5OH-75[H2O-25]" "",
                         "H2O2-85[H2O-15] + CH6N2-75[N2O4-25]" "",
                         "H2O2-85[H2O-15] + CH6N2-50[N2O4-50]" "",
                         "H2O2-85[H2O-15] + C2H8N6" "",
                         "H2O2-85[H2O-15] + CH6N2" "",
                         "H2O2-85[H2O-15] + N2H4" "",
                         "H2O2-85[H2O-15] + CH3OH" "",
                         "H2O2-85[H2O-15] + C12H26" ""]
        case "H2O2 (Hydrogen Peroxide) 95%":
            fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                               "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                               "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)",
                               "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
            Reactants = ["H2O2-95[H2O-05] + H2" "",
                         "H2O2-95[H2O-05] + C2H5OH-95[H2O-O5]" "",
                         "H2O2-95[H2O-05] + C2H5OH-75[H2O-25]" "",
                         "H2O2-95[H2O-05] + CH6N2-75[N2O4-25]" "",
                         "H2O2-95[H2O-05] + CH6N2-50[N2O4-50]" "",
                         "H2O2-95[H2O-05] + C2H8N6" "",
                         "H2O2-95[H2O-05] + CH6N2" "",
                         "H2O2-95[H2O-05] + N2H4" "",
                         "H2O2-95[H2O-05] + CH3OH" "",
                         "H2O2-95[H2O-05] + C12H26" ""]
    reaction = equationizer(Reactants[fuel_ListSample.index(fuel)])
    return reaction
def calculate(reaction):
    Oxid_List = ["O2", "F2", "F2O2", "N2O4", "H2O2-95[H2O-05]", "H2O2-85[H2O-15]", "O3", "HNO3-80[N2O4-20]",
                 "HNO3-73[N2O4-27]", "N2O"]
    OxiDifEnth = [0, 0, 0, -19.56, -205.3, -195.6, -132.2, -142.95, -132.16]

    Fuel_List = ["H2", "CH4", "C2H5OH-95[H2O-05]", "C2H5OH-75[H2O-25]", "C6H5NH2", "NH3", "C2H8N2", "CH6N2", "N2H4",
                 "CH3OH", "C12H26", "CH6N2-50[N2H4-50]", "CH6N2-75[N2H4-25]"]
    Fuel_Enth = [0, -74.65, -277.51, -277.07, 83.2, -46.05, 84.9, 94.5, 95.35, -210.5, -290.675, 94.925, 94.7125]
    reacA1 = reaction[0][0][0]
    reacB1 = reaction[0][1][0]
    reacAE = reaction[0][0][1]
    reacBE = reaction[0][1][1]
    Hr = (reacAE*OxiDifEnth[findex(reacA1, Oxid_List)]) + (reacBE*Fuel_Enth[findex(reacB1, Fuel_List)])
    OF = (reacAE*reacA1)/(reacBE*reacB1)

    productsData, Hp, combust_temp = reaction[1], 0, 0
    Exhaust_List = ["NO2", "CO2", "H2O", "HF", "NF2", "CHF3"]
    gamma = [-1, 1.289, -1, -1, -1, -1]
    density_ref = [-1, -1, -1, -1, -1, -1]
    Cp = []
    Cv = []

    prodExponents = []
    prodExhaust = []
    for x in productsData
    while Hp != Hr:
        for i in
    #Characteristic Exhaust Velocity
    Exhaust_Vel =
    combust_temp =
    return combust_temp, ExhaustVel, OF
########################################################################################################################
Oxidizer = "O2 (Oxygen)"
Fuel = "CH4 (Methane)"
Combust_Temp = calculate(exponentF(Oxidizer, Fuel))[0]
C_ExhaustVel = calculate(exponentF(Oxidizer, Fuel))[1]
OF_Ratio = calculate(exponentF(Oxidizer, Fuel))[2]
########################################################################################################################
