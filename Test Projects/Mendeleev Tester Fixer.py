from mendeleev import element

def score_eval(data):
    ind = 0
    mp_worth = 0.475
    den_worth = 0.7125
    tc_worth = 0.105
    shc_worth = 0.1075

    name = data[0]
    melt_p = data[1]
    dens = data[2]
    ther_con = data[3]
    spef_hc = data[4]

    try: mp_s = (melt_p*mp_worth)
    except:
        mp_s = 0
        ind = + 1
    try: den_s = (dens*den_worth)
    except:
        den_s = 0
        ind = + 1
    try: tc_s = (ther_con*tc_worth)
    except:
        tc_s = 0
        ind = + 1
    try: shc_s = (spef_hc*shc_worth)
    except:
        shc_s = 0
        ind = + 1

    if ind > 0: name = name + str(f"[SOME DATA UNAVAILABLE:{ind}]")

    total = (mp_s + den_s + tc_s + shc_s)
    return total, name
elemA = ""
elemB = ""
while elemA != "Quit" and "Exit" and elemB != "Quit" and "Exit":
    elemA = input("Type the name of elementA:  ")
    elemB = input("Type the name of elementB:  ")

    try: mp_sA = element(elemA).melting_point
    except: mp_sA = 0
    try: den_sA = element(elemA).density
    except: den_sA = 0
    try: tc_sA = element(elemA).thermal_conductivity
    except: tc_sA = 0
    try: shc_sA = element(elemA).molar_heat_capacity
    except: shc_sA = 0
    scoreA = score_eval([element(elemA).name, mp_sA, den_sA, tc_sA, shc_sA])

    try: mp_sB = element(elemB).melting_point
    except: mp_sB = 0
    try: den_sB = element(elemB).density
    except: den_sB = 0
    try: tc_sB = element(elemB).thermal_conductivity
    except: tc_sB = 0
    try: shc_sB = element(elemB).molar_heat_capacity
    except: shc_sB = 0
    scoreB = score_eval([element(elemB).name, mp_sB, den_sB, tc_sB, shc_sB])

    if mp_sA == 0: mp_sA = "None"
    if den_sA == 0: den_sA = "None"
    if tc_sA == 0: tc_sA = "None"
    if shc_sA == 0: shc_sA = "None"

    if mp_sB == 0: mp_sB = "None"
    if den_sB == 0: den_sB = "None"
    if tc_sB == 0: tc_sB = "None"
    if shc_sB == 0: shc_sB = "None"

    print(f"Name: {element(elemA).name} ({element(elemA).symbol})\n\n"
          f"Melting Point: {mp_sA} K\n"
          f"Boiling Point: {element(elemA).boiling_point} K\n"
          f"Density: {den_sA} kg/m3\n"
          f"Thermal Conductivity: {tc_sA} W/mk\n"
          f"Specific Heat Capacity: {shc_sA} J/kgC\n"
          f"Score: {scoreA[0]} U\n")

    print(f"Name: {element(elemB).name} ({element(elemB).symbol})\n\n"
          f"Melting Point: {mp_sB} K\n"
          f"Boiling Point: {element(elemB).boiling_point} K\n"
          f"Density: {den_sB} kg/m3\n"
          f"Thermal Conductivity: {tc_sB} W/mk\n"
          f"Specific Heat Capacity: {shc_sB} J/kgC\n"
          f"Score: {scoreB[0]} U\n\n")
