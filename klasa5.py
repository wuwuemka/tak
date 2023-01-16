from klasa2 import Uczen
class Nerd(Uczen):
    def __init__(self,ktogolubi,ile6,ilerazyzdenerwowalklase,ilesieuczy):
        self.ktogolubi = ktogolubi
        self.ile6 = ile6
        self.ilerazyzdenerwowalklase = ilerazyzdenerwowalklase
        self.ilesieuczy = ilesieuczy

    def showktogolubi(self):
        print(self.ktogolubi)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.ktogolubi = str(input('Kto niby lol? '))
        if inp == 'nie':
            print('ok')
        else:
            pass
    def showile6(self):
        print(self.ile6)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.ile6 = int(input('Ile? '))
        if inp == 'nie':
            print('ok')
        else:
            pass
    def showilerazyzdenerwowalklase(self):
        print(self.ilerazyzdenerwowalklase)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.ilerazyzdenerwowalklase = int(input('Ile razy? '))
        if inp == 'nie':
            print('ok')
        else:
            pass
    def showilesieuczy(self):
        print(self.ilesieuczy)
        inp = input('zmienic? ')
        if inp == 'Tak':
            inp2 = input('Ile? ')
            if inp2 == 'tak':
                self.ilesieuczy = True
            if inp2 == 'nie':
                self.ilesieuczy = False
        if inp == 'nie':
            print('ok')
        else:
            pass