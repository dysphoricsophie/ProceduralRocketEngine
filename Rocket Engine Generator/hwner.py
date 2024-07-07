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

print(equationizer(solver("C2H5OH + HNO3 = NO2 + CO2 + H2O")))
Hf - 100K,Hf - 200K,Hf - 298.15K,Hf - 300K,Hf - 400K,Hf - 500K,Hf - 600K,Hf - 700K,Hf - 800K,Hf - 900K,Hf - 1000K,Hf - 1100K,Hf - 1200K,Hf - 1300K,Hf - 1400K,Hf - 1500K,Hf - 1600K,Hf - 1700K,Hf - 1800K,Hf - 1900K,Hf - 2000K,Hf - 2100K,Hf - 2200K,Hf - 2300K,Hf - 2400K,Hf - 2500K,Hf - 2600K,Hf - 2700K,Hf - 2800K,Hf - 2900K,Hf - 3000K,Hf - 3100K,Hf - 3200K,Hf - 3300K,Hf - 3400K,Hf - 3500K,Hf - 3600K,Hf - 3700K,Hf - 3800K,Hf - 3900K,Hf - 4000K,Hf - 4100K,Hf - 4200K,Hf - 4300K,Hf - 4400K,Hf - 4500K,Hf - 4600K,Hf - 4700K,Hf - 4800K,Hf - 4900K,Hf - 5000K,Hf - 5100K,Hf - 5200K,Hf - 5300K,Hf - 5400K,Hf - 5500K,Hf - 5600K,Hf - 5700K,Hf - 5800K,Hf - 5900K,Hf - 6000K

