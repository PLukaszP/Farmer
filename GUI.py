import farmer
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label

class First(Screen):
    player1_field = ObjectProperty()
    player2_field = ObjectProperty()
    player3_field = ObjectProperty()
    player4_field= ObjectProperty()
    players = []
    def ustalGraczy(self):
        self.players = [self.player1_field.text, self.player2_field.text, self.player3_field.text, self.player4_field.text]
        players = [player for player in self.players if len(player)> 0]
        if len(players) > 1:
            self.ids.start_btn.disabled = False
            self.ids.label_list_of_players.text = f"Gracze: {players}"
            self.players= players
            self.players
            farmer.Game(players)
        else:
            self.ids.label_list_of_players.text = "dwa pola graczy muszą być uzupełnione"


class Second(Screen):

    trade = ('krowę na konia', 'owca_to_maly_pies', 'krowa_to_duzy_pies', 'swinia_to_krowa', 'owca_to_swinia', 'krolik_to_owca',
    'owca_to_krolik', 'swinia_to_owca', 'krowa_to_swinia', 'kon_to_krowa')

    def on_parent(self, *args):
        for el in self.trade:
            self.ids.grid_change.add_widget(Button(text=el, size_hint=(.2, .2)))
    def losuj(self):
        pass

class WinManager(ScreenManager):
    pass

kv = Builder.load_file('widoki.kv')

class GUIApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    GUIApp().run()