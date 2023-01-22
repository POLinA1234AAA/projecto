from rjl import Player
from controler import*
import sys
import pygame as pg 
import c.py



def main():
    
    while True :
        print("""1. register the new player (RG)
                 2. remove player(RP)
                 3. list players(LP)
                 4. start play(SP)
                 5. jame data(GD)
                 6. give up(GU)
                 7. place part(PP)
                 8. view result(VR)
                 9. to record (Re)
                 10. to read(Ra)
                 """)
        comd = input('enter the comand : ').split()
       
        
        if comd[0] == 'RG':
            name_1= input('Name of Player 1: ')
            name_2= input('Name of Player 2: ')
            symbol_1= (input ('enter the symbol of player: ' ))
            symbol_2= (input ('enter the symbol of player: ' ))
           
            name_1 = Player(name_1,symbol_1)
            name_2 = Player(name_2,symbol_2)

            players= []
            players.append(name_1)
            players.append(name_2)
            for p in players:
                print(f'{p.name} you are successfuly registered')

        elif comd[0] == 'RP':
            print (players)
            n = input ('enter the name of player you want to remove: ' )
            res = remove_player(players,n)
            if res == True:
                print (f'{n} you are sucsesfuly removed')
                print(players)
            else:
                print ('you might enter the wrong name ')
        elif comd[0] == 'LP':
            player = Player(name_1,name_2)
            if len(players) > 0:
                for element in players:
                    print(('player name :  '+ player.name + ' player score :'+ str(player.score )+  '  amount of games:   ' + str( player.n_games )+ '   amount of games won:    ' + str (player.n_wins)))
            else:
                print ('no registered players')
                break
        
        elif comd[0] == 'SP': 
            exec(c.py)
            resul = change_stats(self, win_check)
            
            stats = Stats()
            scs=Scores(sc,stats)
            
            
        elif comd[0] == '0':
            break
