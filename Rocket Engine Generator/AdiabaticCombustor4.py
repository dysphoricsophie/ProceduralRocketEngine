import csv
from EqtnBalancer import solver


def split(txt, sep):
    return txt.split(sep)


def equationizer(equation):
    splitted = split(equation, "=")

    lhs = splitted[0]
    reactants = split(lhs, "+")
    reactantA = reactants[0]
    rA_Exponent = split(reactantA, "|")[0]
    reactantA = split(reactantA, "|")[1]
    reactantB = reactants[1]
    rB_Exponent = split(reactantB, "|")[0]
    reactantB = split(reactantB, "|")[1]

    rhs = splitted[1]
    products = split(rhs, "+")
    prodExponents, prodList = [], []
    for i in products:
        stuff = split(i, "|")
        prodExponents.append(stuff[0])
        prodList.append(stuff[1])
    return [[reactantA, rA_Exponent], [reactantB, rB_Exponent]], [prodList, prodExponents]


def exponentF(oxid, fuel):
    Reactants, fuel_ListSample = [], []
    match oxid:
        case "O2 (Oxygen)":
            fuel_ListSample = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                               "C6H5NH2 (Aniline)",
                               "NH3 (Ammonia)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)",
                               "C12H26 (n-Dodecane)"]
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
            fuel_ListSample = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                               "C6H5NH2 (Aniline)",
                               "NH3 (Ammonia)", "C2H8N2 (UnsymmetricalDimethylHydrazine)",
                               "CH6N2 (MonomethylHydrazine)",
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
                               "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)",
                               "N2H4 (Hydrazine)",
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
                               "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)",
                               "N2H4 (Hydrazine)",
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
            fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "CH6N2 (MonomethylHydrazine)",
                               "N2H4 (Hydrazine)",
                               "CH3OH (Methanol)"]
            Reactants = [solver("H2 + HNO3 = NO2 + H2O"),
                         solver("C2H5OH + HNO3 = NO2 + CO2 + H2O"),
                         solver("CH6N2 + HNO3 = CO2 + NO2 + H2O"),
                         solver("N2H4 + HNO3 = NO2 + H2O"),
                         solver("CH3OH + HNO3 = NO2 + CO2 + H2O")]
    reaction = equationizer(Reactants[fuel_ListSample.index(fuel)])
    return reaction  # [reaction, delta_E[fuel_ListSample.index(fuel)]]


def extract_csv_to_2d_array(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Extract the headers
        columns = {header: [] for header in headers}  # Create a dictionary for each column

        for row in reader:
            for header, value in zip(headers, row):
                columns[header].append(value)  # Append the values to corresponding columns

    # Convert dictionary of columns to a 2D array
    array_2d = [columns[header] for header in headers]
    return array_2d


def calculateHr(prodA, prodB, prodC, coefs, A):
    hp = []
    if A == 1:
        for t in range(0, len(prodA)):
            Hp = (float(coefs[2]) * float(prodA[t]))
            hp.append(float(Hp))

    elif A == 2:
        for t in range(0, len(prodA)):
            Hp = (float(coefs[2]) * float(prodA[t])) + (float(coefs[3]) * float(prodB[t]))
            hp.append(float(Hp))

    else:
        for t in range(0, len(prodA)):
            Hp = (float(coefs[2]) * float(prodA[t])) + (float(coefs[3]) * float(prodB[t])) + (
                        float(coefs[4]) * float(prodC[t]))
            hp.append(float(Hp))

    return hp


def reaction_processing(reaction, data):
    A = len(reaction[1][0])
    if A == 1:
        reacA1 = reaction[0][0][0].strip()
        reacAE = reaction[0][0][1].strip()
        reacB1 = reaction[0][1][0].strip()
        reacBE = reaction[0][1][1].strip()

        prodA1 = reaction[1][0][0].strip()
        prodAE = reaction[1][1][0].strip()

        coefs = [reacAE, reacBE, prodAE]
        reacA1z = 0
        reacB1z = 0
        prodA1z = 0
        for i in data[0]:
            if i == reacA1: reacA1z = data[0].index(i)
        for i in data[0]:
            if i == reacB1: reacB1z = data[0].index(i)
        for i in data[0]:
            if i == prodA1: prodA1z = data[0].index(i)

        enth_data = data[1:61]
        Cp_data = data[62:123]
        enth_prodA = []
        Cp_prodA = []

        enth_reacA = (float(data[3][reacA1z]) * 1000)
        enth_reacB = (float(data[3][reacB1z]) * 1000)

        for j in enth_data:
            enth_prodA.append(float(j[prodA1z]) * 1000)

        for j in Cp_data:
            Cp_prodA.append(float(j[prodA1z]))

        return enth_reacA, enth_reacB, enth_prodA, Cp_prodA, coefs, A

    elif A == 2:
        reacA1 = reaction[0][0][0].strip()
        reacAE = reaction[0][0][1].strip()
        reacB1 = reaction[0][1][0].strip()
        reacBE = reaction[0][1][1].strip()

        prodA1 = reaction[1][0][0].strip()
        prodAE = reaction[1][1][0].strip()
        prodB1 = reaction[1][0][1].strip()
        prodBE = reaction[1][1][1].strip()

        coefs = [reacAE, reacBE, prodAE, prodBE]
        reacA1z = 0
        reacB1z = 0
        prodA1z = 0
        prodB1z = 0
        for i in data[0]:
            if i == reacA1: reacA1z = data[0].index(i)
        for i in data[0]:
            if i == reacB1: reacB1z = data[0].index(i)
        for i in data[0]:
            if i == prodA1: prodA1z = data[0].index(i)
        for i in data[0]:
            if i == prodB1: prodB1z = data[0].index(i)

        enth_data = data[1:61]
        Cp_data = data[62:123]
        enth_prodA = []
        enth_prodB = []
        Cp_prodA = []
        Cp_prodB = []

        enth_reacA = (float(data[3][reacA1z]) * 1000)
        enth_reacB = (float(data[3][reacB1z]) * 1000)

        for j in enth_data:
            enth_prodA.append(float(j[prodA1z]) * 1000)
        for j in enth_data:
            enth_prodB.append(float(j[prodB1z]) * 1000)

        for j in Cp_data:
            Cp_prodA.append(float(j[prodA1z]))
        for j in Cp_data:
            Cp_prodB.append(float(j[prodB1z]))

        return enth_reacA, enth_reacB, enth_prodA, enth_prodB, Cp_prodA, Cp_prodB, coefs, A

    else:
        reacA1 = reaction[0][0][0].strip()
        reacAE = reaction[0][0][1].strip()
        reacB1 = reaction[0][1][0].strip()
        reacBE = reaction[0][1][1].strip()

        prodA1 = reaction[1][0][0].strip()
        prodAE = reaction[1][1][0].strip()
        prodB1 = reaction[1][0][1].strip()
        prodBE = reaction[1][1][1].strip()
        prodC1 = reaction[1][0][2].strip()
        prodCE = reaction[1][1][2].strip()

        coefs = [reacAE, reacBE, prodAE, prodBE, prodCE]
        reacA1z = 0
        reacB1z = 0
        prodA1z = 0
        prodB1z = 0
        prodC1z = 0

        for i in data[0]:
            if i == reacA1: reacA1z = data[0].index(i)
        for i in data[0]:
            if i == reacB1: reacB1z = data[0].index(i)
        for i in data[0]:
            if i == prodA1: prodA1z = data[0].index(i)
        for i in data[0]:
            if i == prodB1: prodB1z = data[0].index(i)
        for i in data[0]:
            if i == prodC1: prodC1z = data[0].index(i)

        enth_data = data[1:61]
        Cp_data = data[62:123]
        enth_prodA = []
        enth_prodB = []
        enth_prodC = []
        Cp_prodA = []
        Cp_prodB = []
        Cp_prodC = []

        enth_reacA = (float(data[3][reacA1z]) * 1000)
        enth_reacB = (float(data[3][reacB1z]) * 1000)

        for j in enth_data:
            enth_prodA.append(float(j[prodA1z]) * 1000)
        for j in enth_data:
            enth_prodB.append(float(j[prodB1z]) * 1000)
        for j in enth_data:
            enth_prodC.append(float(j[prodC1z]) * 1000)

        for j in Cp_data:
            Cp_prodA.append(float(j[prodA1z]))
        for j in Cp_data:
            Cp_prodB.append(float(j[prodB1z]))
        for j in Cp_data:
            Cp_prodC.append(float(j[prodC1z]))

        return enth_reacA, enth_reacB, enth_prodA, enth_prodB, enth_prodC, Cp_prodA, Cp_prodB, Cp_prodC, coefs, A


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

        i = 0
        j = n
        mid = 0
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


def calculate(oxidizer, fuel):
    To = 298.15

    file_path = 'enthalpies.csv'
    data = extract_csv_to_2d_array(file_path)
    reaction = exponentF(oxidizer, fuel)
    processed = reaction_processing(reaction, data)
    enth_reacA = processed[0]
    enth_reacB = processed[1]
    enth_prodA = processed[2]
    enth_prodB = processed[3]
    enth_prodC = processed[4]
    coefs = processed[-2]
    A = processed[-1]

    Hr = ((float(coefs[0]) * float(enth_reacA)) + (float(coefs[1]) * float(enth_reacB)))
    Hp = calculateHr(enth_prodA, enth_prodB, enth_prodC, coefs, A)

    delta_enth = []
    for i in Hp:
        change = i - Hr
        delta_enth.append(change)

    print(Hp)
    print(Hr)
    minA = close(Hp, Hr)[0]
    maxA = close(Hp, Hr)[1]
    minB = Hp.index(minA)
    maxB = Hp.index(maxA)

    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
    ref = headers[62:123]
    lower_temp = ref[minB].split(" - ")[1].split("K")[0]
    upper_temp = ref[maxB].split(" - ")[1].split("K")[0]

    Tp = To + ((Hr - maxA) / (minA - maxA) * (float(upper_temp) - float(lower_temp)) + float(lower_temp))
    return Tp


oxids = ["O2 (Oxygen)", "F2 (Fluorine)", "F2O2 (Perfluorine Peroxide)", "N2O4 (Nitrogen Tetroxide)",
         "H2O2 (Hydrogen Peroxide) 95%",
         "H2O2 (Hydrogen Peroxide) 85%", "O3 (Ozone)", "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)",
         "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)"]
for i in oxids:
    fuels = []
    if i == "O2 (Oxygen)":
        fuels = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                 "NH3 (Ammonia)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)",
                 "C12H26 (n-Dodecane)"]
    if i == "F2 (Fluorine)":
        fuels = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                 "NH3 (Ammonia)", "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)",
                 "N2H4 (Hydrazine)",
                 "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
    if i == "F2O2 (Perfluorine Peroxide)":
        fuels = ["H2 (Hydrogen)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
    if i == "O3 (Ozone)":
        fuels = ["H2 (Hydrogen)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
    if i == "N2O4 (Nitrogen Tetroxide)":
        fuels = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                 "75% CH6N2 + 25% N2H4 (UH-25)",
                 "50% CH6N2 + 50% N2H4 (Aerosine-50)", "CH3OH (Methanol)", "C2H8N2 (UnsymmetricalDimethylHydrazine)",
                 "CH6N2 (MonomethylHydrazine)",
                 "N2H4 (Hydrazine)", "C12H26 (n-Dodecane)"]
    if i == "H2O2 (Hydrogen Peroxide) 95%" or i == "H2O2 (Hydrogen Peroxide) 85%":
        fuels = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                 "75% CH6N2 + 25% N2H4 (UH-25)",
                 "50% CH6N2 + 50% N2H4 (Aerosine-50)", "CH3OH (Methanol)", "C2H8N2 (UnsymmetricalDimethylHydrazine)",
                 "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "C12H26 (n-Dodecane)"]
    if i == "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)" or i == "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)":
        fuels = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                 "CH3OH (Methanol)"]

    for k in fuels:
        Oxidizer = i
        Fuel = k
        print(f"{Fuel} + {Oxidizer} ===>", end=" ")
        result = calculate(Oxidizer, Fuel)
        strz = f"Combustion Temperature: {round(result, 3)}K"
        print(strz)
    print()