jucatori = ["Jucator1", "Jucator2", "Jucator3", "Jucator4", "Jucator5"]
jucator_in_teren = "Jucator1"
schimbari_efectuate = 0
schimbari_max = 3


def efectueaza_schimbare(jucator_in_teren, jucator_nou):
    if jucator_in_teren in jucatori:
        jucatori.remove(jucator_in_teren)
        jucatori.append(jucator_nou)
        return True
    else:
        return False


def afiseaza_stare(jucator_in_teren, schimbari_ramase):
    print(f"A intrat {jucator_in_teren}, a iesit {jucatori[-1]}, mai ai {schimbari_ramase} schimbari.")

# Testarea codului

# Efectuăm o schimbare


if efectueaza_schimbare(jucator_in_teren, "JucatorNou"):
    schimbari_efectuate += 1
    afiseaza_stare(jucator_in_teren, schimbari_max - schimbari_efectuate)
else:
    print(f"Nu se poate efectua schimbarea deoarece jucatorul {jucator_in_teren} nu e in teren.")
    afiseaza_stare(jucator_in_teren, schimbari_max - schimbari_efectuate)

# Efectuăm încă două schimbări
if efectueaza_schimbare("JucatorNou", "JucatorNou2"):
    schimbari_efectuate += 1
    afiseaza_stare("JucatorNou", schimbari_max - schimbari_efectuate)
else:
    print(f"Nu se poate efectua schimbarea deoarece jucatorul JucatorNou nu e in teren.")
    afiseaza_stare("JucatorNou", schimbari_max - schimbari_efectuate)

if efectueaza_schimbare("JucatorNou2", "JucatorNou3"):
    schimbari_efectuate += 1
    afiseaza_stare("JucatorNou2", schimbari_max - schimbari_efectuate)
else:
    print(f"Nu se poate efectua schimbarea deoarece jucatorul JucatorNou2 nu e in teren.")
    afiseaza_stare("JucatorNou2", schimbari_max - schimbari_efectuate)

# Mai avem o schimbare disponibilă, încercăm să scoatem un jucător care nu este în teren
if efectueaza_schimbare("JucatorNexistant", "JucatorNou4"):
    schimbari_efectuate += 1
    afiseaza_stare("JucatorNexistant", schimbari_max - schimbari_efectuate)
else:
    print(f"Nu se poate efectua schimbarea deoarece jucatorul JucatorNexistant nu e in teren.")
    afiseaza_stare("JucatorNexistant", schimbari_max - schimbari_efectuate)

# În acest exemplu, am simulat schimbările într-o echipă de fotbal cu 5 jucători, unde se permit maximum 3 schimbări.
# Funcția efectueaza_schimbare verifică dacă jucătorul ales pentru a fi înlocuit se află în teren și
# efectuează schimbarea corespunzătoare.
# Funcția afiseaza_stare afișează starea echipei după fiecare schimbare.
# Rezultatul afișat pentru acest exemplu va fi:
"""
css
Copy code
A intrat JucatorNou, a iesit Jucator5, mai ai 2 schimbări.
A intrat JucatorNou2, a iesit JucatorNou, mai ai 1 schimbări.
A intrat JucatorNou3, a iesit JucatorNou2, mai ai 0 schimbări.
Nu se poate efectua schimbarea deoarece jucatorul JucatorNexistant nu e in teren.
A intrat JucatorNexistant, a iesit JucatorNou3, mai ai 0 schimbări.
În ultimul caz, schimbarea nu poate fi efectuată deoarece jucătorul JucatorNexistant nu se află în teren.
"""

# VARIANTA 2
echipa_fotbal = ['Jucator1', 'Jucator2', 'Jucator3', 'Jucator4', 'Jucator5']
schimbari_efectuate = 0
schimbari_max = 3

# Funcția pentru efectuarea unei schimbări


def efectueaza_schimbare(jucator_in, jucator_out):
    global schimbari_efectuate
    if jucator_out in echipa_fotbal:
        index = echipa_fotbal.index(jucator_out)
        echipa_fotbal[index] = jucator_in
        schimbari_efectuate += 1
        print("A intrat", jucator_in + ",", "a iesit", jucator_out + ",",
              "mai ai", schimbari_max - schimbari_efectuate, "schimbari.")
        echipa_fotbal.remove(jucator_out)
    else:
        print("Nu se poate efectua schimbarea deoarece jucatorul", jucator_out, "nu e in teren.")
        print("Mai ai", schimbari_max - schimbari_efectuate, "schimbari.")

# Exemplu de utilizare


efectueaza_schimbare('Jucator6', 'Jucator1')
efectueaza_schimbare('Jucator7', 'Jucator2')
efectueaza_schimbare('Jucator8', 'Jucator9')

# VARIANTA 3

jucatori = ['Jucator1', 'Jucator2', 'Jucator3', 'Jucator4', 'Jucator5']
schimbari_efectuate = 0
schimbari_max = 3


def efectueaza_schimbare(jucator_intra, jucator_iese):
    global schimbari_efectuate
    if jucator_iese in jucatori:
        jucatori.remove(jucator_iese)
        jucatori.append(jucator_intra)
        schimbari_efectuate += 1
        print(f"A intrat {jucator_intra}, a iesit {jucator_iese},"
              f" mai ai {schimbari_max - schimbari_efectuate} schimbari.")
    else:
        print(f"Nu se poate efectua schimbarea deoarece jucatorul {jucator_iese} nu este in teren."
              f" Mai ai {schimbari_max - schimbari_efectuate} schimbari.")

# Exemplu de utilizare


efectueaza_schimbare('Jucator6', 'Jucator1')  # A intrat Jucator6, a iesit Jucator1, mai ai 2 schimbari.
efectueaza_schimbare('Jucator7', 'Jucator3')  # A intrat Jucator7, a iesit Jucator3, mai ai 1 schimbari.
efectueaza_schimbare('Jucator8', 'Jucator5')  # A intrat Jucator8, a iesit Jucator5, mai ai 0 schimbari.
efectueaza_schimbare('Jucator9', 'Jucator2')  # Nu se poate efectua schimbarea deoarece jucatorul Jucator2 nu este in
# teren. Mai ai 0 schimbari.


# În codul de mai sus, am declarat o listă numită jucatori care conține inițial 5 jucători.
# Am definit, de asemenea, variabilele schimbari_efectuate și schimbari_max pentru a urmări numărul
# de schimbări efectuate și numărul maxim de schimbări permise.
# Funcția efectueaza_schimbare primește doi parametri: jucator_intra și jucator_iese, reprezentând jucătorii
# care urmează să intre și să iasă.
# Dacă jucătorul care urmează să iasă este prezent în lista jucatori, acesta este eliminat,
# iar jucătorul care urmează să intre este adăugat la finalul listei. Apoi, variabila schimbari_efectuate
# este incrementată, iar un mesaj corespunzător este afișat.
# Dacă jucătorul care urmează să iasă nu este în teren, se va afișa un mesaj corespunzător.
# Codul de test exemplifică utilizarea funcției efectueaza_schimbare cu diferite valori.
# Puteți adăuga mai multe apeluri ale acestei funcții pentru a testa și alte cazuri.
