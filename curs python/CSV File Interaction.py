"""
Interactiunea cu fisiere CSV

"""
import csv
"""
CSV = Comma Separated Values
CSV files --> forma tabelara
"""

# v1 luam doar valorile din fiecare linie
with open('employees.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    print(reader)

    for row in reader:
        print(row)
# v2 luam atat denumirea coloanelor  cat si
# valorile aferente fiecarei lini
with open('employees.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)

# salvam randurile /datele dintr-un fisier csv
# intr-o lista, pentru vca vrem sa putem modifica
# mai apoi valori din fisierul  rand

rows = []
with open('employees.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        rows.append(row)


print(rows)

# Scrierea intr-un fisier csv

with open('new_employees.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # v1
    # adaugam cate o linie pe rand
    # for row in rows:
    #    writer.writerow(row)

    # v 2
    # adaugam toate liniile  deodata
    writer.writerows(rows)

