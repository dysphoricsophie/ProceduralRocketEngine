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

