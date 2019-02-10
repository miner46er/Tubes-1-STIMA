import kivy
import Deck
import algoritma_greedy as algo
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class SolverGridLayout(GridLayout):

    deck = Deck.Deck()
    showncards=[['',''],['',''],['',''],['','']]
    count=0
    deck_blank=['./img/back.png','./img/back.png','./img/back.png','./img/back.png','./img/back.png','./img/back.png','./img/back.png','./img/back.png','./img/back.png','./img/back.png','./img/back.png','./img/back.png','./img/back.png','./img/blank.png']

    def solve(self):
        return algo.solve24_greedy([str(card[1]) for card in self.showncards])
    def shuffle(self):
        self.deck.randomizeDeck()
    def draw(self):
        if self.count<13:
            self.showncards = self.deck.drawCards(4)
            self.count=self.count+1

class SolverApp(App):

    def build(self):
        return SolverGridLayout()

solveApp = SolverApp()
solveApp.run()
