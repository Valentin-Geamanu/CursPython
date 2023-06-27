from abc import ABC, abstractmethod
import math
"""
    OOP - advance
Exerciții - studiu în workshopul de weekend
1. ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’

2. INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

3. Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte 
(opțional, doar dacă ai ales să implementezi metoda abstractă aria)

POLYMORPHISM 
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
"""


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descriere(self):
        print('Cel mai probabil am colturi')


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        print('Getter')
        return self.__latura

    @latura.setter
    def latura(self, latura_noua):
        print('setter')
        self.__latura = latura_noua

    @latura.deleter
    def latura(self):
        print('deleter')
        self.__latura = 0

    def aria(self):
        return self.latura ** 2


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, noua_raza):
        self.__raza = noua_raza

    @raza.deleter
    def raza(self):
        print('Deleter')
        self.__raza = 0
    #    del self.__raza

    def aria(self):
        return self.PI * self.raza ** 2

    def descriere(self):
        print('Eu nu am colturi')


patrat1 = Patrat(6)
print(patrat1.latura)
patrat1.latura = 10
print(patrat1.latura)
del patrat1.latura
cerc = Cerc(3)
print(cerc.raza)
cerc.raza = 5
print(cerc.raza)
print(cerc.aria())
cerc.descriere()

"""
4. Creează un obiect de tip Pătrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
"""


class Patrat:
    def __init__(self, latura):
        self.latura = latura

    def calculeaza_perimetru(self):
        return 4 * self.latura

    def calculeaza_arie(self):
        return self.latura ** 2


# Crearea unui obiect de tip Patrat
patrat = Patrat(5)

# Apelarea metodelor obiectului patrat
print("Latura patratului:", patrat.latura)
print("Perimetrul patratului:", patrat.calculeaza_perimetru())
print("Aria patratului:", patrat.calculeaza_arie())


class Cerc:
    def __init__(self, raza):
        self.raza = raza

    def calculeaza_diametru(self):
        return 2 * self.raza

    def calculeaza_circumferinta(self):
        return 2 * math.pi * self.raza

    def calculeaza_arie(self):
        return math.pi * self.raza ** 2


# Crearea unui obiect de tip Cerc
cerc = Cerc(3)

# Apelarea metodelor obiectului cerc
print("Raza cercului:", cerc.raza)
print("Diametrul cercului:", cerc.calculeaza_diametru())
print("Circumferința cercului:", cerc.calculeaza_circumferinta())
print("Aria cercului:", cerc.calculeaza_arie())
