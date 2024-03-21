import os
import sys
import math
import shutil
import random
import string
import psutil
import numpy as np
from time import time
from time import sleep
import aspose.words as aw
from matplotlib import pylab
import matplotlib.pyplot as plt
from os.path import exists as file_exists

start = count()
def MS(strings, tbc):
    IsThere = False
    for s in strings:
        if strings[strings.index(s)] == tbc:
            IsThere = True
            break
    return IsThere
def rN(add, maxV):
    return add + random.randint(0, maxV)
def rando(array):
    random.shuffle(array)
    return random.choice(array)
def split(txt, sep):
    return txt.split(sep)
def findex(array, search):
    return array.index(search)
def NumFormat(num):
    return format(int(num), ',')
def nameGen():
    engine_Name1 = ["\"Argosy\"", "\"Galileo\"", "\"Callisto\"", "\"Nauka\"", "\"Insider\"", "\"Granis\"", "\"Cercozoa\"",
            "\"Rassvet\"", "\"Zvezda\"", "\"Zarya\"", "\"Orion\"", "\"Ares\"", "\"Delta\"", "\"Atlas\"", "\"Dreadnought\"",
            "\"Daedalus\"", "\"Baltia\"", "\"Dizhou\"", "\"Hermes\"", "\"Icarus\"", "\"Connestoga\"", "\"Yupiter\"",
            "\"Emphasis\"", "\"Olympus\"", "\"Kronos\"", "\"Helios\"", "\"Alabaster\"", "\"Falcon\"", "\"Saturn\"",
            "\"Eagle\"", "\"Endeavour\"", "\"Atlantis\"", "\"Cygnus\"", "\"Apollo\"", "\"Horizon\"", "\"Bulava\"",
            "\"Pioneer\"", "\"Voyager\"", "\"Exploration\"", "\"Expedition\"", "\"Vulcan\"", "\"Vysota\"", "\"Aspin\"",
            "\"Federation\"", "\"Sojourner\"", "\"Nautilus\"", "\"Jubilance\"", "\"Lagrange\"",  "\"Volna\"",
            "\"Prometheus\"", "\"Tellus\"", "\"Alpha\"", "\"Delta\"", "\"Proton\"", "\"Neutron\"", "\"Topol\"",
            "\"Electron\"", "\"Pluton\"", "\"Poodle\"", "\"Skipper\"", "\"Convair\"", "\"Nexus\"", "\"Oko\"",
            "\"Vector\"", "\"Terrier\"", "\"Rhino\"", "\"Panther\"", "\"Goliath\"", "\"Juno\"", "\"Shrimp\"",
            "\"Thumper\"", "\"Mainsail\"", "\"Dart\"", "\"Twitch\"", "\"Stratus\"", "\"Oscar\"", "\"Kosmos\"",
            "\"Sentinel\"", "\"Pegasus\"", "\"Kelus\"", "\"Starshot\"", "\"Vernor\"", "\"Mammoth\"", "\"Liberty\"",
            "\"Douglas\"", "\"Heimdall\"", "\"Dynetics\"", "\"Pathfinder\"", "\"Horizon\"", "\"Poisk\"", "\"Cryptomonada",
            "\"Pirs\"", "\"Philae\"", "\"Mariner\"", "\"Centaur\"", "\"Orel\"", "\"Pratt\"", "\"Hyperion\"",
            "\"Sagittarius\"", "\"Apollo\"", "\"Bryton\"", "\"Volga\"", "\"Harmony\"", "\"Cassini\"", "\"Contour\"",
            "\"Altair\"", "\"Dream\"", "\"Baikal\"", "\"Zenith\"", "\"Urpinod\"", "\"Bernal\"", "\"Condor\"",
            "\"Athena\"", "\"Astra\"", "\"Aerolus\"", "\"Rombus\"", "\"Lunokhod\"", "\"Fregat\"", "\"Glonass\"",
            "\"Dragon\"", "\"Salyut\"", "\"Starliner\"", "\"Skylab\"", "\"Briz\"", "\"Colombus\"", "\"Rosetta\"",
            "\"Redstone\"", "\"Antares\"", "\"Philae\"", "\"Prospero\"", "\"Leonardo\"", "\"Parker\"", "\"Dyson\"",
            "\"Oberon\"", "\"DragonFly\"", "\"Energia\"", "\"Buran\"", "\"Urgan\"", "\"Angara\"", "\"Vostok\"",
            "\"Voskhod\"", "\"Shenzhou\"", "\"Ingenuity\"", "\"Oberon\"", "\"Discovery\"", "\"Horizon\"", "\"Visionalis\"",
            "\"Cerasus\"", "\"Progress\"", "\"Unity\"", "\"Surveyor\"", "\"Prospector\"", "\"Ikar\"", "\"Redstone\"",
            "\"Lapis\"", "\"Caesius\"", "\"Iridium\"", "\"Daedlus\"", "\"Aelita\"", "\"Beta\"", "\"Gamma\"", "\"Filosa\"",
            "\"Alpha\"", "\"Epsilon\"", "\"Omega\"", "\"Discoverer\"", "\"Explorer\"", "\"Hornet\"", "\"Serenity\"",
            "\"Ariane\"", "\"Hornet\"", "\"Asimov\"", "\"Pegasus\"", "\"Venture\"", "\"Antares\"", "\"Star\"",
            "\"Archimedes\"", "\"Hera\"", "\"Iris\"", "\"Titan\"", "\"Artemis\"", "\"Phoenix\"", "\"Ross\"", "\"Heliozoa\""
            "\"Sarychev\"", "\"Nemesis\"", "\"Heimdall\"", "\"Sturt\"", "\"Odin\"", "\"Aethelred\"", "\"Vesper\"",
            "\"Aces\"", "\"Argon\"", "\"Olympia\"", "\"Perseus\"", "\"Chyron\"", "\"Proxima\"", "\"Arminus\"",
            "\"Destiny\"", "\"Valient\"", "\"FireFly\"", "\"Obsidian\"", "\"Leviathan\"", "\"Magellan\"", "\"Voyager\"",
            "\"Mariner\"", "\"Joist\"", "\"Crimson\"", "\"Fortune\"", "\"Vanguard\"", "\"Aurora\"", "\"Ulysses\"",
            "\"Crusader\"", "\"Python\"", "\"Kuiper\"", "\"Insurgent\"", "\"Pathfinder\"", "\"Kvant\"", "\"Spektr\"",
            "\"Cassini\"", "\"Zemlya\"", "\"Dawn\"", "\"Kepler\"", "\"Parom\"", "\"Elektron\"", "\"Aeonian\"",
            "\"Node\"", "\"Burya\"", "\"Voyager\"", "\"Ceres\"", "\"Bayern\"", "\"Chasovoy\"", "\"Copernicus\"",
            "\"Quaoar\"", "\"Minotaur\"", "\"Agena\"", "\"Thor\"", "\"Vega\"", "\"Scout\"", "\"Coeus\"", "\"Minerva\"",
            "\"Kratos\"", "\"Neith\"", "\"Omoikane\"", "\"Gayamun\"", "\"Odin\"", "\"Kronos\"", "\"Hope\"", "\"Poles\"",
            "\"Polyot\"", "\"Sputnik\"", "\"Clementine\"", "\"Sojourner\"", "\"Ingenuity\"", "\"Perseverence\"",
            "\"Onatchesko\"", "\"Atlantis\"", "\"Tsyklon\"", "\"Zenit\"", "\"Almaz\"", "\"Soyuz\"", "\"Molniya\"",
            "\"Oreo\"", "\"Yantar\"", "\"Foton\"", "\"Meteor\"", "\"Ekran\"", "\"Strela\"", "\"Bion\"", "\"Piroda\"",
            "\"Salyut\"", "\"Strela\"", "\"Luch\"", "\"Potok\"", "\"Prognoz\"", "\"Orlets\"", "\"Etalon\"", "\"Astron\"",
            "\"Efir\"", "\"Kometa\"", "\"Fram\"", "\"Zemlya\"", "\"Gorizont\"", "\"Arkon\"", "\"Gamma\"", "\"Ekspress\"",
            "\"Gonets\"", "\"Taifun\"", "\"Okean\"", "\"Reflektor\"", "\"Kolibr\"", "\"Sever\"", "\"Comet\"", "\"Peewee\""
            "\"Roton\"", "\"Solaris\"", "\"Altaris\"", "\"Ithacus\"", "\"Dekto\"", "\"Dream\"", "\"Impuls\"", "\"Aves\""
            "\"Vremya\"", "\"Portal\"", "\"Zodiak\"", "\"Slava\"", "\"Inertsiya\"", "\"Stimuls\"", "\"Ambross\"",
            "\"Amal\"", "\"Thea\"", "\"Orphelia\"", "\"Polyot\"", "\"Mudrost\"", "\"Carrack\"", "\"Artak\"", "\"Anapsida\""
            "\"Questar\"", "\"Artyom\"", "\"Tsyclon\"", "\"Ascension\"", "\"Tenacity\"", "\"Contour\"", "\"Zephyr\"",
            "\"Atlanta\"", "\"Polaris\"", "\"Aeolus\"", "\"Mayak\"", "\"Pamir\"", "\"Taimyr\"", "\"Cheget\"", "\"Sirius\"",
            "\"Uragan\"", "\"Agat\"", "\"Skiph\"", "\"Kristall\"", "\"Altair\"", "\"Uran\"", "\"Ingul\"", "\"Carat\"",
            "\"Pulsar\"", "\"Titan\"", "\"Eridanus\"", "\"Parus\"", "\"Cepheus\"", "\"Varagian\"", "\"Olympus\"",
            "\"Tarkhaniy\"", "\"Astraeus\"", "\"Antares\"", "\"Kazbek\"", "\"Burlak\"", "\"Borei\"", "\"Favor\"",
            "\"Rubin\"", "\"Almaz\"", "\"Granit\"", "\"Ruby\"", "\"Sokol\"", "\"Argon\"", "\"Kavkaz\"", "\"Ural\"",
            "\"Berkut\"", "\"Dunay\"", "\"Yastreb\"", "\"Terek\"", "\"Radon\"", "\"Taymyr\"", "\"Pamir\"", "\"Photon\"",
            "\"Elbrus\"", "\"Isayiev\"", "\"Shmel\"", "\"Kobra\"", "\"Shturn\"", "\"Metis\"", "\"Malyutka\"", "\"Fleyta\"",
            "\"Konkurs\"", "\"Bastion\"", "\"Svir\"", "\"Ataka\"", "\"Vodopad\"", "\"Veter\"", "\"Vyuga\"", "\"Vulga\"",
            "\"Tochka\"", "\"Oka\"", "\"Dvina\"", "\"Almaz\"", "\"Araks\"", "\"Kanopus\"", "\"Kliper\"", "\"Kobalt\"",
            "\"Siluet\"", "\"Kondor\"", "\"Lotos\"", "\"Luch\"", "\"Mir\"", "\"Neman\"", "\"Obzor\"", "\"Okean\"",
            "\"Oktan\"", "\"Orlets\"", "\"Poisk\"", "\"Potok\"", "\"Pirs\"", "\"Prognoz\"", "\"Resurs\"", "\"Rodna\"",
            "\"Romb\"", "\"Kapustin\"", "\"Oplot\"", "\"Tsygan\"", "\"Teplokhod\"", "\"Sokosha\"", "\"Rubezh\"",
            "\"Zircon\"", "\"Moskovitz\"", "\"Tryol\"", "\"Ustinov\"", "\"Belyayev\"", "\"Novgorod\"", "\"Argos\"",
            "\"Nerthus\"", "\"Janus\"", "\"Hephaestus\"", "\"Themis\"", "\"Chronos\"", "\"Tethys\"", "\"Minos\"",
            "\"Autumn\"", "\"Resilience\"", "\"Aelita\"", "\"Rheus\"", "\"Solntspek\"", "\"Spitzer\"", "\"Cartago\"",
            "\"Melibea\"", "\"Spartacus\"", "\"Pulsar\"", "\"Fusion\"", "\"Reliant\"", "\"Thunder\"", "\"Novo\"",
            "\"Panthera\"", "\"Nematoda\"", "\"Anelida\"", "\"Chordata\"", "\"Tetrapoda\"", "\"Cyclero\"", "\"Carrier\"",
            "\"Gaia\"", "\"Irtysh\"", "\"Wyvern\"", "\"Tarsier\"", "\"Alpina\"", "\"Espadon\"", "\"Parlos\"", "\"Nebula\"",
            "\"Lazarus\"", "\"Rufus\"", "\"Dornier\"", "\"Argus\"", "\"Kybau\"", "\"Kalau\"", "\"Chasvoy\"", "\"Zephyr\"",
            "\"Temny\"", "\"Gorizont\"", "\"Yars\"", "\"Krugazor\"", "\"Soprotivlenye\"", "\"Shtil\"", "\"Layner\"",
            "\"Arthropoda\"", "\"Hexapoda\"", "\"Crustacea\"", "\"Tardigrada\"", "\"Mollusca\"", "\"Annelida\"",
            "\"Bryozoa\"", "\"Rotifera", "\"Brachiopoda\"", "\"Echinodermata\"", "\"Hemichordata\"", "\"Cnidaria\"",
            "\"Staurozoa\"", "\"Hydrozoa\"", "\"Porifera", "\"Placozoa\"", "\"Craniata\"", "\"Tunicata\"", "\"Conodonta\"",
            "\"Tetrapoda\"", "\"Amniota\"", "\"Synapsida\"", "\"Sauropsida", "\"Mammalia\"", "\"Sarcodina\"", "\"Sporozoa\"",
            "\"Ciliata\"", "\"Toxoplasma\"", "\"Plasmodium\"", "\"Heterokonta\"", "\"Haptophyta\""]
    firstPart = ["RD", "RS", "AJ", "XLR", "NK", "RL", "KDTU", "AR", "BE", "MV", "YF", "PKA", "J", "RSA", "MJ", "XS", "LM10",
            "HM", "LE", "LRE", "CE", "DST", "DOK", "KDU", "KRD", "RO", "LMS", "LMP", "RT", "F", "E", "A", "B", "S.10", "JDK",
            "SPP", "TYS", "SOK", "RES", "FWR", "NAA75", "LR", "MA", "GE", "OSA", "OBA", "NA", "RM02", "RM", "H", "MBB", "MB",
            "DF", "DE", "BF", "X", "BW", "BADR", "HS", "DC", "UA", "FG", "P", "KMV", "M", "SRMU", "V", "KVD", "JD", "PS", "CE"]
    engNameFinalf = " " + rando(engine_Name1)
    firstPart_f = rando(firstPart) + "-"
    finalNumber = rN(12, 1098)
    if finalNumber % 8 == 0:
        engine_Namee = str(firstPart_f) + str(finalNumber) + str(engNameFinalf)
    else:
        uio93 = rN(1, 1000)
        uio94 = rN(1, 12)
        if uio93 % uio94 == 0:
            randomizedCharacter = random.choice(string.ascii_lowercase)
            while (randomizedCharacter == "l") or (randomizedCharacter == "o") or (randomizedCharacter == "i") or \
                    (randomizedCharacter == "q") or (randomizedCharacter == "e") or (randomizedCharacter == "h") or \
                    (randomizedCharacter == "g") or (randomizedCharacter == "c") or (randomizedCharacter == "j"):
                randomizedCharacter = random.choice(string.ascii_lowercase)
                if (randomizedCharacter != "l") and (randomizedCharacter != "o") and (randomizedCharacter != "i") and \
                        (randomizedCharacter != "q") and (randomizedCharacter != "e") and (randomizedCharacter != "h") \
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
def isHypergolic (OCC, FCC):
    isHyper = False
    match OCC:
        case "N2O4 (Nitrogen Tetroxide)":
            match FCC:
                case "50% CH6N2 + 50% N2H4 (Aerosine-50)" | "75% CH6N2 + 25% N2H4 (UH-25)" | "C6H5NH2 (Aniline)" |\
                     "C2H8N2 (UnsymmetricalDimethylHydrazine)" | "CH6N2 (MonomethylHydrazine)" | "N2H4 (Hydrazine)":
                    isHyper = True
                case _:
                    isHyper = False
        case "H2O2 (Hydrogen Peroxide) 95%" | "H2O2 (Hydrogen Peroxide) 85%", "O2 (Oxygen)":
            isHyper = False
        case "O3 (Ozone)" | "F2 (Fluorine)" | "F2 (Fluorine) + O2 (Oxygen)":
            isHyper = True
        case "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)" | "AK20I: 80% HNO3 + 20% N2O4 (Nitric Acid)"|\
              "AK20K: 80% HNO3 + 20% N2O4 (Nitric Acid)" | "AK27I: 73% HNO3 + 27% N2O4 (Nitric Acid)"|\
              "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)":
            match FCC:
                case "CH6N2 (MonomethylHydrazine)" | "N2H4 (Hydrazine)":
                    isHyper = True
                case _:
                    isHyper = False
    return isHyper
def propDataFind (fuel, oxid):
    match oxid:
        case "O2 (Oxygen)":
            fuel_ListSample = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                    "C6H5NH2 (Aniline)", "NH3 (Ammonia)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                    "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
            combustionTemps = [3304, 3379, 3314, 3167, 3657, 3020, 3399, 3275, 3214, 3526]
            mixRatios = [5.00, 2.77, 1.49, 1.29, 1.72, 1.28, 1.15, 0.74, 1.19, 2.29]
            exhaustVels = [3738, 2932, 2713, 2635, 2708, 2815, 2938, 2973, 2687, 2834]
        case "F2 (Fluorine)":
            fuel_ListSample = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                    "C6H5NH2 (Aniline)", "NH3 (Ammonia)", "C2H8N2 (UnsymmetricalDimethylHydrazine)",
                    "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
            combustionTemps = [3689, -1, -1, 4344, -1, 4469, -1, -1, 4544, 4402, -1]
            mixRatios = [6.00, -1.00, -1.00, 2.26, -1.00, 2.81, -1.00, -1.00, 1.82, 2.20, -1.00]
            exhaustVels = [3925, -1, -1, 3106, -1, 3278, -1, -1, 3315, 3146, -1]
        case "F2 (Fluorine) + O2 (Oxygen)":
            fuel_ListSample = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                    "C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                    "CH6N2 (MonomethylHydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)", "N2H4 (Hydrazine)"]
            combustionTemps = [-1, 4530, 4437, -1, 4517, 4584, 4575, 4583, -1, 4571, -1]
            mixRatios = [-1.00, 4.82, 2.56, -1.00, 2.41, 2.41, 2.22, 2.33, -1.00, 3.67, -1.00]
            exhaustVels = [-1, 3281, 3134, -1, 3006, 3255, 3273, 3264, -1, 3166, -1]
        case "O3 (Ozone)":
            fuel_ListSample = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                    "C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                    "CH6N2 (MonomethylHydrazine)", "C12H26 (n-Dodecane)", "CH3OH (Methanol)", "N2H4 (Hydrazine)",
                    "NH3 (Ammonia)"]
            combustionTemps = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
            mixRatios = [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00]
            exhaustVels = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        case "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)" | "AK20I: 80% HNO3 + 20% N2O4 (Nitric Acid)"|\
             "AK20K: 80% HNO3 + 20% N2O4 (Nitric Acid)" | "AK27I: 73% HNO3 + 27% N2O4 (Nitric Acid)"|\
             "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)":
            fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                    "CH3OH (Methanol)"]
            combustionTemps = [2795, 2905, 3033, 2932, 2824]
            mixRatios = [8.00, 2.75, 2.13, 1.28, 2.13]
            exhaustVels = [3112, 2449, 2635, 2702, 2441]
        case "N2O4 (Nitrogen Tetroxide)":
            fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                    "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)", "C2H8N2 (UnsymmetricalDimethylHydrazine)",
                    "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
            combustionTemps = [2973, 3151, 3006, 3468, 3268, 3229, 3296, 3252, 3137, 3058, 3342]
            mixRatios = [6.50, 2.26, 1.93, 2.64, 1.85, 1.59, 2.10, 1.73, 1.08, 1.78, 3.53]
            exhaustVels = [3334, 2540, 2479, 2538, 2730, 2750, 2713, 2742, 2803, 2528, 2619]
        case "H2O2 (Hydrogen Peroxide) 85%":
            fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                    "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)", "C2H8N2 (UnsymmetricalDimethylHydrazine)",
                    "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
            combustionTemps = [2544, 2552, 2447, 2719, 2681, 2668, 2690, 2681, 2630, 2511, 2666]
            mixRatios = [14.00, 4.62, 3.77, 5.95, 4.02, 3.39, 4.63, 3.76, 2.15, 3.55, 7.84]
            exhaustVels = [2882, 2476, 2425, 2495, 2592, 2604, 2582, 2600, 2642, 2464, 2530]
        case "H2O2 (Hydrogen Peroxide) 95%":
            fuel_ListSample = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%", "C6H5NH2 (Aniline)",
                    "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)", "C2H8N2 (UnsymmetricalDimethylHydrazine)",
                    "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
            combustionTemps = [2666, 2762, 2653, 2934, 2870, 2852, 2884, 2871, 2801, 2709, 2878]
            mixRatios = [11.00, 3.97, 3.27, 4.94, 3.32, 2.82, 3.82, 3.13, 1.82, 3.06, 6.50]
            exhaustVels = [1918, 1599, 1566, 1610, 1683, 1692, 1676, 1688, 1718, 1590, 1639]
    x = fuel_ListSample.index(fuel)
    combust_temp = str(combustionTemps[x])
    mixRatio = str(mixRatios[x])
    exhaustVelF = str(exhaustVels[x])
    return combust_temp + ", " + mixRatio + ", " + exhaustVelF
def NzlParameters (alt_Of_Operation):
    nozzle_Type_Chosen, OExpansionRatio = "", ""
    match alt_Of_Operation:
        case "0-20 km (Sea Level)":
            nozzle_Type_List_SL = ["Contour Bell Nozzle", "Parabolic Bell Nozzle", "Conical Nozzle", "Stepped Dual Bell Nozzle"]
            nozzle_Type_Chosen = rando(nozzle_Type_List_SL)
            if nozzle_Type_Chosen == "Conical Nozzle":
                OExpansionRatio = str(rN(10, 9)) + ":1"
            else:
                OExpansionRatio = str(rN(10, 12)) + ":1"
        case "20-30 km (Medium Atmosphere)":
            nozzle_Type_List_HA = ["Contour Bell Nozzle", "Parabolic Bell Nozzle", "Stepped Dual Bell Nozzle"]
            nozzle_Type_Chosen = rando(nozzle_Type_List_HA)
            OExpansionRatio = str(rN(32, 14)) + ":1"
        case "30-80 km (High Atmosphere)":
            nozzle_Type_List_HAi = ["Contour Bell Nozzle", "Parabolic Bell Nozzle", "Stepped Dual Bell Nozzle"]
            nozzle_Type_Chosen = rando(nozzle_Type_List_HAi)
            OExpansionRatio = str(rN(47, 43)) + ":1"
        case "80 km+ (Vacuum)":
            nozzle_Type_List_VA = ["Contour Bell Nozzle", "Parabolic Bell Nozzle", "Expanding Nozzle"]
            nozzle_Type_Chosen = rando(nozzle_Type_List_VA)
            OExpansionRatio = str(rN(90, 110)) + ":1"
        case "Any Altitude (0-80 km+)":
            nozzle_Type_List_Aero = ["Linear Aerospike Nozzle", "Toroidal Aerospike Nozzle", "Stepped Dual Bell Nozzle"]
            nozzle_Type_Chosen = rando(nozzle_Type_List_Aero)
            if nozzle_Type_Chosen == "Stepped Dual Bell Nozzle":
                OExpansionRatio = str(rN(10, 9)) + ":1"
            else:
                OExpansionRatio = "None (Nozzle doesnt have a throat)"
    return nozzle_Type_Chosen + ", " + OExpansionRatio
def StndrdDet(eng_Name, eng_Cycle, oxid_C, fuel_C, tank_RepressA, alt_Operation):
    Eng_Data = split(propDataFind(fuel_C, oxid_C), ", ")
    f_regen, propProperties, F_gimbalangle, chamberN = "", "", "", ""
    combust_temp, mixRatio, exhaustVelFinal = Eng_Data[0], Eng_Data[1], Eng_Data[2]
    tank_Repress = rando(tank_RepressA)

    Operational_Alt = rando(alt_Operation)
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

    uio96, uio97 = rN(1, 999), rN(1, 11)
    if uio96 % uio97 == 0:
        Throttle_MinV, Throttle_MaxV = rN(1, 90), rN(100, 5)
        ThrottleRange = str(Throttle_MinV) + "-" + str(Throttle_MaxV) + "%"
    else:
        ThrottleRange = "Not Throttleable"

    longDur = MS(search_for, purp)
    if longDur:
        cooling_mechanismA = ["Radiative Cooling", "Dump Cooling", "Film Cooling", "Regenerative Cooling", "Transpiration Cooling"]
    else:
        cooling_mechanismA = ["Ablative Cooling", "Radiative Cooling", "Dump Cooling", "Film Cooling", "Regenerative Cooling", "Transpiration Cooling"]
    cooling_Mechanism_Chosen = rando(cooling_mechanismA)
    if cooling_Mechanism_Chosen == "Regenerative Cooling":
        f_regen = "Oxidizer "

    if purp in "Vernier":
        gimbalangle = rN(0, 30)
        if not gimbalangle >= 1 or alt_Operation == "80 km+ (Vacuum)":
            F_gimbalangle = "None"
        else:
            F_gimbalangle = "±" + gimbalangle + "°"
    elif purp in "Course Correction" and not purp in "Lower Stage":
        F_gimbalangle = "None"
    else:
        gimbalangle = rN(0, 10)
        if not gimbalangle >= 1 or alt_Operation == "80 km+ (Vacuum)":
            F_gimbalangle = "None"
        else:
            F_gimbalangle = "±" + str(gimbalangle) + "°"

    chambers = rN(1, 2)
    if chambers == 1 or nozzle_Type_Chosen in "Aerospike":
        chamberN = "Single Chamber"
    elif chambers == 2:
        chamberN = "Dual Chamber"
    elif chambers == 3:
        chamberN = "Quadruple Chamber"
            
    cooling_Mechanism_C = f_regen + cooling_Mechanism_Chosen
    injector = Injector(cooling_Mechanism_C, eng_Cycle)
    output_def(eng_Name, eng_Cycle, oxid_C, fuel_C, Operational_Alt, nozzle_Type_Chosen, tank_Repress, cooling_Mechanism_C,
               propProperties, purp, injector, AR_exit, combust_temp, mixRatio, exhaustVelFinal, ThrottleRange, chamberN,
               F_gimbalangle)
def isCryogenic(oxidizer_chosen, fuel_chosen):
    isCryo = False
    match oxidizer_chosen:
        case "O3 (Ozone)"| "F2 (Fluorine)"| "F2 (Fluorine) + O2 (Oxygen)"| "O2 (Oxygen)": isCryo = True
    match fuel_chosen:
        case "CH3OH (Methanol)"| "C12H26 (n-Dodecane)"| "H2 (Hydrogen)"| "C2H5OH(Ethanol) 95%"| "C2H5OH(Ethanol) 75%"|\
             "NH3 (Ammonia)"| "CH4 (Methane)": isCryo = True
    return isCryo
def uses(isHypergol, isCryogen, alt, En_Cycle):
    compleX = False
    if En_Cycle.upper == "Combustion Tap" or En_Cycle.upper == "Staged" or En_Cycle.upper == "Full Flow":
        compleX = True
    if alt == "0-20 km (Sea Level)" or alt == "20-30 km (Medium Atmosphere)":
        if compleX:
            pot_usesA = ["Lower Stage (Main Propulsion)"]
        else:
            pot_usesA = ["Lower Stage (Main Propulsion)", "Lower Stage (Course Correction)", "Lower Stage (Vernier)"]
        useA = rando(pot_usesA)
    elif alt == "30-80 km (High Atmosphere)" or alt == "80 km+ (Vacuum)":
        if isHypergol and isCryogen:
            if compleX:
                pot_usesA = ["Upper Stage (Main Propulsion)"]
            else:
                pot_usesA = ["Upper Stage(Main Propulsion)", "Upper Stage(Course Correction)", "Upper Stage(Vernier)",
                            "Upper Stage (Ullage)", "Payload (Main Propulsion)", "Payload (ACS)"]
            useA = rando(pot_usesA)
        elif not isHypergol and isCryogen:
            if compleX:
                pot_usesA = ["Upper Stage (Main Propulsion)"]
            else:
                pot_usesA = ["Upper Stage (Main Propulsion)", "Upper Stage (Vernier)"]
            useA = rando(pot_usesA)
        elif isHypergol and not isCryogen:
            if compleX:
                pot_usesA = ["Upper Stage(Main Propulsion)", "Payload (Main Propulsion)", "Space Tug (Main Propulsion)"]
            else:
                pot_usesA = ["Upper Stage(Main Propulsion)", "Upper Stage(Course Correction)", "Upper Stage(Vernier)",
                            "Upper Stage (Ullage)", "Payload (Main Propulsion)", "Payload (ACS)", "Payload (Course Correction)",
                            "Payload (Vernier)", "Space Tug (Main Propulsion)", "Space Tug (Course Correction)",
                            "Space Tug (Vernier)", "Space Tug (Ullage)"]
            useA = rando(pot_usesA)
    else:
        pot_usesA = ["Lower Stage (Main Propulsion)", "Upper Stage(Main Propulsion)", "Payload (Main Propulsion)"]
        useA = rando(pot_usesA)
    return useA
def Injector(cooling_Mechanism, engine_Cycle_Chose):
    fuel_state = "Liquid"
    if cooling_Mechanism in "Regenerative Cooling" or engine_Cycle_Chose in "Expander":
        fuel_state = "Gas"
    injector = ["Showerhead Injector", "Self-impinging Injector", "Cross-impinging Injector", "Swirl Injector", "Pintle Injector"]
    return fuel_state + " " + rando(injector)
def output_monod(ENN, ECC, AOOC, PLC, NTLC, CMC, CCC, purposeB):
    lbrk = "======================================================================================================================"
    print(f"{lbrk}\nEngine Designation: {ENN}\n")
    print(f"Fuel Flow Cycle: {ECC}")
    print(f"Propellant: {PLC}")
    print(f"Altitude Of Operation: {AOOC}")
    print(f"Exhaust Nozzle Geometry: {NTLC}")
    print(f"Engine Use Case: {purposeB}")
    print(f"Nozzle Cooling Mechanism: {CMC}")
    print(f"Propellant catalyst: {CCC}\n")

    file = open("C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles/GenData/obf_rex.txt", "at")
    file.write(f"\n\nEngine Designation: {ENN}\n")
    file.write(f"Fuel Flow Cycle: {ECC}\n")
    file.write(f"Propellant: {PLC}\n")
    file.write(f"Altitude Of Operation: {AOOC}\n")
    file.write(f"Exhaust Nozzle Geometry: {NTLC}\n")
    file.write(f"Engine Use Case: {purposeB}\n")
    file.write(f"Nozzle Cooling Mechanism: {CMC}\n")
    file.write(f"Propellant catalyst: {CCC}")
    file.close()
def output_mono(ENN, ECC, AOOC, PLC, NTLC, CMC, purposeE):
    lbrk = "======================================================================================================================"
    print(f"{lbrk}\nEngine Designation: {ENN}\n")
    print(f"Fuel Flow Cycle: {ECC}")
    print(f"Propellant: {PLC}")
    print(f"Altitude Of Operation: {AOOC}")
    print(f"Exhaust Nozzle Geometry: {NTLC}")
    print(f"Engine Use Case: {purposeE}")
    print(f"Nozzle Cooling Mechanism: {CMC}\n")

    file = open("C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles/GenData/obf_rex.txt", "at")
    file.write(f"\n\nEngine Designation: {ENN}\n")
    file.write(f"Fuel Flow Cycle: {ECC}\n")
    file.write(f"Propellant: {PLC}\n")
    file.write(f"Altitude Of Operation: {AOOC}\n")
    file.write(f"Exhaust Nozzle Geometry: {NTLC}\n")
    file.write(f"Engine Use Case: {purposeE}\n")
    file.write(f"Nozzle Cooling Mechanism: {CMC}")
    file.close()
def output_et(ENN, ECC, AOOC, PLC, NTLC, PGLC, purposeE, pwr):
    lbrk = "======================================================================================================================"
    print(f"{lbrk}\nEngine Designation: {ENN}\n")
    print(f"Fuel Flow Cycle: {ECC}")
    print(f"Propellant(Remass): {PLC}")
    print(f"Altitude Of Operation: {AOOC}")
    print(f"Exhaust Nozzle Geometry: {NTLC}")
    print(f"Engine Use Case: {purposeE}")
    print(f"Engine Power Source: {PGLC}")
    print(f"Rated Power Level: {pwr}\n")

    file = open("C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles/GenData/obf_rex.txt", "at")
    file.write(f"\n\nEngine Designation: {ENN}\n")
    file.write(f"Fuel Flow Cycle: {ECC}\n")
    file.write(f"Propellant(Remass): {PLC}\n")
    file.write(f"Altitude Of Operation: {AOOC}\n")
    file.write(f"Exhaust Nozzle Geometry: {NTLC}\n")
    file.write(f"Engine Use Case: {purposeE}\n")
    file.write(f"Engine Power Source: {PGLC}\n")
    file.write(f"Rated Power Level: {pwr}")
    file.close()
def output_nt(ENN, ECC, AOOC, NCC, PLC, RFC, NTLC, EEV, TRC, CMC, purposeF, react_gen, bimodal, ERC, PRS, ARR, ECT):
    lbrk = "======================================================================================================================"
    MaxElecP = NumFormat((ECT / 100) * 18)
    MaxP = NumFormat(((ECT / 90) * 100) / 1000)
    print(f"{lbrk}\nEngine Designation: {ENN}\n")
    if not ECC == "Radioisotope Engine" and not NCC == "":
        print(f"Fuel Flow Cycle: {NCC} {ECC}")
    else:
        print(f"Fuel Flow Cycle: {ECC}")
    print(f"Propellant (Remass): {PLC}")
    print(f"Propellant State: {PRS}")
    print(f"Reactor Generation: {react_gen}")
    print(f"Reactor Maximum Power: {MaxP} GW")
    print(f"Reactor Fuel Material: {RFC}")
    if NCC == "LANTR":
        print(f"Engine Exhaust Velocity: ({NumFormat(EEV)}/~3850) m/s")
    else:
        print(f"Engine Exhaust Velocity: {NumFormat(EEV)} m/s")
    print(f"Reactor Core Temperature: {NumFormat(ECT)}°K")
    print(f"Reactor Coolant: {ERC}")
    if not bimodal or ECC == "Nuclear SaltWater":
        print(f"Engine Bimodality: Engine isn't bimodal")
        print(f"Engine Electrical Output: None")
    else:
        print(f"Engine Bimodality: Engine is bimodal")
        print(f"Engine Electrical Output: {MaxElecP} MW")
    print(f"Altitude Of Operation: {AOOC}")
    print(f"Exhaust Nozzle Geometry: {NTLC}")
    print(f"Exhaust Nozzle Area Ratio: {ARR}")
    print(f"Exhaust Nozzle Cooling Mechanism: {CMC}")
    print(f"Engine Use Case: {purposeF}")
    print(f"Tank repressurisation Method: {TRC}\n")

    file = open("C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles/GenData/obf_rex.txt", "at")
    file.write(f"\n\nEngine Designation: {ENN}\n")
    if not ECC == "Nuclear SaltWater" and not ECC == "Radioisotope Engine" and not NCC == "":
        file.write(f"Fuel Flow Cycle: {NCC} {ECC}\n")
    else:
        file.write(f"Fuel Flow Cycle: {ECC}\n")
    file.write(f"Propellant (Remass): {PLC}\n")
    file.write(f"Propellant State: {PRS}\n")
    file.write(f"Reactor Generation: {react_gen}\n")
    file.write(f"Reactor Maximum Power: {MaxP} GW\n")
    file.write(f"Reactor Fuel Material: {RFC}\n")
    if NCC == "LANTR":
        file.write(f"Engine Exhaust Velocity: ({NumFormat(EEV)}/~3850) m/s\n")
    else:
        file.write(f"Engine Exhaust Velocity: {NumFormat(EEV)} m/s\n")
    file.write(f"Reactor Core Temperature: {NumFormat(ECT)}°K\n")
    file.write(f"Reactor Coolant: {ERC}\n")
    if not bimodal or ECC == "Nuclear SaltWater":
        file.write(f"Engine Bimodality: Engine isn't bimodal\n")
        file.write(f"Engine Electrical Output: None\n")
    else:
        file.write(f"Engine Bimodality: Engine is bimodal\n")
        file.write(f"Engine Electrical Output: {MaxElecP} MW\n")
    file.write(f"Altitude Of Operation: {AOOC}\n")
    file.write(f"Exhaust Nozzle Geometry: {NTLC}\n")
    file.write(f"Exhaust Nozzle Area Ratio: {ARR}\n")
    file.write(f"Exhaust Nozzle Cooling Mechanism: {CMC}\n")
    file.write(f"Engine Use Case: {purposeF}\n")
    file.write(f"Tank repressurisation Method: {TRC}")
    file.close()
def output_def(ENN, ECC, OCC, FCC, AOOC, NTC, TRC, CMC, propProp, purp, injector, FinalAreaRatio, combust_temp, mixRatio,
               exhaustVel, ThrottleRange, chamberN, F_gimbalangle):
    lbrk = "======================================================================================================================"
    print(f"{lbrk}\nEngine Designation: {ENN}\n")
    print(f"Fuel Flow Cycle: {ECC}")
    print(f"Engine Oxidizer: {OCC}")
    print(f"Engine Fuel: {FCC}")
    print(f"Average Mixture Ratio: {mixRatio}")
    print(f"Propellant properties: {propProp}")
    print(f"Altitude Of Operation: {AOOC}")
    print(f"Exhaust Nozzle Geometry: {NTC}")
    print(f"Exhaust Nozzle Area Ratio: {FinalAreaRatio}")
    print(f"Characteristic Exhaust Velocity: {exhaustVel} m/s")
    print(f"Adiabatic Combustion Temperature: {combust_temp}°K")
    print(f"Engine Gimbal Range: {F_gimbalangle}")
    print(f"Engine Injector Design: {injector}")
    print(f"Engine chamber configuration: {chamberN}")
    print(f"Engine Use Case: {purp}")
    print(f"Tank repressurisation Method: {TRC}")
    print(f"Nozzle Cooling Mechanism: {CMC}")
    print(f"Engine Throttle Range: {ThrottleRange}\n")

    file = open("C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles/GenData/obf_rex.txt", "at")
    file.write(f"\n\nEngine Designation: {ENN}\n")
    file.write(f"Fuel Flow Cycle: {ECC}\n")
    file.write(f"Engine Oxidizer: {OCC}\n")
    file.write(f"Engine Fuel: {FCC}\n")
    file.write(f"Average Mixture Ratio: {mixRatio}\n")
    file.write(f"Propellant properties: {propProp}\n")
    file.write(f"Altitude Of Operation: {AOOC}\n")
    file.write(f"Exhaust Nozzle Geometry: {NTC}\n")
    file.write(f"Exhaust Nozzle Area Ratio: {FinalAreaRatio}\n")
    file.write(f"Characteristic Exhaust Velocity: {exhaustVel} m/s\n")
    file.write(f"Adiabatic Combustion Temperature: {combust_temp}°K\n")
    file.write(f"Engine Gimbal Range: {F_gimbalangle}\n")
    file.write(f"Engine Injector Design: {injector}\n")
    file.write(f"Engine chamber configuration: {chamberN}\n")
    file.write(f"Engine Use Case: {purp}\n")
    file.write(f"Tank repressurisation Method: {TRC}\n")
    file.write(f"Nozzle Cooling Mechanism: {CMC}\n")
    file.write(f"Engine Throttle Range: {ThrottleRange}")
    file.close()

tic, tac = count(), count()
mpl_xs, mpl_ysa, mpl_ysb = [], [], []
repeatCommand, y, fNum, maxN = "YES", 0, 2, 50
#print(f"Welcome to the Advanced Rocket Engine Generator!")
org = "C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles"
org1 = "C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles/DevData"
org2 = "C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles/GenData"
pathe = "C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles/GenData/obf_rex.txt"
logPF = "C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles/GenData/FullFolders/obf_rex[Full]1.txt"
engine_Cycle = ["Gas Generator", "Staged Combustion (Oxidizer Rich)", "Staged Combustion (Fuel Rich)", "Expander (Open/Bleed)",
       "Expander (Closed)", "Dual Expander (Open/Bleed)", "Dual Expander (Closed)", "Pressure-Fed", "Full Flow Staged",
       "Electric Pump Fed", "Combustion Tap Off", "Monopropellant (Cold Gas)", "Monopropellant (Decomposition)", "Gas Core",
       "Droplet Core", "Liquid Core", "Solid Core", "Vapor Core", "Nuclear SaltWater", "Radioisotope Engine", "MagnetoPlasmaDynamic Thruster",
       "Hall Effect Thruster", "Gridded Ion Thruster", "Colloid Thruster", "Variable Specific Impulse Magnetoplasma Rocket (VASIMR)"]
altitude_Of_Operation = ["0-20 km (Sea Level)", "20-30 km (Medium Atmosphere)", "30-80 km (High Atmosphere)", "80 km+ (Vacuum)", "Any Altitude (0-80 km+)"]
tank_Repressurisation = ["Autogenous", "Inert Gas"]
if not file_exists(org):
    os.mkdir(org)
if not file_exists(org1):
    os.mkdir(org1)
if not file_exists(org2):
    os.mkdir(org2)

while repeatCommand != "N":
    """
    print(f"Do you want to generate a new engine? [Y/N]")
    repeatCommand = str(input(">>>>> ")).upper()
    if repeatCommand == "N" or repeatCommand == "NO":
        end = count()
        timen = (end - start) / 1000
        print(f"Engines Created: {y}")
        if timen < 60:
            print(f"Total run count: {timen} secs")
        elif timen / 60 < 2:
            print(f"Total run count: " + math.floor(timen / 60) + " min " + timen % 60 + " secs")
        else:
            print(f"Total run count: " + math.floor(timen / 60) + " mins " + timen % 60 + " secs")
        exit(0)   
    elif repeatCommand == "Y" or repeatCommand == "YES":
    """
    if maxN >= fNum:
        if count() >= tac + 0.9975:
            tac = count()
            mpl_xs.append(tac-start)
            mpl_ysa.append(y)
            mpl_ysb.append(psutil.virtual_memory()[2])
        if not file_exists(pathe):
            init = open(pathe, "x")
            init.close()
        sizeInbytes = os.path.getsize(pathe)
        sizeInKilobytes = (sizeInbytes / 1024)
        if sizeInKilobytes >= 50:
            if file_exists(logPF):
                if file_exists("C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles/GenData/FullFolders/obf_rex[Full]" + str(fNum) + ".txt"):
                    fNum = fNum+1
                else:
                    shutil.copy2(pathe,
                        "C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles/GenData/FullFolders/obf_rex[Full]" + str(fNum) + ".txt")
                    rset = open(pathe, 'wt')
                    rset.write("")
                    rset.close()
            else:
                org3 = "C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles/GenData/FullFolders"
                os.mkdir(org3)
                shutil.copy2("C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles/GenData/obf_rex.txt", logPF)
        engine_Name = nameGen()
        engine_Cycle_Chosen = rando(engine_Cycle)
        match engine_Cycle_Chosen:
            case "Gas Core" | "Droplet Core" | "Liquid Core" | "Solid Core" | "Vapor Core" | "Nuclear SaltWater" |\
                    "Radioisotope Engine":
                 match engine_Cycle_Chosen:
                     case "Radioisotope Engine":
                         remass_List = ["Hydrogen (H2)", "Nitrogen (N2)", "Ammonia (NH3)", "Water (H2O)",
                                "Oxygen (O2)", "Carbon Dioxide (CO2)", "Carbon Monoxide (CO)"]
                         remass_EVD = [1.782, 14.6, 4.25, 6.587, 16, 14.6, 28]
                         remass_List_Chosen = rando(remass_List)
                         propellant_List_Chosen = remass_List_Chosen
                         nuclear_Cycle_Chosen = ""
                         reactor_fuel = ["Polonium-210", "Fermium-252", "Uranium-233", "Plutonium-238"]
                         reactor_Fuel_Chosen = rando(reactor_fuel)
                         propellantState = "Cryogenic Liquid"
                         coreTemp = rN(2000, 200)
                         molmassi = findex(remass_List, remass_List_Chosen)
                         molmass = remass_EVD[molmassi]
                         exhaustVel = (12400 / math.pow(molmass, 0.531))
                     case "Solid Core":
                         remass_List = ["Hydrogen (H2)", "Nitrogen (N2)", "Ammonia (NH3)", "Water (H2O)",
                                        "Oxygen (O2)", "Carbon Dioxide (CO2)", "Carbon Monoxide (CO)"]
                         remass_EVD = [1.782, 14.6, 4.25, 6.587, 16, 14.6, 28]
                         remass_List_Chosen = rando(remass_List)
                         propellant_List_Chosen = remass_List_Chosen
                         nuclear_cycle = ["LANTR", "LEUNTR", "LPNTR", "CERMET", "Pebble-Bed", ""]
                         nuclear_Cycle_Chosen = rando(nuclear_cycle)
                         reactor_fuel = ["Uranium-235", "Plutonium-238"]
                         propellantState = "Cryogenic Liquid"
                         if nuclear_Cycle_Chosen.upper == "LANTR":
                             remass_List_Chosen = "Hydrogen (H2)"
                             enr_level = rN(8, 87)
                             reactor_Fuel_Chosen = str(enr_level) + "% " + rando(reactor_fuel)
                             coreTemp = rN(1900 + (enr_level * 5), 1000)
                             molmassi = findex(remass_List, remass_List_Chosen)
                             molmass = remass_EVD[molmassi]
                             exhaustVel = (17600 / math.pow(molmass, 0.531))
                         elif nuclear_Cycle_Chosen.upper == "LEUNTR":
                             remass_List_Chosen = rando(remass_List)
                             enr_level = rN(5, 10)
                             reactor_Fuel_Chosen = str(enr_level) + "% " + rando(reactor_fuel)
                             coreTemp = rN(1900 + (enr_level * 5), 1000)
                             molmassi = findex(remass_List, remass_List_Chosen)
                             molmass = remass_EVD[molmassi]
                             exhaustVel = (17600 / math.pow(molmass, 0.531))
                         elif nuclear_Cycle_Chosen.upper == "LPNTR":
                             remass_List_Chosen = rando(remass_List)
                             enr_level = rN(8, 87)
                             reactor_Fuel_Chosen = str(enr_level) + "% " + rando(reactor_fuel)
                             coreTemp = rN(1900 + (enr_level * 5), 1000)
                             molmassi = findex(remass_List, remass_List_Chosen)
                             molmass = remass_EVD[molmassi]
                             exhaustVel = (17600 / math.pow(molmass, 0.531))
                         elif nuclear_Cycle_Chosen.upper == "CERMET":
                             remass_List_Chosen = rando(remass_List)
                             enr_level = rN(8, 87)
                             reactor_Fuel_Chosen = str(enr_level) + "% " + rando(reactor_fuel)
                             coreTemp = rN(1900 + (enr_level * 5), 1000)
                             molmassi = findex(remass_List, remass_List_Chosen)
                             molmass = remass_EVD[molmassi]
                             exhaustVel = (17600 / math.pow(molmass, 0.531))
                         elif nuclear_Cycle_Chosen.upper == "Pebble-Bed":
                             remass_List_Chosen = rando(remass_List)
                             propellantState = "Cryogenic Liquid"
                             propellant_List_Chosen = "Uranium(VI) Fluoride (UF6) and " + remass_List_Chosen
                             nuclear_Cycle_Chosen = rando(nuclear_cycle)
                             enr_level = rN(8, 87)
                             reactor_Fuel_Chosen = str(enr_level) + "% " + "Uranium-235"
                             coreTemp = rN(1400 + (enr_level * 5), 1000)
                             molmassi = findex(remass_List, remass_List_Chosen)
                             molmass = remass_EVD[molmassi]
                             exhaustVel = ((9530 * 2) / math.pow(molmass, 0.531))
                         else:
                             remass_List_Chosen = rando(remass_List)
                             enr_level = rN(8, 87)
                             reactor_Fuel_Chosen = str(enr_level) + "% " + rando(reactor_fuel)
                             coreTemp = rN(1900 + (enr_level * 5), 1000)
                             molmassi = findex(remass_List, remass_List_Chosen)
                             molmass = remass_EVD[molmassi]
                             exhaustVel = (11000 / math.pow(molmass, 0.531))
                     case "Colloid Core":
                         remass_List = ["Hydrogen (H2)", "Nitrogen (N2)", "Ammonia (NH3)", "Water (H2O)",
                            "Oxygen (O2)", "Carbon Dioxide (CO2)", "Carbon Monoxide (CO)"]
                         remass_EVD = [1.782, 14.6, 4.25, 6.587, 16, 14.6, 28]
                         remass_List_Chosen = rando(remass_List)
                         propellant_List_Chosen = "Uranium Zirconium Carbide(UC2 + ZrC) Colloid and " + remass_List_Chosen
                         nuclear_Cycle_Chosen = ""
                         propellantState = "Cryogenic Liquid"
                         enr_level = rN(8, 87)
                         reactor_Fuel_Chosen = enr_level + "% " + "Uranium-235"
                         coreTemp = rN(2500 + (enr_level * 5), 1000)
                         molmassi = findex(remass_List, remass_List_Chosen)
                         molmass = remass_EVD[molmassi]
                         exhaustVel = (11800 / math.pow(molmass, 0.531))
                     case "Liquid Core":
                         nuclear_cycle = ["\"Expander Bleed\"", "\"Expander Closed\"", "\"Vortex Confined\"", "LARS"]
                         remass_List = ["Hydrogen (H2)", "Nitrogen (N2)", "Ammonia (NH3)", "Water (H2O)",
                                 "Oxygen (O2)", "Carbon Dioxide (CO2)", "Carbon Monoxide (CO)"]
                         remass_EVD = [1.782, 14.6, 4.25, 6.587, 16, 14.6, 28]
                         materials = ["Tungsten", "Osmium", "Rhenium", "Tantalum"]
                         remass_List_Chosen = rando(remass_List)
                         material = rando(materials)
                         propellantState = "Cryogenic Liquid"
                         propellant_List_Chosen = "Uranium impregnated " + material + " and " + remass_List_Chosen
                         nuclear_Cycle_Chosen = rando(nuclear_cycle)
                         enr_level = rN(8, 87)
                         reactor_Fuel_Chosen = str(enr_level) + "% " + "Uranium-235"
                         coreTemp = rN(3500 + (enr_level * 5), 1000)
                         molmassi = findex(remass_List, remass_List_Chosen)
                         molmass = remass_EVD[molmassi]
                         exhaustVel = (19620 / math.pow(molmass, 0.531))
                     case "Droplet Core":
                         nuclear_cycle = ["\"Expander Bleed\"", "\"Expander Closed\"", "\"Vortex Confined\""]
                         remass_List = ["Hydrogen (H2)", "Nitrogen (N2)", "Ammonia (NH3)", "Water (H2O)",
                                "Oxygen (O2)", "Carbon Dioxide (CO2)", "Carbon Monoxide (CO)"]
                         remass_EVD = [1.782, 14.6, 4.25, 6.587, 16, 14.6, 28]
                         remass_List_Chosen = rando(remass_List)
                         propellantState = "Cryogenic Liquid"
                         propellant_List_Chosen = "Uranium(VI) Fluoride (UF6) and " + remass_List_Chosen
                         nuclear_Cycle_Chosen = rando(nuclear_cycle)
                         enr_level = rN(8, 87)
                         reactor_Fuel_Chosen = str(enr_level) + "% " + "Uranium-235"
                         coreTemp = rN(5400 + (enr_level * 5), 1000)
                         molmassi = findex(remass_List, remass_List_Chosen)
                         molmass = remass_EVD[molmassi]
                         exhaustVel = (19600 / math.pow(molmass, 0.531))
                     case "Vapor Core":
                         remass_List = ["Hydrogen (H2)", "Nitrogen (N2)", "Ammonia (NH3)", "Water (H2O)",
                                "Oxygen (O2)", "Carbon Dioxide (CO2)", "Carbon Monoxide (CO)"]
                         remass_EVD = [1.782, 14.6, 4.25, 6.587, 16, 14.6, 28]
                         remass_List_Chosen = rando(remass_List)
                         propellant_List_Chosen = "Uranium(VI) Fluoride (UF6) and " + remass_List_Chosen
                         nuclear_Cycle_Chosen = ""
                         reactor_Fuel_Chosen = "93% Uranium-235"
                         propellantState = "Cryogenic Liquid"
                         coreTemp = rN(5500, 1000)
                         molmassi = findex(remass_List, remass_List_Chosen)
                         molmass = remass_EVD[molmassi]
                         exhaustVel = (11800 / math.pow(molmass, 0.531))
                     case "Gas Core":
                         remass_List = ["Hydrogen (H2)", "Nitrogen (N2)", "Ammonia (NH3)", "Water (H2O)",
                                "Oxygen (O2)", "Carbon Dioxide (CO2)", "Carbon Monoxide (CO)"]
                         nuclear_cycle = ["\"Nuclear Lightbulb\"", "\"Vortex Confined\"", "\"Wheel Flow\"",
                                "\"Magnetohydrodynamic(MHD) vortex\"", "\"Open Cycle\""]
                         remass_EVD = [1.782, 14.6, 4.25, 6.587, 16, 14.6, 28]
                         remass_List_Chosen = rando(remass_List)
                         propellant_List_Chosen = "Uranium(VI) Fluoride (UF6) and " + remass_List_Chosen
                         nuclear_Cycle_Chosen = rando(nuclear_cycle)
                         reactor_Fuel_Chosen = "93% Uranium-235"
                         propellantState = "Cryogenic Liquid"
                         coreTemp = rN(13650, 1000)
                         molmassi = findex(remass_List, remass_List_Chosen)
                         molmass = remass_EVD[findex(remass_List, remass_List_Chosen)]
                         exhaustVel = (20405 / math.pow(molmass, 0.531))
                     case "Nuclear SaltWater":
                         nuclear_cycle = ["\"Nuclear Lightbulb\"", "\"Vortex Confined\"", "\"Wheel Flow\"",
                                "\"Magnetohydrodynamic(MHD) vortex\"", "\"Open Cycle\""]
                         fissile_salts = ["Uranium", "Plutonium"]
                         fissile_salt = rando(fissile_salts)
                         nuclear_Cycle_Chosen = rando(nuclear_cycle)
                         if not fissile_salt == "Plutonium":
                             propellant_List_Chosen = fissile_salt + "(IV) TetraBromide (UBr4) + Water (H2O)"
                         else:
                             propellant_List_Chosen = fissile_salt + "(III) TriBromide (PuBr3) + Water (H2O)"
                         remass_List_Chosen = "Water (H2O)"
                         nuclear_Cycle_Chosen = ""
                         propellantState = "Aqueous"
                         enri_level = rN(1, 2)
                         if enri_level == 1:
                             coreTemp = rN(25000, 1000)
                             exhaustVel = rN(65500, 1000)
                             reactor_Fuel_Chosen = "3% " + fissile_salt
                         else:
                             coreTemp = rN(126800, 1000)
                             exhaustVel = rN(4725000, 1000)
                             reactor_Fuel_Chosen = "98% " + fissile_salt
                 #============================================================================================
                 if engine_Cycle_Chosen == "Solid Core" or engine_Cycle_Chosen == "Radioisotope Engine":
                     nzll = ["Contour Bell Nozzle", "Parabolic Bell Nozzle"]
                 else:
                     nzll = ["Contour Bell Nozzle", "Parabolic Bell Nozzle", "Magnetic Virtual Nozzle"]
                 nozzle_Type_List_Chosen = rando(nzll)
                 #============================================================================================
                 cooling_mechanism = ["Radiative Cooling", "Dump Cooling", "Film Cooling", "Regenerative Cooling",
                        "Transpiration Cooling"]
                 pot_uses = ["Upper Stage(Main Propulsion)", "Payload (Main Propulsion)", "Space Tug (Main Propulsion)"]
                 #============================================================================================
                 use = rando(pot_uses)
                 altitude_Of_Operation_Chosen = "80 km+ (Vacuum)"
                 tank_Repressurisation_Chosen = rando(tank_Repressurisation)
                 cooling_Mechanism_Chosen = rando(cooling_mechanism)
                 #============================================================================================
                 if engine_Cycle_Chosen == "Liquid Core" or engine_Cycle_Chosen == "Solid Core" or engine_Cycle_Chosen == "Pulsed Nuclear":
                     reactor_gen = ["Generation III+", "Generation IV", "Generation V", "Generation V+"]
                 elif engine_Cycle_Chosen == "Nuclear SaltWater":
                     reactor_gen = ["Engine has no reactor"]
                 elif engine_Cycle_Chosen == "Radioisotope Engine":
                     reactor_gen = ["Generation I"]
                 else:
                     reactor_gen = ["Generation II", "Generation III", "Generation III+",
                            "Generation IV", "Generation V", "Generation V+"]
                 #============================================================================================
                 reactor_gen_Chosen = rando(reactor_gen)
                 uio97 = rN(1, 456)
                 uio98 = rN(1, 77)
                 if uio97%uio98 != 0:
                    isBimodal = True
                 else:
                    isBimodal = False
                 NzlReturnP = NzlParameters(altitude_Of_Operation_Chosen)
                 parts = NzlReturnP.split(", ")
                 AreaRatio = parts[1]
                 output_nt(engine_Name, engine_Cycle_Chosen, altitude_Of_Operation_Chosen, nuclear_Cycle_Chosen,
                        propellant_List_Chosen, reactor_Fuel_Chosen, nozzle_Type_List_Chosen, exhaustVel,
                        tank_Repressurisation_Chosen, cooling_Mechanism_Chosen, use, reactor_gen_Chosen,
                        isBimodal, remass_List_Chosen, propellantState, AreaRatio, coreTemp)
                 y = y+1
            #============================================================================================
            case "MagnetoPlasmaDynamic Thruster" | "Hall Effect Thruster" | "Gridded Ion Thruster" | "Colloid Thruster"|\
                "Variable Specific Impulse Magnetoplasma Rocket (VASIMR)":
                match engine_Cycle_Chosen:
                    case "Hall Effect Thruster":
                        propellant_List = ["Xe (Xenon)", "Kr (Krypton)", "Ar (Argon)", "Bi (Bismuth)",
                                "I2 (Iodine)", "Mg (Magnesium)", "Zn (Zinc)", "C10H16 (Adamantane)"]
                        propellant_List_Chosen = rando(propellant_List)
                        nozzle_Type_List_Chosen = "Hall Effect Thruster Nozzle"
                    case "Gridded Ion Thruster":
                        propellant_List = ["Xe (Xenon)", "Hg (Mercury)", "Cs (Caesium)"]
                        propellant_List_Chosen = rando(propellant_List)
                        nozzle_Type_List_Chosen = "Electrostatic Ion Nozzle"
                    case "Colloid Thruster":
                        propellant_List_Chosen = "NH2OH+NO3 (Hydroxylammonium nitrate)"
                        nozzle_Type_List_Chosen = "Capillary Emitter-Electrode Cone"
                    case "Variable Specific Impulse Magnetoplasma Rocket (VASIMR)":
                        propellant_List = ["Xe (Xenon)", "Kr (Krypton)", "Ar (Argon)"]
                        propellant_List_Chosen = rando(propellant_List)
                        nozzle_Type_List_Chosen = "VASIMR Magnetic Confinement Nozzle"
                    case "MagnetoPlasmaDynamic Thruster":
                        propellant_List = ["Xe (Xenon)", "Ne (Neon)", "Ar (Argon)", "H2 (Hydrogen)", "N2H4 (Hydrazine)", "Li (Lithium)"]
                        propellant_List_Chosen = rando(propellant_List)
                        nozzle_Type_List_Chosen = "Cathode Plug Magnetic Confinement Nozzle"
                pot_uses = ["Payload (Main Propulsion)", "Space Tug (Main Propulsion)"]
                use = rando(pot_uses)
                powerGen_List = ["Hydrogen Fuel cell", "Nuclear Fission Reactor", "Nuclear Fusion Reactor",
                                 "Photovoltaic Panel", "Solar Thermal Panel", "Radioisotope Thermoelectric Generator (RTG)"]
                powerGen_List_Chosen = rando(powerGen_List)
                altitude_Of_Operation_Chosen = "80 km+ (Vacuum)"
                pwr = str((round(rN(20, 980) / 10)) * 10) + " kW"
                output_et(engine_Name, engine_Cycle_Chosen, altitude_Of_Operation_Chosen, propellant_List_Chosen,
                        nozzle_Type_List_Chosen, powerGen_List_Chosen, use, pwr)
                y = y+1
            #============================================================================================
            case "Monopropellant (Decomposition)":
                propellant_List1 = ["H2O2 (Hydrogen Peroxide)", "N2H4 (Hydrazine)", "NH2OH+NO3 (Hydroxylammonium nitrate)",
                        "65% NH4N(NO2)2 (Ammonium Dinitramide) + 35% CH3OH(Methanol)"]
                nozzle_Type_List1 = ["Conical Nozzle", "Contour Bell Nozzle", "Parabolic Bell Nozzle"]
                propellant_List_Chosen = rando(propellant_List1)
                altitude_Of_Operation_Chosen = "80 km+ (Vacuum)"
                nozzle_Type_List_Chosen = rando(nozzle_Type_List1)
                cooling_mechanism = ["Ablative Cooling", "Radiative Cooling"]
                cooling_Mechanism_Chosen = rando(cooling_mechanism)
                catalyst_Chosen = ""
                match propellant_List_Chosen:
                    case "N2H4 (Hydrazine)" | "65% NH4N(NO2)2 (Ammonium Dinitramide) + 35% CH3OH(Methanol)":
                        catalyst_Chosen = "Iridium coated Alumina Pellets"
                    case "H2O2 (Hydrogen Peroxide)":
                        catalyst = ["KMnO4 (Potassium Permanganate) Honeycomb", "Ag (Silver) Honeycomb",
                        "MnO2 (Manganese Dioxide) Honeycomb", "K2Cr2O7 (Potassium dichromate) Honeycomb",
                        "FeO (Iron (II) oxide)"]
                        catalyst_Chosen = rando(catalyst)
                    case "NH2OH+NO3 (Hydroxylammonium nitrate)":
                        catalyst_Chosen = "Iridium coated Copper Pellets"
                pot_uses = ["Upper Stage(Ullage)", "Upper Stage(Vernier)", "Payload (Main Propulsion)",
                        "Payload (Vernier)", "Space Tug (Ullage)", "Space Tug (Vernier)"]
                use = rando(pot_uses)
                output_monod(engine_Name, engine_Cycle_Chosen, altitude_Of_Operation_Chosen, propellant_List_Chosen,
                        nozzle_Type_List_Chosen, cooling_Mechanism_Chosen, catalyst_Chosen, use)
                y = y+1
            #============================================================================================
            case "Monopropellant (Cold Gas)":
                propellant_List2 = ["Nitrogen (N2)", "Helium (He)", "Carbon Dioxide (CO2)", "Ammonia (NH3)", "Hydrogen (H2)",
                        "Methane (CH4)"]
                nozzle_Type_List1 = ["Conical Nozzle", "Contour Bell Nozzle", "Parabolic Bell Nozzle"]
                propellant_List_Chosen = rando(propellant_List2)
                altitude_Of_Operation_Chosen = "80 km+ (Vacuum)"
                nozzle_Type_List_Chosen = rando(nozzle_Type_List1)
                cooling_Mechanism_Chosen = "Ablative Cooling"
                pot_uses = ["Upper Stage(Ullage)", "Upper Stage(Vernier)", "Payload (Main Propulsion)",
                                     "Payload (Vernier)", "Space Tug (Ullage)", "Space Tug (Vernier)"]
                purpose = rando(pot_uses)
                output_mono(engine_Name, engine_Cycle_Chosen, altitude_Of_Operation_Chosen,
                        propellant_List_Chosen, nozzle_Type_List_Chosen, cooling_Mechanism_Chosen, purpose)
                y = y+1
            #============================================================================================
            case "Expander (Closed)" | "Expander (Open/Bleed)":
                oxidizer_List = ["O2 (Oxygen)", "F2 (Fluorine)", "F2 (Fluorine) + O2 (Oxygen)", "O3 (Ozone)"]
                oxidizer_Chosen = rando(oxidizer_List)
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
                    case "F2 (Fluorine) + O2 (Oxygen)" | "O3 (Ozone)":
                        fuel_List = ["H2 (Hydrogen)", "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                StndrdDet(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen,
                        tank_Repressurisation, altitude_Of_Operation)
                y = y+1
            #============================================================================================
            case "Dual Expander (Closed)" | "Dual Expander (Open/Bleed)":
                oxidizer_List = ["O2 (Oxygen)", "F2 (Fluorine)", "F2 (Fluorine) + O2 (Oxygen)"]
                oxidizer_Chosen = rando(oxidizer_List)
                fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)"]
                fuel_Chosen = ""
                match oxidizer_Chosen:
                    case "O2 (Oxygen)" | "F2 (Fluorine)":
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                    case "F2 (Fluorine) + O2 (Oxygen)": fuel_Chosen = "H2 (Hydrogen)"
                StndrdDet(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen,
                        tank_Repressurisation, altitude_Of_Operation)
                y = y+1
            #============================================================================================
            case "Staged Combustion (Fuel Rich)":
                oxidizer_List = ["O2 (Oxygen)", "F2 (Fluorine)", "F2 (Fluorine) + O2 (Oxygen)", "O3 (Ozone)"]
                oxidizer_Chosen = rando(oxidizer_List)
                fuel_Chosen = ""
                match oxidizer_Chosen:
                    case "O2 (Oxygen)" | "F2 (Fluorine)":
                        fuel_List = ["H2 (Hydrogen)", "NH3 (Ammonia)", "N2H4 (Hydrazine)"]
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                    case "F2 (Fluorine) + O2 (Oxygen)" | "O3 (Ozone)": fuel_Chosen = "H2 (Hydrogen)"
                StndrdDet(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen,
                        tank_Repressurisation, altitude_Of_Operation)
                y = y+1
            #============================================================================================
            case "Staged Combustion (Oxidizer Rich)":
                oxidizer_List = ["O2 (Oxygen)", "O3 (Ozone)", "N2O4 (Nitrogen Tetroxide)"]
                oxidizer_Chosen = rando(oxidizer_List)
                fuel_Chosen = ""
                match oxidizer_Chosen:
                    case "O2 (Oxygen)" | "O3 (Ozone)":
                        fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                                "C6H5NH2 (Aniline)", "NH3 (Ammonia)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                                "CH3OH (Methanol)"]
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                    case "N2O4 (Nitrogen Tetroxide)":
                        fuel_List = ["C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                                "C2H8N2 (UnsymmetricalDimethylHydrazine)"]
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                StndrdDet(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen,
                        tank_Repressurisation, altitude_Of_Operation)
                y = y+1
            #============================================================================================
            case "Full Flow Staged Combustion" | "Combustion Tap Off":
                oxidizer_List = ["O2 (Oxygen)", "F2 (Fluorine)", "F2 (Fluorine) + O2 (Oxygen)", "O3 (Ozone)",
                                 "N2O4 (Nitrogen Tetroxide)"]
                oxidizer_Chosen = rando(oxidizer_List)
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
                    case "F2 (Fluorine) + O2 (Oxygen)" | "O3 (Ozone)":
                        fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                                "C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                                "CH6N2 (MonomethylHydrazine)"]
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                    case "N2O4 (Nitrogen Tetroxide)":
                        fuel_List = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                                "C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                                "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH3OH (Methanol)"]
                        random.shuffle(fuel_List)
                        fuel_Chosen = random.choice(fuel_List)
                StndrdDet(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, tank_Repressurisation, altitude_Of_Operation)
                y = y+1
            #============================================================================================
            case _:
                oxidizer_List = ["O2 (Oxygen)", "F2 (Fluorine)", "F2 (Fluorine) + O2 (Oxygen)", "N2O4 (Nitrogen Tetroxide)",
                                 "H2O2 (Hydrogen Peroxide) 95%", "H2O2 (Hydrogen Peroxide) 85%", "O3 (Ozone)",
                                 "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)", "AK20I: 80% HNO3 + 20% N2O4 (Nitric Acid)",
                                 "AK20K: 80% HNO3 + 20% N2O4 (Nitric Acid)", "AK27I: 73% HNO3 + 27% N2O4 (Nitric Acid)",
                                 "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)"]
                oxidizer_Chosen = rando(oxidizer_List)
                if oxidizer_Chosen == "O2 (Oxygen)":
                    fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                            "C6H5NH2 (Aniline)", "NH3 (Ammonia)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                            "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
                    random.shuffle(fuel_List)
                    fuel_Chosen = random.choice(fuel_List)
                elif oxidizer_Chosen == "F2 (Fluorine)":
                    fuel_List = ["H2 (Hydrogen)", "CH4 (Methane)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                            "C6H5NH2 (Aniline)", "NH3 (Ammonia)", "C2H8N2 (UnsymmetricalDimethylHydrazine)",
                            "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
                    random.shuffle(fuel_List)
                    fuel_Chosen = random.choice(fuel_List)
                elif oxidizer_Chosen == "F2 (Fluorine) + O2 (Oxygen)" or oxidizer_Chosen == "O3 (Ozone)":
                    fuel_List = ["H2 (Hydrogen)", "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
                    random.shuffle(fuel_List)
                    fuel_Chosen = random.choice(fuel_List)
                elif oxidizer_Chosen == "AK20F: 80% HNO3 + 20% N2O4 (Nitric Acid)" or oxidizer_Chosen == "AK20I: 80% HNO3 + 20% N2O4 (Nitric Acid)" or\
                    oxidizer_Chosen == "AK20K: 80% HNO3 + 20% N2O4 (Nitric Acid)" or oxidizer_Chosen == "AK27I: 73% HNO3 + 27% N2O4 (Nitric Acid)" or\
                    oxidizer_Chosen == "AK27P: 73% HNO3 + 27% N2O4 (Nitric Acid)":
                    fuel_List = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                            "CH3OH (Methanol)"]
                    random.shuffle(fuel_List)
                    fuel_Chosen = random.choice(fuel_List)
                elif oxidizer_Chosen == "N2O4 (Nitrogen Tetroxide)" or oxidizer_Chosen == "H2O2 (Hydrogen Peroxide) 95%" or\
                    oxidizer_Chosen == "H2O2 (Hydrogen Peroxide) 85%":
                    fuel_List = ["H2 (Hydrogen)", "C2H5OH(Ethanol) 95%", "C2H5OH(Ethanol) 75%",
                            "C6H5NH2 (Aniline)", "75% CH6N2 + 25% N2H4 (UH-25)", "50% CH6N2 + 50% N2H4 (Aerosine-50)",
                            "C2H8N2 (UnsymmetricalDimethylHydrazine)", "CH6N2 (MonomethylHydrazine)", "N2H4 (Hydrazine)",
                            "CH3OH (Methanol)", "C12H26 (n-Dodecane)"]
                    random.shuffle(fuel_List)
                    fuel_Chosen = random.choice(fuel_List)
                StndrdDet(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, tank_Repressurisation, altitude_Of_Operation)
                y = y+1
    elif fNum >= maxN:
        loc_num = 1
        destination = "C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles/DevData/DataDump"
        if os.path.exists("C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles/DevData/DataDump"):
            while not os.path.exists("C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles/DevData/DataDump" + str(loc_num)):
                loc_num = loc_num + 1
            destination = "C:/Users/Public/Operational_Functional_Block/Python_Projects/GenFiles/DevData/DataDump" + str(loc_num)
        os.mkdir(destination)

        end = count()
        timen = (end - start)
        print(f"Amount of engines created: {y}")
        print(f"Amount of engine files created: {fNum}")
        print(f"Amount of engine files created (Kb): {fNum*50}")
        print(f"Average amount of engines per file: {y/fNum}")
        print(f"Average size of one engine (Kb): {(50 * fNum)/y}")
        print(f"Average count taken to generate one engine: {(timen/y)}")
        if timen < 60:
            print(f"Total run count: {timen} secs")
        elif timen / 60 < 2:
            print(f"Total run count: {math.floor(timen/60)} min {timen%60} secs")
        else:
            print(f"Total run count: {math.floor(timen/60)} mins {timen%60} secs")

        fin = open(destination + "/dev.txt", "at")
        fin.write(f"Amount of engines created: {y}")
        fin.write(f"Amount of engine files created: {fNum}")
        fin.write(f"Amount of engine files created (Kb): {fNum * 50}")
        fin.write(f"Average amount of engines per file: {y/fNum}")
        fin.write(f"Average size of one engine (Kb): {(50 * fNum)/y}")
        fin.write(f"Average count taken to generate one engine: {(timen/y)}")
        if timen < 60:
            fin.write(f"Total run count: {timen} secs")
        elif timen / 60 < 2:
            fin.write(f"Total run count: {math.floor(timen / 60)} min {timen % 60} secs")
        else:
            fin.write(f"Total run count: {math.floor(timen / 60)} mins {timen % 60} secs")
        fin.close()

        xsa, ysa, fig = np.array(mpl_xs), np.array(mpl_ysa), pylab.gcf()
        fig.canvas.manager.set_window_title('Graph of testing')
        plt.subplot(1, 2, 1)
        plt.title(EngineType, fontsize=16)
        plt.xlabel('Time (s)')
        plt.ylabel('Number of files')
        plt.xticks(np.arange(0, max(xsa) + max(xsa)/20, round(max(xsa)/10)))
        plt.yticks(np.arange(0, max(ysa) + max(ysa)/20, max(ysa)/20))
        plt.plot(xsa, ysa, linestyle="-", color="red", linewidth=1.1)
        plt.grid(linestyle="--")
        plt.savefig(destination + "/dev_dataA.png")
        plt.suptitle("Graph of data", fontsize=32)

        xsb, ysa, fig = np.array(mpl_xs), np.array(mpl_ysa), pylab.gcf()
        fig.canvas.manager.set_window_title('Graph of testing')
        plt.title(EngineType, fontsize=16)
        ysb = np.array(mpl_ysb)
        plt.xlabel('Time (s)')
        plt.ylabel('Percentage of RAM used')
        plt.xticks(np.arange(0, max(xsb) + max(xsb)/20, round(max(xsb)/20)))
        plt.yticks(np.arange(0, 100, 5))
        plt.plot(xs, ysb, linestyle="-", color="red", linewidth=1.1)
        plt.grid(linestyle="--")
        plt.savefig(destination + "/dev_dataB.png")
        plt.suptitle("Graph of data", fontsize=32)

        exit(0)
"""    
else:
while not repeatCommand.upper == "Y" and not repeatCommand.upper == "N" and not repeatCommand.upper == "YES" and not repeatCommand.upper == "NO":
    print(f"'" + repeatCommand + "'" + " is not a registered command, please input one of the appropriate commands [Y/N] or [Yes/No]")
    repeatCommand = str(input(">>>>> ")).upper()
    if repeatCommand == "Y" or repeatCommand == "N" or repeatCommand == "YES" or repeatCommand == "NO":
        break
"""