from klasa1 import Uzytkownik
class Rodzic(Uzytkownik):
    def __init__(self,czyj,wktorejklasiedziecko,zawod,mapieniondze):
        self.czyj = czyj
        self.wktorejklasiedziecko = wktorejklasiedziecko
        self.zawod = zawod
        self.mapieniondze = mapieniondze
    
    def showczyj(self):
        print(self.czyj)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.czyj = str(input('Nowe dziecko: '))
        if inp == 'nie':
            print('ok')
        else:
            pass
    def showktorejklasiedziecko(self):
        print(self.wktorejklasiedziecko)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.wktorejklasiedziecko = str(input('W ktorej klasie jest dziecko? '))
        if inp == 'nie':
            print('ok')
        else:
            pass
    def showzawod(self):
        print(self.zawod)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.zawod = str(input('Nowy zawód: '))
        if inp == 'nie':
            print('ok')
        else:
            pass
    def showmapieniondze(self):
        print(self.mapieniondze)
        inp = input('zmienic? ')
        if inp == 'Tak':
            inp2 = input('Ma pieniądze? ')
            if inp2 == 'tak':
                self.mapieniondze = True
            if inp2 == 'nie':
                self.mapieniondze = False
        if inp == 'nie':
            print('ok')
        else:
            pass