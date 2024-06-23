import numpy as np
import pandas as pd
from EqtnBalancer import solver

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
        return pd.read_csv(file_path, index_col='Molecule')

    # Function to calculate enthalpy change for a reaction
    def calculate_enthalpy_change(self, reactants, products, data):
        reactant_sum = sum([data.loc[molecule, 'Enthalpy'] * count for molecule, count in reactants.items()])
        product_sum = sum([data.loc[molecule, 'Enthalpy'] * count for molecule, count in products.items()])
        delta_h = product_sum - reactant_sum
        return delta_h

    # Function to calculate temperature change for a reaction
    def calculate_temperature_change(self, delta_h, products, data):
        total_cp = sum([data.loc[molecule, 'Cp'] * count for molecule, count in products.items()])
        delta_t = abs(delta_h * 1000) / total_cp
        return delta_t

    # Main function
    def main(self, eqtn):
        data_file = 'enthalpies.csv'
        data = self.read_data(data_file)

        # Define the reactants and products for the reaction
        reactants = {'H2': 2, 'O2': 1}
        products = {'H2O': 2}

        # Calculate the enthalpy change
        delta_h = self.calculate_enthalpy_change(reactants, products, data)
        print(f"The enthalpy change for the reaction is: {delta_h} kJ/mol")

        # Calculate the temperature change
        delta_t = self.calculate_temperature_change(delta_h, products, data)
        print(f"The temperature change for the reaction is: {round(delta_t, 3)} K")

if __name__ == "__main__":
    adc().main(1)
