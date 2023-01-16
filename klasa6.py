from klasa4 import Nauczyciel

class Dyrektor(Nauczyciel):
    def __init__(self,iledobrychzmian,ilelatpracuje,opinianauczycieli,czyuczy):
        self.iledobrychzmian = iledobrychzmian
        self.ilelatpracuje = ilelatpracuje
        self.opinianauczycieli = opinianauczycieli
        self.czyuczy = czyuczy

    def showiledobrychzmian(self):
        print(self.iledobrychzmian)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.iledobrychzmian = int(input('Ile? '))
        if inp == 'nie':
            print('ok')
        else:
            pass
    def showilelatpracuje(self):
        print(self.ilelatpracuje)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.ilelatpracuje = int(input('Ile? '))
        if inp == 'nie':
            print('ok')
        else:
            pass
    def showopinianauczycieli(self):
        print(self.opinianauczycieli)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.opinianauczycieli = str(input('Nowa opinia: '))
        if inp == 'nie':
            print('ok')
        else:
            pass
    def showczyuczy(self):
        print(self.czyuczy)
        inp = input('zmienic? ')
        if inp == 'Tak':
            inp2 = input('Uczy? ')
            if inp2 == 'tak':
                self.czyuczy = True
            if inp2 == 'nie':
                self.czyuczy = False
        if inp == 'nie':
            print('ok')
        else:
            pass