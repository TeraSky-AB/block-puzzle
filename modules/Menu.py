import pygame as pg

pg.init()
x=450       
y=480
fenetre = pg.display.set_mode((x, y))


def menu():
    imageM = pg.image.load('fond.jpg').convert() 
    fenetre.blit(imageM,(0,0))                               
    pg.display.update                                   
    boutonjouer = pg.rect.Rect((165,216,135,43))        
    boutonquitter = pg.rect.Rect((165,284,135,45))
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
                    #main()
                    print("nous pouvons jouer")
                elif boutonquitter.collidepoint(mousePos):
                    print("normalement on avons quitter le jeu")
                    run = False
                    pg.display.quit()
        pg.display.flip()                              

menu()
