import pygame as pg

pg.init()
x=640         
y=640
fenetre = pg.display.set_mode((x, y))

BACKGROUNDCOLOR = (150, 211, 255)
BOARDCOLOR = (102, 174, 232)
CREAM = (240, 247, 244)
REDPINK = (255, 143, 137)
GREEN = (34,199,139)

def menu():
    imageM = pg.image.load(' image ').convert() 
    fenetre.blit(imageM,(0,0))                               
    pg.display.update                                   
    boutonjouer = pg.rect.Rect((259,286,125,36))        
    boutonquitter = pg.rect.Rect((261,338,123,41))
    run = True                                              
    while run:                                              
        fenetre.blit(imageM,(0,0))                         
        for event in pg.event.get():                    
            
            if event.type == pg.QUIT:                   
                run = False                          
                pg.display.quit()                       
            if event.type == pg.MOUSEBUTTONDOWN:        
                mousePos = event.pos
                if boutonjouer.collidepoint(mousePos):     
                    print("finir image")
                elif boutonquitter.collidepoint(mousePos):  
                    run = False
                    pg.display.quit()
        pg.display.flip()                              

menu()
