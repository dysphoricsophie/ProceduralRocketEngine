import sympy
import re

def solver(eqtn):
    # match a single element and optional count, like Na2
    ELEMENT_CLAUSE = re.compile("([A-Z][a-z]?)([0-9]*)")
    def reformatter(equation):
        eqtin = equation.replace(' ', '|').replace("+", " + ")
        return eqtin
    def understand(compound):
        """
        Given a chemical compound like Na2SO4,
        return a dict of element counts like {"Na":2, "S":1, "O":4}
        """
        assert "(" not in compound, "This parser doesn't support subclauses"
        return {el: (int(num) if num else 1) for el, num in ELEMENT_CLAUSE.findall(compound)}

    Oxids = ["O2", "F2", "F2O2", "N2O4", "H2O2-95[H2O-05]", "H2O2-85[H2O-15]", "O3", "HNO3-80[N2O4-20]", "HNO3-73[N2O4-27]", "N2O"]
    Fuels = ["H2", "CH4", "C2H5OH-95[H2O-05]", "C2H5OH-75[H2O-25]", "C6H5NH2", "NH3", "C2H8N2", "CH6N2", "N2H4", "CH3OH", "C12H26", "CH6N2-50[N2H4-50]", "CH6N2-75[N2H4-25]"]
    if not eqtn.__contains__("("):
        lhs = eqtn.split(" = ")[0]
        lhs_strings = lhs.split(" + ")
        lhs_compounds = [understand(compound) for compound in lhs_strings]

        rhs = eqtn.split(" = ")[1]
        rhs_strings = rhs.split(" + ")
        rhs_compounds = [understand(compound) for compound in rhs_strings]
    else:
        lhs = eqtn.split(" = ")[0]
        lhs_strings = lhs.split(" + ")
        multicomp = lhs_strings[0].replace("(", "").replace(")", "").split("/")
        if (Fuels, multicomp[1]):
            pass
        print(multicomp)
        exit(0)
        lhs_compounds = [understand(compound) for compound in lhs_strings]

        rhs = eqtn.split(" = ")[1]
        rhs_strings = rhs.split(" + ")
        rhs_compounds = [understand(compound) for compound in rhs_strings]

    # Get canonical list of elements
    els = sorted(set().union(*lhs_compounds, *rhs_compounds))
    els_index = dict(zip(els, range(len(els))))

    # Build matrix to solve
    w = len(lhs_compounds) + len(rhs_compounds)
    h = len(els)
    A = [[0] * w for _ in range(h)]
    # load with element coefficients
    for col, compound in enumerate(lhs_compounds):
        for el, num in compound.items():
            row = els_index[el]
            A[row][col] = num
    for col, compound in enumerate(rhs_compounds, len(lhs_compounds)):
        for el, num in compound.items():
            row = els_index[el]
            A[row][col] = -num   # invert coefficients for RHS

    # Solve using Sympy for absolute-precision math
    A = sympy.Matrix(A)
    # find first basis vector == primary solution
    coeffs = A.nullspace()[0]
    # find the least common denominator, multiply through to convert to integer solution
    coeffs *= sympy.lcm([term.q for term in coeffs])

    # Display result
    lhs = reformatter("+".join(["{} {}".format(coeffs[i], s) for i, s in enumerate(lhs_strings)]))
    rhs = reformatter("+".join(["{} {}".format(coeffs[i], s) for i, s in enumerate(rhs_strings, len(lhs_strings))]))
    return "{} = {}".format(lhs, rhs)

formula = input("Input your chemical reaction: ")
print(solver(formula) + '\n')
