"""
#  SINGLETON
class PresedinteRomania:
    instance = None

    def __new__(cls):
        if not cls.instance:  # hasattr e mai util decat 'if not'
            cls.instance = super().__new__(cls)
        return cls.instance

    def __str__(self):
        return 'Eu sunt presedintele Romaniei'

    def say_hello(self):
        return f'Salut {self}'


a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')
"""
# FACTORY PATTERNS

"""
class TranslatorFactory:
    translator = {}

    def localize(self, cuvinte):
        return self.translator.get(cuvinte, 'traducerea nu este valabila')

    def get_translator(self, language):
        if language == 'en':
            return EnglishTranslator()
        elif language == 'fr':
            return FrenchTranslator()
        elif language == 'es':
            return SpanishTranslator
        else:
            print(f'Traducerea nu este valabila')


class EnglishTranslator(TranslatorFactory):
    translator = {
        'masina': 'car'
    }


class FrenchTranslator(TranslatorFactory):
    translator = {
        'masina': ''
    }


class SpanishTranslator(TranslatorFactory):
    translator = {
        'masina': ''
    }


factory = TranslatorFactory()
french_trans = factory.get_translator('fr')
english_trans = factory.get_translator('en')
spanish_trans = factory.get_translator('es')

print(f'In engleza zicem {english_trans.localize("masina")}')
print(f'In spaniola zicem {spanish_trans.localize("masina")}')
print(f'In franceza zicem {french_trans.localize("masina")}')
"""


import random


def generare_numere_loterie():
    numere_loterie = []
    for numbers in range(6):
        numbers = random.randint(1, 49)
        while numbers in numere_loterie:
            numbers = random.randint(1, 49)
        numere_loterie.append(numbers)
    return numere_loterie


def generare_numar_norocos():
    numar_norocos = random.randint(1, 10000000)
    return numar_norocos


numere_loterie = generare_numere_loterie()
numar_norocos = generare_numar_norocos()
print('Numerele norocoase la 6/49 sunt:', numere_loterie)
print('Numarul de noroc este:', numar_norocos)