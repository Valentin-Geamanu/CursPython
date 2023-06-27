print('Hello World')
name = 'Valentin'
print(f'Hi, {name}')
print('Produsul acesta costa 5 lei.', end='*')
print(3)
print(5.5)
print('alb', 'verde')
print('negru', 'violet', sep='*')
# = o singura linie de comentariu

# variabile sunt cutii care stocheaza valori

marca_masina = 'Toyota'
model_masina = 'Rav 4'
print(f'{marca_masina}', f'{model_masina}')
my_var = 6
print(my_var)
my_Var = 12
print(my_var == my_Var)
print(id(my_var))
print(id(my_Var))

# atribuim mai multe valori pentru mai multe variabile in aceasi linie

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# atribuim aceasi valoare pentru mai multe variabile in aceeasi linie

a = b = c = "Apple"
print(a)
print(b)
print(c)

# Tipuri de date

# int= numar intreg
# float = numere zecimale
# boolean = adevarat sau false (True or False)
# string = sire de caractere de la tastatura delimitate de ""  sau ''

"""
 EX1:
a. Defineste o variabila de tip int, numita 'latime'.
b. Defineste o variabila de tip string, numita 'descriere'.
c. Defineste 2 variabile de tip float, numite 'pret' si 'discount'.
d. Defineste o variabila de tip bool, numita 'initializat' care are valoarea True.
e. Printeaza variabilele definite la punctele anterioare.
"""
# a
latime = 130
# b
descriere = 'descriere'
# c
pret = 2.99
discount = 0.99
# d
initializat = True
# e
print(latime)
print(pret)
print(discount)
print(initializat)

# EX2: Folosind o singura linie de cod, defineste 2 variabile, de tip int, cu valoarea 10.

x = y = 10
print('x:', x)
print('y:', y)

# EX3: Folosind o singura linie de cod, initializeaza/ defineste doua variabile de tip string cu valori diferite.

nume = 'Geamanu'
prenume = 'Valentin'
print(nume, prenume)


# concatenarea string-urilor
nume = 'Geamanu'
prenume = 'Valentin'
nume_complet = nume + ' ' + prenume
print(nume_complet)

pret_produs = 25.5

# descriere_produs = 'Produsul nostru costa ' + {pret_produs} + 'euro.'
# nu pot fi concatenate stringuri cu int sau float

descriere_produs = f'Produsul nostru costa  {pret_produs} euro.'
print(descriere_produs)

"""
# EX4: Defineste doua variabile de tip string, numite 'nume', respectiv 'pret'.
# Afiseaza in consola un mesaj care sa contina cele doua variabile.


# EX6:
# a. Defineste doua variabile: nume (string) si varsta (int).
# b. Folosind f-string, afiseaza in consola, o propozitie care sa contina cele doua variabile.
"""

nume = 'Ionescu'
pret = '100'
print(nume + pret)
print(nume + ' a cumparat rosi de ' + pret + 'lei')
print(f'{nume} a cumparat rosi de {pret} lei.')
varsta = 37
print(f'{nume} are {varsta} ani.')


# curs 2 23.05.2023
# type = afiseaza tipul unei variabile

culoare = 'albastru'
print(type(culoare))
numar = 34
print(type(numar))
numar_a = 35.9
print(type(numar_a))
numar1 = 10
numar2 = '10'
print(type(numar1))
print(type(numar2))

# Sunt numar1 si numar2 de acelasi tip?

print(int(numar2))
numar2 = int(numar2)
print(type(numar2))
my_str = '12euro'

# my_str = int(my_str) #da eroare

print(my_str)

# int

numar1 = 23
print('before', type(numar1))
numar1 = str(numar1)
print('after', type(numar1))

# float

numar2 = 23.6
print('before', type(numar2))
numar2 = str(numar2)
print('after', type(numar2))

# int->float

numar3 = 45
print('before', type(numar3))
numar3 = float(numar3)
print('after', type(numar3))

# float -> int

numar4 = 46.8
print('before', type(numar4))
numar4 = int(numar4)
print('after', type(numar4))

"""
EX8:
a. Defineste o variabila de tip int. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de tip int de la punctul a, la tipul float si salveaza rezultatul intr-o alta variabila.
d. Afiseaza in consola tipul variabilei generate la punctul c.
"""

a = 5
print(a)
print(type(a))
b = float(a)
print(b)
print(type(b))

# Functia 'input'
# input()= permite introducerea de valori din tastatura

nume = input('Whats your name:')
print(f'My name is {nume}')
varsta = int(input('How old are you:'))
print(f'My age is: {varsta}')

"""
EX11: Citeste de la tastatura un pret. Obliga utilizatorul sa introduca pretul ca si numar zecimal.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""

pret = float(input('Ce pret are produsul? '))
print(f'Pretul produsului este {pret} lei')

# 📌 Tipul string - metode disponibile

# index
info = 'Afara sunt 2 grade'
print(info[0])  # => 'A' (primul caracter din string se afla la indexul 0)
print(info[1])  # => 'f'
print(info[5])  # => ' ' (la indexul 5 avem un spatiu gol)

# lungimea
info = 'Afara sunt 20 de grade'
print(len(info))

# slicing

info = 'Afara sunt 2 grade'

# Extragem string-ul care incepe cu index-ul 0 pana la index-ul 1, inclusiv
print(info[0:2])  # => 'Af'

# Extragem string-ul care incepe cu index-ul 0 pana la indexul 4, inclusiv
print(info[0:5])  # => 'Afara'
print(info[:5])
# Daca nu specificam end_pos, se va extrage string-ul
# pana la ultimul caracter, inclusiv
print(info[6:])  # => 'sunt 2 grade'

# Daca nu specificam start_pos, se va extrage string-ul
# incepand cu primul caracter.
print(info[:5])  # => 'Afara'

# Inversare string
print(info[::-1])  # => 'edarg 2 tnus arafA'

# slicing intr-un string si sa iau elementele din 2 in 2
cifre = '123456789'
print(cifre[::2])

"""
EX14: Se da string-ul prop3 = 'Concertul va avea loc maine."
a. Salveaza intr-o variabila, folosind slicing, primul cuvant.
b. Extrage primele 3 caractere din prop3.
c. Afiseaza prop3 cu caracterele inversate.
"""
# a
prop3 = 'Concertul va avea loc maine.'

primul_cuvant = print(prop3[:9])

# b

primul_cuvant = print(prop3[0:3])

# c

print(prop3[::-1])

#  Metode ajutatoare string
str1 = 'bAnana'
print(str1.upper())  # => 'BANANA' (tot cu litere mari)
print(str1.capitalize())
print(str1.lower())
str1.count('a')
print(str1.count('a'))
print(str1.replace('A', 'a'))
print(str1.find('A'))

# stringul este ORDONAT  si IMUTABIL
# STRING ORDONAT = elementele pot fi accesate dupa index

my_str = 'abc'
print(my_str[0])

# STRING IMUTABIL = string-ul nu poate fi modificat

my_str = 'aabbcc'
result = my_str.replace('a', 'x')
print(result)
print(my_str)

# my_str[1] = 'x'
# print(my_str)
my_str = 'cde'  # suprascriem
print(my_str)


# OPERATORI

x = 2
y = 3

# # adunarea
print(x + y)  # 5

# # scaderea
print(y - x)  # 1

# # inmultirea
print(x * y)  # 6

# # impartirea
print(y / x)  # 1.5

# # restul impartirii
print(y % x)  # 1

# # ridicarea la putere
print(x ** y)  # 2 la puterea 3 -> 8

# # floor division
print(y // x)  # 3 // 2; 1.5 => 1

# inmultirea pe string-uri
my_str = 'a'

# vreau sa afisez mesajul 'aaa'
print(my_str + my_str + my_str)
print(my_str * 3)

# in cazul impartiri indiferent daca rezultatul va fi un numar intreg sau zecimal
# rezultatul in python va fi de tip float

x = 17
y = 2
# daca ambele numere sunt int -> rezultatul va fi int
print(x // y)  # 8.5 -> rezultatul este 8

x = 17.8
y = 2
# daca cel putin unul din numere este float -> rezultatul va fi float
print(x // y)  # 8.9 -> rezultatul este 8.0

x = -17
y = 2
print(x // y)  # -8.5 -> rezultatul este -9


# Structuri de date
# Liste

# Exemplu de lista ordonatade numere intregi
numbers = [1, 2, 3, 4, 5]
print(numbers)
# Output: [1, 2, 3, 4, 5]
# lista este ordonata
# fiecare element din lista poate fi accesat dupa index
print(numbers[0])
print(numbers[2])
print(numbers[::-1])  # inversarea unei liste

# lista este mutabila
# putem sa modificam sa stergem si sa adaugam element in lista
# Cum adaugam elemente noi in lista?

cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8, 9]

# adaugam cifra 9 in lista cifre la finalul listei
print(cifre)

# adaugam 9 in lista cifre la indexul 2
cifre.insert(2, 9)
print(cifre)
# Cum stergem un element din lista?

cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8]

# stergem ultimul element din lista
cifre.pop()
print(cifre)

# stergem elementul de la indexul 1 in lista cifre
element_sters = cifre.pop(1)
print(element_sters)
print(cifre)

# stergem prima aparitie a unui element in lista
# dupa valoare
cifre.remove(3)
print(cifre)

#
caractere = ['a', 'b', 'a', 'b', 'c', 'a']
print(caractere)
caractere.remove('a')
print(caractere)
caractere.remove('a')
print(caractere)
caractere.remove('a')
print(caractere)

# actualizam valoarea unui element

cifre = [0, 1, 2, 3, 4, 5, ]

# Dictionare
my_dict = {
    'nume_produs': 'produs_1',
    'pret': 23.00,
    'in_stoc': False
}
print(my_dict)

my_dict = {
    'brand': "Volvo",
    'model': "XC 60",
    'year': 2011
}

print(my_dict)
print(my_dict['brand'])
print(len(my_dict))

# contacte = ['0722345678', '0721549888', '0765332967']

contacte = {
    'Ana': '0722345678',
    'Marius': '0721549888',
    'Maria': '0765332967'
}

# dorim sa accesam numarul lui Marius
print(contacte['Marius'])

# dorim sa accesam numarul lui Alin

print(contacte['Alin'])   # -> eroare: KeyError
print(contacte.get('Alin', 0))
