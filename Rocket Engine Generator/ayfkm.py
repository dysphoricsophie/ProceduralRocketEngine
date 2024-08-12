import polars as pl
import pandas as pd
import janaf

temps = ["100", "200", "298.15", "300", "400", "500", "600", "700", "800", "900", "1000", "1100", "1200",
         "1300", "1400", "1500", "1600", "1700", "1800", "1900", "2000", "2100", "2200", "2300", "2400",
         "2500", "2600", "2700", "2800", "2900", "3000", "3100", "3200", "3300", "3400", "3500", "3600",
         "3700", "3800", "3900", "4000", "4100", "4200", "4300", "4400", "4500", "4600", "4700", "4800",
         "4900", "5000", "5100", "5200", "5300", "5400", "5500", "5600", "5700", "5800", "5900", "6000"]
exhA = ["N2", "CF4", "CO2", "HF", "NO2", "NH3", "O3", "CH4", "HNO3", "F2"]
exhB = ["Nitrogen", "Tetrafluoromethane", "Carbon Dioxide", "Hydrogen Fluoride", "Nitrogen Oxide", "Ammonia", "Ozone",
        "Methane", "Nitric Acid", "Fluorine"]
exhC = [22, 21, 20, 23, 19, 13, 8, 10, 9, 12, 4]
Cp = []; Hf = []

for j in exhA:
    df = pd.read_csv("enthalpies.csv")
    try:
        table = janaf.search(formula=str(j + "$"))
    except:
        table = janaf.search(name=str(exhB[exhA.index(j)] + "$"))

    for i in temps:
        Cp.append(table.df.filter(pl.col("T(K)")==float(i)).item(0, "Cp"))
        print(f'{exhB[exhA.index(j)]} ({j}) at {i}K = {table.df.filter(pl.col("T(K)") == float(i)).item(0, "Cp")}')
        df.loc[exhC[exhA.index(j)], ("Cp - " + i + "K")] = table.df.filter(pl.col("T(K)")==float(i)).item(0, "Cp")
        df.to_csv("AllDetails.csv", index=False)
    for z in temps:
        Hf.append(table.df.filter(pl.col("T(K)")==float(z)).item(0, "delta-f H"))
        print(f'{exhB[exhA.index(j)]} ({j}) at {z}K = {table.df.filter(pl.col("T(K)") == float(z)).item(0, "delta-f H")}')
        df.loc[exhC[exhA.index(j)], ("Hf - " + z + "K")] = table.df.filter(pl.col("T(K)")==float(z)).item(0, "delta-f H")
        df.to_csv("enthalpies.csv", index=False)