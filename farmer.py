import random
asciart = """
   _____                          __                                             __n__n__
  / ____|                        / _|                                     .------`-\\00/-'
 | (___  _   _ _ __   ___ _ __  | |_ __ _ _ __ _ __ ___   ___ _ __       /  ##  ## (oo)
  \___ \| | | | '_ \ / _ \ '__| |  _/ _` | '__| '_ ` _ \ / _ \ '__|     / \## __   ./
  ____) | |_| | |_) |  __/ |    | || (_| | |  | | | | | |  __/ |           |//YY \|/
 |_____/ \__,_| .__/ \___|_|    |_| \__,_|_|  |_| |_| |_|\___|_|           |||   |||
              | |
"""
class Hand:
    def __init__(self, name):
        self.name= name
        self.hand = {'kon': 0, 'krowa': 0, 'swinia': 0, 'owca': 0, 'krolik': 0, 'maly_pies': 0, 'duzy_pies': 0, 'lis': 0, 'wilk': 0}
    def __str__(self):
        return f"Koń = {self.hand['kon']}, Krowa = {self.hand['krowa']}, Świnia = {self.hand['swinia']}," \
               f"Owca = {self.hand['owca']}, Królik = {self.hand['krolik']}, Duży pies = {self.hand['duzy_pies']}, " \
               f"Mały pies = {self.hand['maly_pies']}, Lis = {self.hand['lis']}, Wilk= {self.hand['wilk']} "

    def dodajZwierze(self, rzut):
        self.dice1 = rzut[0]
        self.dice2 = rzut[1]
        if self.dice1 == self.dice2:
            ile_par = int(self.hand[self.dice1] / 2)
            self.hand[self.dice1] += (ile_par+1)
        else:
            self.hand[self.dice1] += 1
            self.hand[self.dice2] += 1

    def losuj(self):
        list1 = ("krolik", "krolik", "kon", "swinia", "owca", "krolik", "krolik", "krolik", "owca", "krolik", "swinia", "lis")
        list2 = ("owca", "krolik", "krowa", "owca", "krolik", "krolik", "krolik", "krolik", "owca", "swinia", 'krolik', "wilk")
        dice1 = random.choice(list1)
        dice2 = random.choice(list2)
        rzut= (dice1, dice2)
        return rzut

    def wilk(self):
        if self.hand['wilk']:
            if self.hand['duzy_pies']:
                self.hand['duzy_pies'] -= 1
                self.hand['wilk'] = 0
            else:
                self.hand['krowa'] = 0
                self.hand['swinia'] = 0
                self.hand['owca'] = 0
                self.hand['wilk'] = 0

    def lis(self):
        if self.hand['lis']:
            if self.hand['maly_pies']:
                self.hand['maly_pies'] -= 1
                self.hand['lis'] = 0
            else:
                self.hand['lis'] = 0
                if self.hand['krolik'] > 0:
                    self.hand['krolik'] -= (self.hand['krolik'] - 1)

    def changeTable(self):
        krowa_to_kon = {'warunek': self.hand['krowa'] >= 2, 'wymiana': ('krowa', 2, 'kon', 1), 'press': 1,
                        'komunikat': '2 krowy na 1 konia'}
        owca_to_maly_pies = {'warunek': self.hand['owca'] >= 1, 'wymiana': ('owca', 1, 'maly_pies', 1), 'press': 2,
                             'komunikat': '1 owcę na 1 małego psa'}
        krowa_to_duzy_pies = {'warunek': self.hand['krowa'] >= 1, 'wymiana': ('krowa', 2, 'duzy_pies', 1), 'press': 3,
                              'komunikat': '2 krowy na 1 dużego psa'}
        swinia_to_krowa = {'warunek': self.hand['swinia'] >= 3, 'wymiana': ('swinia', 3, 'krowa', 1),'press': 4,
                           'komunikat': '3 świnie na 1 krowę'}
        owca_to_swinia = {'warunek': self.hand['owca'] >= 2, 'wymiana': ('owca', 2, 'swinia', 1),'press': 5,
                          'komunikat': '2 owce na 1 świnię'}
        krolik_to_owca = {'warunek': self.hand['krolik'] >= 6, 'wymiana': ('krolik', 6, 'owca', 1),'press': 6,
                          'komunikat': '6 królików na 1 owcę'}
        owca_to_krolik = {'warunek': self.hand['owca'] >= 1, 'wymiana': ('owca', 1, 'krolik', 6), 'press': 7,
                          'komunikat': '1 owcę na 6 królików'}
        swinia_to_owca = {'warunek': self.hand['swinia'] >= 1, 'wymiana': ('swinia', 1, 'owca', 2), 'press': 8,
                          'komunikat': '1 świnię na 2 owce'}
        krowa_to_swinia = {'warunek': self.hand['krowa'] >= 1, 'wymiana': ('krowa', 1, 'swinia', 3), 'press': 9,
                           'komunikat': '1 krowę na 3 swinie'}
        kon_to_krowa = {'warunek': self.hand['kon'] >= 1, 'wymiana': ('kon', 1, 'krowa', 2), 'press': 10,
                        'komunikat': '1 konia na 2 krowy'}

        all_change_posibilities = (krowa_to_kon, owca_to_maly_pies, krowa_to_duzy_pies, swinia_to_krowa, owca_to_swinia, krolik_to_owca, owca_to_krolik,
                 swinia_to_owca, krowa_to_swinia, kon_to_krowa)
        current_change_options = [item for item in all_change_posibilities if item['warunek']]
        return current_change_options

    def change(self, current_change_options, choice):
        for item in current_change_options:
            if item['press'] == choice:
                co_zwierze = item['wymiana'][0]
                co_sztuk = item['wymiana'][1]
                na_zwierze = item['wymiana'][2]
                na_sztuk = item['wymiana'][3]
                self.hand[co_zwierze] -= co_sztuk
                self.hand[na_zwierze] += na_sztuk
                print(f"Wymieniłeś {item['komunikat']}")

class Game():
    def __init__(self, names):
        self.players =[]
        for name in names:
            player = Hand(name)
            self.players.append(player)

    def drawEffect(self, player):
        rzut = player.losuj()
        print(f'wylosowano {rzut}')
        player.dodajZwierze(rzut)
        player.lis()
        player.wilk()
        print(f'masz: {player}')

    def changeEffect(self, player):
        tabela =player.changeTable()
        choices= [str(el['press']) for el in tabela]
        choices.append(str(0))
        choice = ''
        while choice not in choices:
            for el in tabela:
                print(f"** Naciśnij {el['press']} aby {el['komunikat']}")
            print('** Naciśnij 0 jeśli nie chcesz jednak wymieniać zwierząt')
            choice = input('co wybierasz? -> ')
            if choice in choices:
                if choice =='0':
                    pass
                else:
                    player.change(tabela,int(choice))
            else:
                print('niewłaściwy wybór')

    def draw_or_change(self, player):
        losuj = True
        wymien = True
        tabela = player.changeTable()
        while losuj or wymien == True:
            choice = ''
            choices = ['a', 'z']
            if tabela:
                for el in tabela:
                    print('** możesz zamienić', el['komunikat'])
                print('Aby skorzystać z  wymiany naciśnij literę  z')
            else:
                wymien = False
            print('Aby losować naciśnij literę a')
            while choice not in choices:
                choice = input('wybierz opcję -> ')
                if choice not in choices:
                    print(f'niewłaściwy wybór')
                if (choice == 'a') and (losuj == True):
                    self.drawEffect(player)
                    losuj = False
                    wymien = False
                if choice == 'z' and (wymien == True):
                    self.changeEffect(player)
                    wymien = False

def main():
    print(asciart)
    zwyciezca = False
    gra= Game(['Gracz_1', 'Gracz_2'])
    while zwyciezca != True:
        for player in gra.players:
            print(f"Kolej gracza: {player.name}")
            print(f'masz {player}')
            gra.draw_or_change(player)
            print('----------')
            condition = (player.hand['kon'] > 0 and player.hand['krowa'] > 0 and player.hand['swinia'] > 0 and
                        player.hand['owca'] > 0 and player.hand['krolik'] > 0)
            if condition:
                zwyciezca =True
                break
    print(f'zwyciezyl {player.name}  {player}')


if __name__ == '__main__':
    main()
