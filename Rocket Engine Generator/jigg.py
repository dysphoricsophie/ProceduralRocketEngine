import csv
with open('enthalpies.csv', 'rt') as toverd:
    reader = csv.reader(toverd, delimiter=',', quoting=csv.QUOTE_NONE)
    inputHeader = next(reader)
    inputRows = [row for row in reader]
print(inputRows[5][0])