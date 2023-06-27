#  Structuri de date
# Seturi
# Exemplu de set neordonat

import random

fruits = {"apple", "banana", "orange", "grape"}
print(fruits)

# Output: {'banana', 'apple', 'orange', 'grape'}

fruits = {"apple", "banana", "orange", "grape"}

# ADAUGAREA unui element in set

# adaugarea unui element care nu exista in set
# in momentul adaugarii

fruits.add("watermelon")
print(fruits)

# adaugarea unui element care exista in set
# in momentul adaugarii

fruits.add("apple")
print(fruits)

# STERGEREA elementelor dintr-un set

# stergerea unui element specific

fruits.remove("apple")
print(fruits)

# stergerea unui element aleator

fruits.pop()
print(fruits)

# Putem adauga elemente MUTABILE intr-un set?
# fruits.add([1, 2]) # da eroare

print(len(fruits))

# cum putem sa eliminam duplicatele dintr-o lista

cifre = [0, 0, 1, 2, 3, 2, 1, 4, 5, 5, 5]
cifre_set = set(cifre)

"""
EX8: Se da setul: my_set = {1, 2, 3, 4}.
a. Adauga nr 5 in set.
b. Adauga nr 6 in set.
c. Adauga nr 1 in set. Ce observi?
d. Sterge un element din set folosind metoda remove().
e. Sterge un element din set folosind metoda pop().
"""

my_set = {1, 2, 3, 4}
my_set.add(5)
print(my_set)
my_set.add(6)
print(my_set)
# 1 exista deja in set si nu mai poate fi adaugat

# my_set.remove(4)
# print(my_set)
my_set.pop()
print(my_set)
element_sters = my_set.pop()
print(element_sters)
print(my_set)
my_set.add(element_sters)
print(my_set)


# Tuple
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
print(len(my_tuple))

"""
EX9:
Se da urmatoarea structura de date:
locatie = (44.34, 12.456)
a. Verifica tipul structurii de date
b. Este aceasta structura de date ordonata?
c. Este aceasta structura de date mutabila?
d. Determina lungimea structurii de date.
e. Salveaza a doua valoare intr-o variabila.
Verifica daca aceasta este mai mare de 13, si afiseaza
un mesaj corespunzator.
"""

locatie = (44.34, 12.456)
print(type(locatie))
# truplu sunt ordonate
print(locatie[0])

# tuplu sunt imutabile

print(len(locatie))

# e
val2 = locatie[1]
if val2 > 13:
    print('val2 mai mare decat 13')
else:
    print('val2 nu este mai mare decat 13')
print('here')


# Cicluri Repetitive
# WHILE/WHILE ELSE

# Exemplul 1 - Afisarea numerelor de la 0 la 3
i = 0

while i <= 3:
    print(i)
    i += 1

"""
# Exemplul 3 - validarea credentialelor de conectare
"""
username = input("Introduceti numele de utilizator: ")
password = input("Introduceti parola: ")

while len(username) < 6 and len(password) < 6:  # dupa prima conditie indeplinite  'while' devine false
    print("Usernamel-ul si parola trebuie sa aiba min 6 caractere!")
    username = input("Introduceti numele de utilizator: ")
    password = input("Introduceti parola: ")
print("Autentificare reusita")

while len(username) < 6 or len(password) < 6:
    print("Usernamel-ul si parola trebuie sa aiba min 6 caractere!")
    username = input("Introduceti numele de utilizator: ")
    password = input("Introduceti parola: ")
print("Autentificare reusita")

# Exemplul 4 - ghicirea unui numar introdus la tastatura

secret_number = random.randint(1, 10)

guessed = False

while not guessed:
    guess_number = int(input("Alege un numar de la 1 la 10: "))
    if guess_number == secret_number:
        print("Felicitari! Ai ghicit!")
        guessed = True     # conditia de iesire
    elif guess_number < secret_number:
        print("Numarul este prea mic. Incercati din nou.")
    else:
        print("Numarul este prea mare. Incercati din nou.")
  

# Exemplul 1 - Afisarea cifrelor de la 0 la 3

i = 0

while i <= 3:
    print(i)
    i += 1
else:
    print("Am terminat ciclul repetitiv while.")

# Exemplul 3 - Cautarea unui element intr-o lista

numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

search_value = int(input("Ce numar cautati? "))

index = 0
while index < len(numbers):
    if numbers[index] == search_value:
        print(f"Valoarea a fost gasita la indexul: {index}")
        break
    index += 1
else:
    print("Valoarea nu a fost gasita in lista!")

#  FOR/FOR ELSE
# For
# executam functia print de 4 ori

for i in range(0, 4, 1):
    # i este o variabila care va reprezenta
    # pe rand, fiecare valoarea din range(4)
    # adica 0, 1, 2, 3

    # in loc de i putem pune orice alt nume

    # avem acces la variabila i doar in interiorul for-ului
    print(i)

# EX3: Afiseaza toate numerele pare pana la 10.

for numar in range(0, 11, 1):
    if numar % 2 == 0:
        print(numar)

for numar in range(0, 11, 1):
    if numar % 2 != 0:
        print(numar)

# Cum verifican daca un numar este prim

nr_prim = int(input('Introduceti un numar'))
for i in range(2, nr_prim):
    if nr_prim % i == 0:
        print(f'{nr_prim} nu este prim')
        break
else:
    print(f'{nr_prim} este prim')
