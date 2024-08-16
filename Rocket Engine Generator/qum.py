from thermo import ChemicalConstantsPackage, PRMIX, CEOSLiquid, CEOSGas, FlashPureVLS
from thermochem.janaf import Janafdb
import cantera as ct

def Enthaly_Calculator(t, species):
    HH_Tr = 0
    STP = 298.15

    # Checks the thermochemical properties using the thermochem module
    if species == 'H2' or species == 'O2' or species == 'H2O' or species ==  'CO2' or species ==  'F2' or species ==  'N2O4'\
        or species ==  'CH4' or species ==  'NO2' or species ==  'CF4' or species ==  'N2' or species ==  'O3' or species ==  'HNO3':
        try:
            db = Janafdb().getphasedata(formula=species)
        except:
            db = Janafdb().getphasedata(formula=species, phase="g")
        HH_Tr = db.hef(t)

    # Checks the thermochemical properties using the cantera imports
    elif species == 'C12H26' or species == 'H2O2':
        if species == 'C12H26':
            gas = ct.Solution("nDodecane_Reitz.yaml")
        else:
            gas = ct.Solution("gri30.yaml")

        gas.TPX = STP, ct.one_atm, {species: 1.0}
        h_298 = gas.enthalpy_mole/1000000

        gas.TP = t, ct.one_atm
        h_T = gas.enthalpy_mole/1000000
        HH_Tr = h_T - h_298

    # Checks the thermochemical properties using the thermo module
    elif species == 'Ethanol' or species == 'Ammonia' or species == "Nitrogen Trifluoride" or species == 'Methanol'\
        or species == "Aniline" or species == "1,1-dimethylhydrazine" or species == "Methylhydrazine" or species == "Hydrazine"\
        or species == "HF" or species == "NF3":
        constants, correlations = ChemicalConstantsPackage.from_IDs([species])
        eos_kwargs = dict(Tcs=constants.Tcs, Pcs=constants.Pcs, omegas=constants.omegas)

        liquid = CEOSLiquid(PRMIX, HeatCapacityGases=correlations.HeatCapacityGases, eos_kwargs=eos_kwargs)
        gas = CEOSGas(PRMIX, HeatCapacityGases=correlations.HeatCapacityGases, eos_kwargs=eos_kwargs)

        flasher = FlashPureVLS(constants, correlations, gas=gas, liquids=[liquid], solids=[])
        h_298 = flasher.flash(T=STP, P=ct.one_atm).H()/1000
        h_T = flasher.flash(T=t, P=ct.one_atm).H()/1000
        HH_Tr = (h_T - h_298)
    return HH_Tr

A1 = ['H2', 'O2', 'H2O', 'CO2', 'F2', 'F2O2', 'N2O4', 'H2O2', 'O3', 'HNO3', 'CH4', 'Ethanol', 'Aniline', 'Ammonia',
      '1,1-dimethylhydrazine', 'Methylhydrazine', 'Hydrazine', 'Methanol', 'C12H26', 'NO2', 'CF4', 'N2', 'HF',
      'Aniline', 'NF3']

Temps = [100, 200, 298.15, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100,
         2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200,
         4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000]
for t_new in enumerate(Temps):
    print(f"\nAt temperature {t_new[1]}K: ")
    for specie in enumerate(A1):
        val = Enthaly_Calculator(t_new[1], specie[1])
        print(f'{specie[0]+1} - Enthalpy difference or H-H(Tr) for {specie[1]} at {t_new[1]}K: {val:.2f} kJ/mol')