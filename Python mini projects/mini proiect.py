from abc import ABC, abstractmethod


class IMasina(ABC):

    @abstractmethod
    def descrie(self):
        pass

    @abstractmethod
    def inmatriculare(self, nr_inmatriculare):
        pass

    @abstractmethod
    def vopseste(self, culoare):
        pass

    @abstractmethod
    def accelereaza(self, viteza):
        pass

    @abstractmethod
    def franeaza(self):
        pass


class Masina(IMasina):
    MARCA = 'Dacia'
    CULORI_DISPONIBILE = {'ROSU', 'VERDE', 'RAPTOR', 'ALBASTRU'}

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima
        self.viteza_actuala = 0
        self.__culoare = 'GRI'
        self.__inmatriculata = False
        self.__nr_inmatriculare = None

    @property
    def culoare(self):
        print("Getter culoare")
        return self.__culoare

    @property
    def inmatriculata(self):
        print("Getter inmatriculata")
        return self.inmatriculata

    @property
    def nr_inmatriculare(self):
        print("Geter nr_inmatriculare")
        return self.__nr_inmatriculare

    def descrie(self):
        print(self.MARCA)
        print(self.model)
        print(self.viteza_maxima)
        print(self.viteza_actuala)
        print(self.__inmatriculata)
        print(self.__culoare)
        print(self.__nr_inmatriculare)

    def inmatriculare(self, nr_inmatriculare):
        self.__nr_inmatriculare = nr_inmatriculare
        self.__inmatriculata = True

    def vopseste(self, culoare):
        if culoare in self.CULORI_DISPONIBILE:
            self.__culoare = culoare
        else:
            print("Culoarea NU este dipsonibila")

    def accelereaza(self, viteza):
        if viteza < 0:
            print('Viteza nu poate sa fie  o valoare negativa')

        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_maxima = viteza

    def franeaza(self):
        self.viteza_maxima = 0


masina1 = Masina("1300", 100)
masina1.descrie()
masina1.inmatriculare("SB-93-STF")
masina1.descrie()
masina1.vopseste("Rosu")
masina1.descrie()
print(masina1.culoare)

print(masina1.viteza_actuala)
masina1.accelereaza(-1)
print(masina1.viteza_actuala)
masina1.accelereaza(200)
print(masina1.viteza_actuala)
masina1.accelereaza(50)
print(masina1.viteza_actuala)
masina1.franeaza()
print(masina1.viteza_actuala)
