import numpy as np
import pandas as pd

T_o = 298.15  # Original Reactant Temperature

def close(array, tarjet):
    def findClosest(arr, n, targete):
        def getClosest(val1, val2, targeta):
            if targeta - val1 >= val2 - targeta:
                return val2
            else:
                return val1
        if targete <= arr[0]:
            return arr[0]
        if targete >= arr[n - 1]:
            return arr[n - 1]

        i = 0; j = n; mid = 0
        while i < j:
            mid = (i + j) // 2
            if arr[mid] == targete:
                return arr[mid]
            if targete < arr[mid]:
                if mid > 0 and targete > arr[mid - 1]:
                    return getClosest(arr[mid - 1], arr[mid], targete)
                j = mid
            else:
                if mid < n - 1 and targete < arr[mid + 1]:
                    return getClosest(arr[mid], arr[mid + 1], targete)
                i = mid + 1

        return arr[mid]

    def run(arr, target):
        mine, maxe = 0, 0
        n = len(arr)
        pust = (findClosest(arr, n, target))
        pust_id = arr.index(pust)
        if arr[pust_id] > target:
            maxe = arr[pust_id]
            mine = arr[pust_id - 1]
        elif arr[pust_id] < target:
            mine = arr[pust_id]
            maxe = arr[pust_id + 1]
        return [mine, maxe]

    return run(array, tarjet)
def read_data(file_path, nm):
    return pd.DataFrame(pd.read_csv(file_path, index_col=nm))
def interpolation(Hp_List, Hr):
    # Hp_List = [[Product Enthalpy, Temperature], [Product Enthalpy, Temperature] ...
    return Hp_List[0][1] + (Hr - Hp_List[0][0]) * ((Hp_List[1][1] - Hp_List[0][1]) / (Hp_List[1][0] - Hp_List[0][0]))
def calculate_enthalpy(reactants, products, data):
    delta_h = []
    enth = ["Hf - 100K", "Hf - 200K", "Hf - 298.15K", "Hf - 300K", "Hf - 400K", "Hf - 500K", "Hf - 600K", "Hf - 700K",
            "Hf - 800K", "Hf - 900K", "Hf - 1000K", "Hf - 1100K", "Hf - 1200K", "Hf - 1300K", "Hf - 1400K", "Hf - 1500K",
            "Hf - 1600K", "Hf - 1700K", "Hf - 1800K", "Hf - 1900K", "Hf - 2000K", "Hf - 2100K", "Hf - 2200K", "Hf - 2300K",
            "Hf - 2400K", "Hf - 2500K", "Hf - 2600K", "Hf - 2700K", "Hf - 2800K", "Hf - 2900K", "Hf - 3000K", "Hf - 3100K",
            "Hf - 3200K", "Hf - 3300K", "Hf - 3400K", "Hf - 3500K", "Hf - 3600K", "Hf - 3700K", "Hf - 3800K", "Hf - 3900K",
            "Hf - 4000K", "Hf - 4100K", "Hf - 4200K", "Hf - 4300K", "Hf - 4400K", "Hf - 4500K", "Hf - 4600K", "Hf - 4700K",
            "Hf - 4800K", "Hf - 4900K", "Hf - 5000K", "Hf - 5100K", "Hf - 5200K", "Hf - 5300K", "Hf - 5400K", "Hf - 5500K",
            "Hf - 5600K", "Hf - 5700K", "Hf - 5800K", "Hf - 5900K", "Hf - 6000K"]
    for j in enth:
        delta_R = sum([data.loc[molecule, j] * count for molecule, count in reactants.items()])
        delta_P = sum([data.loc[molecule, j] * count for molecule, count in products.items()])

        Hp = delta_P - delta_R
        delta_h.append(Hp)
    return delta_h

def calculate_temperature(delta_h, data, products, T_o):
    delta_t = []
    temps = ["Cp - 100K", "Cp - 200K", "Cp - 298.15K", "Cp - 300K", "Cp - 400K", "Cp - 500K", "Cp - 600K", "Cp - 700K",
             "Cp - 800K", "Cp - 900K", "Cp - 1000K", "Cp - 1100K", "Cp - 1200K", "Cp - 1300K", "Cp - 1400K", "Cp - 1500K",
             "Cp - 1600K", "Cp - 1700K", "Cp - 1800K", "Cp - 1900K", "Cp - 2000K", "Cp - 2100K", "Cp - 2200K", "Cp - 2300K",
             "Cp - 2400K", "Cp - 2500K", "Cp - 2600K", "Cp - 2700K", "Cp - 2800K", "Cp - 2900K", "Cp - 3000K", "Cp - 3100K",
             "Cp - 3200K", "Cp - 3300K", "Cp - 3400K", "Cp - 3500K", "Cp - 3600K", "Cp - 3700K", "Cp - 3800K", "Cp - 3900K",
             "Cp - 4000K", "Cp - 4100K", "Cp - 4200K", "Cp - 4300K", "Cp - 4400K", "Cp - 4500K", "Cp - 4600K", "Cp - 4700K",
             "Cp - 4800K", "Cp - 4900K", "Cp - 5000K", "Cp - 5100K", "Cp - 5200K", "Cp - 5300K", "Cp - 5400K", "Cp - 5500K",
             "Cp - 5600K", "Cp - 5700K", "Cp - 5800K", "Cp - 5900K", "Cp - 6000K"]
    for z in delta_h:
        for j in temps:
            delta_P = sum([data.loc[molecule, j] * count for molecule, count in products.items()])
            Tc = (abs(z)/delta_P) + T_o
            delta_t.append(Tc)
    return delta_t

if __name__ == "__main__":
    # Calculate and print the results if the script is run directly

    r = {'C2H5OH': 1, 'O2': 3}
    p = {'H2O': 3, 'CO2': 2}

    data_file = 'enthalpies.csv'
    data = read_data(data_file, 'Compound')

    Hp = calculate_enthalpy(r, p, data)
    Tc = calculate_temperature(Hp, data, p, T_o)

    miner = close(Hp, 0)[0]
    miner_tp = Tc[Hp.index(miner)]
    maxer = close(Hp, 0)[1]
    maxer_tp = Tc[Hp.index(maxer)]

    interpol_T = [miner, miner_tp], [maxer, maxer_tp]
    #print(f"Enthalpy of the products (delta_Enth): {delta_Enth} J/mol")
    #print(f"Final temperature of the reaction (Tc): {Tc} K")
