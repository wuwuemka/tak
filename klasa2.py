from klasa1 import Uzytkownik

class Uczen(Uzytkownik):
    def __init__(self,klasa,ulubionalekcja,wzrost,specnaucz):
        self.klasa = klasa
        self.ulubionaleckja = ulubionalekcja
        self.wzrost = wzrost
        self.specnaucz = specnaucz

    def showklasa(self):
        print(self.klasa)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.klasa = str(input('Nowa klasa: '))
        if inp == 'nie':
            print('ok')
        else:
            pass
    def showulubionalekcja(self):
        print(self.ulubionaleckja)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.password = str(input('Nowa ulub lekcja: '))
        if inp == 'nie':
            print('ok')
        else:
            pass
    def showwzrost(self):
        print(self.wzrost)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.ip = float(input('Nowy wzrost: '))
        if inp == 'nie':
            print('ok')
        else:
            pass
    def showspecnaucz(self):
        print(self.specnaucz)
        inp = input('zmienic? ')
        if inp == 'Tak':
            inp2 = input('ma spec naucz czy nie? ')
            if inp2 == 'tak':
                self.specnaucz = True
            if inp2 == 'nie':
                self.specnaucz = False
        if inp == 'nie':
            print('ok')
        else:
            pass