class Uzytkownik:
    def __init__(self,id,haslo,ip,pracownik_szkoly):
        self.id = id
        self.haslo = haslo
        self.ip = ip
        self.pracownik_szkoly = pracownik_szkoly
    
    def showid(self):
        print(self.id)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.id = int(input('Nowe id: '))
        if inp == 'nie':
            print('ok')
        else:
            pass
    def showhaslo(self):
        print(self.haslo)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.haslo = int(input('Nowe haslo: '))
        if inp == 'nie':
            print('ok')
        else:
            pass
    def showip(self):
        print(self.ip)
        inp = input('zmienic? ')
        if inp == 'Tak':
            self.ip = int(input('Nowe ip: '))
        if inp == 'nie':
            print('ok')
        else:
            pass
    def showpracownik(self):
        print(self.pracownik_szkoly)
        inp = input('zmienic? ')
        if inp == 'Tak':
            inp2 = input('pracownik czy nie')
            if inp2 == 'tak':
                self.pracownik_szkoly = True
            if inp2 == 'nie':
                self.pracownik_szkoly = False
        if inp == 'nie':
            print('ok')
        else:
            pass