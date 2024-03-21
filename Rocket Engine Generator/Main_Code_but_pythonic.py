import math
import random
import string
from time import time
#import docx

start = count()
def bussy(altitude_Of_Operation_Chosen):
    match (altitude_Of_Operation_Chosen):
        case "0-10 km (Sea Level)":
            nozzle_Type_List_SL = ["De Laval Cone (Without Nozzle Extension)", "De Laval Bell (Without Nozzle Extension)"]
            random.shuffle(nozzle_Type_List_SL)
            nozzle_Type_Chosen = random.choice(nozzle_Type_List_SL)
        case "20-30 km (Medium Atmosphere)":
            nozzle_Type_List_HA = ["De Laval Bell (Without Nozzle Extension)", "De Laval Cone (With Nozzle Extension)",
                "De Laval Bell (With Nozzle Extension)", "Dual Bell Nozzle"]
            random.shuffle(nozzle_Type_List_HA)
            nozzle_Type_Chosen = random.choice(nozzle_Type_List_HA)
        case "30-80 km (High Atmosphere)":
            nozzle_Type_List_HAi = ["De Laval Cone (With Nozzle Extension)", "De Laval Bell (With Nozzle Extension)",
                "Dual Bell Nozzle"]
            random.shuffle(nozzle_Type_List_HAi)
            nozzle_Type_Chosen = random.choice(nozzle_Type_List_HAi)
        case "80 km+ (Vacuum)":
            nozzle_Type_List_VA = ["De Laval Cone (With Nozzle Extension)", "De Laval Bell (With Nozzle Extension)",
                "Expanding Nozzle"]
            random.shuffle(nozzle_Type_List_VA)
            nozzle_Type_Chosen = random.choice(nozzle_Type_List_VA)
        case "Any Altitude (0-80 km+)":
            nozzle_Type_List_Aero = ["Linear Aerospike Nozzle", "Toroidal Aerospike Nozzle", "Expansion-Deflection Nozzle"]
            random.shuffle(nozzle_Type_List_Aero)
            nozzle_Type_Chosen = random.choice(nozzle_Type_List_Aero)
    return nozzle_Type_Chosen

def assCrack(engineName, firstP):
    random.shuffle(engineName)
    random.shuffle(firstP)
    engNameFinalf = " " + random.choice(engineName)
    firstPart_f = random.choice(firstP) + "-"
    finalNumber = random.randint(12, 1110)
    if finalNumber % 8 == 0:
        engine_Name = str(firstPart_f) + str(finalNumber) + str(engNameFinalf)
    else:
        uio93 = random.randint(1, 1000)
        uio94 = random.randint(1, 12)
        if uio93 % uio94 == 0:
            randomizedCharacter = random.choice(string.ascii_lowercase)
            while (randomizedCharacter == 'l') or (randomizedCharacter == 'o') or (randomizedCharacter == 'i') or \
                    (randomizedCharacter == 'q') or (randomizedCharacter == 'e') or (randomizedCharacter == 'h') or \
                    (randomizedCharacter == 'g') or (randomizedCharacter == 'c') or (randomizedCharacter == 'j'):
                randomizedCharacter = random.choice(string.ascii_lowercase)
                if (randomizedCharacter != 'l') and (randomizedCharacter != 'o') and (randomizedCharacter != 'i') and \
                        (randomizedCharacter != 'q') and (randomizedCharacter != 'e') and (randomizedCharacter != 'h') \
                        and (randomizedCharacter != 'g') and (randomizedCharacter != 'c') and (
                        randomizedCharacter != 'j'):
                    break
        else:
            randomizedCharacter = random.choice(string.ascii_uppercase)
            while (randomizedCharacter == 'O') or (randomizedCharacter == 'I') or (randomizedCharacter == 'Q'):
                randomizedCharacter = random.choice(string.ascii_uppercase)
                if (randomizedCharacter != 'O') and (randomizedCharacter != 'I') and (randomizedCharacter != 'Q'):
                    break
        engine_Name = str(firstPart_f) + str(finalNumber) + str(randomizedCharacter) + str(engNameFinalf)
    return engine_Name

def outputMonod(ENN, AOOC, PLC, NTLC, CMC, CCC):
    lbrk = "======================================================================================================"
    print(f"{lbrk}\nEngine Designation: {ENN}\n")
    print(f"Propellant: {PLC}")
    print(f"Altitude Of Operation: {AOOC}")
    print(f"Exhaust Nozzle Geometry: {NTLC}")
    print(f"Nozzle Cooling Mechanism: {CMC}")
    print(f"Propellant catalyst: {CCC}\n")

def outputMono(ENN, ECC, AOOC, PLC, NTLC, CMC):
    lbrk = "======================================================================================================"
    print(f"{lbrk}\nEngine Designation: {ENN}\n")
    print(f"Flow Cycle: {ECC}")
    print(f"Propellant: {PLC}")
    print(f"Altitude Of Operation: {AOOC}")
    print(f"Exhaust Nozzle Geometry: {NTLC}")
    print(f"Nozzle Cooling Mechanism: {CMC}\n")

def outputEx(ENN, ECC, OCC, FCC, AOOC, NTC, TRR, CMC, isHyp):
    lbrk = "========================================================================================================"
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

def outputNt(ENN, ECC, AOOC, NCC, PLC, RFC, NTLC, TRC, CMC, bi):
    lbrk = "========================================================================================================"
    print(f"{lbrk}\nEngine Designation: {ENN}\n")
    print(f"Flow Cycle: {NCC} + {ECC}")
    print(f"Propellant (Remass): {PLC}")
    print(f"Reactor Fuel: {RFC}")
    print(f"Engine Bi-modality: {bi}")
    print(f"Altitude Of Operation: {AOOC}")
    print(f"Exhaust Nozzle Geometry: {NTLC}")
    print(f"Tank repressurisation Method: {TRC}")
    print(f"Nozzle Cooling Mechanism: {CMC}\n")

def outputEt(ENN, ECC, AOOC, PLC, NTLC, PGLC):
    lbrk = "======================================================================================================"
    print(f"{lbrk}\nEngine Designation: {ENN}\n")
    print(f"Flow Cycle: {ECC}")
    print(f"Propellant(Remass): {PLC}")
    print(f"Altitude Of Operation: {AOOC}")
    print(f"Exhaust Nozzle Geometry: {NTLC}")
    print(f"Engine Power Source: {PGLC}")
    pwr = str(random.randint(20, 1000)) + " kW"
    print(f"Rated Power Level: {pwr}\n")

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

def isHypergolic(OCC, FCC):
    isHyper = False
    if OCC == "N2O4 (Nitrogen Tetroxide)":
        if FCC == "50% CH6N2 + 50% N2H4 (Aerosine-50)" or FCC == "75% CH6N2 + 25% N2H4 (UH-25)" or FCC == "C6H5NH2 (Aniline)" or \
                FCC == "C2H8N2 (UnsymmetricalDimethylHydrazine)" or FCC == "CH6N2 (MonomethylHydrazine)" or FCC == "N2H4 (Hydrazine)":
            isHyper = True
    elif OCC == "H2O2 (Hydrogen Peroxide) 95%" or OCC == "H2O2 (Hydrogen Peroxide) 85%" or OCC == "O2 (Oxygen)":
        isHyper = False
    elif OCC == "O3 (Ozone)" or OCC == "F2 (Fluorine)" or OCC == "F2 (Fluorine) + O2 (Oxygen)" or \
            OCC == "ClF3 (Chlorine Trifluoride)" or OCC == "ClF5 (Chlorine Pentafluoride)":
        isHyper = True
    elif OCC == "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)" or OCC == "AK20I: 80% HNO3 + 20% N2O4 (Nitric Acid)" or \
            OCC == "AK20K: 80% HNO3 + 20% N2O4 (Nitric Acid)" or OCC == "AK27I: 73% HNO3 + 27% N2O4 (Nitric Acid)" or \
            OCC == "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)":
        if FCC == "CH6N2 (MonomethylHydrazine)" or OCC == "N2H4 (Hydrazine)":
            isHyper = True
        else:
            isHyper = False
    return isHyper

yi = []
print("Welcome to the Advanced Rocket Engine Generator!")
repeatCommand = ""
while repeatCommand != "N":
    print("Do you want to generate a new engine? [Y/N]")
    repeatCommand = str(input(">")).upper()
    if repeatCommand == "N" or repeatCommand == "NO":
        for u in range(yi.length):
            total = (total + yi[u])
        end = count()
        timen = (end - start) / 1000
        if timen < 60:
            print("Total run count: $timen secs")
        elif timen / 60 < 2:
            print("Total run count: " + math.floor(timen / 60) + " min " + timen % 60 + " secs")
        else:
            print("Total run count: " + math.floor(timen / 60) + " mins " + timen % 60 + " secs")
        exit(0)
    elif repeatCommand == "Y" or repeatCommand == "YES":
        engine_Name1 = ["\"Argosy\"", "\"Galileo\"", "\"Callisto\"", "\"Nauka\"", "\"Insider\"", "\"Granis\"", "\"Rassvet\"",
                        "\"Zvezda\"", "\"Zarya\"", "\"Orion\"", "\"Ares\"", "\"Delta\"", "\"Atlas\"", "\"Dreadnought\"",
                        "\"Daedalus\"", "\"Baltia\"", "\"Dizhou\"", "\"Hermes\"", "\"Icarus\"", "\"Connestoga\"", "\"Yupiter\"",
                        "\"Emphasis\"", "\"Olympus\"", "\"Kronos\"", "\"Helios\"", "\"Alabaster\"", "\"Falcon\"", "\"Saturn\"",
                        "\"Eagle\"", "\"Endeavour\"", "\"Atlantis\"", "\"Cygnus\"", "\"Apollo\"", "\"Horizon\"", "\"Bulava\"",
                        "\"Pioneer\"", "\"Voyager\"", "\"Exploration\"", "\"Expedition\"", "\"Vulcan\"", "\"Vysota\"",
                        "\"Federation\"", "\"Sojourner\"", "\"Nautilus\"", "\"Jubilance\"", "\"Lagrange\"", "\"Volna\"",
                        "\"Prometheus\"", "\"Tellus\"", "\"Alpha\"", "\"Delta\"", "\"Proton\"", "\"Neutron\"", "\"Topol\"",
                        "\"Electron\"", "\"Pluton\"", "\"Poodle\"", "\"Skipper\"", "\"Convair\"", "\"Nexus\"", "\"Oko\"",
                        "\"Vector\"", "\"Terrier\"", "\"Rhino\"", "\"Panther\"", "\"Goliath\"", "\"Juno\"", "\"Shrimp\"",
                        "\"Thumper\"", "\"Mainsail\"", "\"Dart\"", "\"Twitch\"", "\"Stratus\"", "\"Oscar\"", "\"Kosmos\"",
                        "\"Sentinel\"", "\"Pegasus\"", "\"Kelus\"", "\"Starshot\"", "\"Vernor\"", "\"Mammoth\"", "\"Liberty\"",
                        "\"Douglas\"", "\"Heimdall\"", "\"Dynetics\"", "\"Pathfinder\"", "\"Horizon\"", "\"Poisk\"", "\"Pirs\"",
                        "\"Philae\"", "\"Mariner\"", "\"Centaur\"", "\"Orel\"", "\"Pratt\"", "\"Hyperion\"", "\"Sagittarius\"",
                        "\"Apollo\"", "\"Bryton\"", "\"Volga\"", "\"Harmony\"", "\"Cassini\"", "\"Contour\"", "\"Altair\"",
                        "\"Dream\"", "\"Baikal\"", "\"Zenith\"", "\"Urpinod\"", "\"Bernal\"", "\"Condor\"", "\"Athena\"",
                        "\"Astra\"", "\"Aerolus\"", "\"Rombus\"", "\"Lunokhod\"", "\"Fregat\"", "\"Glonass\"", "\"Dragon\"",
                        "\"Salyut\"", "\"Starliner\"", "\"Skylab\"", "\"Briz\"", "\"Colombus\"", "\"Rosetta\"", "\"Redstone\"",
                        "\"Antares\"", "\"Philae\"", "\"Prospero\"", "\"Leonardo\"", "\"Parker\"", "\"Dyson\"", "\"Oberon\"",
                        "\"DragonFly\"", "\"Energia\"", "\"Buran\"", "\"Urgan\"", "\"Angara\"", "\"Vostok\"", "\"Voskhod\"",
                        "\"Shenzhou\"", "\"Ingenuity\"", "\"Oberon\"", "\"Discovery\"", "\"Horizon\"", "\"Visionalis\"",
                        "\"Cerasus\"", "\"Progress\"", "\"Unity\"", "\"Surveyor\"", "\"Prospector\"", "\"Ikar\"", "\"Redstone\"",
                        "\"Lapis\"", "\"Caesius\"", "\"Iridium\"", "\"Daedlus\"", "\"Aelita\"", "\"Beta\"", "\"Gamma\"",
                        "\"Alpha\"", "\"Epsilon\"", "\"Omega\"", "\"Discoverer\"", "\"Explorer\"", "\"Hornet\"", "\"Serenity\"",
                        "\"Ariane\"", "\"Hornet\"", "\"Asimov\"", "\"Pegasus\"", "\"Venture\"", "\"Antares\"", "\"Star\"",
                        "\"Archimedes\"", "\"Hera\"", "\"Iris\"", "\"Titan\"", "\"Artemis\"", "\"Phoenix\"", "\"Ross\"", 
                        "\"Sarychev\"", "\"Nemesis\"", "\"Heimdall\"", "\"Sturt\"", "\"Odin\"", "\"Aethelred\"", "\"Vesper\"",
                        "\"Aces\"", "\"Argon\"", "\"Olympia\"", "\"Perseus\"", "\"Chyron\"", "\"Proxima\"", "\"Arminus\"",
                        "\"Destiny\"", "\"Valient\"", "\"FireFly\"", "\"Obsidian\"", "\"Leviathan\"", "\"Magellan\"", "\"Voyager\"",
                        "\"Mariner\"", "\"Joist\"", "\"Crimson\"", "\"Fortune\"", "\"Vanguard\"", "\"Aurora\"", "\"Ulysses\"",
                        "\"Crusader\"", "\"Python\"", "\"Kuiper\"", "\"Insurgent\"", "\"Pathfinder\"", "\"Kvant\"", "\"Spektr\"",
                        "\"Cassini\"", "\"Zemlya\"", "\"Dawn\"", "\"Kepler\"", "\"Parom\"", "\"Elektron\"", "\"Aeonian\"", "\"Node\"",
                        "\"Burya\"", "\"Voyager\"", "\"Ceres\"", "\"Bayern\"", "\"Chasovoy\"", "\"Copernicus\"", "\"Quaoar\"",
                        "\"Minotaur\"", "\"Agena\"", "\"Thor\"", "\"Vega\"", "\"Scout\"", "\"Coeus\"", "\"Minerva\"", "\"Kratos\"",
                        "\"Neith\"", "\"Omoikane\"", "\"Gayamun\"", "\"Odin\"", "\"Kronos\"", "\"Hope\"", "\"Polet\"", "\"Polyot\"",
                        "\"Sputnik\"", "\"Clementine\"", "\"Sojourner\"", "\"Ingenuity\"", "\"Perseverence\"", "\"Onatchesko\"",
                        "\"Atlantis\"", "\"Tsyklon\"", "\"Zenit\"", "\"Almaz\"", "\"Soyuz\"", "\"Molniya\"", "\"Oreol\"",
                        "\"Yantar\"", "\"Foton\"", "\"Meteor\"", "\"Ekran\"", "\"Strela\"", "\"Bion\"", "\"Piroda\"", "\"Salyut\"",
                        "\"Strela\"", "\"Luch\"", "\"Potok\"", "\"Prognoz\"", "\"Orlets\"", "\"Etalon\"", "\"Astron\"", "\"Efir\"",
                        "\"Kometa\"", "\"Fram\"", "\"Zemlya\"", "\"Gorizont\"", "\"Arkon\"", "\"Gamma\"", "\"Ekspress\"",
                        "\"Gonets\"", "\"Taifun\"", "\"Okean\"", "\"Reflektor\"", "\"Kolibr\"", "\"Sever\"", "\"Comet\"", 
                        "\"Roton\"", "\"Solaris\"", "\"Altaris\"", "\"Ithacus\"", "\"Dekto\"", "\"Dream\"", "\"Impuls\"",
                        "\"Vremya\"", "\"Portal\"", "\"Zodiak\"", "\"Slava\"", "\"Inertsiya\"", "\"Stimuls\"", "\"Ambross\"",
                        "\"Amal\"", "\"Thea\"", "\"Orphelia\"", "\"Polyot\"", "\"Mudrost\"", "\"Carrack\"", "\"Artak\"", 
                        "\"Questar\"", "\"Artyom\"", "\"Tsyclon\"", "\"Ascension\"", "\"Tenacity\"", "\"Contour\"", "\"Zephyr\"",
                        "\"Atlanta\"", "\"Polaris\"", "\"Aeolus\"", "\"Mayak\"", "\"Pamir\"", "\"Taimyr\"", "\"Cheget\"",
                        "\"Sirius\"", "\"Uragan\"", "\"Agat\"", "\"Skiph\"", "\"Kristall\"", "\"Altair\"", "\"Uran\"",
                        "\"Ingul\"", "\"Carat\"", "\"Pulsar\"", "\"Titan\"", "\"Eridanus\"", "\"Parus\"", "\"Cepheus\"",
                        "\"Varagian\"", "\"Olympus\"", "\"Tarkhaniy\"", "\"Astraeus\"", "\"Antares\"", "\"Kazbek\"",
                        "\"Burlak\"", "\"Borei\"", "\"Favor\"", "\"Rubin\"", "\"Almaz\"", "\"Granit\"", "\"Ruby\"", 
                        "\"Sokol\"", "\"Argon\"", "\"Kavkaz\"", "\"Ural\"", "\"Berkut\"", "\"Dunay\"", "\"Yastreb\"",
                        "\"Terek\"", "\"Radon\"", "\"Taymyr\"", "\"Pamir\"", "\"Photon\"", "\"Elbrus\"", "\"Isayiev\"", "\"Shmel\"",
                        "\"Kobra\"", "\"Shturn\"", "\"Metis\"", "\"Malyutka\"", "\"Fleyta\"", "\"Konkurs\"", "\"Bastion\"", "\"Svir\"",
                        "\"Ataka\"", "\"Vodopad\"", "\"Veter\"", "\"Vyuga\"", "\"Vulga\"", "\"Tochka\"", "\"Oka\"", "\"Dvina\"",
                        "\"Almaz\"", "\"Araks\"", "\"Kanopus\"", "\"Kliper\"", "\"Kobalt\"", "\"Siluet\"", "\"Kondor\"",
                        "\"Lotos\"", "\"Luch\"", "\"Mir\"", "\"Neman\"", "\"Obzor\"", "\"Okean\"", "\"Oktan\"", "\"Orlets\"",
                        "\"Poisk\"", "\"Potok\"", "\"Pirs\"", "\"Prognoz\"", "\"Resurs\"", "\"Rodnik\"", "\"Romb\"", "\"Kapustin\"",
                        "\"Oplot\"", "\"Tsygan\"", "\"Teplokhod\"", "\"Sokosha\"", "\"Rubezh\"", "\"Zircon\"", "\"Moskva\"",
                        "\"Tryol\"", "\"Ustinov\"", "\"Belyayev\"", "\"Novorod\"", "\"Argos\"", "\"Nerthus\"", "\"Janus\"",
                        "\"Hephaestus\"", "\"Themis\"", "\"Chronos\"", "\"Tethys\"", "\"Minos\"", "\"Autumn\"", "\"Resilience\"",
                        "\"Aelita\"", "\"Rheus\"", "\"Solntspek\"", "\"Spitzer\"", "\"Cartago\"", "\"Melibea\"", "\"Spartacus\"",
                        "\"Pulsar\"", "\"Fusion\"", "\"Reliant\"", "\"Thunder\"", "\"Novo\"", "\"Panthera\"", "\"Nematoda\"",
                        "\"Anelida\"", "\"Chordata\"", "\"Tetrapoda\"", "\"Cyclero\"", "\"Carrier\"", "\"Gaia\"", "\"Irtysh\"",
                        "\"Wyvern\"", "\"Tarsier\"", "\"Alpina\"", "\"Espadon\"", "\"Parlos\"", "\"Nebula\"", "\"Lazarus\"",
                        "\"Rufus\"", "\"Dornier\"", "\"Argus\"", "\"Kybau\"", "\"Kalau\"", "\"Chasvoy\"", "\"Zephyr\"", "\"Temny\"",
                        "\"Gorizont\"", "\"Yars\"", "\"Krugazor\"", "\"Soprotivlenye\"", "\"Shtil\"", "\"Layner\""]
        engine_Cycle = ["Gas Generator", "Staged Combustion (Oxidizer Rich)", "Staged Combustion (Fuel Rich)",
                        "Expander (Open/Bleed)", "Expander (Closed)", "Dual Expander (Open/Bleed)", "Dual Expander (Closed)",
                        "Pressure-Fed", "Full Flow Staged", "Electric Pump Fed", "Combustion Tap Off", "Monopropellant (Cold Gas)",
                        "Monopropellant (Decomposition)", "Gas Core", "Liquid Core", "Solid Core", "Pulsed Nuclear",
                        "Pebble-Bed Core", "Nuclear SaltWater", "MagnetoPlasmaDynamic Thruster", "Hall Effect Thruster",
                        "Gridded Ion Thruster", "Colloid Thruster", "Variable Specific Impulse Magnetoplasma Rocket (VASIMR)"]
        propellant_List1 = ["H2O2 (Hydrogen Peroxide)", "N2H4 (Hydrazine)", "NH2OH+NO3 (Hydroxylammonium nitrate)",
                            "65% NH4N(NO2)2 (Ammonium Dinitramide) + 35% CH3OH(Methanol)"]
        propellant_List2 = ["Nitrogen (N2)", "Helium (He)", "Carbon Dioxide (CO2)", "Ammonia (NH3)",
                            "Hydrogen (H2)", "Methane (CH4)"]
        propellant_List3 = ["Hydrogen (H2)", "Helium (He)", "Nitrogen (N2)", "Hydrogen (H)", "Ammonia (NH3)",
                            "Water (H2O)", "Oxygen (O2)", "Carbon Dioxide (CO2)", "Carbon Monoxide (CO)",
                            "Methane (CH4)"]
        altitude_Of_Operation = ["0-10 km (Sea Level)", "20-30 km (Medium Atmosphere)", "30-80 km (High Atmosphere)",
                                 "80 km+ (Vacuum)", "Any Altitude (0-80 km+)"]
        tank_Repressurisation = ["Autogenous", "Inert Gas"]
        firstPart = ["RD", "RS", "AJ", "XLR", "NK", "RL", "KDTU", "AR", "BE", "MV", "YF", "PKA", "J", "RSA", "MJ", "XS",
                     "LM10", "HM", "LE", "LRE", "CE", "DST", "DOK", "KDU", "KRD", "R", "RO", "LMS", "LMP", "RT", "F", "E",
                     "A", "B", "S.10", "R", "JDK", "SPP", "TYS", "SOK", "RES", "FWR", "NAA75", "LR", "MA", "GE", "OSA",
                     "OBA", "NA", "RM02", "RM", "H", "MBB", "MB", "DF", "DE", "BF", "X", "BW", "BADR", "HS", "DC"]
        engine_Name = assCrack(engine_Name1, firstPart)
        random.shuffle(engine_Cycle)
        engine_Cycle_Chosen = random.choice(engine_Cycle)
        match engine_Cycle_Chosen:
            case "Gas Core" | "Liquid Core" | "Solid Core" | "Pulsed Nuclear" | "Nuclear SaltWater" | "Pebble-Bed Core":
                cooling_mechanism = ["Radiative Cooling", "Dump Cooling", "Film Cooling", "Regenerative Cooling", "Transpiration Cooling"]
                match engine_Cycle_Chosen:
                    case "Gas Core":
                        remass_List = ["Hydrogen (H2)", "Nitrogen (N2)", "Monoatomic Hydrogen (H)", "Ammonia (NH3)",
                                       "Water (H2O)", "Oxygen (O2)", "Carbon Dioxide (CO2)", "Carbon Monoxide (CO)", "Methane (CH4)"]
                        random.shuffle(remass_List)
                        remass_List_Chosen = random.choice(remass_List)
                        propellant_List_Chosen = "Uranium HexaFluoride Salt (UF6) and $remass_List_Chosen as remass"
                        nuclear_cycle1 = ["\"Expander Bleed\"", "\"Expander Closed\"", "\"Nuclear Lightbulb\"",
                                          "\"Vortex Confined\"", "\"Wheel Flow\"", "\"Magnetohydrodynamic(MHD) vortex\"",
                                          "\"Expander Open\""]
                        random.shuffle(nuclear_cycle1)
                        nuclear_Cycle_Chosen = random.choice(nuclear_cycle1)
                        reactor_fuel = ["100-90% Uranium-235", "50% Uranium-235", "25-8% Uranium-235", "1-2% Uranium-235"]
                        random.shuffle(reactor_fuel)
                        reactor_Fuel_Chosen = random.choice(reactor_fuel)
                        nozzle_Type_List_Chosen = "De Laval Bell (With Nozzle Extension)"

                    case "Liquid Core", "Colloid-Core", "Pebble-Bed Core":
                        remass_List2 = ["Hydrogen (H2)", "Nitrogen (N2)", "Monoatomic Hydrogen (H)",
                                        "Ammonia (NH3)", "Water (H2O)", "Oxygen (O2)", "Carbon Dioxide (CO2)",
                                        "Carbon Monoxide (CO)",
                                        "Methane (CH4)"]
                        random.shuffle(remass_List2)
                        remass_List_Chosen = random.choice(remass_List2)
                        propellant_List_Chosen = "Uranium HexaFluoride Salt (UF6) and " + remass_List_Chosen + " as a remass"
                        nuclear_cycle1 = ["\"Expander Bleed\"", "\"Expander Closed\"", "\"Vortex Confined\"",
                                          "\"Expander Open\""]
                        random.shuffle(nuclear_cycle1)
                        nuclear_Cycle_Chosen = random.choice(nuclear_cycle1)
                        reactor_fuel = ["100-90% Uranium-235", "50% Uranium-235", "25-8% Uranium-235", "1-2% Uranium-235"]
                        random.shuffle(reactor_fuel)
                        reactor_Fuel_Chosen = random.choice(reactor_fuel)
                        nozzle_Type_List_Chosen = "De Laval Bell (With Nozzle Extension)"

                    case "Nuclear SaltWater":
                        propellant_List_Chosen = "Uranium TetraBromide (UBr4) + Water (H2O)"
                        reactor_fuel = ["100-90% Uranium-235", "50% Uranium-235", "25-8% Uranium-235",
                                        "1-2% Uranium-235"]
                        random.shuffle(reactor_fuel)
                        reactor_Fuel_Chosen = random.choice(reactor_fuel)
                        nozzle_Type_List_Chosen = "De Laval Bell (With Nozzle Extension)"

                    case _:
                        random.shuffle(propellant_List3)
                        propellant_List_Chosen = random.choice(propellant_List3)
                        nuclear_cycle1 = ["\"Expander Bleed\"", "\"Expander Closed\"", "\"Expander Open\""]
                        random.shuffle(nuclear_cycle1)
                        nuclear_Cycle_Chosen = random.choice(nuclear_cycle1)
                        reactor_fuel = ["100-90% Uranium-235", "50% Uranium-235", "20-8% Uranium-235", "1-2% Uranium-235",
                                        "100-90% Plutonium-238", "50% Plutonium-238", "25-8% Plutonium-238", "1-2% Plutonium-238"]
                        random.shuffle(reactor_fuel)
                        reactor_Fuel_Chosen = random.choice(reactor_fuel)
                        nozzle_Type_List_Chosen = "De Laval Bell (With Nozzle Extension)"
                altitude_Of_Operation_Chosen = "80 km+ (Vacuum)"
                random.shuffle(tank_Repressurisation)
                tank_Repressurisation_Chosen = random.choice(tank_Repressurisation)
                random.shuffle(cooling_mechanism)
                cooling_Mechanism_Chosen = random.choice(cooling_mechanism)
                bimodal_decider = random.randint(15, 168)
                if bimodal_decider % 2 == 0:
                    bimodal = True
                outputNt(engine_Name, engine_Cycle_Chosen, altitude_Of_Operation_Chosen, nuclear_Cycle_Chosen,
                         propellant_List_Chosen, reactor_Fuel_Chosen, nozzle_Type_List_Chosen,
                         tank_Repressurisation_Chosen, cooling_Mechanism_Chosen, bimodal)
            
            case "MagnetoPlasmaDynamic Thruster" | "Hall Effect Thruster" | "Gridded Ion Thruster" | "Colloid Thruster" | "Variable Specific Impulse Magnetoplasma Rocket (VASIMR)":
                powerGen_List = ["Hydrogen Fuel cell", "Nuclear Fission Reactor", "Nuclear Fusion Reactor", "Photovoltaic Panel",
                                 "Solar Thermal Panel", "Radioisotope Thermoelectric Generator (RTG)"]
                match engine_Cycle_Chosen:
                    case "Hall Effect Thruster":
                        propellant_List = ["Xenon", "Krypton", "Argon", "Bismuth", "Iodine","Magnesium", "Zinc", "Adamantane"]
                        random.shuffle(propellant_List)
                        propellant_List_Chosen = random.choice(propellant_List)
                        nozzle_Type_List_Chosen = "Hall Effect Thruster Nozzle"
                    case "Gridded Ion Thruster":
                        propellant_List = ["Xenon", "Mercury", "Caesium"]
                        random.shuffle(propellant_List)
                        propellant_List_Chosen = random.choice(propellant_List)
                        nozzle_Type_List_Chosen = "Electrostatic Ion Nozzle"
                    case "Colloid Thruster":
                        propellant_List_Chosen = "NH2OH+NO3 (Hydroxylammonium nitrate)"
                        nozzle_Type_List_Chosen = "Capillary Emitter-Electrode Cone"
                    case "Variable Specific Impulse Magnetoplasma Rocket (VASIMR)":
                        propellant_List = ["Xenon", "Krypton", "Argon"]
                        random.shuffle(propellant_List)
                        propellant_List_Chosen = random.choice(propellant_List)
                        nozzle_Type_List_Chosen = "VASIMR Magnetic Confinement Nozzle"
                    case "MagnetoPlasmaDynamic Thruster":
                        propellant_List = ["Xenon", "Neon", "Argon", "Hydrogen", "Hydrazine", "Lithium"]
                        random.shuffle(propellant_List)
                        propellant_List_Chosen = random.choice(propellant_List)
                        nozzle_Type_List_Chosen = "Cathode Plug Magnetic Confinement Nozzle"
                random.shuffle(powerGen_List)
                powerGen_List_Chosen = random.choice(powerGen_List)
                altitude_Of_Operation_Chosen = "80 km+ (Vacuum)"
                outputEt(engine_Name, engine_Cycle_Chosen, altitude_Of_Operation_Chosen,
                         propellant_List_Chosen, nozzle_Type_List_Chosen, powerGen_List_Chosen)
            
            case "Monopropellant (Decomposition)":
                engine_Name = assCrack(engine_Name1, firstPart)
                cooling_mechanism = ["Ablative Cooling", "Radiative Cooling"]
                nozzle_Type_List1 = ["De Laval Cone (Without Nozzle Extension)", "De Laval Bell (Without Nozzle Extension)"]
                random.shuffle(nozzle_Type_List1)
                nozzle_Type_List_Chosen = random.choice(nozzle_Type_List1)
                random.shuffle(propellant_List1)
                propellant_List_Chosen = random.choice(propellant_List1)
                altitude_Of_Operation_Chosen = "80 km+ (Vacuum)"
                random.shuffle(cooling_mechanism)
                cooling_Mechanism_Chosen = random.choice(cooling_mechanism)
                if propellant_List_Chosen == "N2H4 (Hydrazine)" or propellant_List_Chosen == "65% NH4N(NO2)2 (Ammonium Dinitramide) + 35% CH3OH(Methanol)":
                    catalyst_Chosen = "Iridium coated Alumina Pellets"
                elif propellant_List_Chosen == "H2O2 (Hydrogen Peroxide)":
                    catalyst_Chosen = "KMNO4 (Potassium Permanganate) Honeycomb"
                elif "NH2OH+NO3 (Hydroxylammonium nitrate)":
                    catalyst_Chosen = "Iridium coated Copper Pellets"
                outputMonod(engine_Name, altitude_Of_Operation_Chosen, propellant_List_Chosen,nozzle_Type_List_Chosen,
                            cooling_Mechanism_Chosen, catalyst_Chosen)
                
            case "Monopropellant (Cold Gas)":
                cooling_mechanism = ["Ablative Cooling", "Radiative Cooling", "Dump Cooling", "Film Cooling"]
                nozzle_Type_List1 = ["De Laval Cone (Without Nozzle Extension)", "De Laval Bell (Without Nozzle Extension)"]
                random.choice(propellant_List2)
                propellant_List_Chosen = random.choice(propellant_List2)
                altitude_Of_Operation_Chosen = "80 km+ (Vacuum)"
                random.choice(nozzle_Type_List1)
                nozzle_Type_List_Chosen = random.choice(nozzle_Type_List1)
                random.choice(cooling_mechanism)
                cooling_Mechanism_Chosen = random.choice(cooling_mechanism)
                outputMono(engine_Name, engine_Cycle_Chosen, altitude_Of_Operation_Chosen, propellant_List_Chosen,
                           nozzle_Type_List_Chosen, cooling_Mechanism_Chosen)
                
            case "Expander (Closed)" | "Expander (Open/Bleed)":
                oxidizer_List = ["O2 (Oxygen)", "F2 (Fluorine)", "F2 (Fluorine) + O2 (Oxygen)", "O3 (Ozone)"]
                cooling_mechanism = ["Ablative Cooling", "Radiative Cooling", "Dump Cooling", "Film Cooling",
                                     "Regenerative Cooling", "Transpiration Cooling"]
                random.choice(oxidizer_List)
                oxidizer_Chosen = random.choice(oxidizer_List)
                match oxidizer_Chosen:
                    case "O2 (Oxygen)":
                        fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 85%",
                                     "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)", "NH3 (Ammonia)",
                                     "CH6N2 (MonomethylHydrazine)",
                                     "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H24 (Kerosene)", "B2H6 (Diborane)",
                                     "B5H9 (Pentaborane)"]
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                    case "F2 (Fluorine)":
                        fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 85%",
                                     "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)", "NH3 (Ammonia)", "N2H4 (Hydrazine)",
                                     "C2H8N2 (UnsymetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)",
                                     "CH3OH (Methanol)", "C12H24 (Kerosene)", "B2H6 (Diborane)", "B5H9 (Pentaborane)"]
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                    case "F2 (Fluorine) + O2 (Oxygen)" | "O3 (Ozone)":
                        fuel_List = ["H2 (Hydrogen)", "N2H4 (Hydrazine)", "CH3OH (Methanol)",
                                     "C12H24 (Kerosene)", "B2H6 (Diborane)", "B5H9 (Pentaborane)"]
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                random.shuffle(altitude_Of_Operation)
                altitude_Of_Operation_Chosen = random.choice(altitude_Of_Operation)
                nozzle_Type_Chosen = bussy(altitude_Of_Operation_Chosen)
                random.shuffle(cooling_mechanism)
                cooling_Mechanism_Chosen = random.choice(cooling_mechanism)
                isHype = isHypergolic(oxidizer_Chosen, fuel_Chosen)
                outputEx(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, altitude_Of_Operation_Chosen,
                         nozzle_Type_Chosen, "Autogenous", cooling_Mechanism_Chosen, isHype)
                
            case "Dual Expander (Closed)" | "Dual Expander (Open/Bleed)":
                oxidizer_List = ["O2 (Oxygen)", "F2 (Fluorine)", "F2 (Fluorine) + O2 (Oxygen)"]
                cooling_mechanism = ["Ablative Cooling", "Radiative Cooling", "Dump Cooling", "Film Cooling",
                                     "Regenerative Cooling", "Transpiration Cooling"]
                random.choice(oxidizer_List)
                oxidizer_Chosen = random.choice(oxidizer_List)
                fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)"]
                match oxidizer_Chosen:
                    case "O2 (Oxygen)" | "F2 (Fluorine)":
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                    case "F2 (Fluorine) + O2 (Oxygen)" : fuel_Chosen = "H2 (Hydrogen)"
                random.shuffle(altitude_Of_Operation)
                altitude_Of_Operation_Chosen = random.choice(altitude_Of_Operation)
                nozzle_Type_Chosen = bussy(altitude_Of_Operation_Chosen)
                random.shuffle(cooling_mechanism)
                cooling_Mechanism_Chosen = random.choice(cooling_mechanism)
                isHype = isHypergolic(oxidizer_Chosen, fuel_Chosen)
                outputEx(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, altitude_Of_Operation_Chosen,
                         nozzle_Type_Chosen, "Autogenous", cooling_Mechanism_Chosen, isHype)
                
            case "Staged Combustion (Fuel Rich)":
                oxidizer_List = ["O2 (Oxygen)", "F2 (Fluorine)", "F2 (Fluorine) + O2 (Oxygen)", "O3 (Ozone)"]
                cooling_mechanism = ["Ablative Cooling", "Radiative Cooling", "Dump Cooling", "Film Cooling",
                                     "Regenerative Cooling", "Transpiration Cooling"]
                random.choice(oxidizer_List)
                oxidizer_Chosen = random.choice(oxidizer_List)
                match oxidizer_Chosen:
                    case "O2 (Oxygen)" | "F2 (Fluorine)":
                        fuel_List = ["H2 (Hydrogen)", "NH3 (Ammonia)", "N2H4 (Hydrazine)"]
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                
                    case "F2 (Fluorine) + O2 (Oxygen)" | "O3 (Ozone)": fuel_Chosen = "H2 (Hydrogen)"
                random.shuffle(tank_Repressurisation)
                tank_Repressurisation_Chosen = random.choice(tank_Repressurisation)
                random.shuffle(altitude_Of_Operation)
                altitude_Of_Operation_Chosen = random.choice(altitude_Of_Operation)
                nozzle_Type_Chosen = bussy(altitude_Of_Operation_Chosen)
                random.shuffle(cooling_mechanism)
                cooling_Mechanism_Chosen = random.choice(cooling_mechanism)
                isHype = isHypergolic(oxidizer_Chosen, fuel_Chosen)
                outputDef(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, altitude_Of_Operation_Chosen,
                          nozzle_Type_Chosen, tank_Repressurisation_Chosen, cooling_Mechanism_Chosen, isHype)
            
            case "Staged Combustion (Oxidizer Rich)":
                oxidizer_List = ["O2 (Oxygen)", "O3 (Ozone)", "N2O4 (Nitrogen Tetroxide)"]
                cooling_mechanism = ["Ablative Cooling", "Radiative Cooling", "Dump Cooling", "Film Cooling",
                                     "Regenerative Cooling", "Transpiration Cooling"]
                random.choice(oxidizer_List)
                oxidizer_Chosen = random.choice(oxidizer_List)
                match oxidizer_Chosen:
                    case "O2 (Oxygen)" | "O3 (Ozone)":
                        fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 85%", "C2H5OH(Ethanol) 75%",
                                     "C6H5NH2 (Aniline)", "NH3 (Ammonia)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                                     "CH3OH (Methanol)"]
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                    case "N2O4 (Nitrogen Tetroxide)":
                        fuel_List = ["C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)",
                                     "50% CH6N2 + 50% N2H4 (Aerosine-50)", "C2H8N2 (UnsymetricalDimethylHydrazine)"]
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                random.shuffle(tank_Repressurisation)
                tank_Repressurisation_Chosen = random.choice(tank_Repressurisation)
                random.shuffle(altitude_Of_Operation)
                altitude_Of_Operation_Chosen = random.choice(altitude_Of_Operation)
                nozzle_Type_Chosen = bussy(altitude_Of_Operation_Chosen)
                random.shuffle(cooling_mechanism)
                cooling_Mechanism_Chosen = random.choice(cooling_mechanism)
                isHype = isHypergolic(oxidizer_Chosen, fuel_Chosen)
                outputDef(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, altitude_Of_Operation_Chosen,
                          nozzle_Type_Chosen, tank_Repressurisation_Chosen, cooling_Mechanism_Chosen, isHype)
            
            case "Full Flow Staged Combustion" | "Combustion Tap Off":
                oxidizer_List = ["O2 (Oxygen)", "F2 (Fluorine)", "F2 (Fluorine) + O2 (Oxygen)", "N2H4 (Hydrazine)",
                                 "O3 (Ozone)", "N2O4 (Nitrogen Tetroxide)"]
                cooling_mechanism = ["Ablative Cooling", "Radiative Cooling", "Dump Cooling",
                                     "Film Cooling", "Regenerative Cooling", "Transpiration Cooling"]
                random.choice(oxidizer_List)
                oxidizer_Chosen = random.choice(oxidizer_List)
                match oxidizer_Chosen:
                    case "O2 (Oxygen)":
                        fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 85%",
                                     "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)", "NH3 (Ammonia)",
                                     "CH6N2 (MonomethylHydrazine)",
                                     "N2H4 (Hydrazine)", "CH3OH (Methanol)", "B2H6 (Diborane)", "B5H9 (Pentaborane)"]
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                    case "F2 (Fluorine)":
                        fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 85%",
                                     "C2H5OH(Ethanol) 75%", "NH3 (Ammonia)", "C2H8N2 (UnsymetricalDimethylHydrazine)",
                                     "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)"]
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                    case "F2 (Fluorine) + O2 (Oxygen)" | "O3 (Ozone)":
                        fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 85%",
                                     "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)",
                                     "50% CH6N2 + 50% N2H4 (Aerosine-50)", "CH6N2 (MonomethylHydrazine)", "B2H6 (Diborane)",
                                     "B5H9 (Pentaborane)"]
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                    case "N2H4 (Hydrazine)" | "N2O4 (Nitrogen Tetroxide)":
                        fuel_List = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 85%", "C2H5OH(Ethanol) 75%",
                                     "C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)",
                                     "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                                     "C2H8N2 (UnsymetricalDimethylHydrazine)", "CH3OH (Methanol)", "B2H6 (Diborane)"]
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                random.shuffle(tank_Repressurisation)
                tank_Repressurisation_Chosen = random.choice(tank_Repressurisation)
                random.shuffle(altitude_Of_Operation)
                altitude_Of_Operation_Chosen = random.choice(altitude_Of_Operation)
                nozzle_Type_Chosen = bussy(altitude_Of_Operation_Chosen)
                random.shuffle(cooling_mechanism)
                cooling_Mechanism_Chosen = random.choice(cooling_mechanism)
                isHype = isHypergolic(oxidizer_Chosen, fuel_Chosen)
                outputDef(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, altitude_Of_Operation_Chosen,
                          nozzle_Type_Chosen, tank_Repressurisation_Chosen, cooling_Mechanism_Chosen, isHypergolic)
            
            case _:
                cooling_mechanism = ["Ablative Cooling", "Radiative Cooling", "Dump Cooling",
                                     "Film Cooling", "Regenerative Cooling", "Transpiration Cooling"]
                oxidizer_List = ["O2 (Oxygen)", "F2 (Fluorine)", "F2 (Fluorine) + O2 (Oxygen)","N2O4 (Nitrogen Tetroxide)",
                                 "H2O2 (Hydrogen Peroxide) 95%", "H2O2 (Hydrogen Peroxide) 85%", "O3 (Ozone)",
                                 "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)","AK20I: 80% HNO3 + 20% N2O4 (Nitric Acid)",
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
                    case "F2 (Fluorine) + O2 (Oxygen)"| "O3 (Ozone)":
                        fuel_List = ["H2 (Hydrogen)", "CH3OH (Methanol)", "C12H24 (Kerosene)", "B2H6 (Diborane)","B5H9 (Pentaborane)"]
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                    case "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)" | "AK20I: 80% HNO3 + 20% N2O4 (Nitric Acid)" |\
                         "AK20K: 80% HNO3 + 20% N2O4 (Nitric Acid)" | "AK27I: 73% HNO3 + 27% N2O4 (Nitric Acid)" |\
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
                random.shuffle(tank_Repressurisation)
                tank_Repressurisation_Chosen = random.choice(tank_Repressurisation)
                random.shuffle(altitude_Of_Operation)
                altitude_Of_Operation_Chosen = random.choice(altitude_Of_Operation)
                nozzle_Type_Chosen = bussy(altitude_Of_Operation_Chosen)
                random.shuffle(cooling_mechanism)
                cooling_Mechanism_Chosen = random.choice(cooling_mechanism)
                isHype = isHypergolic(oxidizer_Chosen, fuel_Chosen)
                outputDef(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, altitude_Of_Operation_Chosen,
                          nozzle_Type_Chosen, tank_Repressurisation_Chosen, cooling_Mechanism_Chosen, isHype)
    else:
        while repeatCommand == "Y" and repeatCommand == "N" and repeatCommand == "YES" and repeatCommand == "NO":
            print("Wrong input! Please input an appropriate command [Y/N] ot [YES/NO]")
            print("> ")
            repeatCommand = str(input(">")).upper()
            if repeatCommand == "Y" or repeatCommand == "N" or repeatCommand == "YES" or repeatCommand == "NO":
                break