
my_list = [5, 10, 15, 25]
print(my_list[:: -2])

#   FUNCTII:
# functie simpla -> nu are parametri si nu returneaza nimic


def first_function():
    print("Hello World!")


first_function()
first_function()
for number in range(1, 11):
    print(number)


def get_number():
    for number in range(1, 11):
        print(number)


get_number()


def get_numbers(start, end):
    for number in range(start, end):
        print(number)


get_numbers(1, 11)
get_numbers(3, 7)

# functie cu parametri care nu returneaza nimic
# functie cu 1 singur argument/parametru


def print_hi(user):
   print(f"Hi, {user}")


print_hi('Andy87')
print_hi('Andrei')

# functie cu parametri care nu returneaza nimic
# functie cu doi parametri


def add_numbers(a, b):
    result = a + b

# print(f'Sum: {result}')


add_numbers(1, 2)
add_numbers(3, 4)

add_numbers(a=1, b=3)
add_numbers(a=3, b=1)

number1 = int(input('introdu valoare pentru a:'))
number2 = int(input('introdu valoare pentru b:'))
add_numbers(number1, number2)
add_numbers(a=number1, b=number2)


"""
EX2: Scrie o functie care parcurge o lista de numere data si
afiseaza mesajul 'Este par' pentru numerele pare si
'Este impar' pentru numere impare.
Daca in lista se gaseste un element care nu e numar intreg,
afiseaza un mesaj utilizatorului si apoi sari peste
elementul respectiv.
(Foloseste functia built-in isinstance()
pentru verificare daca elementul curent e int sau nu)
"""
my_str = 'abc'
print(isinstance(my_str, int))


def par_impar(lista):
    for num in lista:
        if isinstance(num, int):
            if num % 2 == 0:
                print(num, 'este par')
            else:
                print(num, 'este impar')
        else:
            print('Elementul', num, 'nu este un numar intreg')


par_impar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "string"])


# FUNCTIA 'RETURN'
# functie cu return

def numar_preferat():
    numar = 7
    return numar


numar = numar_preferat()
print(numar)

"""
1. Scrie un program care afiseaza primii 7 multiplii
a lui 7.
HINT: for loop + if + break
Expected Output: 0 7 14 21 28 35 42 49
"""

result = ''
for numar in range(0, 8):
    x = 7 * numar
    result += str(x)
    result += ' '
print(result)

result1 = ''
y = 0
for i in range(0, 100):
    if y == 7:
        break
    if i % 7 == 0:
        result1 += str(i) + ' '
        y += 1
print(result1)

# Exemplul 1:
x = 5 / 0  # ZeroDivisionError

# Exemplul 2:
my_dict = {'pret': 25.00, 'nume': 'perna'}
print(my_dict['culoare'])  # KeyError

try:
    # execute/run this code
    x = 5 / 0
except ZeroDivisionError:
    # execute this block when exception occured
    print("Can not divide by zero!")
else:
    # execute this block if no exception occured
    print("Yeah! Your answer is: ", x)
finally:
    # always execute this block of code
    print("This is always executed!")


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Al doilea parametru trebuie "
                                "sa fie diferit de 0.")
    return a / b


print(divide(1, 0))


#  CURS 6 OOP
# Clase in Python

class Car:
    # fields (atributtes) atribute ale clasei
    make = 'Dacia'
    model = None
    year = 2022
    color = None

    # methods
    def accelerate(self):
        self.year
        print(f'Masina {self.make} face Vrum vrrrum')

    def stop(self):
        print('STOP')


# creem o instanta / obiect a clasei Car


car1 = Car()
print(car1.year)
print(car1.color)
car1.accelerate()
car1.color = 'red'
print(car1.color)

car2 = Car()
print('car2 color', car2.color)
Car.color = 'blue'
car3 = Car()
print('car3 color', car3.color)


# CONSTRUCTORI:
# __init__

class Car:
    # fields (attributes)/ atribute ale clasei
    make = 'Dacia'
    year = 2022

    # metoda de initializare / constructor

    def __init__(self, m, c):
        self.model = m  # atribut al obiectului
        self.color = c  # atribut al obiectului


car1 = Car('Duster', 'white')
car2 = Car('Logan', 'blue')

car3 = Car(m="Duster", c='red')
car3 = Car(c="red", m='Duster')
print(car3.color)
# car3 = Car('Duster')


print(car1.make)
print(car1.model)
print(car1.color)


# valori default pentru parametri
# functii


def multiply(a, b=2):
    return a * b


print(multiply(1, 5))
print(multiply(4))


# clase


class Employee:
    def __init__(self, name, age, working_experiance):
        self.name = name
        self.age = age
        self.working_experiance = working_experiance

    def describe(self):
        print(f'{self.name} lucreaza la aceatsa companie de {self.working_experiance} ani')


employee1 = Employee('Ana', 38, 5)
employee1.describe()

student1 = Employee('Gelu', 20, 0)
student1.describe()
student1.working_experiance = 2
print(student1.working_experiance)
student1.describe()
