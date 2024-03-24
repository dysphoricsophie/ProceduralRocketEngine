totality = [["apple", "banana", "cherry"], ["kiwi", "mango", "grapefruit"]]
productsData = totality[0]  # Assuming productsData is the first row of Totality

ProA = "kiwi"
ProB = "banana"

indexA = -1
indexB = -1

for i in range(len(totality[0])):
    if totality[0][i] == ProA:
        indexA = i
    if totality[0][i] == ProB:
        indexB = i

print(f"ProA is found at index {indexA} in the first row")
print(f"ProB is found at index {indexB} in the first row")
