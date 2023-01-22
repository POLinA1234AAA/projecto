import pygame.font
import pygame as pg
import sys


class Player():
    def __init__(self,name,symbol,n_games,n_wins,n_score):
        self.name = name
        self.symbol = symbol
        self.n_games = 0
        self.n_wins = 0
        self.n_score = 0  


    
    def change_stats(self, win_check):
        if sign == 'x':
            self.n_games+=1
            self.n_wins+=1
            self.n_score+=1
        if sign == 'y':
            self.n_games+=1
            self.n_wins+=1
            self.n_score+=1
        resu = print(f'{n_games},{n_wins},{n_score}')
        return(resu )
        
        
# class Stats():
#     def __init__(self):
#         self.reset_stats()
        

    # def reset_stats(self):
    #     # sta changing
    #     self.n_games = 0
    #     self.n_wins = 0
    #     self.score = 0  





# class Scores():
#     def __init__(self,sc,stats):
#         self.sc = sc
#         self.sc_rect = sc.get_rect()
#         self.stats = stats
#         self.text_color =(139,195,74)
#         self.font = pg.font.SysFont('Calibri', 45)
#         self.image_score()
#         self.image_n_games()
#         self.image_n_wins()

#     def image_score(self):
#         #  text of score
#         self.score_img= self.font.render(str(self.stats.score),True ,self.text_color<(0,0,0))
#         # self.score_rect = self.score_img.get_rect(topright(20,-40))
#         # self.score_rect= self.score_rect.right -40
#         self.score_img.get_rect(right = -40) 
#         self.score_img.get_rect(top = 20)
#         # self.score_rect = self.score_rect.top +20
    
#     def image_n_games(self):
#         self.n_games_img= self.font.render(str(self.stats.n_games),True ,self.text_color<(0,0,0))
#         # self.n_games_rect = self.n_games_img.get_rect()
#         # self.n_games_rect= self.score_rect.right -40
#         # self.n_games_rect = self.score_rect.top +20
#         # self.n_games_rect = self.n_games_img.get_rect(topright(20,-40))
#         self.n_games_img.get_rect(right = -40) 
#         self.n_games_img.get_rect(top = 20)
#     def image_n_wins(self):
#         self.n_wins_img= self.font.render(str(self.stats.n_wins),True ,self.text_color<(0,0,0))
#         # self.n_wins_rect = self.n_wins_img.get_rect(topright(20,-40))
#         # self.n_wins_rect= self.score_rect.right -40
#         # self.n_wins_rect =self.score_rect.top +20
#         self.n_wins_img.get_rect(right = -40) 
#         self.n_wins_img.get_rect(top = 20)
#     def image_high_score(self):
#         """преобразование рекорда в графическое изображение"""
#         self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
#         self.high_score_rect = self.high_score_image.get_rect()
#         self.high_score_rect.centerx = self.screen_rect.centerx
#         self.high_score_rect.top = self.screen_rect.top + 20



#     def show_score(self):
 
#         self.sc.blit(self.score_img,self.score_rect)
#         self.sc.blit(self.high_score_image, self.high_score_rect)
  

#     def show_n_games(self):
       
#         self.sc.blit(self.n_games_img,self.n_games_rect)
#         self.sc.blit(self.high_score_image, self.high_score_rect)
     
    
#     def show_n_wins(self):
        
#         self.sc.blit(self.n_wins_img,self.n_wins_rect)
#         self.sc.blit(self.high_score_image, self.high_score_rect)
    


