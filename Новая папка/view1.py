from controler import*
from model1 import Player, Game , Field , Checker 
def main():
    players = []
    # game=Game()
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
            l =(input ('enter the name of player: ' ))
            symbol= (input ('enter the symbol of player: ' ))
            player_ = Player(l,symbol)
            players.append(player_)
            for p in players:
                print(f'{p.name} you are successfuly registered')
                
        elif comd[0] == 'RP':
            print (players)
            n = input ('enter the name of player you want to remove: ' )
            res= remove_player(players,n)
            if res == True:
                print (f'{n} you are sucsesfuly removed')
                print(players)
            else:
                print ('you might enter the wrong name ')
        elif comd[0] == 'LP':
            
            if len(players) > 0:
                print(('player name :  '+ player_.name + '   amount of games:   ' + str( player_.n_games )+ '   amount of games won:    ' + str (player_.n_wins)))
            else:
                print ('no registered players')
            break
        elif comd[0] == 'SP':
           
                
            lenght = int(input('enter  lenght  of the playing board:  '))
            # high = int(input('enter  high  of the playing board:  '))
            # lenghts = int(input('enter  wighd  of the special block:  '))
            # highs =int(input('enter  high  of the  special block:  '))
            print(players)
                
            # player1name=input('enter the name of player  who"s  is going to play first :  ')
            # player1 = player_name (players, player1name)
            # player2name =input('enter the name of player  who"s  is going to play second :  ')
            # player2 = player_name (players, player1name)
            field = Field(high,lenght)
            

            print(' size of board : ' + str (field.size))
            game = Game( board,player1,player2 )
            greet = game.greet_user(currplayer)
        
            # play_= game.play()
            # board_ = game.board()
                
             
            cheakempry = field.is_cell_empty( x, y)
            setsels = field.set_cell( x, y, value)
           
                
                

        # elif comd[0]== 'GD':
        #     if len(players) > 0:
        #         print ('information about the cur player :''player name :  '+ player_.name + '   amount of games:   ' + str( player_.n_games )+ '   amount of games won:    ' + str (player_.n_wins))
        # elif comd[0] == 'GU':   
        #     for p in players :
        #         print ('information about the cur player :''player name :  '+ player_.name + '   amount of games:   ' + str( player_.n_games )+ '   amount of games won:    ' + str (player_.n_wins))
        #         gameover = Field.game_over( player_symbol)
        #         print(f'{p.name} gived up')

        #         break

        # elif comd[0] == 'PP':
        #     for p in players :
               
        # elif comd[0] == 'VR':
        #     for  p in players :
        #         if len(players) > 0:
        #             print (f'{p.name} player result is '+ str( player_.n_wins))
        #     break

        # elif comd [0]== 'Re':

        # elif comd [0]== 'Ra':
        elif comd[0] == '0':
            break


class PlayingField(object):
    EMPTY_CELL = ' '
    
    def __init__(self, high,lenght,):
        self.size = high *lenght
        
        self.count = self.size * self.size
       
        self.cells = []
      

        # for i in range(self.size):


        def field (self):
           
        result = " " * 5
        for i in range(self.size):
            result += f"{i:^4}"
            line = "\n" + " " * 4 + "-" * (self.size * 4 + 1)
            result += line
            for i in range(self.size):
                row = f"{i:^4}" + "|"
                for j in range(self.size):
                    row += f"{self.cells[i][j]:^4}" + "|"
                result += "\n" + row + line
            return result


    def show_field(self):
        for row in self.field():
            for player in row:
                print('_' if player is None else player.symbol,end=' ')
            print()

    def set_player(self, x, y, player):
        if self.field[y][x] is not None:
            return False

        self.field[y][x]= player

        return True
    def full_board(self):
        for row in self.field: 
            for col in row: # <-- now we're iterating through each list in self.field
                if col is None:
                    return False   # the board is not full if there's at least one empty space
        return True  # looking at every element and they were all occupied
    
   
        #     self.cells.append([PLayingField.EMPTY_CELL] * self.size)