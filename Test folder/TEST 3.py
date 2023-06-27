# Utilizând un for:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    print(f"Mașina mea preferată este {masina}")
# Utilizând un for each (sintaxa for-each este specifică limbajului Python):


masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    print(f"Mașina mea preferată este {masina}")
# Utilizând un while:


masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

index = 0
while index < len(masini):
    print(f"Mașina mea preferată este {masini[index]}")
    index += 1
# Utilizând un for else:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina != masini[0] and masina != masini[-1]:
        masina = masina.upper()
    else:
        continue
    print(masina)
else:
    print(masini)
# Iterarea prin listă pentru a căuta un Mercedes:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Mercedes':
        print('Am găsit mașina dorită de dvs')
        break
    else:
        print(f'Am găsit mașina {masina}. Mai căutam')
# Prezentarea mașinilor către un cumpărător indecis:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Trabant' or masina == 'Lăstun':
        continue
    print(f'S-ar putea să vă placă mașina {masina}')
# Modernizarea parcului de mașini:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for index, masina in enumerate(masini):
    if masina == 'Lăstun' or masina == 'Trabant':
        masini_vechi.append(masina)
        masini[index] = 'Tesla'

print(f"Modele vechi: {', '.join(masini_vechi)}")
print(f"Modele noi: {', '.join(masini)}")
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
        print(f"Pentru un buget de sub {buget} euro puteți alege mașina {masina}")
# Iterarea prin listă (nu este specificat care listă, așa că voi itera prin masini):


masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    print(masina)
