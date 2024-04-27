Fuel_List = ["H2", "CH4", "C2H5OH-95[H2O-05]", "C2H5OH-75[H2O-25]", "C6H5NH2", "NH3", "C2H8N2", "CH6N2", "N2H4",
             "CH3OH", "C12H26", "CH6N2-50[N2H4-50]", "CH6N2-75[N2H4-25]"]
Fuel_Enth = [0, -74.65, -277.51, -277.07, 83.2, -46.05, 84.9, 94.5, 95.35, -210.5, -290.675, 94.925, 94.7125]

for i in range(len(Fuel_List)):
    print(Fuel_List[i])
    print(Fuel_Enth[i])