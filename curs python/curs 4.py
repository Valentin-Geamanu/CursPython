
from abc import ABC, abstractmethod

print('Hello World')


class Chef:

    def __init__(self, experience):
        self.experience = experience

    def make_salad(self):
        print("salad")

    def make_fries(self):
        print("fries")


# child class - mosteneste din clasa Chef
# se trece intre paranteze numele clasei parinte
class JapaneseChef(Chef):

    def make_sushi(self):
        print("sushi")


# child class - mosteneeste din clasa Chef
# se trece intre paranteze numele clasei parinte

class ItalianChef(Chef):

    def make_pizza(self):
        print("pizza")


chef1 = Chef(2)
chef1.make_salad()
chef1.make_fries()
print(chef1.experience)

chef2 = JapaneseChef(15)
chef2.make_sushi()

chef2.make_salad()
chef2.make_fries()
print(chef2.experience)

chef3 = ItalianChef(23)
chef3.make_pizza()

chef3.make_salad()
chef3.make_fries()
print(chef3.experience)


class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"Animal {self.name} has {self.age} years old.")


class Dog(Animal):

    # Pentru a adauga proprietati noi:
    # 1. Extindem lista de parametrii pe care
    # metoda __init__ ii poate lua.
    # 2. Apelam __init__-ul din clasa parinte, folosindu-ne de
    # super(), cu parametrii pentrunecesari pentru clasa parinte.
    def __init__(self, name, age, sound, color):
        super().__init__(name, age)
        self.sound = sound
        self.color = color

    # Pentru a extinde metode din clasa parinte:
    # Facem apel la metoda din clasa parinte folosind super()
    def describe(self):
        super().describe()
        print(f"Animal's color is {self.color}.")
        print(f"He says: {self.sound}.")


animal = Animal(name='Spike', age=4)
print(animal.age)
print(animal.name)
animal.describe()

dog1 = Dog(
    name='Max',
    age=12,
    color='white',
    sound='ham ham'
)

print(dog1.name)
print(dog1.age)
print(dog1.color)
print(dog1.sound)


"""
EX1: MOSTENIRE
a. Defineste o clasa numita Persoana.
Aceasta clasa va avea urmatoarele atribute (in constructor):
- nume
- varsta

Implementeaza metoda descrie(), care va afisa mesajul:
'Persoana {nume} are {varsta} ani.'

b. Defineste clasa Angajat, care mosteneste din clasa Persoana.
Aceasta clasa va lua in constructor inca doi parametri,
salariu si post.
Defineste metoda afiseaza_salariu, care returneaza
atributul salariu.

c. Creeaza un obiect de tip clasa Persoana.
Acceseaza si afiseaza proprietatile acesteia.
Apeleaza/invoca metoda descrie.

d. Creeaza un obiect de tip Angajat.
Acceseaza si afiseaza proprietatile acesteia.
Apeleaza/invoca metodele disponibile pe aceasta.

e. Extinde metoda descrie din clasa Angajat,
astfel incat sa se afiseze
si o propozitie care contine atributele salariu si post.
"""


class Persoana:

    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def describe(self):
        print(f'Persoana {self.nume} are {self.varsta} ani')


class Angajat(Persoana):

    def __init__(self, nume, varsta, salariu, post):
        super().__init__(nume, varsta)
        self.salariu = salariu
        self.post = post

    def show_salariu(self):
        return self.salariu

    def describe(self):
        super().describe()
        print(f'Salariul este {self.salariu} pentru postul de {self.post}')


pers1 = Persoana('Vasile', 45)
print(pers1.nume)
print(pers1.varsta)
pers1.describe()

emp1 = Angajat('Andrei', 34, 1500, 'necalificat')
print(emp1.nume)
print(emp1.varsta)
print(emp1.salariu)
print(emp1.post)

print(f"{emp1.nume} has the salary of {emp1.show_salariu()} lei")
emp1.describe()


# Exemplu de class methods polimorfice


class Romania:
    def language(self):
        print("Romanian")


class USA:
    def language(self):
        print("English")


obj_ro = Romania()
obj_usa = USA()

obj_ro.language()
obj_usa.language()


def get_country_language(country_obj):
    country_obj.language()


get_country_language(obj_ro)
get_country_language(obj_usa)


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    def describe(self):
        print('This animal is my favorit!')


class Dog(Animal):

    def sound(self):
        print("Ham ham")

    def sleep(self):
        print('ZZZZ')


class Cat(Animal):

    def sound(self):
        print("Miau miau")

    def sleep(self):
        print("Prrrr")


cat = Cat()
cat.sound()
cat.sleep()
cat.describe()
dog = Dog()
dog.sleep()
dog.sound()
dog.describe()


"""
EX3: ABSTRACTIZARE
a. Defineste interfata Car. Aceasta va avea o metoda
abstracta numita car_model.

b. Defineste clasele Tesla si BMW, care implementeaza
interfata Car.
Metoda car_model trebuie sa afiseze un mesaj legat
de modelul masinii.

Instantiaza clasele Tesla si BMW si invoca metoda 
car_model pe fiecare din acestea.
"""


class Car(ABC):
    @abstractmethod
    def car_model(self, model):
        pass


class Tesla(Car):
    def __init__(self, model):
        self.model = model

    def car_model(self):
        print(f'Acesta este {self.model}')


class Bmw(Car):
    def __init__(self, model):
        self.model = model

    def car_model(self):
        print(f'Acesta este {self.model}')


bmw = Bmw("e46")
bmw.car_model()

tesla = Tesla('s3')
tesla.car_model()


class Car:

    def __init__(self, brand, price):
        self.__brand = brand  # atribut privat
        self._price = price   # atribut protejat

    def run(self):
        print(f"Please run {self.__brand}")


car = Car("Dacia", 6000)

# print(car.__brand)  # -> eroare

print(car._price)

car.run()


class Car:
    __color = 'grey'

    def get_color(self):  # folosim getter sa afisam culoarea
        return self.__color

    def set_color(self, culoarea_dorita):  # folosim setter ca sa setam o alta culoare
        self.__color = culoarea_dorita


"""

class User:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    def get_passowrd(self):
        return '*' * len(self.__password)

    def set_password(self, new_password):
        if len(new_password) < 10:
            print('Parola noua trebiue sa aiba 10 caractere')
            return



    for index in range(0, len(new_password)):
        if new_password
"""

numar = int(input('introdu un numar:'))
rezultat = 0
try:
    rezultat = 10 / numar
except ZeroDivisionError:
    print('Nu se poate face impartirea la 0.')
else:
    # se intra inn nlocul else doar daca nu s-a aruncat exceptia
    print('Blocul esle')
finally:
    # indiferent daca se arunca sau nu exceptia , blocul finaly este executat

    print('Finaly se executa mereu')
print(rezultat)


class Car:

    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        print('Getter')
        if self.__color is not None:
            self.__color.upper()
        return self.color
           
    @color.setter
    def color(self, culoare_noua):
        print('Setter')
        self.__color = culoare_noua
     
    @color.deleter
    def color(self):
        print('Deleter')
        self.__color = None


car1 = Car('rosu')
print(car1.color)

car1.color = 'verde'
print(car1.color)


class Person:

    def __init__(self, name, cnp, age, height):
        self.name = name
        self.__cnp = cnp  # Atribut privat
        self.age = age
        self.height = height

    @property
    def cnp(self):
        print('Getter cnp')
        return self.__cnp

    @cnp.setter
    def cnp(self, new_cnp):
        print('Setter cnp')
        if len(new_cnp) == 13:
            self.__cnp = new_cnp
        else:
            print('Invalid cnp value')


person1 = Person('George', '1970629204466', 26, 180)
print(person1.cnp)
person1.cnp = '155548632'
print(person1.cnp)
