import polars as pl
import janaf

j = "Hydrazine"
i = 5000
table = janaf.search(phase=(j+"(g)"))
print(f'{str(j + "$")} at {i}K = {table.df.filter(pl.col("T(K)") == float(i)).item(0, "Cp")}')
print(f'{str(j + "$")} at {i}K = {table.df.filter(pl.col("T(K)") == float(i)).item(0, "delta-f H")}')