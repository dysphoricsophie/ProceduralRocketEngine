import csv
import numpy as np
import pandas as pd
from molmass import Formula
from EqtnBalancer import solver

def findex(array, search):
    return array.index(search)
def interpolation(Hp_List, Hr):
    # Assuming Hp_List has at least 2 elements
    x0, y0 = Hp_List[0]  # unpack first data point
    x1, y1 = Hp_List[1]  # unpack second data point
    m = (y1 - y0) / (x1 - x0)  # calculate slope
    return y0 + m * (Hr - x0)  # linear interpolation formula
def linear_interpolate(start_value, end_value, target_value):
    if start_value == end_value:
        return target_value, 0.0

    range_value = end_value - start_value
    interpolation_factor = (target_value - start_value) / range_value

    interpolation_factor = max(0.0, min(interpolation_factor, 1.0))
    interpolated_value = start_value + (interpolation_factor * range_value)

    return interpolated_value, interpolation_factor
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
def read_data(file_path, nm):
    return pd.DataFrame(pd.read_csv(file_path, index_col=nm))
def calculate_enthalpy_change(reactants, products, data):
    # Function to calculate enthalpy change for a reaction
    delta_h = []
    enth = ["Hf - 100K", "Hf - 200K", "Hf - 298.15K", "Hf - 300K", "Hf - 400K", "Hf - 500K", "Hf - 600K", "Hf - 700K",
            "Hf - 800K", "Hf - 900K", "Hf - 1000K", "Hf - 1100K", "Hf - 1200K", "Hf - 1300K", "Hf - 1400K", "Hf - 1500K",
            "Hf - 1600K", "Hf - 1700K", "Hf - 1800K", "Hf - 1900K", "Hf - 2000K", "Hf - 2100K", "Hf - 2200K", "Hf - 2300K",
            "Hf - 2400K", "Hf - 2500K", "Hf - 2600K", "Hf - 2700K", "Hf - 2800K", "Hf - 2900K", "Hf - 3000K", "Hf - 3100K",
            "Hf - 3200K", "Hf - 3300K", "Hf - 3400K", "Hf - 3500K", "Hf - 3600K", "Hf - 3700K", "Hf - 3800K", "Hf - 3900K",
            "Hf - 4000K", "Hf - 4100K", "Hf - 4200K", "Hf - 4300K", "Hf - 4400K", "Hf - 4500K", "Hf - 4600K", "Hf - 4700K",
            "Hf - 4800K", "Hf - 4900K", "Hf - 5000K", "Hf - 5100K", "Hf - 5200K", "Hf - 5300K", "Hf - 5400K", "Hf - 5500K",
            "Hf - 5600K", "Hf - 5700K", "Hf - 5800K", "Hf - 5900K", "Hf - 6000K"]
    for j in enth:
        product_sum = 0; reactant_sum = 0
        for molecule, count in products.items():
            value = data.loc[molecule, j]
            product = (1000*value) * count
            product_sum += product
        Hp = product_sum

        for molecule, count in reactants.items():
            value = data.loc[molecule, j]
            reactant = (1000*value) * count
            reactant_sum += reactant
        Hr = reactant_sum

        Ht = Hp - Hr
        delta_h.append(float(Ht))
    return delta_h
def calculate_temperature_change(delta_h, data, products):
    # Function to calculate enthalpy change for a reaction
    delta_t = []
    temps = ["Cp - 100K", "Cp - 200K", "Cp - 298.15K", "Cp - 300K", "Cp - 400K", "Cp - 500K", "Cp - 600K", "Cp - 700K",
             "Cp - 800K", "Cp - 900K", "Cp - 1000K", "Cp - 1100K", "Cp - 1200K", "Cp - 1300K", "Cp - 1400K", "Cp - 1500K",
             "Cp - 1600K", "Cp - 1700K", "Cp - 1800K", "Cp - 1900K", "Cp - 2000K", "Cp - 2100K", "Cp - 2200K", "Cp - 2300K",
             "Cp - 2400K", "Cp - 2500K", "Cp - 2600K", "Cp - 2700K", "Cp - 2800K", "Cp - 2900K", "Cp - 3000K", "Cp - 3100K",
             "Cp - 3200K", "Cp - 3300K", "Cp - 3400K", "Cp - 3500K", "Cp - 3600K", "Cp - 3700K", "Cp - 3800K", "Cp - 3900K",
             "Cp - 4000K", "Cp - 4100K", "Cp - 4200K", "Cp - 4300K", "Cp - 4400K", "Cp - 4500K", "Cp - 4600K", "Cp - 4700K",
             "Cp - 4800K", "Cp - 4900K", "Cp - 5000K", "Cp - 5100K", "Cp - 5200K", "Cp - 5300K", "Cp - 5400K", "Cp - 5500K",
             "Cp - 5600K", "Cp - 5700K", "Cp - 5800K", "Cp - 5900K", "Cp - 6000K"]
    for z in delta_h:
        for j in temps:
            product_sum = 0
            for molecule, count in products.items():
                value = data.loc[molecule, j]
                product = (1000 * value) * count
                product_sum += product
            Hp = product_sum

            Tc = (abs(z) / float(Hp)) + 298.15
            delta_t.append(float(Tc))
    return delta_t
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
            fuel_ListSample = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                               "NH3 (Ammonia)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
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
        case "F2O2 (Perfluorine Peroxide)":
            fuel_ListSample = ["H2 (Hydrogen)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
            Reactants = [solver("H2 + F2O2 = HF + H2O"),
                         solver("CH3OH + F2O2 = CF4 + CO2 + HF"),
                         solver("C12H26 + F2O2 = CF4 + HF + H2O")]
        case "O3 (Ozone)":
            fuel_ListSample = ["H2 (Hydrogen)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
            Reactants = [solver("H2 + O3 = H2O"),
                         solver("CH3OH + O3 = CO2 + H2O"),
                         solver("C12H26 + O3 = CO2 + H2O")]
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
        case "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)" | "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)":
            fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                               "CH3OH (Methanol)"]
            Reactants = [solver("H2 + HNO3 = NO2 + H2O"),
                         solver("C2H5OH + HNO3 = NO2 + CO2 + H2O"),
                         solver("CH6N2 + HNO3 = CO2 + NO2 + H2O"),
                         solver("N2H4 + HNO3 = NO2 + H2O"),
                         solver("CH3OH + HNO3 = NO2 + CO2 + H2O")]
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
    print(reaction)
    reacA1 = reaction[0][0][0].strip()
    reacB1 = reaction[0][1][0].strip()
    reacAE = reaction[0][0][1].strip()
    reacBE = reaction[0][1][1].strip()

    print(reacA1)
    print(reacB1)
    print(reacAE)
    print(reacBE)

    # Define the reactants and products for the reaction
    reactants = {reacA1: int(reacAE),reacB1: int(reacBE)}
    products = {}
    if reaction[1][0] == 1:
        products[reaction[1][0]] = int(reaction[1][1])
    else:
        for i in reaction[1][0]:
            products[i] = int(reaction[1][1][reaction[1][0].index(i)])
    print(f"{reactants}\n{products}")

    data_file = 'enthalpies.csv'
    data = read_data(data_file, 'Compound')

    delta_h = list(calculate_enthalpy_change(reactants, products, data)) # Calculate the enthalpy change
    delta_t = calculate_temperature_change(delta_h, data, products) # Calculate the temperature change

    miner = close(delta_h, 0)[0]
    maxer = close(delta_h, 0)[1]
    miner_tp = delta_t[delta_h.index(miner)]
    maxer_tp = delta_t[delta_h.index(maxer)]
    interpol_T = [miner, miner_tp], [maxer, maxer_tp]

    OF = (float(reacBE) * Formula(reacB1).mass) / (float(reacAE) * Formula(reacA1).mass)

    #Characteristic Exhaust Velocity
    ExhaustVel = 0
    combust_temp = interpolation(interpol_T, 0)
    return combust_temp, ExhaustVel, OF

fuels = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)", "NH3 (Ammonia)",
         "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
oxids = ["O2 (Oxygen)", "F2 (Fluorine)", "F2O2 (Perfluorine Peroxide)", "N2O4 (Nitrogen Tetroxide)", "H2O2 (Hydrogen Peroxide) 95%",
           "H2O2 (Hydrogen Peroxide) 85%", "O3 (Ozone)", "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)","AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)"]
for i in oxids:
    for k in fuels:
        Oxidizer = i; Fuel = k
        Test = False
        if Test:
            try:
                results = calculate(exponentF(Oxidizer, Fuel))
                Combust_Temp = results[0]
                C_ExhaustVel = results[1]
                OF_Ratio = results[2]
            except:
                pass
            else:
                maxLen = 90
                strz = f"{Fuel} + {Oxidizer} -> Combustion Temperature: {round(Combust_Temp, 3)}"
                Xtra = maxLen - len(strz)
                strz = strz.split("-> ")
                for y in range(0, (Xtra - 1)): strz[0] += "-"
                print(strz[0] + "> "+ strz[1])
        else:
            results = calculate(exponentF(Oxidizer, Fuel))
            Combust_Temp = results[0]
            C_ExhaustVel = results[1]
            OF_Ratio = results[2]

            maxLen = 90
            strz = f"{Fuel} + {Oxidizer} -> Combustion Temperature: {round(Combust_Temp, 3)}\n"
            Xtra = maxLen - len(strz)

            strz = strz.split("-> ")
            for y in range(0, (Xtra - 1)): strz[0] += "-"

            print(strz[0] + "> " + strz[1])