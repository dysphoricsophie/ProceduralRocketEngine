# coding=windows-1252
import json

def array_to_json(array):
    """
    Convert an array to a dictionary, create a JSON file, and add the dictionary in JSON object format.

    param array: List of values to be converted to a dictionary.
    param json_filename: Name of the JSON file to be created.
    """
    # Step 1: Remove "\n" at the end of each string item
    processed_array = [item.replace("\n", "") for item in array]

    # Step 2: Split each string item by ": " and create a dictionary
    result_dict = {}
    for item in processed_array:
        key, value = item.split(": ", 1)
        result_dict[key] = value
    json_object = {"Engine Data": result_dict}

    # Step 3: Write the dictionary to a JSON file
    with open('output.json', 'w', encoding='windows-1252') as json_file:
        json.dump(json_object, json_file, indent=4)

# Example usage
array = ['Engine Designation: BW-1027r "Novo"\n\n', 'Fuel Flow Cycle: Gas Generator\n', 'Engine Oxidizer: F2 (Fluorine)\n',
         'Engine Fuel: H2 (Hydrogen)\n', 'Average Mixture Ratio: 6.0\n', 'Propellant properties: Hypergolic and cryogenic\n',
         'Altitude Of Operation: 20-30 km (Medium Atmosphere)\n', 'Exhaust Nozzle Geometry: Contour Bell Nozzle\n',
         'Exhaust Expansion Ratio: 33:1\n', 'Characteristic Exhaust Velocity: 3925 m/s\n', 'Adiabatic Combustion Temperature: 3689°K\n',
         'Engine Gimbal Range: None\n', 'Engine Injector Design: Liquid Showerhead Injector\n', 'Engine chamber configuration: Single Chamber\n',
         'Engine Use Case: Lower Stage (Vernier)\n', 'Tank repressurisation Method: Autogenous\n', 'Nozzle Cooling Mechanism: Dump Cooling\n',
         'Engine Throttle Range: Not Throttleable\n\n']
array_to_json(array)
