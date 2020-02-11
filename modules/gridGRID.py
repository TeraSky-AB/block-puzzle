import pygame as pg
from pygame import Vector2, Rect
from pygame.locals import *     #pygame.locals has the constants like QUIT, MOUSEBUTTON, and K_ESCAPE
import sys, os, random, time

class Settings:
    background_color = (150, 211, 255)
    board_color = (102, 174, 232)
    block_color = ((255, 255, 255), (240, 247, 244), (255, 143, 137), (34,199,139))
    box_size = 30
    box_size_small = 25
    margin = 2
    board_size = 10
    
class AllPieces:
    def __init__(self):
        self.pieces = (
            ('00000','00000','00100','00000','00000'), # 0  : Unity block
            ('00000','00000','00110','00000','00000'), # 1  : 2 line
            ('00000','00000','01110','00000','00000'), # 2  : 3 line
            ('00000','00000','01100','00100','00000'), # 3  : Comma
            ('00000','00000','01100','01100','00000'), # 4  : 2x2 block
            ('00000','00000','11110','00000','00000'), # 5  : 4 line
            ('00000','00000','11111','00000','00000'), # 6  : 5 line
            ('00000','01110','01110','01110','00000'), # 7  : 3x3 block
            ('00000','00000','11100','00100','00100'), # 8  : Big comma
            ('00000','00000','01100','00100','00100'), # 9  : Logical not figure
            ('00000','00000','01100','00110','00000'), # 10 : Snake look alike
            ('00000','00000','01110','00100','00000')  # 11 : T figure
        )

    def choice_pieces(self):
        return [self.pieces[1], self.pieces[3], self.pieces[5]]
        # return [random.choice(self.pieces), random.choice(self.pieces), random.choice(self.pieces)]


class Pieces:
    def __init__(self, piece, position):
        self.piece = piece
        self.position = Vector2(position)

    def draw(self, screen):
        self.rect_list = []
        for row in range(5):
            for column in range(5):
                if self.piece[row][column] == '1':
                    self.pos = Vector2(self.position)
                    self.pos.x += column * (Settings.box_size + Settings.margin)
                    self.pos.y += row * (Settings.box_size + Settings.margin)
                    self.rect_list.append(pg.Rect(self.pos, Vector2(Settings.box_size, Settings.box_size)))
        
        for rect in self.rect_list:
            pg.draw.rect(screen, Settings.block_color[3], rect)

    def move(self):
        return self.rect_list

    def moving(self, pos: Vector2):
        row = (pos.y - self.position.y) // (Settings.box_size + Settings.margin)
        column = (pos.x - self.position.x) // (Settings.box_size + Settings.margin)
        if row < 0 or row > self.pos.x:
            return False
        if column < 0 or column > self.pos.y:
            return False
        return None

    def get_position(self):
        return self.position

    def set_position(self, pos: Vector2):
        self.position = pos


class Board:
    def __init__(self):
        self.board = []
        self.pts = 0
    
    def board(self):
        for row in range(19):
            for column in range(19):
                self.board.append(0)

    def click_range(self, x, y):
        if x < 140 or x > 460 or y < 90 or y > 410:
            print("Click is out of range")
            return False
        else:
            return True

    def place_piece(self, x, y, piece):
        for i in range(5):
            for j in range(5):
                self.board[x][y] += int(piece[i][j])

    def draw(self, screen):
        for row in range(Settings.board_size):
            for column in range(Settings.board_size):
                color = Settings.board_color
                pos = Vector2(140,90)     #top left position
                pos.x += column * (Settings.box_size + Settings.margin)
                pos.y += row * (Settings.box_size + Settings.margin)
                pg.draw.rect(screen, color, Rect(pos, Vector2(Settings.box_size, Settings.box_size)))

    def get_rect(self):
        return self.rect

    def get_board(self):
        return self.board

pg.init()

class Game:
    def __init__(self):
        self.fps = 60
        self.clock = pg.time.Clock()
        self.title = "Block Puzzle !"
        self.screen_size = 600, 600
        self.screen = pg.display.set_mode(self.screen_size)
        self.all_pieces = AllPieces()
        self.board = Board()
        self.pieces = None
        self.create_pieces()
        self.selected_piece = None # drag 
        self.mouse_offset = Vector2(0, 0) 
    
    def image(self, screen):
        pass

    def points(self):
        pts = 0
        police = pg.font.SysFont('arial', 35, bold=True)
        texte = police.render('SCORE : '+ str(pts), False, (37, 80, 109))
        self.screen.blit(texte, (20, 20))
            
    def create_pieces(self):
        random_pieces = self.all_pieces.choice_pieces()
        x = 50
        y = 405
        self.pieces = []
        for piece in random_pieces:
            self.pieces.append(Pieces(piece, Vector2(x, y)))
            x += 175


    def draw(self):
        self.screen.fill(Settings.background_color)
        self.board.draw(self.screen)
        for piece in self.pieces:
            piece.draw(self.screen)
        pg.display.set_caption(self.title)
        self.points()
        pg.display.flip()

   
    def menu(self):
        self.image = pg.image.load('fond1.jpg').convert()
        self.screen.blit(self.image, (0, 0))
        self.bouton_jouer = pg.rect.Rect((230,357,140,45))
        self.bouton_quitter = pg.rect.Rect((230,424,140,45))
        self.possour = None
        running = True
        while running:
            self.screen.blit(self.image, (0,0))
            for event in pg.event.get():
                if event.type == QUIT:
                    running = False
                    pg.display.quit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
                if event.type == MOUSEBUTTONDOWN:
                    self.possour = event.pos
                    if self.bouton_jouer.collidepoint(self.possour):
                        self.main()
                    elif self.bouton_quitter.collidepoint(self.possour):
                        running = False
                        pg.display.quit()
            pg.display.flip()

    def main(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

                # if event.type == MOUSEBUTTONDOWN:
                #     for piece in self.pieces:
                #         if piece.moving(Vector2(event.pos)):
                #             self.selected_piece = piece
                #             self.mouse_offset = event.pos - piece.get_position()
                #             print(self.mouse_offset)

                # if event.type == MOUSEMOTION and self.selected_piece is not None:
                #     self.selected_piece.set_position(event.pos - self.mouse_offset)
                #     print(event.pos, self.mouse_offset)

                if event.type == MOUSEBUTTONDOWN:
                    for piece in self.pieces:
                        moving = piece.move()
                        for move in moving:
                            if move.collidepoint(event.pos):
                                mouse_x, mouse_y = event.pos
                                my_x, my_y = move.topleft
                                self.selected_piece = mouse_x - my_x, mouse_y - my_y

                if event.type == MOUSEBUTTONUP:
                    mouse_x, mouse_y = event.pos
                    for piece in self.pieces:
                        moving = piece.move()
                        for move in moving:
                            if move.collidepoint(event.pos):
                                column = mouse_x // (Settings.box_size + Settings.margin)
                                row = mouse_y // (Settings.box_size + Settings.margin)
                                if self.board.click_range(mouse_x, mouse_y):
                                    self.board.place_piece(row, column, piece)
                            self.selected_piece = None
                    
            if self.selected_piece:
                for piece in self.pieces:
                    moving = piece.move()
                    for move in moving:
                        mouse_x, mouse_y = pg.mouse.get_pos()
                        off_x, off_y = self.selected_piece
                        move.topleft = mouse_x - off_x, mouse_y - off_y
                        print(mouse_x, mouse_y, off_x, off_y)
                    
                # if event.type == MOUSEBUTTONUP:
                #     if self.selected_piece is not None:
                #         pass

                # if event.type == MOUSEMOTION and self.selected_piece is not None:
                #     self.selected_piece.set_position(event.pos - self.mouse_offset)

            self.create_pieces()
            self.draw()
        self.clock.tick(self.fps)

if __name__ == '__main__':
    Game().menu()

