import os
import random

class Deck:

    def __init__(self):
        '''
        Menginisialisasi kelas Deck dengan atribut cards yang berisi list of tuple.
        Tuple tersebut berisi file path gambar kartu dan nilai dari setiap kartu.
        '''
        __cardNameModifier = ['c', 'd', 'h', 's']

        imgDir = os.path.join(os.path.dirname(__file__), 'img')

        self.cards = []

        for i in range(1, 14):
                for modifier in __cardNameModifier:
                    fileName = str(i) + modifier  + '.png'
                    self.cards.append((os.path.join(imgDir, fileName), i))

    def getCardsCount(self):
        return len(self.cards)

    def randomizeDeck(self):
        '''
        Mengacak list berisi path ke.
        '''
        random.shuffle(self.cards)

    def drawCards(self, x = 1):
        '''
        Returns
        '''
        return [self.cards.pop() for i in range(1, x+1)]
