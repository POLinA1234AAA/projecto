# from model1 import*
import pygame.font
import pygame as pg
import sys

def remove_player(players,n):
    print(players)

    for element in players:
        print(element.name ) 
        print (n)
        if element.name == n :
            players.remove(element)
            return True
    return False

def update(sc,stats,scs):
    scs.show_score()
    scs.show_n_wins()
    scs.show_n_games()
