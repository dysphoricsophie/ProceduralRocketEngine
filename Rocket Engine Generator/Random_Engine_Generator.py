from asyncio import wait
import os
import subprocess
import sys
import random
import string
from time import sleep
import webbrowser
import pygame
from pygame.rect import Rect

pygame.init()
        
width, height = 1000, 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
font = pygame.font.Font('freesansbold.ttf', 32)
Blue = (0,0,255)
White = (255,255,255)
Light_Blue = (180, 221, 255)
Gray = (200, 200, 200)
lilDarkerGray = (165, 165, 165)
Dark_Gray = (20, 20, 20)
Black = (0,0,0)
def rsg():
    pass
def reg():
    class DropDown():
        def __init__(self, color_menu, color_option, x, y, w, h, font, main, options):
            self.color_menu = color_menu
            self.color_option = color_option
            self.rect = pygame.Rect(x, y, w, h)
            self.font = font
            self.main = main
            self.options = options
            self.draw_menu = False
            self.menu_active = False
            self.active_option = -1

        def draw(self, surf):
            pygame.draw.rect(surf, self.color_menu[self.menu_active], self.rect, 0)
            msg = self.font.render(self.main, 1, (0, 0, 0))
            surf.blit(msg, msg.get_rect(center = self.rect.center))

            if self.draw_menu:
                for i, text in enumerate(self.options):
                    rect = self.rect.copy()
                    rect.y += (i+1) * self.rect.height
                    pygame.draw.rect(surf, self.color_option[1 if i == self.active_option else 0], rect, 0)
                    msg = self.font.render(text, 1, (0, 0, 0))
                    surf.blit(msg, msg.get_rect(center = rect.center))

        def update(self, events):
            mpos = pygame.mouse.get_pos()
            self.menu_active = self.rect.collidepoint(mpos)
            
            self.active_option = -1
            for i in range(len(self.options)):
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height
                if rect.collidepoint(mpos):
                    self.active_option = i
                    break

            if not self.menu_active and self.active_option == -1:
                self.draw_menu = False

            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.menu_active:
                        self.draw_menu = not self.draw_menu
                    elif self.draw_menu and self.active_option >= 0:
                        self.draw_menu = False
                        return self.active_option
            return -1
    #------------------------------------------------------------------
    Btn_sps = 10
    cntrx = (width/6)
    main_y = 212

    # main button
    btnw1, btnh1 = 210, 75
    xs1 = cntrx - (btnw1/2)
    ys1 = main_y
    neil1 = [xs1, ys1, btnw1, btnh1]
    jim_bob1 = tuple(neil1)
    random_gen = pygame.Rect(jim_bob1)
    #------------------------------------------------------------------
    btnw2, btnh2 = 210, 75
    xs2 = cntrx - (btnw2/2)
    ys2 = ys1 + 85
    neil2 = [xs2, ys2, btnw2, btnh2]
    jim_bob2 = tuple(neil2)
    basic_gen = pygame.Rect(jim_bob2)
    #------------------------------------------------------------------
    btnw3, btnh3 = 210, 75
    xs3 = cntrx - (btnw3/2)
    ys3 = ys2 + 85
    neil3 = [xs3, ys3, btnw3, btnh3]
    jim_bob3 = tuple(neil3)
    advanced_gen = pygame.Rect(jim_bob3)

    # credits + guide
    btnw4, btnh4 = 98, 38
    xs4 = (cntrx - 53) - (btnw4/2)
    ys4 = ys3 + 85
    neil4 = [xs4, ys4, btnw4, btnh4]
    jim_bob4 = tuple(neil4)
    guide = pygame.Rect(jim_bob4)
    #------------------------------------------------------------------
    btnw5, btnh5 = 98, 38
    xs5 = (cntrx + 53) - (btnw5/2)
    ys5 = ys3 + 85
    neil5 = [xs5, ys5, btnw5, btnh5]
    jim_bob5 = tuple(neil5)
    credits = pygame.Rect(jim_bob5)

    # exit
    btnw6, btnh6 = 50, 20
    xs6 = 10
    ys6 = 572
    neil6 = [xs6, ys6, btnw6, btnh6]
    jim_bob6 = tuple(neil6)
    exit_btn = pygame.Rect(jim_bob6)

    # social media
    imp1 = pygame.image.load("./Assets/reddit.png")
    btnw8, btnh8 = 40, 40
    imp1 = pygame.transform.scale(imp1, (btnw8, btnh8))
    xs8 = 882 - (btnw8)
    ys8 = 590 - (btnh8)
    neil8 = [xs8, ys8, btnw8, btnh8]
    jim_bob8 = tuple(neil8)
    #------------------------------------------------------------------
    imp2 = pygame.image.load("./Assets/discord.png")
    btnw9, btnh9 = 40, 40
    imp2 = pygame.transform.scale(imp2, (btnw9, btnh9))
    xs9 = (xs8 + (btnw9+Btn_sps))
    ys9 = 590 - (btnh9)
    neil9 = [xs9, ys9, btnw9, btnh9]
    jim_bob9 = tuple(neil9)
    #------------------------------------------------------------------
    imp3 = pygame.image.load("./Assets/website.png")
    btnw10, btnh10 = 40, 40
    imp3 = pygame.transform.scale(imp3, (btnw10, btnh10))
    xs10 = (xs9 + (btnw10+Btn_sps))
    ys10 = 590 - (btnh10)
    neil10 = [xs10, ys10, btnw10, btnh10]
    jim_bob10 = tuple(neil10)

    #Back Button
    ggg = pygame.image.load("./Assets/reload.png")
    gge = ggg.copy()
    imp4 = pygame.transform.flip(gge, True, False)
    btnw11, btnh11 = 30, 30
    imp4 = pygame.transform.scale(imp4, (btnw11, btnh11))
    xs11 = 365
    ys11 = 507
    neil11 = [xs11, ys11, btnw11, btnh11]
    jim_bob11 = tuple(neil11)

    #Reload Button
    imp5 = pygame.image.load("./Assets/reload.png")
    btnw12, btnh12 = 30, 30
    imp5 = pygame.transform.scale(imp5, (btnw12, btnh12))
    xs12 = 400
    ys12 = 507
    neil12 = [xs12, ys12, btnw12, btnh12]
    jim_bob12 = tuple(neil12)
    #------------------------------------------------------------------
    reddit_btn = screen.blit(imp1, jim_bob8)
    discord_btn = screen.blit(imp2, jim_bob9)
    web_btn = screen.blit(imp3, jim_bob10)
    back_btn = screen.blit(imp4, jim_bob11)
    reload_btn = screen.blit(imp5, jim_bob12)
    def search_str(file_path, word):
        with open(file_path, 'r') as file:
            content = file.read()
            if word in content:
                return True
            else:
                return False
    def guide_code():
        info = ["The Random Engine Generator App does exactly as you would thing it would ",
        "does, it generates rocket engines with a degree of randomness depending ",
        "on the option chosen by the user with settings such as Basic Generation, ",
        "Random Generation and Advanced generation which adjusts to the user's ",
        "knowledge of rocket science and rocket engine mechanics.",
        ""]
        button_info = ["",
        "Here is what the buttons do: ",
        " ---> Random Generation - randomly generates an engine with in-depth data like ",
        "      the propellant flow cycle and nozzle geometry. We recomend that new users to use ",
        "      this setting to learn and generate rocket engines.",
        " ---> Basic Generation - Makes use of simple prompts to generate ",
        "      the engine of your dreams. We recomend this option to users that ",
        "     are a bit more familiar with rocket science terms and the app.",
        " ---> Advanced Generation - Uses prompts that will ask for more ",
        "      in-depth questions to the user like the nozzle geometry and engine ",
        "      gimbal range. We only recomend this option for the most experienced ",
        "      users out there.",
        ""]
        source_code_access = ["", "Here is the link to the source code: http://pastebin.com/u/MAKS_Enjoyer",
        "(Btw if you choose to edit my code, give me some credit please)"]
        text = [info, button_info, source_code_access]
        list(text)
        jake = 173
        for i in text:
            for y in i:
                if i.index(y) == 0:
                    jimy = [380,jake]
                    font = pygame.font.SysFont("Segoe UI", 13)
                    textsurface = font.render(y, True, Gray)
                    screen.blit(textsurface, jimy)
                else:
                    jake = jake + 19
                    jimy = [380,jake]
                    font = pygame.font.SysFont("Segoe UI", 13)
                    textsurface = font.render(y, True, Gray)
                    screen.blit(textsurface, jimy)
            jimy = [380, (jake + 19)]
            font = pygame.font.SysFont("Segoe UI", 13)
            textsurface = font.render("", True, Gray)
            screen.blit(textsurface, jimy)
    def random_code():
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
            outputEOD = "Engine Designation: " + ENN
            outputTP = "Propellant: " + PLC
            outputAOC = "Altitude Of Operation: " + AOOC
            outputENG = "Exhaust Nozzle Geometry: " + NTLC
            outputNCM = "Nozzle Cooling Mechanism: " + CMC
            outputEPC = "Propellant catalyst: " + CCC

            MonoD = [outputEOD, outputTP, outputAOC, outputENG, outputNCM, outputEPC]
            return MonoD

        def outputMono(ENN, ECC, AOOC, PLC, NTLC, CMC):
            outputEOD = "Engine Designation: " + ENN
            outputEFC = "Flow Cycle: " + ECC
            outputTP = "Propellant: " + PLC
            outputAOC = "Altitude Of Operation: " + AOOC
            outputENG = "Exhaust Nozzle Geometry: " + NTLC
            outputNCM = "Nozzle Cooling Mechanism: " + CMC

            Mono = [outputEOD, outputEFC, outputTP, outputAOC, outputENG, outputNCM]
            return Mono

        def outputEx(ENN, ECC, OCC, FCC, AOOC, NTC, TRR, CMC, isHyp):
            isCryo = False
            if OCC == "O3 (Ozone)" or OCC == "F2 (Fluorine)" or OCC == "F2 (Fluorine) + O2 (Oxygen)" or \
                    OCC == "ClF3 (Chlorine Trifluoride)" or OCC == "ClF5 (Chlorine Pentafluoride)" or OCC == "O2 (Oxygen)":
                isCryo = True
            if FCC == "CH3OH (Methanol)" or FCC == "C12H24 (Kerosene)" or FCC == "H2 (Hydrogen)" or FCC == "C2H5OH(Ethanol) 85%" or \
                    FCC == "C2H5OH(Ethanol) 75%" or FCC == "B2H6 (Diborane)" or FCC == "B5H9 (Pentaborane)" or FCC == "NH3 (Ammonia)" or FCC == "CH4 (Methane)":
                isCryo = True
            if isHyp:
                message = "Propellant properties: Hypergolic"
            else:
                message = "Propellant properties: Not Hypergolic"
            if isCryo is True and isHyp is True:
                message = message + " and cryogenic"
            elif isCryo is True and isHyp is False:
                message = message + " but cryogenic"
            elif isCryo is False and isHyp is True:
                message = message + " but not cryogenic"
            else:
                message = message + " or cryogenic"
            uio96 = random.randint(1, 1000)
            uio97 = random.randint(1, 12)
            if uio96 % uio97 == 0:
                Throttle_MinV = random.randint(1, 100)
                Throttle_MaxV = random.randint(100, 115)
                ThrottleRange = str(Throttle_MinV) + " - " + str(Throttle_MaxV) + "%"
            else:
                ThrottleRange = "Not Throttleable"
            gimbalangle = random.randint(0, 15)
            if gimbalangle <= 0 or AOOC == "80 km+ (Vacuum)":
                piss = "None"
            else:
                piss = str(gimbalangle) + " degrees"

            outputEOD = "Engine Designation: " + ENN
            outputPFC = "Flow Cycle: " + ECC
            outputEO = "Engine Oxidizer: " + OCC
            outputEF = "Engine Fuel: " + FCC
            outputAOC = "Altitude Of Operation: " + AOOC
            outputNTC = "Exhaust Nozzle Geometry: " + NTC
            outputHCC = message
            outputEGR = "Engine Gimbal Range: " + piss
            outputTRM = "Tank repressurisation Method: " + TRR
            outputNCM = "Nozzle Cooling Mechanism: " + CMC
            outputETR = "Engine Throttle Range: " + ThrottleRange

            EX = [outputEOD, outputPFC, outputEO, outputEF, outputAOC, outputNTC, outputHCC, outputEGR, outputTRM, outputNCM, outputETR]
            return EX

        def outputNt(ENN, ECC, AOOC, NCC, PLC, RFC, NTLC, TRC, CMC, bi):
            outputEOD = "Engine Designation: " + ENN
            outputPFC = "Flow Cycle: " + NCC + " " + ECC
            outputERP = "Propellant (Remass): " + PLC
            outputERF = "Reactor Fuel: " + RFC
            outputEBM = "Engine Bi-modality: " + str(bi)
            outputAOP = "Altitude Of Operation: " + AOOC
            outputENG = "Exhaust Nozzle Geometry: " + NTLC
            outputTRM = "Tank repressurisation Method: " + TRC
            outputNCM = "Nozzle Cooling Mechanism: " + CMC

            NT = [outputEOD, outputPFC, outputERP, outputERF, outputEBM, outputAOP, outputENG, outputTRM, outputNCM]
            return NT

        def outputEt(ENN, ECC, AOOC, PLC, NTLC, pygameLC):
            pwr = str(random.randint(20, 1000)) + " kW"
            outputEOD = "Engine Designation: " + ENN
            outputPFC = "Flow Cycle: " + ECC
            outputERP = "Propellant(Remass): " + PLC
            outputAOC = "Altitude Of Operation: " + AOOC
            outputENG = "Exhaust Nozzle Geometry: " + NTLC
            outputEPS = "Engine Power Source: " + pygameLC
            outputRPL = "Rated Power Level: " + pwr

            ET = [outputEOD, outputPFC, outputERP, outputAOC, outputENG, outputEPS, outputRPL]
            return ET

        def outputDef(ENN, ECC, OCC, FCC, AOOC, NTC, TRR, CMC, isHyp):
            isCryo = False
            if OCC == "O3 (Ozone)" or OCC == "F2 (Fluorine)" or OCC == "F2 (Fluorine) + O2 (Oxygen)" or \
                    OCC == "ClF3 (Chlorine Trifluoride)" or OCC == "ClF5 (Chlorine Pentafluoride)" or OCC == "O2 (Oxygen)":
                isCryo = True
            if FCC == "CH3OH (Methanol)" or FCC == "C12H24 (Kerosene)" or FCC == "H2 (Hydrogen)" or FCC == "C2H5OH(Ethanol) 85%" or \
                    FCC == "C2H5OH(Ethanol) 75%" or FCC == "B2H6 (Diborane)" or FCC == "B5H9 (Pentaborane)" or FCC == "NH3 (Ammonia)" or FCC == "CH4 (Methane)":
                isCryo = True
            if isHyp:
                message = "Propellant properties: Hypergolic"
            else:
                message = "Propellant properties: Not Hypergolic"
            if isCryo is True and isHyp is True:
                message = message + " and cryogenic"
            elif isCryo is True and isHyp is False:
                message = message + " but cryogenic"
            elif isCryo is False and isHyp is True:
                message = message + " but not cryogenic"
            else:
                message = message + " or cryogenic"
            uio96 = random.randint(1, 1000)
            uio97 = random.randint(1, 12)
            if uio96 % uio97 == 0:
                Throttle_MinV = random.randint(1, 100)
                Throttle_MaxV = random.randint(100, 115)
                ThrottleRange = str(Throttle_MinV) + " - " + str(Throttle_MaxV) + "%"
            else:
                ThrottleRange = "Not Throttleable"
            gimbalangle = random.randint(0, 15)
            if gimbalangle <= 0 or AOOC == "80 km+ (Vacuum)":
                piss = "None"
            else:
                piss = str(gimbalangle) + " degrees"
            outputEOD = "Engine Designation: " + ENN
            outputPFC = "Flow Cycle: " + ECC
            outputEO = "Engine Oxidizer: " + OCC
            outputEF = "Engine Fuel: " + FCC
            outputAOC = "Altitude Of Operation: " + AOOC
            outputNTC = "Exhaust Nozzle Geometry: " + NTC
            outputHCC = message
            outputEGR = "Engine Gimbal Range: " + piss
            outputTRM = "Tank repressurisation Method: " + TRR
            outputNCM = "Nozzle Cooling Mechanism: " + CMC
            outputETR = "Engine Throttle Range: " + ThrottleRange

            DEF = [outputEOD, outputPFC, outputEO, outputEF, outputAOC, outputNTC, outputHCC, outputEGR, outputTRM, outputNCM, outputETR]
            return DEF

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
        nuclear_Cycle_Chosen = ""
        match engine_Cycle_Chosen:
            case "Gas Core" | "Liquid Core" | "Solid Core" | "Pulsed Nuclear" | "Nuclear SaltWater" | "Pebble-Bed Core":
                cooling_mechanism = ["Radiative Cooling", "Dump Cooling", "Film Cooling", "Regenerative Cooling", "Transpiration Cooling"]
                match engine_Cycle_Chosen:
                    case "Gas Core":
                        remass_List = ["Hydrogen (H2)", "Nitrogen (N2)", "Monoatomic Hydrogen (H)", "Ammonia (NH3)",
                                        "Water (H2O)", "Oxygen (O2)", "Carbon Dioxide (CO2)", "Carbon Monoxide (CO)", "Methane (CH4)"]
                        random.shuffle(remass_List)
                        remass_List_Chosen = random.choice(remass_List)
                        propellant_List_Chosen = "Uranium HexaFluoride (UF6) + " + remass_List_Chosen
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
                        propellant_List_Chosen = "Uranium HexaFluoride (UF6) + " + remass_List_Chosen
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
                bimodal = False
                if bimodal_decider % 2 == 0:
                    bimodal = True
                NT = outputNt(engine_Name, engine_Cycle_Chosen, altitude_Of_Operation_Chosen, nuclear_Cycle_Chosen,
                            propellant_List_Chosen, reactor_Fuel_Chosen, nozzle_Type_List_Chosen,
                            tank_Repressurisation_Chosen, cooling_Mechanism_Chosen, bimodal)
                return NT
            
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
                ET = outputEt(engine_Name, engine_Cycle_Chosen, altitude_Of_Operation_Chosen,
                            propellant_List_Chosen, nozzle_Type_List_Chosen, powerGen_List_Chosen)
                return ET
            
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
                MonoD = outputMonod(engine_Name, altitude_Of_Operation_Chosen, propellant_List_Chosen,nozzle_Type_List_Chosen,
                            cooling_Mechanism_Chosen, catalyst_Chosen)
                return MonoD
                
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
                Mono = outputMono(engine_Name, engine_Cycle_Chosen, altitude_Of_Operation_Chosen, propellant_List_Chosen,
                            nozzle_Type_List_Chosen, cooling_Mechanism_Chosen)
                return Mono
                
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
                EX = outputEx(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, altitude_Of_Operation_Chosen,
                            nozzle_Type_Chosen, "Autogenous", cooling_Mechanism_Chosen, isHype)
                return EX
                
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
                EX = outputEx(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, altitude_Of_Operation_Chosen,
                            nozzle_Type_Chosen, "Autogenous", cooling_Mechanism_Chosen, isHype)
                return EX
                
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
                DEF = outputDef(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, altitude_Of_Operation_Chosen,
                            nozzle_Type_Chosen, tank_Repressurisation_Chosen, cooling_Mechanism_Chosen, isHype)
                return DEF
            
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
                DEF = outputDef(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, altitude_Of_Operation_Chosen,
                            nozzle_Type_Chosen, tank_Repressurisation_Chosen, cooling_Mechanism_Chosen, isHype)
                return DEF
            
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
                DEF = outputDef(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, altitude_Of_Operation_Chosen,
                            nozzle_Type_Chosen, tank_Repressurisation_Chosen, cooling_Mechanism_Chosen, isHype)
                return DEF
            
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
                DEF = outputDef(engine_Name, engine_Cycle_Chosen, oxidizer_Chosen, fuel_Chosen, altitude_Of_Operation_Chosen,
                            nozzle_Type_Chosen, tank_Repressurisation_Chosen, cooling_Mechanism_Chosen, isHype)
                return DEF
    def basic_code():
        pass
    def advanced_code():
        pass
    def credits_code():
        jimy = [675,310]
        font = pygame.font.SysFont("Arial", 30)
        textsurface = font.render("Creator: MAKS_Enjoyer", False, Gray) 
        jimy[0] = (jimy[0] - (textsurface.get_width()/2))
        screen.blit(textsurface, jimy)
    def render(color, input_rect, base_font, user_text, IsCredits, IsRandom, IsGuide, IsBasic, current, main_y):
        screen.fill((Dark_Gray))
        pygame.draw.rect(screen, Gray, random_gen)
        pygame.draw.rect(screen, Gray, basic_gen)
        pygame.draw.rect(screen, Gray, advanced_gen)
        pygame.draw.rect(screen, Gray, guide)
        pygame.draw.rect(screen, Gray, credits)
        pygame.draw.rect(screen, Gray, exit_btn)
        reddit_btn = screen.blit(imp1, jim_bob8)
        discord_btn = screen.blit(imp2, jim_bob9)
        web_btn = screen.blit(imp3, jim_bob10)
        #------------------------------------------------------------------
        #Rectangle Thingy for the screen
        (x, y, width, height) = (360, 162, 620, 380)
        border_width = 3
        pygame.draw.rect(screen, Dark_Gray, (x, y, width, height))
        pygame.draw.rect(screen, Gray, (x, y, width, height), width=border_width)
        #-------------------------------------------------------------------
        font1 = pygame.font.SysFont("Segoe UI Black", 70)
        textsurface1 = font1.render("Rocket Engine Builder", True, Gray)  
        jim1 = textsurface1.get_rect(center = screen.get_rect().center)
        jim1[1] = 0
        screen.blit(textsurface1, jim1)
        #-------------------------------------------------------------------
        font2 = pygame.font.SysFont("Arial", 20, True)
        textsurface2 = font2.render("Choose a configuration:", True, Gray)    
        jim2 = textsurface2.get_rect(center = screen.get_rect().center)
        jim2[0] = (167 - (textsurface2.get_width()/2))
        jim2[1] = main_y - 32
        screen.blit(textsurface2, jim2)
        #-------------------------------------------------------------------
        font2 = pygame.font.SysFont("Arial", 18)
        textsurface2 = font2.render("Random Generation", True, Dark_Gray)  
        jim2 = textsurface2.get_rect(center = screen.get_rect().center)
        jim2[0] = cntrx - 80
        jim2[1] = ys1 + 25
        screen.blit(textsurface2, jim2)    
        #-------------------------------------------------------------------
        font2 = pygame.font.SysFont("Arial", 18)
        textsurface2 = font2.render("Basic Generation", True, Dark_Gray)  
        jim2 = textsurface2.get_rect(center = screen.get_rect().center)
        jim2[0] = cntrx - 71
        jim2[1] = ys1 + 110
        screen.blit(textsurface2, jim2)      
        #-------------------------------------------------------------------
        font2 = pygame.font.SysFont("Arial", 18)
        textsurface2 = font2.render("Advanced Generation", True, Dark_Gray)  
        jim2 = textsurface2.get_rect(center = screen.get_rect().center)
        jim2[0] = cntrx - 86
        jim2[1] = ys2 + 111
        screen.blit(textsurface2, jim2) 
        #------------------------------------------------------------------- 
        font2 = pygame.font.SysFont("Arial", 18)
        textsurface2 = font2.render("Credits", True, Dark_Gray)  
        jim2 = textsurface2.get_rect(center = screen.get_rect().center)
        jim2[0] = ((cntrx + 53) - (btnw4/2)) + 19
        jim2[1] = main_y + 263
        screen.blit(textsurface2, jim2) 
        #------------------------------------------------------------------- 
        font2 = pygame.font.SysFont("Arial", 18)
        textsurface2 = font2.render("Help", True, Dark_Gray)  
        jim2 = textsurface2.get_rect(center = screen.get_rect().center)
        jim2[0] = ((cntrx - 53) - (btnw4/2)) + 30
        jim2[1] = main_y + 263
        screen.blit(textsurface2, jim2) 
        #------------------------------------------------------------------- 
        if IsRandom == False and IsAdvanced == False and IsBasic == False:
            jimy2 = [675,133]
            font4 = pygame.font.SysFont("Arial", 20)
            textsurface4 = font4.render("Press a button on your left to start...", True, Gray) 
            jimy2[0] = (jimy2[0] - (textsurface4.get_width()/2))
            screen.blit(textsurface4, jimy2)          
            guide_code() 
        #-------------------------------------------------------------------
        font3 = pygame.font.SysFont("Garamond", 22)
        textsurface3 = font3.render("EXIT", False, Dark_Gray)
        jim3 = [17,575]
        screen.blit(textsurface3, jim3)     
        #-------------------------------------------------------------------
        if IsCredits == True:
            credits_code()
        #-------------------------------------------------------------------
        if IsRandom == True:
            back_btn = screen.blit(imp4, jim_bob11)
            reload_btn = screen.blit(imp5, jim_bob12)
            Foldr_path = r"C:/Users/Public/Operational_Functional_Block/Python_Projects/LogData/RandomSection"
            filepath = os.path.join(Foldr_path, 'log_file.txt')
            if not os.path.exists(Foldr_path):
                os.makedirs(Foldr_path)
            f = open(filepath, "a")
            ass = current[0]
            for i in current:
                if current.index(i) == 0:
                    jimy = [680,173]
                    font = pygame.font.SysFont("Segoe UI", 22)
                    textsurface = font.render(i, True, Gray)
                    jimy[0] = (jimy[0] - (textsurface.get_width()/2))
                    screen.blit(textsurface, jimy)
                else:
                    jimy = [380,((current.index(i)*19) + 200)]
                    font = pygame.font.SysFont("Segoe UI", 14)
                    textsurface = font.render(i, True, Gray)
                    screen.blit(textsurface, jimy)
            if search_str(filepath, ass) == False:
                for i in current:
                    if current.index(i) == 0:
                        f.write(i + '\n')
                    else:
                        if current.index(i) == (len(current)-1):
                            f.write(i + '\n' + '\n')
                            f.close()
                        else:
                            f.write(i + '\n')
            IsRandom = False
        #-------------------------------------------------------------------
        if IsAdvanced == True:
            pygame.draw.rect(screen, color, input_rect)
            text_surface = base_font.render(user_text, True, Gray)
            screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            input_rect.w = max(100, text_surface.get_width()+10) 
            advanced_code() 
        #-------------------------------------------------------------------
        if IsGuide == True:
            guide_code()
        #-------------------------------------------------------------------
        if IsBasic == True:
            w01 = 335
            h01 = 50
            x01 = 680 - (w01/2)
            y01 = 340 - (h01/2)
            list1 = DropDown(
            [(200, 200, 200), (165, 165, 165)], [(182, 182, 182), (172, 172, 172)],
            x01, y01, w01, h01, pygame.font.SysFont("Segoe UI Black", 18), 
            "Select the Purpose of the Engine", ["Lander", "Launcher", "SpaceTug"])

            selected_option = list1.update(events)
            if selected_option >= 0:
                sock = list1.options[selected_option]
                print(sock)
            list1.draw(screen)
            basic_code()
        #-------------------------------------------------------------------
        pygame.display.flip()

    clock.tick(60)
    run = True
    IsBasic = False
    IsGuide = False
    IsRandom = False
    IsCredits = False
    IsAdvanced = False
    base_font = pygame.font.Font(None, 32)
    user_text = ""
    basic_info = ""
    color_active = (0,0,0)
    color_passive = (0,0,0)
    color = color_passive
    input_rect = pygame.Rect(400, 200, 140, 32)
    active = False
    count = -1
    prevR = []
    current = []
    while run:
        render(color, input_rect, base_font, user_text, IsCredits, IsRandom, IsGuide, IsBasic, current, main_y)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos 
                if IsRandom == True:
                    if back_btn.collidepoint(mouse_pos):
                        IsBasic = False
                        IsGuide = False
                        IsCredits = False
                        IsAdvanced = False
                        if prevR.index(current) > 0:
                            current = prevR[prevR.index(current)-1]
                        else:
                            pass
                    if reload_btn.collidepoint(mouse_pos):
                        IsBasic = False
                        IsGuide = False
                        IsRandom = True
                        IsCredits = False
                        IsAdvanced = False
                        if (prevR.index(current) + 1) <= count and count > 2:
                            if next + 2 >= len(prevR.index(current)):
                                next = len(prevR.index(current))+1
                            else:
                                next = prevR.index(current)+2
                            current = prevR[next]
                            print("Count = " + str(count))
                            print("Current Index = " + str(prevR.index(current)))
                        elif (prevR.index(current) + 1) > count:
                            current = random_code()
                            prevR.append(current)
                            print("Count = " + str(count))
                            print("Current Index = " + str(prevR.index(current)))
                        else:
                            print("EdgeCase: Error encountered while buttons were buttoning")
                            print("Count = " + str(count))
                            print("Current Index = " + str(prevR.index(current)))
                        count = count + 1
                        if count > prevR.index(current):
                            count = prevR.index(current)
                if random_gen.collidepoint(mouse_pos):
                    IsBasic = False
                    IsGuide = False
                    IsRandom = True
                    IsCredits = False
                    IsAdvanced = False
                    if count <= 0:
                        current = random_code()
                    prevR.append(current)
                    count = count + 1
                    print("Count = " + str(count))
                    print("Current Index = " + str(prevR.index(current)))
                if basic_gen.collidepoint(mouse_pos):
                    IsBasic = True
                    IsGuide = False
                    IsRandom = False
                    IsCredits = False
                    IsAdvanced = False
                if advanced_gen.collidepoint(mouse_pos):
                    IsBasic = False
                    IsGuide = False
                    IsRandom = False
                    IsCredits = False
                    IsAdvanced = True 
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if input_rect.collidepoint(event.pos):
                            active = True
                        else:
                            active = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        elif event.key == pygame.K_RETURN:
                            final = user_text
                            if final != "trans rights are human rights":
                                user_text = ""
                        else:
                            user_text += event.unicode
                    if active:
                        color = color_active
                    else:
                        color = color_passive       
                    #-------------------------------------------------------------------    
                if guide.collidepoint(mouse_pos):
                    IsBasic = False
                    IsGuide = True
                    IsRandom = False
                    IsCredits = False
                    IsAdvanced = False
                    guide_code()
                if credits.collidepoint(mouse_pos):
                    IsBasic = False
                    IsGuide = False
                    IsRandom = False
                    IsCredits = True
                    IsAdvanced = False
                if reddit_btn.collidepoint(mouse_pos):
                    webbrowser.open(r"https://reddit.com/")    
                if discord_btn.collidepoint(mouse_pos):
                    webbrowser.open(r"https://youtube.com/")    
                if web_btn.collidepoint(mouse_pos):
                    webbrowser.open(r"https://stackoverflow.com/")      
                if exit_btn.collidepoint(mouse_pos):
                    sys.exit()     
        if IsBasic == True:
            IsGuide = False
            IsRandom = False
            IsCredits = False
            IsAdvanced = False
            list1 = DropDown(
                [(200, 200, 200), (165, 165, 165)],
                [(182, 182, 182), (172, 172, 172)],
                (680-167), (340-25), 335, 50, 
                pygame.font.SysFont(None, 30), 
                "Select the Purpose of the Engine", ["Lander", "Launcher", "SpaceTug"])
            selected_option = list1.update(events)
            if selected_option >= 0:
                basic_info = list1.options[selected_option]
                print(basic_info)
            list1.draw(screen)                                                                
        render(color, input_rect, base_font, user_text, IsCredits, IsRandom, IsGuide, IsBasic, current, main_y)        
    pygame.quit()
reg()