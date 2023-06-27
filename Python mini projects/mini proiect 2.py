

class TodoList:
    def __init__(self):
        self.todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere

    def finalizeaza_task(self, nume):
        if nume in self.todo:
            del self.todo[nume]
        else:
            print("nu a sters")

    def afiseaza_todo_list(self):
        for asd in self.todo.keys():
            print(asd)
#  def afiseaza_todo_list(self):   var 2
#     print(list(self.todo.keys()))


task = TodoList()
task.adauga_task("curatenie", "la ora 10")
print(task.todo)
task.adauga_task("cumparaturi", "la salar")
print(task.todo)
task.finalizeaza_task("curatenie")
print(task.todo)
task.finalizeaza_task("bani")
print(task.todo)
task.adauga_task("sedinta", "strada_primaverii")
task.adauga_task("zii de nastere", "la_george")
task.afiseaza_todo_list()


def calculeaza_suma(a, b):
    return a + b


print(calculeaza_suma(1, 2))


def calculeaza_suma2(a, b):
    suma = a + b
    return suma
    # print(suma)


print(calculeaza_suma2(1, 2))

suma_calculata = calculeaza_suma2(1, 2)
print(suma_calculata)
