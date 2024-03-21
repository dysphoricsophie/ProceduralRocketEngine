import random

def isHypergolic(OCC, FCC):
    if OCC == "N2O4 (Nitrogen Tetroxide)":
        if FCC == "50% CH6N2 + 50% N2H4 (Aerosine-50)" or FCC == "75% CH6N2 + 25% N2H4 (UH-25)" or FCC == "C6H5NH2 (Aniline)" or \
                FCC == "C2H8N2 (UnsymmetricalDimethylHydrazine)" or FCC == "CH6N2 (MonomethylHydrazine)" or FCC == "N2H4 (Hydrazine)":
            isHypergolic = True
    elif OCC == "H2O2 (Hydrogen Peroxide) 95%" or OCC == "H2O2 (Hydrogen Peroxide) 85%" or OCC == "O2 (Oxygen)":
        isHypergolic = False
    elif OCC == "O3 (Ozone)" or OCC == "F2 (Fluorine)" or OCC == "F2 (Fluorine) + O2 (Oxygen)" or \
            OCC == "ClF3 (Chlorine Trifluoride)" or OCC == "ClF5 (Chlorine Pentafluoride)":
        isHypergolic = True
    elif OCC == "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)" or OCC == "AK20I: 80% HNO3 + 20% N2O4 (Nitric Acid)" or \
            OCC == "AK20K: 80% HNO3 + 20% N2O4 (Nitric Acid)" or OCC == "AK27I: 73% HNO3 + 27% N2O4 (Nitric Acid)" or \
            OCC == "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)":
        if FCC == "CH6N2 (MonomethylHydrazine)" or OCC == "N2H4 (Hydrazine)":
            isHypergolic = True
        else:
            isHypergolic = False
    return isHypergolic
def outputDef(ENN, ECC, OCC, FCC, AOOC, NTC, TRR, CMC, isHyp):
    lbrk = "======================================================================================================"
    print(f"{lbrk}\nEngine Designation: {ENN}\n")
    print(f"Flow Cycle: {ECC}")
    print(f"Engine Oxidizer: {OCC}")
    isCryo = False
    if OCC == "O3 (Ozone)" or OCC == "F2 (Fluorine)" or OCC == "F2 (Fluorine) + O2 (Oxygen)" or \
            OCC == "ClF3 (Chlorine Trifluoride)" or OCC == "ClF5 (Chlorine Pentafluoride)" or OCC == "O2 (Oxygen)":
        isCryo = True
    if FCC == "CH3OH (Methanol)" or FCC == "C12H24 (Kerosene)" or FCC == "H2 (Hydrogen)" or FCC == "C2H5OH(Ethanol) 85%" or \
            FCC == "C2H5OH(Ethanol) 75%" or FCC == "B2H6 (Diborane)" or FCC == "B5H9 (Pentaborane)" or FCC == "NH3 (Ammonia)" or FCC == "CH4 (Methane)":
        isCryo = True
    print(f"Engine Fuel: {FCC}")
    if isHyp:
        message = "Propellant properties: Hypergolic"
    else:
        message = "Propellant properties: Not Hypergolic"
    if isCryo is True and isHyp is True:
        message = message + " and cryogenic"
        print(message)
    elif isCryo is True and isHyp is False:
        message = message + " but cryogenic"
        print(message)
    elif isCryo is False and isHyp is True:
        message = message + " but not cryogenic"
        print(message)
    else:
        message = message + " or cryogenic"
        print(message)
    uio96 = random.randint(1, 1000)
    uio97 = random.randint(1, 12)
    if uio96 % uio97 == 0:
        Throttle_MinV = random.randint(1, 100)
        Throttle_MaxV = random.randint(100, 115)
        ThrottleRange = str(Throttle_MinV) + " - " + str(Throttle_MaxV)
    else:
        ThrottleRange = "Not Throttleable"
    gimbalangle = random.randint(0, 15)
    if gimbalangle <= 0 or AOOC == "80 km+ (Vacuum)":
        piss = "None"
    else:
        piss = str(gimbalangle) + " degrees"
    print(f"Altitude Of Operation: {AOOC}")
    print(f"Exhaust Nozzle Geometry: {NTC}")
    print(f"Engine Gimbal Range: {piss}")
    print(f"Tank repressurisation Method: {TRR}")
    print(f"Nozzle Cooling Mechanism: {CMC}")
    print(f"Engine Throttle Range: {ThrottleRange}\n")


cooling_mechanism = ["Ablative Cooling", "Radiative Cooling", "Dump Cooling",
                     "Film Cooling", "Regenerative Cooling", "Transpiration Cooling"]
oxidizer_List = ["O2 (Oxygen)", "F2 (Fluorine)", "F2 (Fluorine) + O2 (Oxygen)", "N2O4 (Nitrogen Tetroxide)",
                 "H2O2 (Hydrogen Peroxide) 95%", "H2O2 (Hydrogen Peroxide) 85%", "O3 (Ozone)",
                 "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)", "AK20I: 80% HNO3 + 20% N2O4 (Nitric Acid)",
                 "AK20K: 80% HNO3 + 20% N2O4 (Nitric Acid)", "AK27I: 73% HNO3 + 27% N2O4 (Nitric Acid)",
                 "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)", "ClF3 (Chlorine Trifluoride)",
                 "ClF5 (Chlorine Pentafluoride)"]
random.choice(oxidizer_List)
oxidizer_Chosen = random.choice(oxidizer_List)
match oxidizer_Chosen:
    case "O2 (Oxygen)":
        fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 85%",
                     "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)", "NH3 (Ammonia)",
                     "CH6N2 (MonomethylHydrazine)",
                     "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H24 (Kerosene)", "B2H6 (Diborane)",
                     "B5H9 (Pentaborane)", "C2H6 (Ethane)"]
        random.shuffle(fuel_List)
        fuel_Chosen = random.choice(fuel_List)
    case "F2 (Fluorine)":
        fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 85%", "C2H5OH(Ethanol) 75%",
                     "C6H5NH2 (Aniline)", "NH3 (Ammonia)", "C2H8N2 (UnsymetricalDimethylHydrazine)",
                     "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)",
                     "C12H24 (Kerosene)", "B2H6 (Diborane)", "B5H9 (Pentaborane)"]
        random.shuffle(fuel_List)
        fuel_Chosen = random.choice(fuel_List)
    case "F2 (Fluorine) + O2 (Oxygen)" | "O3 (Ozone)":
        fuel_List = ["H2 (Hydrogen)", "CH3OH (Methanol)", "C12H24 (Kerosene)", "B2H6 (Diborane)", "B5H9 (Pentaborane)"]
        random.shuffle(fuel_List)
        fuel_Chosen = random.choice(fuel_List)
    case "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)" | "AK20I: 80% HNO3 + 20% N2O4 (Nitric Acid)" | \
         "AK20K: 80% HNO3 + 20% N2O4 (Nitric Acid)" | "AK27I: 73% HNO3 + 27% N2O4 (Nitric Acid)" | \
         "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)" | "ClF3 (Chlorine Trifluoride)" | "ClF5 (Chlorine Pentafluoride)":
        fuel_List = ["C2H5OH(Ethanol) 85%", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)"]
        random.shuffle(fuel_List)
        fuel_Chosen = random.choice(fuel_List)
    case "N2O4 (Nitrogen Tetroxide)" | "H2O2 (Hydrogen Peroxide) 95%" | "H2O2 (Hydrogen Peroxide) 85%":
        fuel_List = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 85%", "C2H5OH(Ethanol) 75%",
                     "C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)",
                     "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                     "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)",
                     "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H24 (Kerosene)"]
        random.shuffle(fuel_List)
        fuel_Chosen = random.choice(fuel_List)
isHyp = isHypergolic(oxidizer_Chosen, fuel_Chosen)
print(isHyp)