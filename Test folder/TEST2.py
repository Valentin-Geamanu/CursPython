masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    print("Mașina mea preferată este", masina)
# Utilizând un for-each loop:


masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    print("Mașina mea preferată este", masina)
# Utilizând un while loop:


masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

i = 0
while i < len(masini):
    print("Mașina mea preferată este", masini[i])
    i += 1
# Utilizând un for loop cu else:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for index, masina in enumerate(masini):
    if index != 0 and index != len(masini) - 1:
        masini[index] = masina.upper()

else:
    print(masini)
# Iterarea prin lista pentru a găsi mașina dorită:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Mercedes':
        print('Am găsit mașina dorită de dvs.')
        break
    else:
        print('Am găsit mașina', masina, 'Mai căutam')
# Prezentarea mașinilor către un cumpărător indecis:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Trabant' or masina == 'Lăstun':
        continue
    print('S-ar putea să vă placă mașina', masina)
# Actualizarea parcului de mașini:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for index, masina in enumerate(masini):
    if masina == 'Lăstun' or masina == 'Trabant':
        masini_vechi.append(masina)
        masini[index] = 'Tesla'

print('Modele vechi:', masini_vechi)
print('Modele noi:', masini)

# Prezentarea mașinilor în funcție de buget:

pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

buget = 15000

for masina, pret in pret_masini.items():
    if pret <= buget:
        print("Pentru un buget de sub 15000 euro puteți alege mașina", masina)