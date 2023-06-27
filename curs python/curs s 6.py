
# Interactiunea cu un fisier text
"""
open() = functie folosita pentru a interactiona
cu un fisier in Python
ne returneaza o referinta catre fisierul cu care dorim
sa interactionam 9practic fisierul este deschis)

Functia open() poate  sa ia mai multi parametri:

1. un parametru OBLIGATORIU, numit  file

"""
# open('my_first_file')

fisier = open(file='../my_first_file.txt', mode='r')

# metoda readlines() --> citeste to continutul fisierului

lines = fisier.readline()
print(lines)
print(lines[0])

