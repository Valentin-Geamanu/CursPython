

# Interactiunea cu fisierele:

f = open('my_first_file.txt', 'r')
print(f.read())
f.close()

# ce se intampla daca apar erori inainte sa inchidem fisierul
"""
f = open('my_first_file.txt', 'r')

if aaaaa:
    print('doing something')
f.close()
# apare o eroare in codul nostru inainte sa se ajunga la inchiderea fisierului
# fisierul nu va fi inchis niciodata
# consumam resurse ier datele raman exxpuse/vurnerabile.
"""
# imbunatatirea codului de mai sus:
# varianta 1:

f = open('my_first_file.txt', 'r')

try:
    print(f.read())
    if aaaaa:
        print('doing something')
except Exception:
    print('avem o exceptie')
finally:
    print('la final inchidem fisierul orice ar fi')
    f.close()

# varianta 2:
# folosirea de context managers

with open('my_first_file.txt', 'r') as f:
    # variabila f contine/ repezinta rezultatul expreiei apelate in blocul with
    # si este disponibila in interiorul blocului with
    print('suntem in blocul with')
    print(f.read())
print('Suntem in afara blocului with')
# print(f.read()) eroare in momentul cand am iesit din blocul withfisierul nu mai este deschis


class File:
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


with File("my_first_file.txt", "r") as file:
    print(file.read())

print('here')
