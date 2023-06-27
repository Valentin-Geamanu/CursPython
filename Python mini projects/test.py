"""

class Dreptunghi:
    lungime = 39
    latime = 54
    culoare = 'blue'

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        print(f'Dreptunghiul are o lungime de {self.lungime}, latime de {self.latime}. Culoarea este: {self.culoare}')

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
"""

# calcularea mediei
"""
note_examen = int(input('Introdu notele de la examen:' ))
while note_examen >= 0:
    print(note_examen)
    if note_examen == -1:
        break
    print(note_examen)
"""
"""
note = []
nota = int(input('Introduceti nota (introduceti -1 pentru a incheia lista de note):'))
while nota != -1:
    note.append(nota)
    nota = int(input('Introduceti nota (introduceti -1 pentru a incheia lista de note):'))
media = sum(note) / len(note)
print('Media notelor este:', media)
"""

# def note_examen(mate, romana, engleza, geografie ):
#    media = sum(note_examen()) / len(note_examen())
#    print(f'Media notelor este:', media)

# note_examen(5, 7, 8, 10)




