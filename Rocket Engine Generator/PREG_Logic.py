# coding=windows-1252
import os
import math
import random
import shutil
import string
from os.path import exists as file_exists

def combustion(prop, exhaust, n_of_items):
    pass
def master_search(strings, tbc):
    IsThere = False
    for s in strings:
        if strings[strings.index(s)] == tbc:
            IsThere = True
            break
    return IsThere
def random_number(add, maxV): return add + random.randint(0, maxV)
def findexA(array, search): return array.index(search)
def findexB(array, search):
    found_it = None
    found_loc = -1
    for idx, i in enumerate(array):
        if isinstance(i, str) and search in i:
            found_it = i
            found_loc = idx
            break
    if found_it is None:
        return [None, -1]
    else:
        return [found_it, found_loc]
def findexC(array, search):
    state = False
    for i in array:
        if search in i:
            state = True
            break
        else:
            pass
    return state
def randomize(array):
    #
    random.shuffle(array)
    return random.choice(array)
def split(txt, sep): return txt.split(sep)
def NumFormat(num): return format(round(num, 2), ",")
def main_code(filelogging):
    def nameGen():
        engine_Name1 = []
        file = open("Names.txt", "r")
        for x in file:
            engine_Name1.append(f"{x}")
        firstPart = ["RD", "RS", "AJ", "XLR", "NK", "RL", "KDTU", "AR", "BE", "MV", "YF", "PKA", "J", "RSA", "MJ", "XS",
                     "LM10", "HM", "LE", "LRE", "CE", "DST", "DOK", "KDU", "KRD", "RO", "LMS", "LMP", "RT", "F", "E",
                     "V"
                     "A", "B", "S.10", "JDK", "SPP", "TYS", "SOK", "RES", "FWR", "NAA75", "LR", "MA", "GE", "OSA", "FG",
                     "OBA", "NA", "RM02", "RM", "H", "MBB", "MB", "DF", "DE", "BF", "X", "BW", "BADR", "HS", "DC", "UA",
                     "P", "KMV", "M", "SRMU", "KVD", "JD", "PS", "CE"]
        engNameFinalf = " " + randomize(engine_Name1)
        firstPart_f = randomize(firstPart) + "-"
        finalNumber = random_number(12, 1098)
        if finalNumber % 8 == 0:
            engine_Namee = str(firstPart_f) + str(finalNumber) + str(engNameFinalf)
        else:
            uio93 = random_number(1, 1000)
            uio94 = random_number(1, 12)
            if uio93 % uio94 == 0:
                randomizedCharacter = random.choice(string.ascii_lowercase)
                while (randomizedCharacter == "l") or (randomizedCharacter == "o") or (randomizedCharacter == "i") or \
                        (randomizedCharacter == "q") or (randomizedCharacter == "e") or (randomizedCharacter == "h") or \
                        (randomizedCharacter == "g") or (randomizedCharacter == "c") or (randomizedCharacter == "j"):
                    randomizedCharacter = random.choice(string.ascii_lowercase)
                    if (randomizedCharacter != "l") and (randomizedCharacter != "o") and (
                            randomizedCharacter != "i") and \
                            (randomizedCharacter != "q") and (randomizedCharacter != "e") and (
                            randomizedCharacter != "h") \
                            and (randomizedCharacter != "g") and (randomizedCharacter != "c") and (
                            randomizedCharacter != "j"):
                        break
            else:
                randomizedCharacter = random.choice(string.ascii_uppercase)
                while (randomizedCharacter == "O") or (randomizedCharacter == "I") or (randomizedCharacter == "Q"):
                    randomizedCharacter = random.choice(string.ascii_uppercase)
                    if (randomizedCharacter != "O") and (randomizedCharacter != "I") and (randomizedCharacter != "Q"):
                        break
            engine_Namee = str(firstPart_f) + str(finalNumber) + str(randomizedCharacter) + str(engNameFinalf)
        return engine_Namee
    def isHypergolic(OCC, FCC):
        isHyper = False
        match OCC:
            case "N2O4 (Nitrogen Tetroxide)":
                match FCC:
                    case "50% CH6N2 + 50% N2H4 (Aerosine-50)" | "75% CH6N2 + 25% N2H4 (UH-25)" | "C6H5NH2 (Aniline)" | \
                         "C2H8N2 (UnsymmetricalDimethylHydrazine)" | "CH6N2 (MonomethylHydrazine)" | "N2H4 (Hydrazine)":
                        isHyper = True
                    case _:
                        isHyper = False
            case "H2O2 (Hydrogen Peroxide) 95%" | "H2O2 (Hydrogen Peroxide) 85%", "O2 (Oxygen)":
                isHyper = False
            case "O3 (Ozone)" | "F2 (Fluorine)" | "F2O2 (Perfluorine Peroxide)":
                isHyper = True
            case "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)" | "AK20I: 80% HNO3 + 20% N2O4 (Nitric Acid)" | \
                 "AK20K: 80% HNO3 + 20% N2O4 (Nitric Acid)" | "AK27I: 73% HNO3 + 27% N2O4 (Nitric Acid)" | \
                 "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)":
                match FCC:
                    case "CH6N2 (MonomethylHydrazine)" | "N2H4 (Hydrazine)":
                        isHyper = True
                    case _:
                        isHyper = False
        return isHyper
    def isCryogenic(OCC, FCC):
        isCryo = False
        match OCC:
            case "O3 (Ozone)" | "F2 (Fluorine)" | "F2O2 (Perfluorine Peroxide)" | "O2 (Oxygen)": isCryo = True
        match FCC:
            case "CH3OH (Methanol)" | "C12H26 (n-Dodecane)" | "H2 (Hydrogen)" | "C2H5OH(Ethanol) 95%" | "C2H5OH(Ethanol) 75%" | \
                 "NH3 (Ammonia)" | "CH4 (Methane)": isCryo = True
        return isCryo
    def initialisation(fNum):
        if not file_exists(org): os.mkdir(org)
        if not file_exists(org1): os.mkdir(org1)
        if not file_exists(org2): os.mkdir(org2)
        if not file_exists(pathe):
            init = open(pathe, "x")
            init.close()
        sizeInbytes = os.path.getsize(pathe)
        sizeInKilobytes = (sizeInbytes / 1024)
        if sizeInKilobytes >= 50:
            if file_exists(logPF):
                if file_exists("./GenFiles/GenData/FullFolders/obf_rex[Full]" + str(fNum) + ".txt"):
                    fNum += 1
                else:
                    shutil.copy2(pathe, "./GenFiles/GenData/FullFolders/obf_rex[Full]" + str(fNum) + ".txt")
                    rset = open(pathe, 'wt')
                    rset.write("")
                    rset.close()
            else:
                org3 = "./GenFiles/GenData/FullFolders"
                os.mkdir(org3)
                shutil.copy2("./GenFiles/GenData/obf_rex.txt", logPF)
    def propDataFind(fuel, oxid):
        global fuel_ListSample, combustionTemps, mixRatios, exhaustVels
        match oxid:
            case "O2 (Oxygen)":
                fuel_ListSample = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                                   "C6H5NH2 (Aniline)", "NH3 (Ammonia)", "CH6N2 (MonomethylHydrazine)",
                                   "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
                combustionTemps = [3304, 3379, 3314, 3167, 3657, 3020, 3399, 3275, 3214, 3526]
                mixRatios = [5.00, 2.77, 1.49, 1.29, 1.72, 1.28, 1.15, 0.74, 1.19, 2.29]
                exhaustVels = [3738, 2932, 2713, 2635, 2708, 2815, 2938, 2973, 2687, 2834]
            case "F2 (Fluorine)":
                fuel_ListSample = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                                   "C6H5NH2 (Aniline)", "NH3 (Ammonia)", "C2H8N2 (UnsymmetricalDimethylHydrazine)",
                                   "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)",
                                   "C12H26 (n-Dodecane)"]
                combustionTemps = [3689, -1, -1, 4344, -1, 4469, -1, -1, 4544, 4402, -1]
                mixRatios = [6.00, -1.00, -1.00, 2.26, -1.00, 2.81, -1.00, -1.00, 1.82, 2.20, -1.00]
                exhaustVels = [3925, -1, -1, 3106, -1, 3278, -1, -1, 3315, 3146, -1]
            case "F2O2 (Perfluorine Peroxide)":
                fuel_ListSample = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                                   "C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                                   "CH6N2 (MonomethylHydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)",
                                   "N2H4 (Hydrazine)"]
                combustionTemps = [-1, 4530, 4437, -1, 4517, 4584, 4575, 4583, -1, 4571, -1]
                mixRatios = [-1.00, 4.82, 2.56, -1.00, 2.41, 2.41, 2.22, 2.33, -1.00, 3.67, -1.00]
                exhaustVels = [-1, 3281, 3134, -1, 3006, 3255, 3273, 3264, -1, 3166, -1]
            case "O3 (Ozone)":
                fuel_ListSample = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                                   "C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                                   "CH6N2 (MonomethylHydrazine)", "C12H26 (n-Dodecane)", "CH3OH (Methanol)",
                                   "N2H4 (Hydrazine)", "NH3 (Ammonia)"]
                combustionTemps = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
                mixRatios = [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00]
                exhaustVels = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
            case "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)" | "AK20I: 80% HNO3 + 20% N2O4 (Nitric Acid)" | \
                 "AK20K: 80% HNO3 + 20% N2O4 (Nitric Acid)" | "AK27I: 73% HNO3 + 27% N2O4 (Nitric Acid)" | \
                 "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)":
                fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "CH6N2 (MonomethylHydrazine)",
                                   "N2H4 (Hydrazine)", "CH3OH (Methanol)"]
                combustionTemps = [2795, 2905, 3033, 2932, 2824]
                mixRatios = [8.00, 2.75, 2.13, 1.28, 2.13]
                exhaustVels = [3112, 2449, 2635, 2702, 2441]
            case "N2O4 (Nitrogen Tetroxide)":
                fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                                   "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                                   "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)",
                                   "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
                combustionTemps = [2973, 3151, 3006, 3468, 3268, 3229, 3296, 3252, 3137, 3058, 3342]
                mixRatios = [6.50, 2.26, 1.93, 2.64, 1.85, 1.59, 2.10, 1.73, 1.08, 1.78, 3.53]
                exhaustVels = [3334, 2540, 2479, 2538, 2730, 2750, 2713, 2742, 2803, 2528, 2619]
            case "H2O2 (Hydrogen Peroxide) 85%":
                fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                                   "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                                   "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)",
                                   "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
                combustionTemps = [2544, 2552, 2447, 2719, 2681, 2668, 2690, 2681, 2630, 2511, 2666]
                mixRatios = [14.00, 4.62, 3.77, 5.95, 4.02, 3.39, 4.63, 3.76, 2.15, 3.55, 7.84]
                exhaustVels = [2882, 2476, 2425, 2495, 2592, 2604, 2582, 2600, 2642, 2464, 2530]
            case "H2O2 (Hydrogen Peroxide) 95%":
                fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                                   "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                                   "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)",
                                   "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
                combustionTemps = [2666, 2762, 2653, 2934, 2870, 2852, 2884, 2871, 2801, 2709, 2878]
                mixRatios = [11.00, 3.97, 3.27, 4.94, 3.32, 2.82, 3.82, 3.13, 1.82, 3.06, 6.50]
                exhaustVels = [1918, 1599, 1566, 1610, 1683, 1692, 1676, 1688, 1718, 1590, 1639]
        x = fuel_ListSample.index(fuel)
        combust_temp = str(combustionTemps[x])
        mixRatio = str(mixRatios[x])
        exhaustVelF = str(exhaustVels[x])
        return combust_temp + ", " + mixRatio + ", " + exhaustVelF
    def NzlParameters(alt_Of_Operation):
        nozzle_Type_Chosen, OExpansionRatio = "", ""
        match alt_Of_Operation:
            case "0-20 km (Sea Level)":
                nozzle_Type_List_SL = ["Contour Bell Nozzle", "Parabolic Bell Nozzle", "Conical Nozzle",
                                       "Stepped Dual Bell Nozzle"]
                nozzle_Type_Chosen = randomize(nozzle_Type_List_SL)
                if nozzle_Type_Chosen == "Conical Nozzle":
                    OExpansionRatio = str(random_number(10, 9)) + ":1"
                else:
                    OExpansionRatio = str(random_number(10, 12)) + ":1"
            case "20-30 km (Medium Atmosphere)":
                nozzle_Type_List_HA = ["Contour Bell Nozzle", "Parabolic Bell Nozzle", "Stepped Dual Bell Nozzle"]
                nozzle_Type_Chosen = randomize(nozzle_Type_List_HA)
                OExpansionRatio = str(random_number(32, 14)) + ":1"
            case "30-80 km (High Atmosphere)":
                nozzle_Type_List_HAi = ["Contour Bell Nozzle", "Parabolic Bell Nozzle", "Stepped Dual Bell Nozzle"]
                nozzle_Type_Chosen = randomize(nozzle_Type_List_HAi)
                OExpansionRatio = str(random_number(47, 43)) + ":1"
            case "80 km+ (Vacuum)":
                nozzle_Type_List_VA = ["Contour Bell Nozzle", "Parabolic Bell Nozzle", "Expanding Nozzle"]
                nozzle_Type_Chosen = randomize(nozzle_Type_List_VA)
                OExpansionRatio = str(random_number(90, 110)) + ":1"
            case "Any Altitude (0-80 km+)":
                nozzle_Type_List_Aero = ["Linear Aerospike Nozzle", "Toroidal Aerospike Nozzle",
                                         "Stepped Dual Bell Nozzle"]
                nozzle_Type_Chosen = randomize(nozzle_Type_List_Aero)
                if nozzle_Type_Chosen == "Stepped Dual Bell Nozzle":
                    OExpansionRatio = str(random_number(10, 9)) + ":1"
                else:
                    OExpansionRatio = "None (Nozzle doesnt have a throat)"
        return nozzle_Type_Chosen + ", " + OExpansionRatio
    def StndrdDet(eng_Name, eng_Cycle, oxid_C, fuel_C, tank_RepressA, alt_Operation):
        Eng_Data = split(propDataFind(fuel_C, oxid_C), ", ")
        f_regen, propProperties, F_gimbalangle, chamberN = "", "", "", ""
        combust_temp, mixRatio, exhaustVelFinal = Eng_Data[0], Eng_Data[1], Eng_Data[2]
        tank_Repress = randomize(tank_RepressA)

        Operational_Alt = randomize(alt_Operation)
        NzlData = split(NzlParameters(Operational_Alt), ", ")
        nozzle_Type_Chosen, AR_exit = NzlData[0], NzlData[1]
        isHyp = isHypergolic(oxid_C, fuel_C)
        isCryo = isCryogenic(oxid_C, fuel_C)
        purp = uses(isHypergolic, isCryogenic, Operational_Alt, eng_Cycle)
        search_for = ["Upper", "Payload", "Space"]

        if isCryo and isHyp:
            propProperties = "Hypergolic and cryogenic"
        elif isCryo and not isHyp:
            propProperties = "Not Hypergolic but cryogenic"
        elif not isCryo and isHyp:
            propProperties = "Hypergolic but not cryogenic"
        else:
            propProperties = "Neither Hypergolic nor cryogenic"

        uio96, uio97 = random_number(1, 999), random_number(1, 11)
        if uio96 % uio97 == 0:
            Throttle_MinV, Throttle_MaxV = random_number(1, 90), random_number(100, 5)
            ThrottleRange = str(Throttle_MinV) + "-" + str(Throttle_MaxV) + "%"
        else:
            ThrottleRange = "Not Throttleable"

        longDur = master_search(search_for, purp)
        if longDur:
            cooling_mechanismA = ["Radiative Cooling", "Dump Cooling", "Film Cooling", "Regenerative Cooling",
                                  "Transpiration Cooling"]
        else:
            cooling_mechanismA = ["Ablative Cooling", "Radiative Cooling", "Dump Cooling", "Film Cooling",
                                  "Regenerative Cooling", "Transpiration Cooling"]
        cooling_Mechanism_Chosen = randomize(cooling_mechanismA)
        if cooling_Mechanism_Chosen == "Regenerative Cooling":
            f_regen = "Oxidizer "

        if purp in "Vernier":
            gimbalangle = random_number(0, 30)
            if not gimbalangle >= 1 or alt_Operation == "80 km+ (Vacuum)":
                F_gimbalangle = "None"
            else:
                F_gimbalangle = "±" + gimbalangle + "°"
        elif purp in "Course Correction" and not purp in "Lower Stage":
            F_gimbalangle = "None"
        else:
            gimbalangle = random_number(0, 10)
            if not gimbalangle >= 1 or alt_Operation == "80 km+ (Vacuum)":
                F_gimbalangle = "None"
            else:
                F_gimbalangle = "±" + str(gimbalangle) + "°"

        chambers = random_number(1, 4)
        if chambers == 1 or nozzle_Type_Chosen in "Aerospike":
            chamberN = "Single Chamber"
        elif chambers == 2:
            chamberN = "Dual Chamber"
        elif chambers == 3:
            chamberN = "Triple Chamber"
        elif chambers == 4:
            chamberN = "Quadruple Chamber"
        else:
            chamberN = "Multiple Chambers (6+)"

        cooling_Mechanism_C = f_regen + cooling_Mechanism_Chosen
        injector = Injector(cooling_Mechanism_C, eng_Cycle)
        output = output_def(eng_Name, eng_Cycle, oxid_C, fuel_C, Operational_Alt, nozzle_Type_Chosen, tank_Repress,
                            cooling_Mechanism_C, propProperties, purp, injector, AR_exit, combust_temp, mixRatio,
                            exhaustVelFinal, ThrottleRange, chamberN, F_gimbalangle)
        return output
    def uses(isHypergol, isCryogen, alt, En_Cycle):
        global useA
        compleX = False
        if En_Cycle.upper == "Combustion Tap" or En_Cycle.upper == "Staged" or En_Cycle.upper == "Full Flow":
            compleX = True
        if alt == "0-20 km (Sea Level)" or alt == "20-30 km (Medium Atmosphere)":
            if compleX:
                pot_usesA = ["Lower Stage (Main Propulsion)"]
            else:
                pot_usesA = ["Lower Stage (Main Propulsion)", "Lower Stage (Course Correction)",
                             "Lower Stage (Vernier)"]
            useA = randomize(pot_usesA)
        elif alt == "30-80 km (High Atmosphere)" or alt == "80 km+ (Vacuum)":
            if isHypergol and isCryogen:
                if compleX:
                    pot_usesA = ["Upper Stage (Main Propulsion)"]
                else:
                    pot_usesA = ["Upper Stage (Main Propulsion)", "Upper Stage (Course Correction)",
                                 "Upper Stage (Vernier)",
                                 "Upper Stage (Ullage)", "Payload (Main Propulsion)", "Payload (ACS)"]
                useA = randomize(pot_usesA)
            elif not isHypergol and isCryogen:
                if compleX:
                    pot_usesA = ["Upper Stage (Main Propulsion)"]
                else:
                    pot_usesA = ["Upper Stage (Main Propulsion)", "Upper Stage (Vernier)"]
                useA = randomize(pot_usesA)
            elif isHypergol and not isCryogen:
                if compleX:
                    pot_usesA = ["Upper Stage (Main Propulsion)", "Payload (Main Propulsion)",
                                 "Space Tug (Main Propulsion)"]
                else:
                    pot_usesA = ["Upper Stage (Main Propulsion)", "Upper Stage (Course Correction)",
                                 "Upper Stage (Vernier)",
                                 "Upper Stage (Ullage)", "Payload (Main Propulsion)", "Payload (ACS)",
                                 "Payload (Course Correction)",
                                 "Payload (Vernier)", "Space Tug (Main Propulsion)", "Space Tug (Course Correction)",
                                 "Space Tug (Vernier)", "Space Tug (Ullage)"]
                useA = randomize(pot_usesA)
        else:
            pot_usesA = ["Lower Stage (Main Propulsion)", "Upper Stage (Main Propulsion)", "Payload (Main Propulsion)"]
            useA = randomize(pot_usesA)
        return useA
    def Injector(cooling_Mechanism, engine_Cycle_Chose):
        fuel_state = "Liquid"
        if cooling_Mechanism in "Regenerative Cooling" or engine_Cycle_Chose in "Expander":
            fuel_state = "Gas"
        injector = ["Showerhead Injector", "Self-impinging Injector", "Cross-impinging Injector", "Swirl Injector",
                    "Pintle Injector"]
        return fuel_state + " " + randomize(injector)
    def output_monod(ENN, ECC, AOOC, PLC, NTLC, CMC, CCC, purposeB):
        output = [f"Engine Designation: {ENN}\n", f"Fuel Flow Cycle: {ECC}\n", f"Propellant: {PLC}\n",
                  f"Altitude Of Operation: {AOOC}\n",
                  f"Exhaust Nozzle Geometry: {NTLC}\n", f"Engine Use Case: {purposeB}\n",
                  f"Nozzle Cooling Mechanism: {CMC}\n",
                  f"Propellant catalyst: {CCC}\n\n"]
        file = open("./GenFiles/GenData/obf_rex.txt", "at")
        for x in output:
            file.write(x)
        return output
    def output_mono(ENN, ECC, AOOC, PLC, NTLC, CMC, purposeE):
        output = [f"Engine Designation: {ENN}\n", f"Fuel Flow Cycle: {ECC}\n", f"Propellant: {PLC}\n",
                  f"Altitude Of Operation: {AOOC}\n", f"Exhaust Nozzle Geometry: {NTLC}\n",
                  f"Engine Use Case: {purposeE}\n", f"Nozzle Cooling Mechanism: {CMC}\n\n"]
        file = open("./GenFiles/GenData/obf_rex.txt", "at")
        for x in output:
            file.write(x)
        return output
    def output_et(ENN, ECC, AOOC, PLC, NTLC, PGLC, purposeE, pwr):
        output = [f"Engine Designation: {ENN}\n", f"Fuel Flow Cycle: {ECC}\n", f"Propellant(Remass): {PLC}\n",
                  f"Altitude Of Operation: {AOOC}\n", f"Exhaust Nozzle Geometry: {NTLC}\n",
                  f"Engine Use Case: {purposeE}\n", f"Engine Power Source: {PGLC}\n", f"Rated Power Level: {pwr}\n\n"]
        file = open("./GenFiles/GenData/obf_rex.txt", "at")
        for x in output:
            file.write(x)
        return output
    def output_nt(ENN, ECC, AOOC, NCC, PLC, RFC, NTLC, EEV, TRC, CMC, purposeF, react_gen, bimodal, ERC, PRS, ARR, ECT):
        MaxElecP = NumFormat((ECT / 100) * 18)
        MaxP = NumFormat(((ECT / 90) * 100) / 1000)
        output = [f"Engine Designation: {ENN}\n"]
        if not ECC == "Radioisotope Engine" and not NCC == "":
            output.append(f"Fuel Flow Cycle: {NCC} {ECC}\n")
        else:
            output.append(f"Fuel Flow Cycle: {ECC}\n")
        output.append(f"Propellant (Remass): {PLC}\n")
        output.append(f"Propellant State: {PRS}\n")
        output.append(f"Reactor Generation: {react_gen}\n")
        output.append(f"Reactor Maximum Power: {MaxP} GW\n")
        output.append(f"Reactor Fuel Material: {RFC}\n")
        if NCC == "LANTR":
            try:
                output.append(f"Engine Exhaust Velocity: {NumFormat(EEV)}/~3850 m/s\n")
            except:
                output.append(f"Engine Exhaust Velocity: ERROR\n")
        else:
            try:
                output.append(f"Engine Exhaust Velocity: {NumFormat(EEV)} m/s\n")
            except:
                output.append(f"Engine Exhaust Velocity: ERROR\n")
        output.append(f"Reactor Core Temperature: {NumFormat(ECT)}°K\n")
        output.append(f"Reactor Coolant: {ERC}\n")
        if bimodal:
            output.append(f"Engine Bimodality: Engine is bimodal\n")
        else:
            output.append(f"Engine Bimodality: Engine is not bimodal\n")
        output.append(f"Engine Electrical Output: {MaxElecP} MW\n")
        output.append(f"Altitude Of Operation: {AOOC}\n")
        output.append(f"Exhaust Nozzle Geometry: {NTLC}\n")
        output.append(f"Exhaust Expansion Ratio: {ARR}\n")
        output.append(f"Exhaust Nozzle Cooling Mechanism: {CMC}\n")
        output.append(f"Engine Use Case: {purposeF}\n")
        output.append(f"Tank repressurisation Method: {TRC}\n\n")
        if filelogging:
            file = open("./GenFiles/GenData/obf_rex.txt", "at")
            for x in output:
                file.write(x)
            file.close()
        return output
    def output_def(ENN, ECC, OCC, FCC, AOOC, NTC, TRC, CMC, propProp, purp, injector, FinalAreaRatio, combust_temp, mixRatio, exhaustVel5, ThrottleRange, chamberN, F_gimbalangle):
        output = [f"Engine Designation: {ENN}\n", f"Fuel Flow Cycle: {ECC}\n", f"Engine Oxidizer: {OCC}\n",
                  f"Engine Fuel: {FCC}\n", f"Average Mixture Ratio: {mixRatio}\n", f"Propellant properties: {propProp}\n",
                  f"Altitude Of Operation: {AOOC}\n", f"Exhaust Nozzle Geometry: {NTC}\n",
                  f"Exhaust Expansion Ratio: {FinalAreaRatio}\n", f"Characteristic Exhaust Velocity: {exhaustVel5} m/s",
                  f"Adiabatic Combustion Temperature: {combust_temp}°K", f"Engine Gimbal Range: {F_gimbalangle}\n",
                  f"Engine Injector Design: {injector}\n", f"Engine chamber configuration: {chamberN}\n",
                  f"Engine Use Case: {purp}\n", f"Tank repressurisation Method: {TRC}\n",
                  f"Nozzle Cooling Mechanism: {CMC}\n",
                  f"Engine Throttle Range: {ThrottleRange}\n\n"]
        file = open("./GenFiles/GenData/obf_rex.txt", "at")
        for x in output:
            file.write(x)
        return output

    y, fNum = 0, 2
    org = "./GenFiles"
    org1 = "./GenFiles/DevData"
    org2 = "./GenFiles/GenData"
    pathe = "./GenFiles/GenData/obf_rex.txt"
    logPF = "./GenFiles/GenData/FullFolders/obf_rex[Full]1.txt"

    engine_Cycle = ["Gas Generator", "Staged Combustion (Oxidizer Rich)", "Staged Combustion (Fuel Rich)", "Expander (Open/Bleed)",
                    "Expander (Closed)", "Dual Expander (Open/Bleed)", "Dual Expander (Closed)", "Pressure-Fed", "Full Flow Staged",
                    "Electric Pump Fed", "Combustion Tap Off", "Monopropellant (Cold Gas)", "Monopropellant (Decomposition)",
                    "Gas Core", "Droplet Core", "Liquid Core", "Solid Core", "Vapor Core", "Nuclear SaltWater", "Radioisotope Engine",
                    "MagnetoPlasmaDynamic Thruster", "Hall Effect Thruster", "Gridded Ion Thruster", "Colloid Thruster",
                    "Variable Specific Impulse Magnetoplasma Rocket (VASIMR)"]
    altitude_Of_Operation = ["0-20 km (Sea Level)", "20-30 km (Medium Atmosphere)", "30-80 km (High Atmosphere)", "80 km+ (Vacuum)",
                             "Any Altitude (0-80 km+)"]
    tank_Repressurisation = ["Autogenous", "Inert Gas"]

    initialisation(fNum)
    engine_Name = nameGen()
    engine_Cycle_Chosen = randomize(engine_Cycle)

    match engine_Cycle_Chosen:
        case "Gas Core" | "Droplet Core" | "Liquid Core" | "Solid Core" | "Vapor Core" | "Nuclear SaltWater" | "Radioisotope Engine":
            match engine_Cycle_Chosen:
                case "Radioisotope Engine":
                    remass_List = ["Hydrogen (H2)", "Nitrogen (N2)", "Ammonia (NH3)", "Water (H2O)", "Oxygen (O2)",
                                   "Carbon Dioxide (CO2)", "Carbon Monoxide (CO)"]
                    reactor_fuel = ["Polonium-210", "Fermium-252", "Uranium-233", "Plutonium-238"]
                    remass_EVD = [1.782, 14.6, 4.25, 6.587, 16, 14.6, 28]
                    f_energy = [5.407, 6.925, 6.856, 5.487]
                    propellantState = "Solid Nuclear Fuel"
                    nuclear_Cycle_Chosen = ""

                    enri_level = random_number(15, 80)
                    max_t = random_number(1950, 50)
                    remass_List_Chosen = random.choice(remass_List)
                    propellant_List_Chosen = remass_List_Chosen
                    reactor_Fuel_Chosen = randomize(reactor_fuel)

                    coreTemp = (max_t - (max_t * 0.125)) + (1 + (17 * (enri_level / f_energy[findexA(reactor_fuel, reactor_Fuel_Chosen)])))

                    molmassi = findexA(remass_List, remass_List_Chosen)
                    molmass = remass_EVD[molmassi] + 5
                    divider = (((molmass + 5) - (enri_level / 20)) / f_energy[
                        findexA(reactor_fuel, reactor_Fuel_Chosen)]) ** 0.531
                    exhaustVel = (12400 / divider)
                case "Solid Core":
                    remass_List = ["Hydrogen (H2)", "Nitrogen (N2)", "Ammonia (NH3)", "Water (H2O)", "Oxygen (O2)",
                                   "Carbon Dioxide (CO2)", "Carbon Monoxide (CO)"]
                    remass_EVD = [1.782, 14.6, 4.25, 6.587, 16, 14.6, 28]
                    nuclear_cycle = ["LANTR", "LEUNTR", "LPNTR", "CERMET", "Pebble-Bed", "", "TRIGA"]
                    reactor_fuel = ["Uranium-235", "Plutonium-238"]
                    propellantState = "Solid Nuclear Fuel"

                    remass_List_Chosen = random.choice(remass_List)
                    propellant_List_Chosen = remass_List_Chosen
                    nuclear_Cycle_Chosen = randomize(nuclear_cycle)

                    if nuclear_Cycle_Chosen.upper == "LANTR":
                        remass_List_Chosen = "Hydrogen (H2)"

                        enri_level = random_number(18, 87) / 10
                        reactor_Fuel_Chosen = str(enri_level) + "% " + randomize(reactor_fuel)
                        coreTemp = random_number(1900 + (enri_level * 5), 1000)

                        molmassi = findexA(remass_List, remass_List_Chosen)
                        molmass = remass_EVD[molmassi] + 5
                        divider = (math.pow(((molmass*10) - enri_level), 0.531))/10

                        exhaustVel = (17600 / divider)
                    elif nuclear_Cycle_Chosen.upper == "LEUNTR":
                        remass_List_Chosen = random.choice(remass_List)

                        enri_level = random_number(5, 10) / 10
                        reactor_Fuel_Chosen = str(enri_level) + "% " + randomize(reactor_fuel)
                        coreTemp = random_number(1900 + (enri_level * 5), 1000)

                        molmassi = findexA(remass_List, remass_List_Chosen)
                        molmass = remass_EVD[molmassi] + 5
                        divider = (math.pow(((molmass*10) - enri_level), 0.531))/10

                        exhaustVel = (17600 / divider)
                    elif nuclear_Cycle_Chosen.upper == "LPNTR":
                        remass_List_Chosen = random.choice(remass_List)

                        enri_level = random_number(8, 87) / 10
                        reactor_Fuel_Chosen = str(enri_level) + "% " + randomize(reactor_fuel)
                        coreTemp = random_number(1900 + (enri_level * 5), 1000)

                        molmassi = findexA(remass_List, remass_List_Chosen)
                        molmass = remass_EVD[molmassi] + 5
                        divider = (math.pow(((molmass*10) - enri_level), 0.531))/10

                        exhaustVel = (17600 / divider)
                    elif nuclear_Cycle_Chosen.upper == "CERMET":
                        remass_List_Chosen = random.choice(remass_List)

                        enri_level = random_number(8, 87) / 10
                        reactor_Fuel_Chosen = str(enri_level) + "% " + randomize(reactor_fuel)
                        coreTemp = random_number(1900 + (enri_level * 5), 1000)

                        molmassi = findexA(remass_List, remass_List_Chosen)
                        molmass = remass_EVD[molmassi] + 5
                        divider = (math.pow(((molmass*10) - enri_level), 0.531))/10

                        exhaustVel = (17600 / divider)
                    elif nuclear_Cycle_Chosen.upper == "Pebble-Bed":
                        remass_List_Chosen = random.choice(remass_List)

                        enri_level = random_number(8, 87) / 10
                        propellantState = "Cryogenic Liquid"
                        propellant_List_Chosen = "Uranium(VI) Fluoride (UF6) and " + remass_List_Chosen
                        nuclear_Cycle_Chosen = randomize(nuclear_cycle)
                        reactor_Fuel_Chosen = str(enri_level) + "% " + "Uranium-235"
                        coreTemp = random_number(1400 + (enri_level * 5), 1000)

                        molmassi = findexA(remass_List, remass_List_Chosen)
                        molmass = remass_EVD[molmassi] + 5
                        divider = (math.pow(((molmass*10) - enri_level), 0.531))/10

                        exhaustVel = ((9530 * 2) / divider)
                    else:
                        remass_List_Chosen = random.choice(remass_List)
                        enri_level = random_number(8, 87) / 10
                        reactor_Fuel_Chosen = str(enri_level) + "% " + randomize(reactor_fuel)
                        coreTemp = random_number(1900 + (enri_level * 5), 1000)
                        molmassi = findexA(remass_List, remass_List_Chosen)
                        molmass = remass_EVD[molmassi] + 5
                        divider = (math.pow(((molmass*10) - enri_level), 0.531))/10
                        exhaustVel = (11000 / divider)
                case "Colloid Core":
                    remass_List = ["Hydrogen (H2)", "Nitrogen (N2)", "Ammonia (NH3)", "Water (H2O)", "Oxygen (O2)",
                                   "Carbon Dioxide (CO2)", "Carbon Monoxide (CO)"]
                    enri_level = random_number(8, 87) / 10
                    remass_EVD = [1.782, 14.6, 4.25, 6.587, 16, 14.6, 28]
                    remass_List_Chosen = random.choice(remass_List)
                    propellant_List_Chosen = "Uranium Zirconium Carbide(UC2 + ZrC) Colloid and " + remass_List_Chosen
                    nuclear_Cycle_Chosen = ""
                    propellantState = "Solid Nuclear Fuel"
                    reactor_Fuel_Chosen = enri_level + "% " + "Uranium-235"
                    coreTemp = random_number(2500 + (enri_level * 5), 1000)
                    molmassi = findexA(remass_List, remass_List_Chosen)
                    molmass = remass_EVD[molmassi] + 5
                    divider = (math.pow(((molmass*10) - enri_level), 0.531))/10
                    exhaustVel = (11800 / divider)
                case "Liquid Core":
                    nuclear_cycle = ["\"Expander Bleed\"", "\"Expander Closed\"", "\"Vortex Confined\"", "LARS"]
                    remass_List = ["Hydrogen (H2)", "Nitrogen (N2)", "Ammonia (NH3)", "Water (H2O)", "Oxygen (O2)",
                                   "Carbon Dioxide (CO2)", "Carbon Monoxide (CO)"]
                    remass_EVD = [1.782, 14.6, 4.25, 6.587, 16, 14.6, 28]
                    materials = ["Tungsten", "Osmium", "Rhenium", "Tantalum"]
                    enri_level = random_number(8, 87) / 10
                    remass_List_Chosen = random.choice(remass_List)
                    material = randomize(materials)
                    propellantState = "Nuclear Fuel in Molten Pellets"
                    propellant_List_Chosen = "Uranium impregnated " + material + " and " + remass_List_Chosen
                    nuclear_Cycle_Chosen = randomize(nuclear_cycle)
                    reactor_Fuel_Chosen = str(enri_level) + "% " + "Uranium-235"
                    coreTemp = random_number(3500 + (enri_level * 5), 1000)
                    molmassi = findexA(remass_List, remass_List_Chosen)
                    molmass = remass_EVD[molmassi] + 5
                    divider = (math.pow(((molmass*10) - enri_level), 0.531))/10
                    exhaustVel = (19620 / divider)
                case "Droplet Core":
                    nuclear_cycle = ["\"Expander Bleed\"", "\"Expander Closed\"", "\"Vortex Confined\""]
                    remass_List = ["Hydrogen (H2)", "Nitrogen (N2)", "Ammonia (NH3)", "Water (H2O)", "Oxygen (O2)",
                                   "Carbon Dioxide (CO2)", "Carbon Monoxide (CO)"]
                    enri_level = random_number(8, 87) / 10
                    remass_EVD = [1.782, 14.6, 4.25, 6.587, 16, 14.6, 28]
                    remass_List_Chosen = random.choice(remass_List)
                    propellantState = "Semi-Gaseous Nuclear Fuel"
                    propellant_List_Chosen = "Uranium(VI) Fluoride (UF6) and " + remass_List_Chosen
                    nuclear_Cycle_Chosen = randomize(nuclear_cycle)
                    reactor_Fuel_Chosen = str(enri_level) + "% " + "Uranium-235"
                    coreTemp = random_number(5400 + (enri_level * 5), 1000)
                    molmassi = findexA(remass_List, remass_List_Chosen)
                    molmass = remass_EVD[molmassi] + 5
                    divider = (math.pow(((molmass*10) - enri_level), 0.531))/10
                    exhaustVel = (19600 / divider)
                case "Vapor Core":
                    remass_List = ["Hydrogen (H2)", "Nitrogen (N2)", "Ammonia (NH3)", "Water (H2O)", "Oxygen (O2)",
                                   "Carbon Dioxide (CO2)", "Carbon Monoxide (CO)"]
                    remass_EVD = [1.782, 14.6, 4.25, 6.587, 16, 14.6, 28]
                    remass_List_Chosen = random.choice(remass_List)
                    propellant_List_Chosen = "Uranium(VI) Fluoride (UF6) and " + remass_List_Chosen
                    nuclear_Cycle_Chosen = ""
                    reactor_Fuel_Chosen = "93% Uranium-235"
                    propellantState = "Semi-Gaseous Nuclear Fuel"
                    coreTemp = random_number(5500, 1000)
                    enri_level = 93 / 10
                    molmassi = findexA(remass_List, remass_List_Chosen)
                    molmass = remass_EVD[molmassi] + 5
                    divider = (math.pow(((molmass*10) - enri_level), 0.531))/10
                    exhaustVel = 11800 / divider
                case "Gas Core":
                    remass_List = ["Hydrogen (H2)", "Nitrogen (N2)", "Ammonia (NH3)", "Water (H2O)", "Oxygen (O2)",
                                   "Carbon Dioxide (CO2)", "Carbon Monoxide (CO)"]
                    nuclear_cycle = ["\"Quartz Confinement (Nuclear Lightbulb)\"", "\"Vortex Confinement\"",
                                     "\"Wheel Flow Confinement\"", "\"Magnetohydrodynamic(MHD) Confinement\"",
                                     "\"Open Cycle\""]
                    remass_EVD = [1.782, 14.6, 4.25, 6.587, 16, 14.6, 28]
                    remass_List_Chosen = random.choice(remass_List)
                    propellant_List_Chosen = "Uranium(VI) Fluoride (UF6) and " + remass_List_Chosen
                    nuclear_Cycle_Chosen = randomize(nuclear_cycle)
                    reactor_Fuel_Chosen = "93% Uranium-235"
                    propellantState = "Gaseous Nuclear Fuel"
                    coreTemp = random_number(13650, 1000)
                    enri_level = 93
                    molmassi = findexA(remass_List, remass_List_Chosen)
                    molmass = remass_EVD[molmassi]
                    divider = ((molmass + 5) - (enri_level / 10)) ** 0.531
                    exhaustVel = 20405 / divider
                case "Nuclear SaltWater":
                    nuclear_cycle = ["\"Zubrin NSWR\"", "\"Lithium-6 NSWR\""]
                    nuclear_Cycle_Chosen = randomize(nuclear_cycle)
                    remass_List_Chosen = "Water (H2O)"
                    propellantState = "Aqueous (Dissolved in propellant)"
                    if nuclear_Cycle_Chosen == "Zubrin NSWR":
                        fissile_salts = ["Uranium", "Plutonium"]
                        fissile_salt = randomize(fissile_salts)
                        enri_level = random_number(3, 95)
                        if fissile_salt == "Uranium":
                            propellant_List_Chosen = fissile_salt + "(IV) TetraBromide (UBr3) + Water (H2O)"
                            coreTemp = random_number(126800 * (math.pow(enri_level, .95) / 98), 1000)
                            divider = math.pow(enri_level, 1.62115) / 162.115
                            exhaustVel = (random_number(4725000, 1000) / 10) * divider
                            reactor_Fuel_Chosen = str(enri_level) + "% " + fissile_salt
                        elif fissile_salt == "Plutonium":
                            propellant_List_Chosen = fissile_salt + "(III) TriBromide (PuBr4) + Water (H2O)"
                            coreTemp = random_number(146800 * (math.pow(enri_level, .95) / 98), 1000)
                            divider = math.pow(enri_level, 1.62115) / 162.115
                            exhaustVel = (random_number(4925000, 1000) / 10) * divider
                            reactor_Fuel_Chosen = str(enri_level) + "% " + fissile_salt
                    else:
                        fissile_salt = random.choice(["Lithium-6 Hydride (LiH)", "Lithium-6 Hydroxide (LiOH)"])
                        enri_level = random_number(20, 78)
                        if fissile_salt == "Lithium-6 Hydride (LiH)":
                            propellant_List_Chosen = fissile_salt + " + Water (H2O)"
                        else:
                            propellant_List_Chosen = fissile_salt + " + Ethanol (C2H5OH)"
                            remass_List_Chosen = "Ethanol (C2H5OH)"
                        coreTemp = random_number(106800 * (math.pow(enri_level, .95) / 98), 1000)
                        divider = math.pow(enri_level, 1.62115) / 162.115
                        exhaustVel = (random_number(1200000, 1000) / 10) * divider
                        reactor_Fuel_Chosen = str(enri_level) + "% " + fissile_salt
            # ============================================================================================
            if engine_Cycle_Chosen == "Solid Core" or engine_Cycle_Chosen == "Radioisotope Engine":
                nzll = ["Contour Bell Nozzle", "Parabolic Bell Nozzle"]
            else:
                nzll = ["Contour Bell Nozzle", "Parabolic Bell Nozzle", "Magnetic Virtual Nozzle"]
            nozzle_Type_List_Chosen = randomize(nzll)
            # ============================================================================================
            cooling_mechanism = ["Radiative Cooling", "Dump Cooling", "Film Cooling", "Regenerative Cooling",
                                 "Transpiration Cooling"]
            pot_uses = ["Upper Stage(Main Propulsion)", "Payload (Main Propulsion)", "Space Tug (Main Propulsion)"]
            # ============================================================================================
            use = randomize(pot_uses)
            altitude_Of_Operation_Chosen = "80 km+ (Vacuum)"
            tank_Repressurisation_Chosen = randomize(tank_Repressurisation)
            cooling_Mechanism_Chosen = randomize(cooling_mechanism)
            # ============================================================================================
            if engine_Cycle_Chosen == "Liquid Core" or engine_Cycle_Chosen == "Solid Core" or engine_Cycle_Chosen == "Pulsed Nuclear":
                reactor_gen = ["Generation II", "Generation III+", "Generation IV", "Generation V", "Generation V+"]
            elif engine_Cycle_Chosen == "Nuclear SaltWater":
                reactor_gen = ["Generation V+"]
            elif engine_Cycle_Chosen == "Radioisotope Engine":
                reactor_gen = ["Generation I"]
            else:
                reactor_gen = ["Generation II", "Generation III", "Generation III+", "Generation IV", "Generation V", "Generation V+"]
            # ============================================================================================
            reactor_gen_Chosen = randomize(reactor_gen)
            uio97 = random_number(1, 456)
            uio98 = random_number(1, 77)
            if uio97 % uio98 != 0: isBimodal = True
            else: isBimodal = False
            NzlReturnP = NzlParameters(altitude_Of_Operation_Chosen)
            parts = NzlReturnP.split(", ")
            AreaRatio = parts[1]
            output = output_nt(engine_Name, engine_Cycle_Chosen, altitude_Of_Operation_Chosen, nuclear_Cycle_Chosen,
                               propellant_List_Chosen, reactor_Fuel_Chosen, nozzle_Type_List_Chosen, exhaustVel,
                               tank_Repressurisation_Chosen, cooling_Mechanism_Chosen, use, reactor_gen_Chosen,
                               isBimodal, remass_List_Chosen, propellantState, AreaRatio, coreTemp)
        # ============================================================================================
        case "MagnetoPlasmaDynamic Thruster" | "Hall Effect Thruster" | "Gridded Ion Thruster" | "Colloid Thruster" | \
             "Variable Specific Impulse Magnetoplasma Rocket (VASIMR)":
            match engine_Cycle_Chosen:
                case "Hall Effect Thruster":
                    propellant_List = ["Xe (Xenon)", "Kr (Krypton)", "Ar (Argon)", "Bi (Bismuth)",
                                       "I2 (Iodine)", "Mg (Magnesium)", "Zn (Zinc)", "C10H16 (Adamantane)"]
                    propellant_List_Chosen = randomize(propellant_List)
                    nozzle_Type_List_Chosen = "Hall Effect Thruster Nozzle"
                case "Gridded Ion Thruster":
                    propellant_List = ["Xe (Xenon)", "Hg (Mercury)", "Cs (Caesium)"]
                    propellant_List_Chosen = randomize(propellant_List)
                    nozzle_Type_List_Chosen = "Electrostatic Ion Nozzle"
                case "Colloid Thruster":
                    propellant_List_Chosen = "NH2OH+NO3 (Hydroxylammonium nitrate)"
                    nozzle_Type_List_Chosen = "Capillary Emitter-Electrode Cone"
                case "Variable Specific Impulse Magnetoplasma Rocket (VASIMR)":
                    propellant_List = ["Xe (Xenon)", "Kr (Krypton)", "Ar (Argon)"]
                    propellant_List_Chosen = randomize(propellant_List)
                    nozzle_Type_List_Chosen = "VASIMR Magnetic Confinement Nozzle"
                case "MagnetoPlasmaDynamic Thruster":
                    propellant_List = ["Xe (Xenon)", "Ne (Neon)", "Ar (Argon)", "H2 (Hydrogen)", "N2H4 (Hydrazine)",
                                       "Li (Lithium)"]
                    propellant_List_Chosen = randomize(propellant_List)
                    nozzle_Type_List_Chosen = "Cathode Plug Magnetic Confinement Nozzle"
            pot_uses = ["Payload (Main Propulsion)", "Space Tug (Main Propulsion)"]
            use = randomize(pot_uses)
            powerGen_List = ["Hydrogen Fuel cell", "Nuclear Fission Reactor", "Nuclear Fusion Reactor",
                             "Photovoltaic Panel",
                             "Solar Thermal Panel", "Radioisotope Thermoelectric Generator (RTG)"]
            powerGen_List_Chosen = randomize(powerGen_List)
            altitude_Of_Operation_Chosen = "80 km+ (Vacuum)"
            pwr = str((round(random_number(20, 980) / 10)) * 10) + " kW"
            output = output_et(engine_Name, engine_Cycle_Chosen, altitude_Of_Operation_Chosen, propellant_List_Chosen,
                               nozzle_Type_List_Chosen, powerGen_List_Chosen, use, pwr)
        # ============================================================================================
        case "Monopropellant (Decomposition)":
            propellant_List1 = ["H2O2 (Hydrogen Peroxide)", "N2H4 (Hydrazine)", "NH2OH+NO3 (Hydroxylammonium nitrate)",
                                "65% NH4N(NO2)2 (Ammonium Dinitramide) + 35% CH3OH(Methanol)"]
            nozzle_Type_List1 = ["Conical Nozzle", "Contour Bell Nozzle", "Parabolic Bell Nozzle"]
            propellant_List_Chosen = randomize(propellant_List1)
            altitude_Of_Operation_Chosen = "80 km+ (Vacuum)"
            nozzle_Type_List_Chosen = randomize(nozzle_Type_List1)
            cooling_mechanism = ["Ablative Cooling", "Radiative Cooling"]
            cooling_Mechanism_Chosen = randomize(cooling_mechanism)
            catalyst_Chosen = ""
            match propellant_List_Chosen:
                case "N2H4 (Hydrazine)" | "65% NH4N(NO2)2 (Ammonium Dinitramide) + 35% CH3OH(Methanol)":
                    catalyst_Chosen = "Iridium coated Alumina Pellets"
                case "H2O2 (Hydrogen Peroxide)":
                    catalyst = ["KMnO4 (Potassium Permanganate) Honeycomb", "Ag (Silver) Honeycomb",
                                "FeO (Iron (II) oxide)", "MnO2 (Manganese Dioxide) Honeycomb", "K2Cr2O7 (Potassium dichromate) Honeycomb"]
                    catalyst_Chosen = randomize(catalyst)
                case "NH2OH+NO3 (Hydroxylammonium nitrate)":
                    catalyst_Chosen = "Iridium coated Copper Pellets"
            pot_uses = ["Upper Stage(Ullage)", "Upper Stage(Vernier)", "Payload (Main Propulsion)", "Payload (Vernier)",
                        "Space Tug (Ullage)", "Space Tug (Vernier)"]
            use = randomize(pot_uses)
            output = output_monod(engine_Name, engine_Cycle_Chosen, altitude_Of_Operation_Chosen, propellant_List_Chosen,
                                  nozzle_Type_List_Chosen, cooling_Mechanism_Chosen, catalyst_Chosen, use)
        # ============================================================================================
        case "Monopropellant (Cold Gas)":
            propellant_List2 = ["Nitrogen (N2)", "Helium (He)", "Carbon Dioxide (CO2)", "Ammonia (NH3)", "Hydrogen (H2)",
                                "Methane (CH4)"]
            nozzle_Type_List1 = ["Conical Nozzle", "Contour Bell Nozzle", "Parabolic Bell Nozzle"]
            propellant_List_Chosen = randomize(propellant_List2)
            altitude_Of_Operation_Chosen = "80 km+ (Vacuum)"
            nozzle_Type_List_Chosen = randomize(nozzle_Type_List1)
            cooling_Mechanism_Chosen = "Ablative Cooling"
            pot_uses = ["Upper Stage(Ullage)", "Upper Stage(Vernier)", "Payload (Main Propulsion)", "Payload (Vernier)",
                        "Space Tug (Ullage)", "Space Tug (Vernier)"]
            purpose = randomize(pot_uses)
            output = output_mono(engine_Name, engine_Cycle_Chosen, altitude_Of_Operation_Chosen, propellant_List_Chosen,
                                 nozzle_Type_List_Chosen, cooling_Mechanism_Chosen, purpose)
        # ============================================================================================
        case "Expander (Closed)" | "Expander (Open/Bleed)":
            oxidizer_List = ["O2 (Oxygen)", "F2 (Fluorine)", "F2O2 (Perfluorine Peroxide)", "O3 (Ozone)"]
            oxidizer_Chosen = randomize(oxidizer_List)
            fuel_Chosen = ""
            match oxidizer_Chosen:
                case "O2 (Oxygen)":
                    fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                                 "C6H5NH2 (Aniline)", "NH3 (Ammonia)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                                 "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
                    random.shuffle(fuel_List)
                    fuel_Chosen = random.choice(fuel_List)
                case "F2 (Fluorine)":
                    fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                                 "C6H5NH2 (Aniline)", "NH3 (Ammonia)", "C2H8N2 (UnsymmetricalDimethylHydrazine)",
                                 "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
                    random.shuffle(fuel_List)
                    fuel_Chosen = random.choice(fuel_List)
                case "F2O2 (Perfluorine Peroxide)" | "O3 (Ozone)":
                    fuel_List = ["H2 (Hydrogen)", "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
                    random.shuffle(fuel_List)
                    fuel_Chosen = random.choice(fuel_List)
            output = StndrdDet(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, tank_Repressurisation, altitude_Of_Operation)
        # ============================================================================================
        case "Dual Expander (Closed)" | "Dual Expander (Open/Bleed)":
            oxidizer_List = ["O2 (Oxygen)", "F2 (Fluorine)", "F2O2 (Perfluorine Peroxide)"]
            oxidizer_Chosen = randomize(oxidizer_List)
            fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)"]
            fuel_Chosen = ""
            match oxidizer_Chosen:
                case "O2 (Oxygen)" | "F2 (Fluorine)":
                    random.shuffle(fuel_List)
                    fuel_Chosen = random.choice(fuel_List)
                case "F2O2 (Perfluorine Peroxide)":
                    fuel_Chosen = "H2 (Hydrogen)"
            output = StndrdDet(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, tank_Repressurisation, altitude_Of_Operation)
        # ============================================================================================
        case "Staged Combustion (Fuel Rich)":
            oxidizer_List = ["O2 (Oxygen)", "F2 (Fluorine)", "F2O2 (Perfluorine Peroxide)", "O3 (Ozone)"]
            oxidizer_Chosen = randomize(oxidizer_List)
            fuel_Chosen = ""
            match oxidizer_Chosen:
                case "O2 (Oxygen)" | "F2 (Fluorine)":
                    fuel_List = ["H2 (Hydrogen)", "NH3 (Ammonia)", "N2H4 (Hydrazine)"]
                    random.shuffle(fuel_List)
                    fuel_Chosen = random.choice(fuel_List)
                case "F2O2 (Perfluorine Peroxide)" | "O3 (Ozone)":
                    fuel_Chosen = "H2 (Hydrogen)"
            output = StndrdDet(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, tank_Repressurisation, altitude_Of_Operation)
        # ============================================================================================
        case "Staged Combustion (Oxidizer Rich)":
            oxidizer_List = ["O2 (Oxygen)", "O3 (Ozone)", "N2O4 (Nitrogen Tetroxide)"]
            oxidizer_Chosen = randomize(oxidizer_List)
            fuel_Chosen = ""
            match oxidizer_Chosen:
                case "O2 (Oxygen)" | "O3 (Ozone)":
                    fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                                 "C6H5NH2 (Aniline)", "NH3 (Ammonia)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                                 "CH3OH (Methanol)"]
                    random.shuffle(fuel_List)
                    fuel_Chosen = random.choice(fuel_List)
                case "N2O4 (Nitrogen Tetroxide)":
                    fuel_List = ["C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)",
                                 "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                                 "C2H8N2 (UnsymmetricalDimethylHydrazine)"]
                    random.shuffle(fuel_List)
                    fuel_Chosen = random.choice(fuel_List)
            output = StndrdDet(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, tank_Repressurisation, altitude_Of_Operation)
        # ============================================================================================
        case "Full Flow Staged Combustion" | "Combustion Tap Off":
            oxidizer_List = ["O2 (Oxygen)", "F2 (Fluorine)", "F2O2 (Perfluorine Peroxide)", "O3 (Ozone)",
                             "N2O4 (Nitrogen Tetroxide)"]
            oxidizer_Chosen = randomize(oxidizer_List)
            fuel_Chosen = ""
            match oxidizer_Chosen:
                case "O2 (Oxygen)":
                    fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                                 "C6H5NH2 (Aniline)", "NH3 (Ammonia)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                                 "CH3OH (Methanol)"]
                    random.shuffle(fuel_List)
                    fuel_Chosen = random.choice(fuel_List)
                case "F2 (Fluorine)":
                    fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                                 "NH3 (Ammonia)", "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)",
                                 "N2H4 (Hydrazine)", "CH3OH (Methanol)"]
                    random.shuffle(fuel_List)
                    fuel_Chosen = random.choice(fuel_List)
                case "F2O2 (Perfluorine Peroxide)" | "O3 (Ozone)":
                    fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                                 "C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                                 "CH6N2 (MonomethylHydrazine)"]
                    random.shuffle(fuel_List)
                    fuel_Chosen = random.choice(fuel_List)
                case "N2O4 (Nitrogen Tetroxide)":
                    fuel_List = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                                 "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                                 "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH3OH (Methanol)"]
                    random.shuffle(fuel_List)
                    fuel_Chosen = random.choice(fuel_List)
            output = StndrdDet(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, tank_Repressurisation,
                               altitude_Of_Operation)
        # ============================================================================================
        case _:
            oxidizer_List = ["O2 (Oxygen)", "F2 (Fluorine)", "F2O2 (Perfluorine Peroxide)", "N2O4 (Nitrogen Tetroxide)",
                             "H2O2 (Hydrogen Peroxide) 95%", "H2O2 (Hydrogen Peroxide) 85%", "O3 (Ozone)",
                             "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)", "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)"]
            oxidizer_Chosen = randomize(oxidizer_List)
            if oxidizer_Chosen == "O2 (Oxygen)":
                fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                             "NH3 (Ammonia)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
                random.shuffle(fuel_List)
                fuel_Chosen = random.choice(fuel_List)
            elif oxidizer_Chosen == "F2 (Fluorine)":
                fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                             "NH3 (Ammonia)", "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)",
                             "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
                random.shuffle(fuel_List)
                fuel_Chosen = random.choice(fuel_List)
            elif oxidizer_Chosen == "F2O2 (Perfluorine Peroxide)" or oxidizer_Chosen == "O3 (Ozone)":
                fuel_List = ["H2 (Hydrogen)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
                random.shuffle(fuel_List)
                fuel_Chosen = random.choice(fuel_List)
            elif oxidizer_Chosen == "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)" or oxidizer_Chosen == "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)":
                fuel_List = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)"]
                random.shuffle(fuel_List)
                fuel_Chosen = random.choice(fuel_List)
            elif oxidizer_Chosen == "N2O4 (Nitrogen Tetroxide)" or oxidizer_Chosen == "H2O2 (Hydrogen Peroxide) 95%" or \
                    oxidizer_Chosen == "H2O2 (Hydrogen Peroxide) 85%":
                fuel_List = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)", "C12H26 (n-Dodecane)",
                             "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)", "CH3OH (Methanol)",
                             "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)"]
                random.shuffle(fuel_List)
                fuel_Chosen = random.choice(fuel_List)
            output = StndrdDet(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, tank_Repressurisation, altitude_Of_Operation)
    return output