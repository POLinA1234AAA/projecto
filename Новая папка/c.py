import pygame as pg 
import sys
# from rjl import Player
# def win_check(self, mas, symbol ,scs,stats,sc):
#     zeroes = 0
    
#     for row in mas:
#         zeroes += row.count(0)
#         if row.count(symbol) == 3:
#             stats.score+=10
#             n_wins+=1
#             n_games +=1
#             scs.image_score()
#             scs.image_n_games()
#             scs.image_n_wins()
#             check_high_score(stats,scs)
            
            

#             return symbol
    
#     for col in range(3):
#         if mas[0][col] == symbol and mas[1][col] == symbol and mas[2][col] == symbol:
#             stats.score+=10
#             n_wins+=1
#             n_games +=1
#             scs.image_score()
#             scs.image_n_games()
#             scs.image_n_wins()
#             check_high_score(stats,scs)
#             return sing
            
#     if mas[0][0] == symbol and mas[1][1] == symbol and mas[2][2] == symbol:
#         stats.score+=10
#         n_wins+=1
#         n_games +=1
#         scs.image_score()
#         scs.image_n_games()
#         scs.image_n_wins()
#         check_high_score(stats,scs)
#         return symbol
#     if mas[0][2] == symbol and mas[1][1] == symbol and mas[2][0] == symbol:
#         stats.score+=10
#         n_wins+=1
#         n_games +=1
#         scs.image_score()
#         scs.image_n_games()
#         scs.image_n_wins()
#         check_high_score(stats,scs)
#         return symbol
#     if zeroes == 0:
#         n_wins+=1
#         scs.image_n_wins()
#         check_high_score(stats,scs)
#         return 'draw'
    

def win_check(mas, sing):
    zeroes = 0
 

    for row in mas:
        zeroes += row.count(0)
        if row.count(sing) == 3:
    
            return sing
         
    for col in range(3):
        if mas[0][col] == sing and mas[1][col] == sing and mas[2][col] == sing:
          
            return  sing
            
        if mas[0][0] == sing and mas[1][1] == sing and mas[2][2] == sing:
        
            # return sing
            return  sing
        if mas[0][2] == sing and mas[1][1] == sing and mas[2][0] == sing:
        
            # return sing
            return sing
        if zeroes == 0:
            n_games+=1
            return sing
        return False

pg.init()
sizeblock = 100
margine = 15

WIDTH = HEIGTH = sizeblock * 3 + margine * 4 
RES = WIDTH, HEIGTH

sc = pg.display.set_mode(RES)
pg.display.set_caption('Крестики нолики!')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ROZOVI = (189, 30, 128)
FIOLETOVI = (125, 81, 196)
NASROZOVI = (255,20,147)
ORHID = (138,43,226)

mas = [[0] * 3 for i in range(3)]
query = 0
game_over = False 


while True:
    # sc.fill(BLACK)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            # quit()
            sys.exit(0)
        elif event.type == pg.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pg.mouse.get_pos()
            col = x_mouse // (sizeblock + margine)
            row = y_mouse // (sizeblock + margine)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else: 
                    mas[row][col] = 'o'
                query += 1
        elif event.type == pg.KEYDOWN and event.key==pg.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            sc.fill(BLACK)

    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = FIOLETOVI
                elif mas[row][col] == 'o':
                    color = ROZOVI
                else:
                    color = WHITE
                x = col * sizeblock + (col + 1) * margine
                y = row * sizeblock + (row + 1) * margine
                pg.draw.rect(sc, color, (x, y, sizeblock, sizeblock))
                if color == FIOLETOVI:
                    pg.draw.line(sc, NASROZOVI, (x + 10, y + 10), (x + sizeblock - 10, y + sizeblock - 10), 5)
                    pg.draw.line(sc, NASROZOVI, (x + sizeblock - 10, y + 10), (x + 10, y + sizeblock - 10), 5)
                elif color == ROZOVI:
                    pg.draw.circle(sc, ORHID, (x + sizeblock // 2, y + sizeblock // 2), sizeblock // 2 - 5, 5)
        for event in pg.event.get():   

            # if (query - 1) % 2 == 0:
            #     game_over = win_check(mas, 'x',scs,stats,sc)
            # else:
            #     game_over = win_check(mas, 'o',scs,stats,sc)
            if (query - 1) % 2 == 0:
                game_over = win_check(mas, 'x')
            else:
                game_over = win_check(mas, 'o')


        if game_over:
            sc.fill(BLACK)
            font = pg.font.SysFont('Calibri', 45)
            text1 = font.render(game_over, True, WHITE, 5)
            text_rect = text1.get_rect()
            text_x = sc.get_width() / 2 - text_rect.width / 2
            text_y = sc.get_height() / 2 - text_rect.height / 2
            sc.blit(text1, [text_x, text_y])
            # up = update(sc,stats,scs)

    pg.display.update()
   
    # clock.tick(FPS)
# import pygame as pg 
# pg.init()

# def win_check(mas, sing):
#     zeroes = 0
#     for row in mas:
#         zeroes += row.count(0)
#         if row.count(sing) == 4:
#             return sing
#             print(1)
#     for col in range(4):
#         if mas[0][col] == sing and mas[1][col] == sing and mas[2][col] == sing and mas[3][col] == sing:
#             return sing
#     if mas[0][0] == sing and mas[1][1] == sing and mas[2][2] == sing and mas[3][3] == sing:
#         return sing
#     if mas[0][3] == sing and mas[1][2] == sing and mas[2][1] == sing and mas[3][0] == sing:
#         return sing
#     if zeroes == 0:
#         return 'No win, No defeat'
#     return False


# sizeblock = 100
# margine = 15

# WIDTH = HEIGTH = sizeblock * 4 + margine * (5)
# RES = WIDTH, HEIGTH

# sc = pg.display.set_mode(RES)
# pg.display.set_caption('Крестики нолики!')

# clock = pg.time.Clock()

# FPS = 30

# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# ROZOVI = (189, 30, 128)
# FIOLETOVI = (125, 81, 196)
# NASROZOVI = (255,20,147)
# ORHID = (138,43,226)

# mas = [[0] * 4 for i in range(4)]
# query = 0

# while True:
#     sc.fill(BLACK)
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             quit()
#         elif event.type == pg.MOUSEBUTTONDOWN:
#             x_mouse, y_mouse = pg.mouse.get_pos()
#             col = x_mouse // (sizeblock + margine)
#             row = y_mouse // (sizeblock + margine)
#             if mas[col][row] == 0:
#                 if query % 2 == 0:
#                     mas[col][row] = 'x'
#                 else: 
#                     mas[col][row] = 'o'
#                 query += 1

#     for row in range(4):
#         for col in range(4):
#             if mas[col][row] == 'x':
#                 color = FIOLETOVI
#             elif mas[col][row] == 'o':
#                 color = ROZOVI
#             else:
#                 color = WHITE
#             x = col * sizeblock + (col + 1) * margine
#             y = row * sizeblock + (row + 1) * margine
#             pg.draw.rect(sc, color, (x, y, sizeblock, sizeblock))
#             if color == FIOLETOVI:
#                 pg.draw.line(sc, NASROZOVI, (x + 10, y + 10), (x + sizeblock - 10, y + sizeblock - 10), 5)
#                 pg.draw.line(sc, NASROZOVI, (x + sizeblock - 10, y + 10), (x + 10, y + sizeblock - 10), 5)
#             elif color == ROZOVI:
#                 pg.draw.circle(sc, ORHID, (x + sizeblock // 2, y + sizeblock // 2), sizeblock // 2 - 5, 5)
#         for event in pg.event.get():   
#             if (query - 1) % 2 == 0:
#                 game_over = win_check(mas, 'x')
#             else:
#                 game_over = win_check(mas, 'o')

#         if game_over:
#             sc.fill(BLACK)
#             font = pg.font.SysFont('Calibri', 45)
#             text1 = font.render(game_over, True, WHITE, 5)
#             text_rect = text1.get_rect()
#             text_x = sc.get_width() / 2 - text_rect.width / 2
#             text_y = sc.get_height() / 2 - text_rect.height / 2
#             sc.blit(text1, [text_x, text_y])

#     pg.display.update()
#     clock.tick(FPS)