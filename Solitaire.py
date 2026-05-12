import random
import pygame
import sys
import random
import time
from pygame.locals import *

pygame.init()

FPS = pygame.time.Clock()
FPS.tick(60)

Screen_Width = 1200
Screen_Height = (9/16)*Screen_Width

background = pygame.image.load("green.png")
background = pygame.transform.scale_by(background, 2)

DISPLAYSURF = pygame.display.set_mode((Screen_Width, Screen_Height))
DISPLAYSURF.fill((255, 255, 255))
pygame.display.set_caption("Solitaire")

Cards = ["AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"]
Red_Cards = ["AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
Black_Cards = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"]

Face_Down = []
Face_Up = []

Right_Draw_Pile = []
for i in range(24):
    card = random.choice(Cards)
    Face_Down.append(card)
    Cards.remove(card)
    Right_Draw_Pile.append(card)

Left_Draw_Pile = []

Col_1 = []
for i in range(1):
    card = random.choice(Cards)
    Face_Up.append(card)
    Cards.remove(card)
    Col_1.append(card)

Col_2 = []
for i in range(1):
    card = random.choice(Cards)
    Face_Down.append(card)
    Cards.remove(card)
    Col_2.append(card)
for i in range(1):
    card = random.choice(Cards)
    Face_Up.append(card)
    Cards.remove(card)
    Col_2.append(card)

Col_3 = []
for i in range(2):
    card = random.choice(Cards)
    Face_Down.append(card)
    Cards.remove(card)
    Col_3.append(card)
for i in range(1):
    card = random.choice(Cards)
    Face_Up.append(card)
    Cards.remove(card)
    Col_3.append(card)

Col_4 = []
for i in range(3):
    card = random.choice(Cards)
    Face_Down.append(card)
    Cards.remove(card)
    Col_4.append(card)
for i in range(1):
    card = random.choice(Cards)
    Face_Up.append(card)
    Cards.remove(card)
    Col_4.append(card)

Col_5 = []
for i in range(4):
    card = random.choice(Cards)
    Face_Down.append(card)
    Cards.remove(card)
    Col_5.append(card)
for i in range(1):
    card = random.choice(Cards)
    Face_Up.append(card)
    Cards.remove(card)
    Col_5.append(card)

Col_6 = []
for i in range(5):
    card = random.choice(Cards)
    Face_Down.append(card)
    Cards.remove(card)
    Col_6.append(card)
for i in range(1):
    card = random.choice(Cards)
    Face_Up.append(card)
    Cards.remove(card)
    Col_6.append(card)

Col_7 = []
for i in range(6):
    card = random.choice(Cards)
    Face_Down.append(card)
    Cards.remove(card)
    Col_7.append(card)
for i in range(1):
    card = random.choice(Cards)
    Face_Up.append(card)
    Cards.remove(card)
    Col_7.append(card)

Final_1 = []
Final_2 = []
Final_3 = []
Final_4 = []

def card_red(card):
    if card in Red_Cards:
        return True
    elif card in Black_Cards:
        return False

Card_Size = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}

def flip_card(card):
    if card in Face_Down:
        Face_Up.append(card)
        Face_Down.remove(card)
    elif card in Face_Up:
        Face_Down.append(card)
        Face_Up.remove(card)

def top_card(column):
    if len(column) == 0:
        return "empty"
    else:
        top_card = column[-1]
        return top_card
    
def draw_card():
    if len(Right_Draw_Pile) == 0:
        for i in range(len(Left_Draw_Pile)):
            Shuffling_Card = Left_Draw_Pile[-1]
            Right_Draw_Pile.append(Shuffling_Card)
            Left_Draw_Pile.remove(Shuffling_Card)
            flip_card(Shuffling_Card)
    else:
        New_Card = Right_Draw_Pile[-1]
        Left_Draw_Pile.append(New_Card)
        Right_Draw_Pile.remove(New_Card)
        flip_card(New_Card)

def which_col(card):
    if card in Right_Draw_Pile:
        return Right_Draw_Pile
    elif card in Left_Draw_Pile:
        return Left_Draw_Pile
    elif card in Final_1:
        return Final_1
    elif card in Final_2:
        return Final_2
    elif card in Final_3:
        return Final_3
    elif card in Final_4:
        return Final_4
    elif card in Col_1:
        return Col_1
    elif card in Col_2:
        return Col_2
    elif card in Col_3:
        return Col_3
    elif card in Col_4:
        return Col_4
    elif card in Col_5:
        return Col_5
    elif card in Col_6:
        return Col_6
    elif card in Col_7:
        return Col_7

def can_stack(Still_Col, Moving_Card, Moving_Col):
    Still_Card = top_card(Still_Col)
    if Moving_Card in Face_Down:
        return False
    elif Still_Card in Face_Down:
        return False
    elif Moving_Card == "empty":
        return False
    elif Still_Col == Moving_Col:
        return False
    elif Still_Col == Left_Draw_Pile or Still_Col == Right_Draw_Pile:
        return False
    elif "F" in str(Still_Col) and "F" in str(Moving_Col):
        return False
    elif "F" in str(Moving_Col):
        if Moving_Col[-1] != Moving_Card:
            return False
    elif "D" in str(Moving_Col):
        if Moving_Col[-1] != Moving_Card:
            return False
    elif "C" in str(Still_Col):
        if Still_Card == "empty":
            if Moving_Card[0: -1] == "K":
                return True
            else:
                return False
        elif Card_Size[Moving_Card[0: -1]] + 1 != Card_Size[Still_Card[0: -1]]:
            return False
        else:
            if card_red(Still_Card) and card_red(Moving_Card):
                return False
            if not card_red(Still_Card) and not card_red(Moving_Card):
                return False
            else:
                return True
    elif "F" in str(Still_Col):
        if Moving_Col[-1] != Moving_Card:
            return False
        elif Still_Card == "empty":
            if Moving_Card[0: -1] == "A":
                return True
            else:
                return False
        elif Card_Size[Still_Card[0: -1]] + 1 != Card_Size[Moving_Card[0: -1]]:
            return False
        elif Still_Card[-1] != Moving_Card[-1]:
            return False
        else:
            return True

def play(Still_Col, Moving_Card, Moving_Col):
    Moving_Card_Index = Moving_Col.index(Moving_Card)
    for i in range((len(Moving_Col) - Moving_Card_Index)):
        Still_Col.append(Moving_Col[Moving_Card_Index])
        Moving_Col.remove(Moving_Col[Moving_Card_Index])
    if top_card(Moving_Col) in Face_Down:
        flip_card(top_card(Moving_Col))

class Card(pygame.sprite.Sprite):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        filename = f"cards/{rank}{suit}.png"
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale_by(self.image, 1)
        self.rect = self.image.get_rect()

AceH = Card("H", "A")
cards = pygame.sprite.Group()
cards.add(AceH)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.blit(background, (0,0))
    for entity in cards:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    pygame.display.update()
    FPS.tick(60)    



# terminate if game not possible