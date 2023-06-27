'''
print('Hello World', 'First workshop')

# Lets Start

# variablia este o cutie de valori

my_int = my_second_int = 10

print('Salut', my_int)


1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o.
Inversează ordinea folosind slicing și suprascrie această listă.
Printează varianta actuală (inversată).
Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea.
Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.


arr = ['do', 're' , 'mi' , 'fa', 'sol', 'la', 'si', 'do']

def reverse_list(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
          # variabila tampon
          #data loss
          temp = arr[left]
          arr[left] = arr[right]
          arr[right] = temp
          left += 1
          right -= 1
    return arr

#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
print(reverse_list(arr))

'''

"""
Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găsește 2 variante să le unești într-o singură listă. 
"""
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]

list = list1 + list2
print(list)

list = list1.append(list2)
print(list)

# initializinglists
test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]

# using * operator to concat
res_list = [test_list1, test_list2]

# Printing concatenated list
print("Concatenated list using * operator : "
      + str(res_list))
# Sortează și afișează lista generată la exercițiul anterior.
# Șterge numărul 0 folosind o funcție.
# Afișaza iar lista.

list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
list = list1 + list2
print(list)



# Folosind un if verifică lista generată la exercițiul 3 și afișează:
# Lista este goală.
# Lista nu este goală.

# if len(list) != 0


# 8. Având dicționarul dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# Folosește o funcție că să afișezi Elevii (cheile)
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}

print(dict1.items())
for item in dict1.items():
    print(item)
#for key,value in dict1.items():
#    print(key,'A luat nota ', value)
# Pentru modificarea unei chei
dict1.update({'Dorel': 6})
print(dict1)
# Pentru eliminarea unei chei
dict1.pop('Gigel')
print(dict1)
# Pentru adaugarea unei chei
dict1.update({'Ionica':9})
print(dict1)
for key,value in dict1.items():
   print(key,'A luat nota ', value)

"""
1.Având lista:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

Folosește un for că să iterezi prin toată lista și să afișezi ‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while.
"""
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
x = 'Toyota'

for masina in masini:

   if masina == x:
       print(f'Masina mea preferata este {masina}')
    else:
    print(f'Masina ta nu este in lista')
"""
for masina in masini:
    while masina != x:
      print(f'Masina mea preferata este {masina}')"""










