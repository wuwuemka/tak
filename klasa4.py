from klasa1 import Uzytkownik
class Nauczyciel(Uzytkownik):
    def __init__(self,admin,kwalifikacje,przedmiot,wychowawca):
        self.admin = admin
        self.kwalifikacje = kwalifikacje
        self.przedmiot = przedmiot
        self.wychowawca = wychowawca
    
    def showadmin(self):
        print(self.admin)
        inp = input('zmienic? ')
        if inp == 'Tak':
            inp2 = input('Admin czy nie? ')
            if inp2 == 'tak':
                self.admin = True
            if inp2 == 'nie':
                self.admin = False
        if inp == 'nie':
            print('ok')
        else:
            pass
    def pokakwalifikacje(self):
        print(self.kwalifikacje)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.kwalifikacje = str(input('Nowe kwalifikaje: '))
        if inp == 'nie':
            print('ok')
        else:
            pass
    def showprzedmiot(self):
        print(self.przedmiot)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.przedmiot = str(input('Czego uczy? '))
        if inp == 'nie':
            print('ok')
        else:
            pass
    def pokawychowawca(self):
        print(self.wychowawca)
        inp = input('zmienic? ')
        if inp == 'Tak':
            inp2 = input('Jest wychowawcą? ')
            if inp2 == 'tak':
                self.wychowawca = True
            if inp2 == 'nie':
                self.wychowawca = False
        if inp == 'nie':
            print('ok')
        else:
            pass