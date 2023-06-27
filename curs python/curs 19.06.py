from abc import ABC, abstractmethod


class FormaGeometrica:

    def __init__(self, culoare):
        self.culoare = culoare

    def descrie(self):
        print(f'Forma geometrica are culoare {self.culoare}')


class Dreptunghi(FormaGeometrica):

    def __init__(self, coloare, latime, lungime):
        super().__init__(coloare)
        self.latime = latime
        self.lungime = lungime

    def aria(self):
        return self.latime * self.lungime


f1 = FormaGeometrica('albastru')
f1.descrie()

dreptunghi1 = Dreptunghi('galben', 5, 8)
dreptunghi1.descrie()
dreptunghi1.aria()


def func1(num):
    return num + 25


func1(5)
print(num)


def func1(name, age=20):
    print(name, age)


func1('Emma', 25)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self):
        return self.salary + self.bonus


employee1 = Employee('Archer Arios', 5000)
manager1 = Manager('Jhon Snow', 8000, 2000)
print(employee1.get_salary())
print(manager1.get_salary())


# Design Patterns
# Creational design pattern: Singleton DP


class SingletonClass:
    __instance = None
    sector = "IT"

    def __init__(self, name):
        # initializam attribute,
        # chemat in momentul instantei obiectului
        self.name = name

    def __new__(cls, *args):
        # initializam clasa, metoda magica __new__
        # se apeleaza inaintea __init__
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


obj1 = SingletonClass("JavaScript")
print(obj1.name)
print(obj1.sector)
print(obj1)
print(id(obj1))

obj2 = SingletonClass("Python")
print(obj2.name)
print(obj2.sector)
print(obj2)
print(id(obj2))

print(obj1.name)
print(obj1 == obj2)
print(obj1 is obj2)

obj3 = SingletonClass("Assembly")
print(obj1.name)
print(obj2.name)
print(obj3.name)


# Structural design pattern: Proxy DP


class AbstractCar(ABC):

    @abstractmethod
    def drive(self):
        pass


class Car(AbstractCar):
    def drive(self):
        print("You are driving the car.")


class Driver:
    def __init__(self, age):
        self.age = age


class ProxyCar(AbstractCar):
    def __init__(self, driver: Driver):
        self.car = Car()
        self.driver = driver

    def drive(self):
        if self.driver.age < 18:
            print("Sorry little driver, you are too young to drive.")
        else:
            self.car.drive()


driver = Driver(16)
print(driver.age)
# Daca instantiem direct clasa Car,
# nu avem constrangere asupra varstei
car = Car()
car.drive()

# Asa ca nu instantiem direct Car, ci instantiem ProxyCar,
# aceasta verificand varsta soferului
proxy_car = ProxyCar(driver)
proxy_car.drive()

new_driver = Driver(20)
proxy_car = ProxyCar(new_driver)
proxy_car.drive()


# Behavioral design pattern: Observer DP


class ObservablePerson:
    name = "Default User"

    def __init__(self):
        self._observers = []

    def __str__(self):
        return f"I am {self.name}"

    def register_observer(self, observer):
        # inregistram un observer
        self._observers.append(observer)

    def notify_observers(self, message):
        # fiecare Observer este notificat
        # prin apelul functiei notify din clasa Observer
        for obs in self._observers:
            obs.notify(self, message)


class Observer:
    def __init__(self, name, observable):
        # in momentul instantierii Observerului, acesta este
        # inregistrat in lista de observeri ai obiectului Observable
        self.name = name
        observable.register_observer(self)

    def notify(self, observable, message):
        print(f"Observer: {self.name} Got message: {message}")
        print(f" from observable obj: {observable}")


subject = ObservablePerson()
observer_obj1 = Observer("obs1", subject)
observer_obj2 = Observer("obs2", subject)

# in momentul apelului ambele obiecte observer primesc notificare
subject.notify_observers("An event occured....")
