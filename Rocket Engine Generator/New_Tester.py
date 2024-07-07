import math

import numpy as np
import pandas as pd

def findex(array, search):
    return array.index(search)
def interpolation(Hp_List, Hr):
    # Hp_List = [[Product Enthalpy, Temperature], [Product Enthalpy, Temperature] ...
    return Hp_List[0][1] + (Hr - Hp_List[0][0]) * ((Hp_List[1][1] - Hp_List[0][1]) / (Hp_List[1][0] - Hp_List[0][0]))
def check(string, sub_str):
    if string.find(sub_str) == -1:
        return False
    else:
        return True
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
        global mine, maxe
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
def split(txt, sep):
    return txt.split(sep)
def closest_value(input_list, input_value):
    arr = np.asarray(input_list)
    i = (np.abs(arr - input_value)).argmin()
    return arr[i]

class adc():
    def __init__(self, **kwargs):
        # Initial Variable Declartion
        super().__init__(**kwargs)
    # Function to read enthalpies and specific heat capacities from a .csv file
    def read_data(self, file_path):
        return pd.read_csv(file_path, index_col='Compound')

    # Function to calculate enthalpy change for a reaction
    def calculate_enth_change(self, reactants, products, data):
        delta_h = []
        enths = ["Hf - 100K", "Hf - 200K", "Hf - 298.15K", "Hf - 300K", "Hf - 400K", "Hf - 500K", "Hf - 600K", "Hf - 700K", "Hf - 800K", "Hf - 900K",
                 "Hf - 1000K", "Hf - 1100K", "Hf - 1200K", "Hf - 1300K", "Hf - 1400K", "Hf - 1500K", "Hf - 1600K", "Hf - 1700K", "Hf - 1800K",
                 "Hf - 1900K", "Hf - 2000K", "Hf - 2100K", "Hf - 2200K", "Hf - 2300K", "Hf - 2400K", "Hf - 2500K", "Hf - 2600K", "Hf - 2700K",
                 "Hf - 2800K", "Hf - 2900K", "Hf - 3000K", "Hf - 3100K", "Hf - 3200K", "Hf - 3300K", "Hf - 3400K", "Hf - 3500K", "Hf - 3600K",
                 "Hf - 3700K", "Hf - 3800K", "Hf - 3900K", "Hf - 4000K", "Hf - 4100K", "Hf - 4200K", "Hf - 4300K", "Hf - 4400K", "Hf - 4500K",
                 "Hf - 4600K", "Hf - 4700K", "Hf - 4800K", "Hf - 4900K", "Hf - 5000K", "Hf - 5100K", "Hf - 5200K", "Hf - 5300K", "Hf - 5400K",
                 "Hf - 5500K", "Hf - 5600K", "Hf - 5700K", "Hf - 5800K", "Hf - 5900K", "Hf - 6000K"]
        for k in enths:
            reactant_sum = sum([data.loc[molecule, k] * count for molecule, count in reactants.items()])
            product_sum = sum([data.loc[molecule, k] * count for molecule, count in products.items()])
            delta_h.append([product_sum,reactant_sum])
        return delta_h

    def calculate_temp_change(self, delta_h, products, data):
        # Function to calculate enthalpy change for a reaction
        delta_t = []
        delta_enth = []
        temps = ["Cp - 100K", "Cp - 200K", "Cp - 298.15K", "Cp - 300K", "Cp - 400K", "Cp - 500K", "Cp - 600K", "Cp - 700K", "Cp - 800K", "Cp - 900K",
                 "Cp - 1000K", "Cp - 1100K", "Cp - 1200K", "Cp - 1300K", "Cp - 1400K", "Cp - 1500K", "Cp - 1600K", "Cp - 1700K", "Cp - 1800K",
                 "Cp - 1900K", "Cp - 2000K", "Cp - 2100K", "Cp - 2200K", "Cp - 2300K", "Cp - 2400K", "Cp - 2500K", "Cp - 2600K", "Cp - 2700K",
                 "Cp - 2800K", "Cp - 2900K", "Cp - 3000K", "Cp - 3100K", "Cp - 3200K", "Cp - 3300K", "Cp - 3400K", "Cp - 3500K", "Cp - 3600K",
                 "Cp - 3700K", "Cp - 3800K", "Cp - 3900K", "Cp - 4000K", "Cp - 4100K", "Cp - 4200K", "Cp - 4300K", "Cp - 4400K", "Cp - 4500K",
                 "Cp - 4600K", "Cp - 4700K", "Cp - 4800K", "Cp - 4900K", "Cp - 5000K", "Cp - 5100K", "Cp - 5200K", "Cp - 5300K", "Cp - 5400K",
                 "Cp - 5500K", "Cp - 5600K", "Cp - 5700K", "Cp - 5800K", "Cp - 5900K", "Cp - 6000K"]
        for z in delta_h:
            for j in temps:
                product_sum = sum([data.loc[molecule, j] * count for molecule, count in products.items()])
                delta_enth.append((abs((z[0]-z[1]))*1000)/product_sum)
            delta_t.append(delta_enth)
            delta_enth = []
        return delta_t

    # Main function
    def main(self, eqtn):
        data_file = 'enthalpies.csv'
        data = self.read_data(data_file)

        # Define the reactants and products for the reaction
        reactants = {'H2': 2, 'O2': 1}
        products = {'H2O': 2}

        # Calculate the enthalpy change
        delta_h = self.calculate_enth_change(reactants, products, data)
        prod_enth = []
        for item in delta_h: prod_enth.append(item[1])
        reactant_enth = []
        for item in delta_h: reactant_enth.append(item[0])
        delta = []; fg = []
        for l in range(len(delta_h)):
            delta.append((float(prod_enth[l]) - float(reactant_enth[l])))
            fg.append((float(prod_enth[l]) - float(reactant_enth[l])))
        delta.sort()
        print(f"The enthalpy change for the reaction is: {fg[fg.index(delta[0])]} kJ/mol")

        # Calculate the temperature change
        delta_t = self.calculate_temp_change(delta_h, products, data)
        print(f"The temperature change for the reaction is: {round(delta_t[fg.index(delta[0])][0], 3)} K")

if __name__ == "__main__":
    adc().main(1)
