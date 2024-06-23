import csv
import numpy as np
from molmass import Formula
from EqtnBalancer import solver

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
def close(array, tarjet):
    def findClosest(arr, n, targete):
        def getClosest(val1, val2, targeta):
            if targeta - val1 >= val2 - targeta:
                return val2
            else:
                return val1
        if targete <= arr[0]:
            return arr[0]
        if targete >= arr[n - 1]:
            return arr[n - 1]

        i = 0; j = n; mid = 0
        while i < j:
            mid = (i + j) // 2
            if arr[mid] == targete:
                return arr[mid]
            if targete < arr[mid]:
                if mid > 0 and targete > arr[mid - 1]:
                    return getClosest(arr[mid - 1], arr[mid], targete)
                j = mid
            else:
                if mid < n - 1 and targete < arr[mid + 1]:
                    return getClosest(arr[mid], arr[mid + 1], targete)
                i = mid + 1

        return arr[mid]

    def run(arr, target):
        global mine, maxe
        n = len(arr)
        pust = (findClosest(arr, n, target))
        pust_id = arr.index(pust)
        if arr[pust_id] > target:
            maxe = arr[pust_id]
            mine = arr[pust_id - 1]
        elif arr[pust_id] < target:
            mine = arr[pust_id]
            maxe = arr[pust_id + 1]
        return [mine, maxe]

    return run(array, tarjet)
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
                         solver("CH3OH + O2 = H2O + CO2"),
                         solver("C12H26 + O2 = H2O + CO2")]
            delta_E = []
        case "F2 (Fluorine)":
            fuel_ListSample = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                             "NH3 (Ammonia)", "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)",
                             "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
            Reactants = [solver("H2 + F2 = HF"),
                         solver("CH4 + F2 = CF4 + HF"),
                         solver("C2H5OH + F2 = CF4 + CO2 + HF"),
                         solver("C2H5OH + F2 = CF4 + CO2 + HF"),
                         solver("C6H5NH2 + F2 = HF + NF3 + CF4"),
                         solver("NH3 + F2 = NF3 + HF"),
                         solver("C2H8N2 + F2 = HF + NF3 + CF4"),
                         solver("CH6N2 + F2 = HF + NF3 + CF4"),
                         solver("N2H4 + F2 = NF3 + HF"),
                         solver("CH3OH + F2 = CF4 + CO2 + HF"),
                         solver("C12H26 + F2 = CF4 + HF")]
            delta_E = []
        case "F2O2 (Perfluorine Peroxide)":
            fuel_ListSample = ["H2 (Hydrogen)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
            Reactants = [solver("H2 + F2O2 = HF + H2O"),
                         solver("CH3OH + F2O2 = CF4 + CO2 + HF"),
                         solver("C12H26 + F2O2 = CF4 + HF + H2O")]
            delta_E = []
        case "O3 (Ozone)":
            fuel_ListSample = ["H2 (Hydrogen)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
            Reactants = [solver("H2 + O3 = H2O"),
                         solver("CH3OH + O3 = CO2 + H2O"),
                         solver("C12H26 + O3 = CO2 + H2O")]
            delta_E = []
        case "N2O4 (Nitrogen Tetroxide)":
            fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                             "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)", "CH3OH (Methanol)",
                             "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                               "C12H26 (n-Dodecane)"]
            Reactants = [solver("H2 + N2O4 = N2 + H2O"),
                         solver("C2H5OH + N2O4 = NO2 + CO2 + H2O"),
                         solver("C2H5OH + N2O4 = NO2 + CO2 + H2O"),
                         solver("C6H5NH2 + N2O4 = NO2 + CO2 + H2O"),
                         solver("CH6N2 + N2O4 = CO2 + N2 + H2O"),
                         solver("CH6N2 + N2O4 = CO2 + N2 + H2O"),
                         solver("CH3OH + N2O4 = NO2 + CO2 + H2O"),
                         solver("NH3 + N2O4 = NO2 + H2O"),
                         solver("C2H8N2 + N2O4 = CO2 + N2 + H2O"),
                         solver("CH6N2 + N2O4 = CO2 + N2 + H2O"),
                         solver("N2H4 + N2O4 = N2 + H2O"),
                         solver("C12H26 + N2O4 = CO2 + N2 + H2O")]
            delta_E = []
        case "H2O2 (Hydrogen Peroxide) 95%" | "H2O2 (Hydrogen Peroxide) 85%":
            fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                             "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)", "CH3OH (Methanol)",
                             "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                               "C12H26 (n-Dodecane)"]
            Reactants = [solver("H2 + H2O2 = H2O"),
                         solver("C2H5OH + H2O2 = CO2 + H2O"),
                         solver("C2H5OH + H2O2 = CO2 + H2O"),
                         solver("C6H5NH2 + H2O2 = CO2 + H2O + NO2"),
                         solver("CH6N2 + H2O2 = H2O + NO2 + CO2"),
                         solver("CH6N2 + H2O2 = H2O + NO2 + CO2"),
                         solver("CH3OH + H2O2 = CO2 + H2O"),
                         solver("C2H8N2 + H2O2 = CO2 + H2O + NO2"),
                         solver("CH6N2 + H2O2 = H2O + NO2 + CO2"),
                         solver("N2H4 + H2O2 = H2O + NO2"),
                         solver("C12H26 + H2O2 = H2O + CO2")]
            delta_E = []
        case "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)" | "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)":
            fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                               "CH3OH (Methanol)"]
            Reactants = [solver("H2 + HNO3 = NO2 + H2O"),
                         solver("C2H5OH + HNO3 = NO2 + CO2 + H2O"),
                         solver("CH6N2 + HNO3 = CO2 + NO2 + H2O"),
                         solver("N2H4 + HNO3 = NO2 + H2O"),
                         solver("CH3OH + HNO3 = NO2 + CO2 + H2O")]
            delta_E = []
    reaction = equationizer(Reactants[fuel_ListSample.index(fuel)])
    return reaction #[reaction, delta_E[fuel_ListSample.index(fuel)]]
def prop_exh(productsData):
    global Hp_List, Hp_Temp
    Temperatures = []
    Gas1 = []
    Gas2 = []
    Gas3 = []
    Gas4 = []
    Gas5 = []
    Gas6 = []
    Gas7 = []
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

    if len(productsData[1]) == 1:
        indexA = -1
        ProA = str(productsData[0][0])
        heado = []
        head = []
        for j in range(0, len(Totality)):
            heado.append(Totality[j][0])
        for x in heado:
            head.append(x.split("(")[1].strip(")"))

        for i in range(0, len(head)):
            if head[i] == ProA.strip(" "):
                indexA = i

        Exh_A = Totality[indexA]
        Hp_List = []
        Hp_Temp = []
        for x in range(1, len(Totality[0])):
            try:
                ExpoA = float(productsData[1][0])
                EnthA = Totality[indexA][x + 2]
                Hp = ExpoA * (float(Exh_A[2]) + float(EnthA))
                Hp_List.append(float(Hp))
                Hp_Temp.append(float(Totality[0][x + 2]))
            except:
                pass
    elif len(productsData[1]) == 2:
        indexA = -1
        ProA = str(productsData[0][0])
        indexB = -1
        ProB = str(productsData[0][1])
        heado = []
        head = []
        for j in range(0, len(Totality)):
            heado.append(Totality[j][0])
        for x in heado:
            head.append(x.split("(")[1].strip(")"))

        for i in range(0, len(head)):
            if head[i] == ProA.strip(" "):
                indexA = i
            if head[i] == ProB.strip(" "):
                indexB = i

        Exh_A = Totality[indexA]
        Exh_B = Totality[indexB]
        Hp_List = []
        Hp_Temp = []
        for x in range(1, len(Totality[0])):
            try:
                ExpoA = float(productsData[1][0])
                ExpoB = float(productsData[1][1])
                EnthA = Totality[indexA][x + 2]
                EnthB = Totality[indexB][x + 2]
                Hp = ExpoA * (float(Exh_A[2]) + float(EnthA)) + ExpoB * (float(Exh_B[2]) + float(EnthB))
                Hp_List.append(float(Hp))
                Hp_Temp.append(float(Totality[0][x + 2]))
            except:
                pass
    elif len(productsData[1]) == 3:
        indexA = -1
        ProA = str(productsData[0][0])
        indexB = -1
        indexC = -1
        ProB = str(productsData[0][1])
        ProC = str(productsData[0][2])
        heado = []
        head = []
        for j in range(0, len(Totality)):
            heado.append(Totality[j][0])
        for x in heado:
            head.append(x.split("(")[1].strip(")"))

        for i in range(0, len(head)):
            if head[i] == ProA.strip(" "):
                indexA = i
            if head[i] == ProB.strip(" "):
                indexB = i
            if head[i] == ProC.strip(" "):
                indexC = i

        Exh_A = Totality[indexA]
        Exh_B = Totality[indexB]
        Exh_C = Totality[indexC]
        Hp_List = []
        Hp_Temp = []
        for x in range(1, len(Totality[0])):
            try:
                ExpoA = float(productsData[1][0])
                ExpoB = float(productsData[1][1])
                ExpoC = float(productsData[1][2])
                EnthA = Totality[indexA][x + 2]
                EnthB = Totality[indexB][x + 2]
                EnthC = Totality[indexC][x + 2]
                Hp = ExpoA * (float(Exh_A[2]) + float(EnthA)) + ExpoB * (float(Exh_B[2]) + float(EnthB)) + ExpoC * (
                            float(Exh_C[2]) + float(EnthC))
                Hp_List.append(float(Hp))
                Hp_Temp.append(float(Totality[0][x + 2]))
            except:
                pass
    return [Hp_List, Hp_Temp]
def calculate(reaction):
    global EnthA, EnthB
    Oxid_List = ["O2", "F2", "F2O2", "N2O4", "H2O2-95[H2O-05]", "H2O2-85[H2O-15]", "O3", "HNO3-80[N2O4-20]",
                 "HNO3-73[N2O4-27]"]
    Oxi_Enth = [0, 0, 0, 19.56, -205.3, -195.6, -132.2, -142.95, -132.16]

    Fuel_List = ["H2", "CH4", "C2H5OH-95[H2O-05]", "C2H5OH-75[H2O-25]", "C6H5NH2", "NH3", "C2H8N2", "CH6N2", "N2H4",
                 "CH3OH", "C12H26", "CH6N2-50[N2H4-50]", "CH6N2-75[N2H4-25]"]
    Fuel_Enth = [0, -74.65, -277.51, -277.07, 83.2, -46.05, 84.9, 94.5, 95.35, -210.5, -290.675, 94.925, 94.7125]
    reacA1 = reaction[0][0][0].strip()
    print(reacA1)
    reacB1 = reaction[0][1][0].strip()
    print(reacB1)
    reacAE = reaction[0][0][1].strip()
    print(reacAE)
    reacBE = reaction[0][1][1].strip()
    print(reacBE)

    Hr = (float(reacBE) * Oxi_Enth[findex(Oxid_List, reacB1)]) + (float(reacAE) * Fuel_Enth[findex(Fuel_List, reacA1)])
    OF = (float(reacBE)*Formula(reacB1).mass)/(float(reacAE)*Formula(reacA1).mass)
    productsData, Hp, combust_temp = reaction[1], 0, 0

    res = prop_exh(productsData)

    Hp_List = res[0]
    Hp_Temp = res[1]

    miner = close(Hp_List, Hr)[0]
    miner_tp = Hp_Temp[Hp_List.index(miner)]
    maxer = close(Hp_List, Hr)[1]
    maxer_tp = Hp_Temp[Hp_List.index(maxer)]

    interpol_T = [miner, miner_tp], [maxer, maxer_tp]

    #Characteristic Exhaust Velocity
    ExhaustVel = 0
    combust_temp = interpolation(interpol_T, Hr)
    return combust_temp, ExhaustVel, OF

fuels = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
           "NH3 (Ammonia)", "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
           "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
oxids = ["O2 (Oxygen)", "F2 (Fluorine)", "F2O2 (Perfluorine Peroxide)", "N2O4 (Nitrogen Tetroxide)", "H2O2 (Hydrogen Peroxide) 95%",
           "H2O2 (Hydrogen Peroxide) 85%", "O3 (Ozone)", "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)","AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)"]

for i in fuels:
    for k in oxids:
        Oxidizer = k; Fuel = i
        results = calculate(exponentF(Oxidizer, Fuel))
        Combust_Temp = results[0]; C_ExhaustVel = results[1]; OF_Ratio = results[2]
        print(f"Oxidizer: {k} | --------- | Fuel: {i} | --------- |{results}|")