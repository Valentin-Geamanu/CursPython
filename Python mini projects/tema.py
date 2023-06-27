print('Hello Python')

# Exercitiul 1: in cadrul unui  comentariu, explica ce este o variabila

# Raspuns: O variabila este o cutie/zona din memorie in care sunt adaugate valori. 

# Exercitiul 2: Declara si initializeaza cate o variabila din fiecare din urmatoarele tipuri de variabile.
# Exercitiul 3: Utilizeaza functia type pentru a verifica daca au tipul de date asteptat.
# Exertitiul 5: Printeaza in consola cu functia print(), 4 propoziti folosind cele 4 variabile.
# Rezolva nepotrivirile de tip prin ce modalitati doresti.

""""""
# a) string
name = 'Valentin'
print('My name is:', name)
print(type(name))
# b) intiger
age = 35
print('I am ', age, 'years old')
print(type(age))
# c) Float
money = 35.5
print('I have', money, 'Ron in my wallet')
print(type(money))
# d Boolean
empty_wallet = True
print('Tonight my wallet will be zero funds', empty_wallet)
print(type(empty_wallet))

# Exertitiul 4: rotunjeste "float-ul" folosind functia round()
# Salveaza aceasta modificare in aceasi variabila (suprascriere)
card = 67.35
print(type(card))
print(round(card))
card = round(card)
print(card)
print(type(card))

# Exercitiul 6: Citeste de la tastatura:
# a) numele
name = input('Enter your name:')
# b) prenumele
surname = input('Enter your surname:')
print(f'Your full name is:', name, surname)
# c) Afiseaza numarul de caractere .
full_name = name + surname
print(f'full_name has {len(full_name)} caractere')

# Exertitiul 7: Citeste de la tastatura lungimea si latimea apoi afiseaja aria dreptunghiului.

lungime_d = int(input('adauga lungimea:'))
latime_d = int(input(' adauga latimea:'))
aria_d = lungime_d * latime_d
print(f'Aria dreptunghuilui este {aria_d}.')


# Exertitiul 8: Avem stringul: 'Coral is either the stupidest animal or the smartest rock'
# afisati de cate ori apare cuvantul 'the' ;
# Exercitiul 9:printeaza rezultatul.
# Exertituil 10: Foloseste un assert ca sa  verifici daca acest string contine doar numere

prop1 = 'Coral is either the stupidest animal or the smartest rock'
print(prop1.count('the'))
x = prop1.count('the')
print(f' Cuvantul "the" apare de {x} ori.')
assert prop1.isnumeric()

# Exercitiul 11:citeste  de la tastarutra un string de dimensiune impar
# si afiseaza caracrterul din mijloc.

impar = input('Scrie un string cu un nr de caractere impar:')
if len(impar) % 2 == 0:
    print('Stringul nostru contine un nr de caracter par.')
else:
    res = len(impar) // 2
    print(impar[res])
