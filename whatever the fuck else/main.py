import random

while True:
    engine_Name = ['Olympia',
                   'Destiny',
                   "Valiant",
                   "Obsidian",
                   "Leviathan",
                   "Aurora",
                   "Crusader",
                   "Merlin",
                   "Python",
                   "Hypnos",
                   "Juniper",
                   "Dawn",
                   "Kepler",
                   "Parom",
                   "Elektron",
                   "Aeonian",
                   "Ceres",
                   "Chasovoy",
                   "Copernicus",
                   "Quaoar",
                   "Athena",
                   "Minotaur",
                   "Agena",
                   "Thor",
                   "Vega",
                   "Athena",
                   "Coeus",
                   "Minerva",
                   "Kratos",
                   "Odin"]
    random.shuffle(engine_Name)

    engine_Cycle = ["Gas Generator",
                    "Staged Combustion (Oxidiser Rich)",
                    "Staged Combustion (Fuel Rich)",
                    "Expander (Open)",
                    "Expander (Closed)",
                    "Dual Expander (Open)",
                    "Dual Expander (Closed)",
                    "Pressure-Fed",
                    "Full Flow Staged",
                    "Electric Pump Fed",
                    "Combustion Tap Off",
                    "Monopropellant (Cold Gas)",
                    "Monopropellant (Decomposition)"]

    oxidiser_List1 = ['O2 (Oxygen)',
                      'F2 (Fluorine)',
                      'F2 (Fluorine) + O2 (Oxygen)',
                      'N2O4 (Nitrogen Tetroxide)',
                      'N2H4 (Hydrazine)',
                      'H2O2 (Hydrogen Peroxide) 95%',
                      'H2O2 (Hydrogen Peroxide) 85%',
                      'N2O (Nitrous Oxide)',
                      'O3 (Ozone)',
                      'AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)',
                      'AK20I: 80% HNO3 + 20% N2O4 (Nitric Acid)',
                      'AK20K: 80% HNO3 + 20% N2O4 (Nitric Acid)',
                      'AK27I: 73% HNO3 + 27% N2O4 (Nitric Acid)',
                      'AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)',
                      'OF2 (Oxygen Difluoride)',
                      'N2F4 (Tetrafluorohydrazine)',
                      'ClF3 (Chlorine Trifluoride)',
                      'ClF5 (Chlorine Pentafluoride)']

    fuel_List1 = ['H2 (Hydrogen)',
                  'CH4 (Methane)',
                  'C2H5OH(Ethanol) 85%',
                  'C2H5OH(Ethanol) 75%',
                  'C6H5NH2 (Aniline)',
                  'NH3 (Ammonia)',
                  '75% CH6N2 + 25% N2H4 (UH-25)',
                  '50% CH6N2 + 50% N2H4 (Aerosine-50)',
                  'C2H8N2 (UnsymetricalDimethylHydrazine)',
                  'CH6N2 (MonomethylHydrazine)',
                  'N2H4 (Hydrazine)',
                  'CH3OH (Methanol)',
                  'C12H24 (Kerosene)',
                  'B2H6 (Diborane)',
                  'B5H9 (Pentaborane)',
                  'C2H6 (Ethane)']

    propellant_List1 = ['H2O2 (Hydrogen Peroxide)',
                        'N2H4 (Hydrazine)',
                        'NH2OH+NO3 (Hydroxyl ammonium nitrate)']

    propellant_List2 = ['Nitrogen (N2)',
                        'Helium (He)',
                        'Carbon Dioxide (CO2)',
                        'Ammonia (NH3)',
                        'Hydrogen (H2)',
                        'Methane (CH4)']

    altitude_Of_Operation = ["0-10 km (Sea Level)",
                             "20-30 km (Medium Atmosphere)",
                             "30-80 km (High Atmosphere)",
                             "80 km+ (Vacuum)",
                             "Any Altitude (0-80 km+)"]

    tank_Repressurisation = ['Autogenous',
                             'Inert gas']

    nozzle_Type_List = ["Linear Aerospike",
                        "Toroidal Aerospike",
                        "Converging Diverging Cone (Without Nozzle Extension)",
                        "Converging Diverging Cone (With Nozzle Extension)",
                        "Converging Diverging Bell (With Nozzle Extension)",
                        "Converging Diverging Bell (Without Nozzle Extension)"]

    random.shuffle(engine_Cycle)
    engine_Cycle_Chosen = random.choice(engine_Cycle)
    if 'Monopropellant (Decomposition)' in engine_Cycle_Chosen:
        random.shuffle(propellant_List1)
        propellant_List1_Chosen = random.choice(propellant_List1)
        altitude_Of_Operation_Chosen = '80 km+ (Vacuum)'
        tank_Repressurisation_Chosen = 'Inert Gas'
        random.shuffle(nozzle_Type_List)
        nozzle_Type_List.remove("Linear Aerospike")
        nozzle_Type_List.remove("Toroidal Aerospike")
        nozzle_Type_List.remove("Converging Diverging Cone (With Nozzle Extension)")
        nozzle_Type_List.remove("Converging Diverging Bell (With Nozzle Extension)")
        nozzle_Type_List_Chosen = random.choice(nozzle_Type_List)
        engine_Name_Chosen = random.choice(engine_Name)
        print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
        print(f"Your Engine is called: {engine_Name_Chosen}")
        print(" ")
        print(f"Your Engine Cycle is: {engine_Cycle_Chosen}")
        print(f"Your Propellant is: {propellant_List1_Chosen}")
        print(f"Your Altitude of operation is: {altitude_Of_Operation_Chosen}")
        print(f"Your engine's nozzle type should be : {nozzle_Type_List_Chosen}")
        print(
            f"Tank repressurisation would use an {tank_Repressurisation_Chosen} system, as an Autogenous one would be impossible")
        print("")
        print("Done!")
    elif 'Monopropellant (Cold Gas)' in engine_Cycle_Chosen:
        random.shuffle(propellant_List2)
        propellant_List2_Chosen = random.choice(propellant_List2)
        altitude_Of_Operation_Chosen = '80 km+ (Vacuum)'
        tank_Repressurisation_Chosen = 'Inert Gas'
        random.shuffle(nozzle_Type_List)
        nozzle_Type_List.remove("Linear Aerospike")
        nozzle_Type_List.remove("Toroidal Aerospike")
        nozzle_Type_List.remove("Converging Diverging Cone (With Nozzle Extension)")
        nozzle_Type_List.remove("Converging Diverging Bell (With Nozzle Extension)")
        nozzle_Type_List_Chosen = random.choice(nozzle_Type_List)
        engine_Name_Chosen = random.choice(engine_Name)
        print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
        print(f"Your Engine is called: {engine_Name_Chosen}")
        print(" ")
        print(f"Your Engine Cycle is: {engine_Cycle_Chosen}")
        print(f"Your Propellant is: {propellant_List2_Chosen}")
        print(f"Your Altitude of operation is: {altitude_Of_Operation_Chosen}")
        print(f"Your engine's nozzle type should be : {nozzle_Type_List_Chosen}")
        print(
            f"Tank repressurisation would use an {tank_Repressurisation_Chosen} system, as an Autogenous one would be impossible")
        print("")
        print("Done!")
    elif engine_Cycle_Chosen == 'Expander (Closed)' or engine_Cycle_Chosen == 'Expander (Open)':
        oxidiser_List1.remove('N2O4 (Nitrogen Tetroxide)')
        oxidiser_List1.remove('N2H4 (Hydrazine)')
        oxidiser_List1.remove('H2O2 (Hydrogen Peroxide) 95%')
        oxidiser_List1.remove('H2O2 (Hydrogen Peroxide) 85%')
        oxidiser_List1.remove('N2O (Nitrous Oxide)')
        oxidiser_List1.remove('AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)')
        oxidiser_List1.remove('AK20I: 80% HNO3 + 20% N2O4 (Nitric Acid)')
        oxidiser_List1.remove('AK20K: 80% HNO3 + 20% N2O4 (Nitric Acid)')
        oxidiser_List1.remove('AK27I: 73% HNO3 + 27% N2O4 (Nitric Acid)')
        oxidiser_List1.remove('AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)')
        oxidiser_List1.remove('OF2 (Oxygen Difluoride)')
        oxidiser_List1.remove('N2F4 (Tetrafluorohydrazine)')
        oxidiser_List1.remove('ClF3 (Chlorine Trifluoride)')
        oxidiser_List1.remove('ClF5 (Chlorine Pentafluoride)')
        random.shuffle(oxidiser_List1)
        oxidiser_Chosen = random.choice(oxidiser_List1)
        if 'O2 (Oxygen)' in oxidiser_Chosen:
            fuel_List1.remove('75% CH6N2 + 25% N2H4 (UH-25)')
            fuel_List1.remove('50% CH6N2 + 50% N2H4 (Aerosine-50)')
            fuel_List1.remove('C2H8N2 (UnsymetricalDimethylHydrazine)')
        elif "F2 (Fluorine)" in oxidiser_Chosen:
            fuel_List1.remove('75% CH6N2 + 25% N2H4 (UH-25)')
            fuel_List1.remove('50% CH6N2 + 50% N2H4 (Aerosine-50)')
        elif "F2 (Fluorine) + O2 (Oxygen)" in oxidiser_Chosen or "O3 (Ozone)" in oxidiser_Chosen:
            fuel_List1.remove('CH4 (Methane)')
            fuel_List1.remove('C2H5OH(Ethanol) 85%')
            fuel_List1.remove('C2H5OH(Ethanol) 75%')
            fuel_List1.remove('C6H5NH2 (Aniline)')
            fuel_List1.remove('NH3 (Ammonia)')
            fuel_List1.remove('75% CH6N2 + 25% N2H4 (UH-25)')
            fuel_List1.remove('50% CH6N2 + 50% N2H4 (Aerosine-50)')
            fuel_List1.remove('CH6N2 (MonomethylHydrazine)')
            fuel_List1.remove('N2H4 (Hydrazine)')
        random.shuffle(fuel_List1)
        fuel_Chosen = random.choice(fuel_List1)
        random.shuffle(altitude_Of_Operation)
        altitude_Of_Operation_Chosen = random.choice(altitude_Of_Operation)
        if altitude_Of_Operation_Chosen != "0-10 km (Sea Level)":
            nozzle_Type_List.remove("Converging Diverging Cone (Without Nozzle Extension)")
            nozzle_Type_List.remove("Converging Diverging Bell (Without Nozzle Extension)")
        elif altitude_Of_Operation_Chosen == "Any Altitude of operation":
            nozzle_Type_List.remove("Converging Diverging Cone (With Nozzle Extension)")
            nozzle_Type_List.remove("Converging Diverging Bell (With Nozzle Extension)")
            nozzle_Type_List.remove("Converging Diverging Cone (Without Nozzle Extension)")
            nozzle_Type_List.remove("Converging Diverging Bell (Without Nozzle Extension)")
        random.shuffle(tank_Repressurisation)
        tank_Repressurisation_Chosen = random.choice(tank_Repressurisation)
        random.shuffle(nozzle_Type_List)
        nozzle_Type_List_Chosen = random.choice(nozzle_Type_List)
        engine_Name_Chosen = random.choice(engine_Name)
        print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
        print(f"Your Engine is called: {engine_Name_Chosen}")
        print(" ")
        print(f"Your Engine Cycle is: {engine_Cycle_Chosen}")
        print(f"Your Oxidiser is: {oxidiser_Chosen}")
        print(f"Your Fuel is: {fuel_Chosen}")
        print(f"Your Altitude of operation is: {altitude_Of_Operation_Chosen}")
        print(f"Your engine's nozzle type should be : {nozzle_Type_List_Chosen}")
        print(f"Tank repressurisation would be done through an {tank_Repressurisation_Chosen} repressurisation system")
        print("")
        print("Done!")
    elif engine_Cycle_Chosen == 'Dual Expander (Closed)' or engine_Cycle_Chosen == 'Dual Expander (Open)':
        oxidiser_List1.remove('N2O4 (Nitrogen Tetroxide)')
        oxidiser_List1.remove('N2H4 (Hydrazine)')
        oxidiser_List1.remove('H2O2 (Hydrogen Peroxide) 95%')
        oxidiser_List1.remove('H2O2 (Hydrogen Peroxide) 85%')
        oxidiser_List1.remove('N2O (Nitrous Oxide)')
        oxidiser_List1.remove('AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)')
        oxidiser_List1.remove('AK20I: 80% HNO3 + 20% N2O4 (Nitric Acid)')
        oxidiser_List1.remove('AK20K: 80% HNO3 + 20% N2O4 (Nitric Acid)')
        oxidiser_List1.remove('AK27I: 73% HNO3 + 27% N2O4 (Nitric Acid)')
        oxidiser_List1.remove('AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)')
        oxidiser_List1.remove('OF2 (Oxygen Difluoride)')
        oxidiser_List1.remove('N2F4 (Tetrafluorohydrazine)')
        oxidiser_List1.remove('ClF3 (Chlorine Trifluoride)')
        oxidiser_List1.remove('ClF5 (Chlorine Pentafluoride)')
        random.shuffle(oxidiser_List1)
        oxidiser_Chosen = random.choice(oxidiser_List1)
        if 'O2 (Oxygen)' in oxidiser_Chosen:
            fuel_List1.remove('C2H5OH(Ethanol) 85%')
            fuel_List1.remove('C2H5OH(Ethanol) 75%')
            fuel_List1.remove('C6H5NH2 (Aniline)')
            fuel_List1.remove('NH3 (Ammonia)')
            fuel_List1.remove('75% CH6N2 + 25% N2H4 (UH-25)')
            fuel_List1.remove('50% CH6N2 + 50% N2H4 (Aerosine-50)')
            fuel_List1.remove('C2H8N2 (UnsymetricalDimethylHydrazine)')
            fuel_List1.remove('CH6N2 (MonomethylHydrazine)')
            fuel_List1.remove('N2H4 (Hydrazine)')
            fuel_List1.remove('CH3OH (Methanol)')
            fuel_List1.remove('C12H24 (Kerosene)')
            fuel_List1.remove('B2H6 (Diborane)')
            fuel_List1.remove('B5H9 (Pentaborane)')
            fuel_List1.remove('C2H6 (Ethane)')
        elif "F2 (Fluorine)" in oxidiser_Chosen:
            fuel_List1.remove('C2H5OH(Ethanol) 85%')
            fuel_List1.remove('C2H5OH(Ethanol) 75%')
            fuel_List1.remove('C6H5NH2 (Aniline)')
            fuel_List1.remove('NH3 (Ammonia)')
            fuel_List1.remove('75% CH6N2 + 25% N2H4 (UH-25)')
            fuel_List1.remove('50% CH6N2 + 50% N2H4 (Aerosine-50)')
            fuel_List1.remove('C2H8N2 (UnsymetricalDimethylHydrazine)')
            fuel_List1.remove('CH6N2 (MonomethylHydrazine)')
            fuel_List1.remove('N2H4 (Hydrazine)')
            fuel_List1.remove('CH3OH (Methanol)')
            fuel_List1.remove('C12H24 (Kerosene)')
            fuel_List1.remove('B2H6 (Diborane)')
            fuel_List1.remove('B5H9 (Pentaborane)')
            fuel_List1.remove('C2H6 (Ethane)')
        elif "F2 (Fluorine) + O2 (Oxygen)" in oxidiser_Chosen or "O3 (Ozone)" in oxidiser_Chosen:
            fuel_List1.remove('C2H5OH(Ethanol) 85%')
            fuel_List1.remove('C2H5OH(Ethanol) 75%')
            fuel_List1.remove('C6H5NH2 (Aniline)')
            fuel_List1.remove('NH3 (Ammonia)')
            fuel_List1.remove('75% CH6N2 + 25% N2H4 (UH-25)')
            fuel_List1.remove('50% CH6N2 + 50% N2H4 (Aerosine-50)')
            fuel_List1.remove('C2H8N2 (UnsymetricalDimethylHydrazine)')
            fuel_List1.remove('CH6N2 (MonomethylHydrazine)')
            fuel_List1.remove('N2H4 (Hydrazine)')
            fuel_List1.remove('CH3OH (Methanol)')
            fuel_List1.remove('C12H24 (Kerosene)')
            fuel_List1.remove('B2H6 (Diborane)')
            fuel_List1.remove('B5H9 (Pentaborane)')
            fuel_List1.remove('C2H6 (Ethane)')
        random.shuffle(fuel_List1)
        fuel_Chosen = random.choice(fuel_List1)
        random.shuffle(altitude_Of_Operation)
        altitude_Of_Operation_Chosen = random.choice(altitude_Of_Operation)
        if altitude_Of_Operation_Chosen != "0-10 km (Sea Level)":
            nozzle_Type_List.remove("Converging Diverging Cone (Without Nozzle Extension)")
            nozzle_Type_List.remove("Converging Diverging Bell (Without Nozzle Extension)")
        elif altitude_Of_Operation_Chosen == "Any Altitude of operation":
            nozzle_Type_List.remove("Converging Diverging Cone (With Nozzle Extension)")
            nozzle_Type_List.remove("Converging Diverging Bell (With Nozzle Extension)")
            nozzle_Type_List.remove("Converging Diverging Cone (Without Nozzle Extension)")
            nozzle_Type_List.remove("Converging Diverging Bell (Without Nozzle Extension)")
        random.shuffle(tank_Repressurisation)
        tank_Repressurisation_Chosen = random.choice(tank_Repressurisation)
        random.shuffle(nozzle_Type_List)
        nozzle_Type_List_Chosen = random.choice(nozzle_Type_List)
        engine_Name_Chosen = random.choice(engine_Name)
        print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
        print(f"Your Engine is called: {engine_Name_Chosen}")
        print(" ")
        print(f"Your Engine Cycle is: {engine_Cycle_Chosen}")
        print(f"Your Oxidiser is: {oxidiser_Chosen}")
        print(f"Your Fuel is: {fuel_Chosen}")
        print(f"Your Altitude of operation is: {altitude_Of_Operation_Chosen}")
        print(f"Your engine's nozzle type should be : {nozzle_Type_List_Chosen}")
        print(f"Tank repressurisation would be done through an {tank_Repressurisation_Chosen} repressurisation system")
        print("")
        print("Done!")
    elif engine_Cycle_Chosen == 'Staged Combustion (Fuel Rich)' or engine_Cycle_Chosen == 'Full Flow Staged Combustion' or engine_Cycle_Chosen == 'Combustion Tap Off':
        oxidiser_List1.remove('N2O4 (Nitrogen Tetroxide)')
        oxidiser_List1.remove('H2O2 (Hydrogen Peroxide) 95%')
        oxidiser_List1.remove('H2O2 (Hydrogen Peroxide) 85%')
        oxidiser_List1.remove('N2O (Nitrous Oxide)')
        oxidiser_List1.remove('AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)')
        oxidiser_List1.remove('AK20I: 80% HNO3 + 20% N2O4 (Nitric Acid)')
        oxidiser_List1.remove('AK20K: 80% HNO3 + 20% N2O4 (Nitric Acid)')
        oxidiser_List1.remove('AK27I: 73% HNO3 + 27% N2O4 (Nitric Acid)')
        oxidiser_List1.remove('AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)')
        oxidiser_List1.remove('OF2 (Oxygen Difluoride)')
        oxidiser_List1.remove('N2F4 (Tetrafluorohydrazine)')
        oxidiser_List1.remove('ClF3 (Chlorine Trifluoride)')
        oxidiser_List1.remove('ClF5 (Chlorine Pentafluoride)')
        random.shuffle(oxidiser_List1)
        oxidiser_Chosen = random.choice(oxidiser_List1)
        fuel_List1.remove('CH4 (Methane)')
        fuel_List1.remove('C2H5OH(Ethanol) 85%')
        fuel_List1.remove('C2H5OH(Ethanol) 75%')
        fuel_List1.remove('C6H5NH2 (Aniline)')
        fuel_List1.remove('75% CH6N2 + 25% N2H4 (UH-25)')
        fuel_List1.remove('50% CH6N2 + 50% N2H4 (Aerosine-50)')
        fuel_List1.remove('C2H8N2 (UnsymetricalDimethylHydrazine)')
        fuel_List1.remove('CH6N2 (MonomethylHydrazine)')
        fuel_List1.remove('CH3OH (Methanol)')
        fuel_List1.remove('C12H24 (Kerosene)')
        fuel_List1.remove('C2H6 (Ethane)')
        if 'O2 (Oxygen)' in oxidiser_Chosen:
            fuel_List1.remove('75% CH6N2 + 25% N2H4 (UH-25)')
            fuel_List1.remove('50% CH6N2 + 50% N2H4 (Aerosine-50)')
            fuel_List1.remove('C2H8N2 (UnsymetricalDimethylHydrazine)')
        elif "F2 (Fluorine)" in oxidiser_Chosen:
            fuel_List1.remove('75% CH6N2 + 25% N2H4 (UH-25)')
            fuel_List1.remove('50% CH6N2 + 50% N2H4 (Aerosine-50)')
        elif "F2 (Fluorine) + O2 (Oxygen)" in oxidiser_Chosen or "O3 (Ozone)" in oxidiser_Chosen:
            fuel_List1.remove('CH4 (Methane)')
            fuel_List1.remove('C2H5OH(Ethanol) 85%')
            fuel_List1.remove('C2H5OH(Ethanol) 75%')
            fuel_List1.remove('C6H5NH2 (Aniline)')
            fuel_List1.remove('NH3 (Ammonia)')
            fuel_List1.remove('75% CH6N2 + 25% N2H4 (UH-25)')
            fuel_List1.remove('50% CH6N2 + 50% N2H4 (Aerosine-50)')
            fuel_List1.remove('CH6N2 (MonomethylHydrazine)')
            fuel_List1.remove('N2H4 (Hydrazine)')
        elif 'N2H4' in oxidiser_Chosen:
            fuel_List1.remove('CH4 (Methane)')
            fuel_List1.remove('NH3 (Ammonia)')
            fuel_List1.remove('CH6N2 (MonomethylHydrazine)')
            fuel_List1.remove('N2H4 (Hydrazine)')
            fuel_List1.remove('B5H9 (Pentaborane)')
            fuel_List1.remove('C2H6 (Ethane)')
        random.shuffle(fuel_List1)
        fuel_Chosen = random.choice(fuel_List1)
        random.shuffle(altitude_Of_Operation)
        altitude_Of_Operation_Chosen = random.choice(altitude_Of_Operation)
        if altitude_Of_Operation_Chosen != "0-10 km (Sea Level)":
            nozzle_Type_List.remove("Converging Diverging Cone (Without Nozzle Extension)")
            nozzle_Type_List.remove("Converging Diverging Bell (Without Nozzle Extension)")
        elif altitude_Of_Operation_Chosen == "Any Altitude of operation":
            nozzle_Type_List.remove("Converging Diverging Cone (With Nozzle Extension)")
            nozzle_Type_List.remove("Converging Diverging Bell (With Nozzle Extension)")
            nozzle_Type_List.remove("Converging Diverging Cone (Without Nozzle Extension)")
            nozzle_Type_List.remove("Converging Diverging Bell (Without Nozzle Extension)")
        random.shuffle(tank_Repressurisation)
        tank_Repressurisation_Chosen = random.choice(tank_Repressurisation)
        random.shuffle(nozzle_Type_List)
        nozzle_Type_List_Chosen = random.choice(nozzle_Type_List)
        engine_Name_Chosen = random.choice(engine_Name)
        print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
        print(f"Your Engine is called: {engine_Name_Chosen}")
        print(" ")
        print(f"Your Engine Cycle is: {engine_Cycle_Chosen}")
        print(f"Your Oxidiser is: {oxidiser_Chosen}")
        print(f"Your Fuel is: {fuel_Chosen}")
        print(f"Your Altitude of operation is: {altitude_Of_Operation_Chosen}")
        print(f"Your engine's nozzle type should be : {nozzle_Type_List_Chosen}")
        print(f"Tank repressurisation would be done through an {tank_Repressurisation_Chosen} repressurisation system")
        print("")
        print("Done!")
    else:
        random.shuffle(oxidiser_List1)
        oxidiser_Chosen = random.choice(oxidiser_List1)
        if 'O2 (Oxygen)' in oxidiser_Chosen:
            fuel_List1.remove('75% CH6N2 + 25% N2H4 (UH-25)')
            fuel_List1.remove('50% CH6N2 + 50% N2H4 (Aerosine-50)')
            fuel_List1.remove('C2H8N2 (UnsymetricalDimethylHydrazine)')
        elif "F2 (Fluorine)" in oxidiser_Chosen:
            fuel_List1.remove('75% CH6N2 + 25% N2H4 (UH-25)')
            fuel_List1.remove('50% CH6N2 + 50% N2H4 (Aerosine-50)')
        elif "F2 (Fluorine) + O2 (Oxygen)" in oxidiser_Chosen or "O3 (Ozone)" in oxidiser_Chosen:
            fuel_List1.remove('CH4 (Methane)')
            fuel_List1.remove('C2H5OH(Ethanol) 85%')
            fuel_List1.remove('C2H5OH(Ethanol) 75%')
            fuel_List1.remove('C6H5NH2 (Aniline)')
            fuel_List1.remove('NH3 (Ammonia)')
            fuel_List1.remove('75% CH6N2 + 25% N2H4 (UH-25)')
            fuel_List1.remove('50% CH6N2 + 50% N2H4 (Aerosine-50)')
            fuel_List1.remove('CH6N2 (MonomethylHydrazine)')
            fuel_List1.remove('N2H4 (Hydrazine)')
        elif 'AK2' in oxidiser_Chosen or 'ClF' in oxidiser_Chosen:
            fuel_List1.remove('H2 (Hydrogen)')
            fuel_List1.remove('CH4 (Methane)')
            fuel_List1.remove('C2H5OH(Ethanol) 75%')
            fuel_List1.remove('C6H5NH2 (Aniline)')
            fuel_List1.remove('NH3 (Ammonia)')
            fuel_List1.remove('75% CH6N2 + 25% N2H4 (UH-25)')
            fuel_List1.remove('50% CH6N2 + 50% N2H4 (Aerosine-50)')
            fuel_List1.remove('C2H8N2 (UnsymetricalDimethylHydrazine)')
            fuel_List1.remove('C12H24 (Kerosene)')
            fuel_List1.remove('B2H6 (Diborane)')
            fuel_List1.remove('B5H9 (Pentaborane)')
            fuel_List1.remove('C2H6 (Ethane)')
        elif 'N2H4' in oxidiser_Chosen:
            fuel_List1.remove('CH4 (Methane)')
            fuel_List1.remove('NH3 (Ammonia)')
            fuel_List1.remove('CH6N2 (MonomethylHydrazine)')
            fuel_List1.remove('N2H4 (Hydrazine)')
            fuel_List1.remove('B5H9 (Pentaborane)')
            fuel_List1.remove('C2H6 (Ethane)')
        elif 'N2O4' in oxidiser_Chosen or 'H2O2' in oxidiser_Chosen:
            fuel_List1.remove('H2 (Hydrogen)')
            fuel_List1.remove('CH4 (Methane)')
            fuel_List1.remove('C2H5OH(Ethanol) 85%')
            fuel_List1.remove('C2H5OH(Ethanol) 75%')
            fuel_List1.remove('C6H5NH2 (Aniline)')
            fuel_List1.remove('NH3 (Ammonia)')
            fuel_List1.remove('75% CH6N2 + 25% N2H4 (UH-25)')
            fuel_List1.remove('50% CH6N2 + 50% N2H4 (Aerosine-50)')
            fuel_List1.remove('CH3OH (Methanol)')
            fuel_List1.remove('C12H24 (Kerosene)')
            fuel_List1.remove('B2H6 (Diborane)')
            fuel_List1.remove('C2H6 (Ethane)')
        elif 'N2H4' in oxidiser_Chosen:
            fuel_List1.remove('H2 (Hydrogen)')
            fuel_List1.remove('CH4 (Methane)')
            fuel_List1.remove('C2H5OH(Ethanol) 85%')
            fuel_List1.remove('C2H5OH(Ethanol) 75%')
            fuel_List1.remove('C6H5NH2 (Aniline)')
            fuel_List1.remove('NH3 (Ammonia)')
            fuel_List1.remove('75% CH6N2 + 25% N2H4 (UH-25)')
            fuel_List1.remove('50% CH6N2 + 50% N2H4 (Aerosine-50)')
            fuel_List1.remove('C2H8N2 (UnsymetricalDimethylHydrazine)')
            fuel_List1.remove('CH6N2 (MonomethylHydrazine)')
            fuel_List1.remove('N2H4 (Hydrazine)')
            fuel_List1.remove('CH3OH (Methanol)')
            fuel_List1.remove('C12H24 (Kerosene)')
            fuel_List1.remove('C2H6 (Ethane)')
        random.shuffle(fuel_List1)
        fuel_Chosen = random.choice(fuel_List1)
        random.shuffle(altitude_Of_Operation)
        altitude_Of_Operation_Chosen = random.choice(altitude_Of_Operation)
        if altitude_Of_Operation_Chosen != "0-10 km (Sea Level)":
            nozzle_Type_List.remove("Converging Diverging Cone (Without Nozzle Extension)")
            nozzle_Type_List.remove("Converging Diverging Bell (Without Nozzle Extension)")
        elif altitude_Of_Operation_Chosen == "Any Altitude of operation":
            nozzle_Type_List.remove("Converging Diverging Cone (With Nozzle Extension)")
            nozzle_Type_List.remove("Converging Diverging Bell (With Nozzle Extension)")
            nozzle_Type_List.remove("Converging Diverging Cone (Without Nozzle Extension)")
            nozzle_Type_List.remove("Converging Diverging Bell (Without Nozzle Extension)")
        random.shuffle(tank_Repressurisation)
        tank_Repressurisation_Chosen = random.choice(tank_Repressurisation)
        random.shuffle(nozzle_Type_List)
        nozzle_Type_List_Chosen = random.choice(nozzle_Type_List)
        engine_Name_Chosen = random.choice(engine_Name)
        print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
        print(f"Your Engine is called: {engine_Name_Chosen}")
        print(" ")
        print(f"Your Engine Cycle is: {engine_Cycle_Chosen}")
        print(f"Your Oxidiser is: {oxidiser_Chosen}")
        print(f"Your Fuel is: {fuel_Chosen}")
        print(f"Your Altitude of operation is: {altitude_Of_Operation_Chosen}")
        print(f"Your engine's nozzle type should be : {nozzle_Type_List_Chosen}")
        print(f"Tank repressurisation would be done through an {tank_Repressurisation_Chosen} repressurisation system")
        print("")
        print("Done!")
    print(" ")
    print(" ")
    print("Do you wanna make another engine? [Y/N]")
    repeatCommand = str(input(">")).upper()
    if repeatCommand == "n":
        break
