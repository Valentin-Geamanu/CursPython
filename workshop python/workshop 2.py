"""
a = 67
b = 78
c = a + b
print(c)
def c():
    c = a+b
    return c
def sum(a, b):
    return a + b
def parity(n):
    if n % 2 == 0:
        return True
    return False
print(f'suma returnata este, {sum(10, 48)}')
print(f'paritate: {parity(n)}')
nume = 'Geamanu'
prenume = 'Valentin'
nume_mijlociu = 'Dumitru'
full_name = nume + nume_mijlociu + prenume
print(nume, nume_mijlociu, prenume)
def nume(nume, mune_mijlociu, prenume ):
    if type( nume ) == str and type(nume_mijlociu) == str and type( prenume) == str:
        return len(full_name)
    return -1
print(f'lungime numelui complet  este {len(full_name)} caractere')
if nume(10, 20, 30 ) > 0
"""

"""
13. Funcție care primește o listă de cifre (adică doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""

"""
def item_count(my_list):
    dict1 = {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0
    }
    for item in dict.keys():
        dict1[item] = my_list.count(int(item))

    return dict1
"""

# clase si OOP
# cele 4 principii OOP: abstractizare, incapsulare, mostenire, polimorfism


class Dreptunghi:
    lungime = 39
    latime = 54
    culoare = 'blue'

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        print(f'Acest dreptunghi are o lungime de {self.lungime} si o latime de {self.latime}. Culoarea lui este {self.culoare}')

    def area(self):
        return self.lungime * self.latime

    def perimetru(self):
        return 2 * (self.lungime + self.latime)

    def change_color(self, new_color):
        self.culoare = new_color


dreptunghi = Dreptunghi(39, 54, 'blue')
dreptunghi.change_color('greem')
print(f'Aria dreptunghiului este {dreptunghi.area()}')
dreptunghi.descriere()
print(f'perimetrul este {dreptunghi.perimetru()}')

























