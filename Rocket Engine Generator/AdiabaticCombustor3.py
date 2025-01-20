from thermo import ChemicalConstantsPackage, PRMIX, CEOSLiquid, CEOSGas, FlashPureVLS
import cantera as ct
from EqtnBalancer import solver

def split(txt, sep):
    return txt.split(sep)
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
                         solver("C2H5OH + F2 = CF4 + H2O + HF"),
                         solver("C2H5OH + F2 = CF4 + H2O + HF"),
                         solver("C6H5NH2 + F2 = CF4 + N2 + HF"),
                         solver("NH3 + F2 = HF + NF3"),
                         solver("C2H8N2 + F2 = CF4 + HF + N2"),
                         solver("CH6N2 + F2 = HF + NF3 + CF4"),
                         solver("N2H4 + F2 = NF3 + HF"),
                         solver("CH3OH + F2 = CF4 + CO2 + HF"),
                         solver("C12H26 + F2 = CF4 + HF")]
        case "F2O2 (Perfluorine Peroxide)":
            fuel_ListSample = ["H2 (Hydrogen)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
            Reactants = [solver("H2 + F2O2 = HF + H2O"),
                         solver("CH3OH + F2O2 = H2O + CO2 + HF"),
                         solver("C12H26 + F2O2 = CO2 + HF + H2O")]
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
                         solver("C2H5OH + N2O4 = CO2 + N2 + H2O"),
                         solver("C2H5OH + N2O4 = CO2 + N2 + H2O"),
                         solver("C6H5NH2 + N2O4 = CO2 + H2O + N2"),
                         solver("CH6N2 + N2O4 = CO2 + N2 + H2O"),
                         solver("CH6N2 + N2O4 = CO2 + N2 + H2O"),
                         solver("CH3OH + N2O4 = N2 + CO2 + H2O"),
                         solver("NH3 + N2O4 = N2 + H2O"),
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
    return reaction
def calculateHr(prodA, prodB, prodC, prods, coefs, A):
    hp = []
    A1 = ['H2', 'O2', 'H2O', 'CO2', 'F2', 'F2O2', 'N2O4', 'H2O2', 'O3', 'HNO3', 'CH4', 'Ethanol', 'Aniline', 'Ammonia',
          '1,1-dimethylhydrazine', 'Methylhydrazine', 'Hydrazine', 'Methanol', 'C12H26', 'NO2', 'CF4', 'N2', 'HF',
          'Aniline', 'NF3']
    A2 = [0, 0, -241.826, 0, 0, 31.61, 10.9, -135.403, 141.744, -134.19, -74.518, -235.03, 86.81, -45.556, 48.3, 54.14,
          97.56, -200.92, -353.5, 34.071, -933.76, 0, -272.726, 86.81, -123]

    if A == 1:
        for t in range(0, len(prodA)):
            Hp = (float(coefs[2]) * (float(prodA[t]) + A2[A1.index(prods[0])]))
            hp.append(float(Hp))

    elif A == 2:
        for t in range(0, len(prodA)):
            Hp = (float(coefs[2]) * (float(prodA[t]) + A2[A1.index(prods[0])])) + (float(coefs[3]) * (float(prodB[t]) + A2[A1.index(prods[1])]))
            hp.append(float(Hp))

    else:
        for t in range(0, len(prodA)):
            Hp = (float(coefs[2]) * (float(prodA[t]) + A2[A1.index(prods[0])])) + (float(coefs[3]) * (float(prodB[t]) + A2[A1.index(prods[1])])) + (float(coefs[4]) * (float(prodC[t]) + A2[A1.index(prods[2])]))
            hp.append(float(Hp))

    return hp
def reaction_processing(reaction):
    A = len(reaction[1][0])
    Temps = [100, 200, 298.15, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800,
             1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600,
             3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400,
             5500, 5600, 5700, 5800, 5900, 6000]
    A1 = ["H2", "O2", "H2O", "CO2", "F2", "F2O2", "N2O4", "H2O2", "O3", "HNO3", "CH4", "C2H5OH", "C6H5NH2", "NH3",
        "C2H8N2", "CH6N2", "N2H4", "CH3OH", "C12H26", "NO2", "CF4", "N2", "HF", "C6H7N"]
    A2 = [0, 0, -228.582, 0, 0, 31.61, 9.079, -136.106, 142.674, -134.306, -74.873, -277.5, 0, -45.898, 48.9, 94.6,
        95.353, -277.5, -350.9, 33.095, -393.522, -933.199, 0, -272.546, 86.81]

    if A == 1:
        reacA1 = reaction[0][0][0].strip(); reacAE = reaction[0][0][1].strip()
        reacB1 = reaction[0][1][0].strip(); reacBE = reaction[0][1][1].strip()

        prodA1 = reaction[1][0][0].strip(); prodAE = reaction[1][1][0].strip()

        coefs = [reacAE, reacBE, prodAE]

        enth_reacA = A2[A1.index(reacA1)]
        enth_reacB = A2[A1.index(reacB1)]
        enth_prodA = []
        for t_new in Temps:
            val = Enthaly_Calculator(t_new, prodA1)
            enth_prodA.append(val)

        return enth_reacA, enth_reacB, enth_prodA, [prodA1], coefs, A

    elif A == 2:
        reacA1 = reaction[0][0][0].strip(); reacAE = reaction[0][0][1].strip()
        reacB1 = reaction[0][1][0].strip(); reacBE = reaction[0][1][1].strip()

        prodA1 = reaction[1][0][0].strip(); prodAE = reaction[1][1][0].strip()
        prodB1 = reaction[1][0][1].strip(); prodBE = reaction[1][1][1].strip()

        coefs = [reacAE, reacBE, prodAE, prodBE]

        enth_reacA = A2[A1.index(reacA1)]
        enth_reacB = A2[A1.index(reacB1)]
        enth_prodA = []; enth_prodB = []

        for t_new in Temps:
            valA = Enthaly_Calculator(t_new, prodA1)
            valB = Enthaly_Calculator(t_new, prodB1)

            enth_prodA.append(valA)
            enth_prodB.append(valB)

        return enth_reacA, enth_reacB, enth_prodA, enth_prodB, [prodA1, prodB1], coefs, A

    else:
        reacA1 = reaction[0][0][0].strip(); reacAE = reaction[0][0][1].strip()
        reacB1 = reaction[0][1][0].strip(); reacBE = reaction[0][1][1].strip()

        prodA1 = reaction[1][0][0].strip(); prodAE = reaction[1][1][0].strip()
        prodB1 = reaction[1][0][1].strip(); prodBE = reaction[1][1][1].strip()
        prodC1 = reaction[1][0][2].strip(); prodCE = reaction[1][1][2].strip()

        coefs = [reacAE, reacBE, prodAE, prodBE, prodCE]

        enth_reacA = A2[A1.index(reacA1)]
        enth_reacB = A2[A1.index(reacB1)]
        enth_prodA = []; enth_prodB = []; enth_prodC = []

        for t_new in Temps:
            valA = Enthaly_Calculator(t_new, prodA1)
            valB = Enthaly_Calculator(t_new, prodB1)
            valC = Enthaly_Calculator(t_new, prodC1)

            enth_prodA.append(valA)
            enth_prodB.append(valB)
            enth_prodC.append(valC)

        return enth_reacA, enth_reacB, enth_prodA, enth_prodB, enth_prodC, [prodA1, prodB1, prodC1], coefs, A
def Enthaly_Calculator(t, species):
    STP = 298.15

    constants, correlations = ChemicalConstantsPackage.from_IDs([species])
    eos_kwargs = dict(Tcs=constants.Tcs, Pcs=constants.Pcs, omegas=constants.omegas)

    liquid = CEOSLiquid(PRMIX, HeatCapacityGases=correlations.HeatCapacityGases, eos_kwargs=eos_kwargs)
    gas = CEOSGas(PRMIX, HeatCapacityGases=correlations.HeatCapacityGases, eos_kwargs=eos_kwargs)

    flasher = FlashPureVLS(constants, correlations, gas=gas, liquids=[liquid], solids=[])
    h_298 = flasher.flash(T=STP, P=ct.one_atm).H()/1000
    h_T = flasher.flash(T=t, P=ct.one_atm).H()/1000
    HH_Tr = (h_T - h_298)
    return HH_Tr
def close(arr, target):
    """
    Find the two closest numbers in the array to the target number.

    Parameters:
    arr (list of int/float): The list of numbers to search through.
    target (int/float): The target number to find the closest numbers to.

    Returns:
    list of int/float: A list containing the closest smaller and larger numbers to the target.
    """
    # Sort the array to ensure numbers are in order
    arr.sort()

    # Initialize variables to hold the closest smaller and larger numbers
    smaller, larger = None, None

    # Iterate through the array to find the closest smaller and larger numbers
    for num in arr:
        if num < target:
            smaller = num
        elif num > target:
            larger = num
            break  # Exit loop once the first larger number is found

    if smaller is None or larger is None:
        raise IndexError(f"Index could not be dound within list, could not find {target} within {arr}")
    return [smaller, larger]
def calculate(oxidizer, fuel):
    To = 298.15

    reaction = exponentF(oxidizer, fuel)
    processed = reaction_processing(reaction)
    enth_reacA = processed[0]
    enth_reacB = processed[1]
    enth_prodA = list[float](processed[2])
    enth_prodB = list[float](processed[3])
    enth_prodC = list[float](processed[4])
    prods = processed[-3]
    coefs = processed[-2]
    A = processed[-1]

    Hr = ((float(coefs[0]) * float(enth_reacA)) + (float(coefs[1]) * float(enth_reacB)))
    Hp = calculateHr(enth_prodA, enth_prodB, enth_prodC, prods, coefs, A)
    delta_H = []
    for z in Hp: delta_H.append(float(z) - float(Hr))

    min_max = close(delta_H, 0)

    minA = min_max[0]
    maxA = min_max[1]

    minB = delta_H.index(minA)
    maxB = delta_H.index(maxA)

    Temps = [0, 100, 200, 298.15, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800,
             1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600,
             3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400,
             5500, 5600, 5700, 5800, 5900, 6000]
    lower_temp = Temps[minB]
    upper_temp = Temps[maxB]

    Tp = To + ((Hr - maxA) / (minA - maxA) * (float(upper_temp) - float(lower_temp)) + float(lower_temp))
    return Tp

oxids = ["O2 (Oxygen)", "F2 (Fluorine)", "F2O2 (Perfluorine Peroxide)", "N2O4 (Nitrogen Tetroxide)", "H2O2 (Hydrogen Peroxide) 95%",
           "H2O2 (Hydrogen Peroxide) 85%", "O3 (Ozone)", "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)","AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)"]
for i in oxids:
    fuels = []
    if i == "O2 (Oxygen)":
        fuels = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                 "NH3 (Ammonia)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
    if i == "F2 (Fluorine)":
        fuels = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                 "NH3 (Ammonia)", "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                 "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
    if i == "F2O2 (Perfluorine Peroxide)":
        fuels = ["H2 (Hydrogen)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
    if i == "O3 (Ozone)":
        fuels = ["H2 (Hydrogen)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
    if i == "N2O4 (Nitrogen Tetroxide)":
        fuels = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)",
                 "50% CH6N2 + 50% N2H4 (Aerosine-50)", "CH3OH (Methanol)", "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)",
                 "N2H4 (Hydrazine)", "C12H26 (n-Dodecane)"]
    if i == "H2O2 (Hydrogen Peroxide) 95%" or i == "H2O2 (Hydrogen Peroxide) 85%":
        fuels = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)",
                 "50% CH6N2 + 50% N2H4 (Aerosine-50)", "CH3OH (Methanol)", "C2H8N2 (UnsymmetricalDimethylHydrazine)",
                 "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "C12H26 (n-Dodecane)"]
    if i == "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)" or i == "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)":
        fuels = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)"]

    for k in fuels:
        Oxidizer = i; Fuel = k
        print(f"Combustion Temperature of {Fuel} & {Oxidizer} =", end =" ")
        result = calculate(Oxidizer, Fuel)
        strz = f"{round(result, 3)}K"
        print(strz)
    print()