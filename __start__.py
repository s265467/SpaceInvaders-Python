#!/bin/usr/env python

#caricamento librerie, classi 
import pygame
from spaceinv.enemy_manager import EnemyManager
from spaceinv.ship import Ship
from spaceinv.bullet import BulletManager
from spaceinv.explosion import ExplosionManager
from spaceinv.bullet_enemy import BulletEnManager
from gamelib.sprite import Sprite
from pygame.locals import *
from sys import exit
import random

#inizializzazione libreria di gioco
pygame.init()

#definizioni delle variabili di grafica per l'accelerazione hardware
screen = pygame.display.set_mode((950,700), DOUBLEBUF | HWSURFACE)
pygame.display.set_caption("Space Invaders - My first game")
surf = pygame.display.get_surface()

#definizioni degli oggetti globali caricati dalle classi importate
ship  = Ship(surf)
enemy = EnemyManager(surf)
exp   = ExplosionManager(surf)
bm    = BulletManager(surf, enemy, exp)
bem   = BulletEnManager(surf)

#inizializzazione player
ship.init(bm)   

#genera la griglia dei nemici    
def enemy_grid(en):
    row = 0
    e_type = ["b" , "c" , "a" ]
    while row < 3:
        col = 0
        while col < 6:
            en.add(col * 80, row *80, e_type[row])
            col += 1
        row += 1

#variabile di appoggio per movimento ship()
dx = 0

#Inizializzazioni di opzioni di render
clock = pygame.time.Clock() # per il render

#Per sparo dei nemici
count = 0
time  = 150
defeat = ""
victory = ""

#Randomizzatore dei nemici
def shoot_player(en):
    global victory
    count = 0
    list_e = en._enemies
    
    #verifica se ci sono ancora nemici in campo
    if not list_e:  
       victory = " Victory, You Won! | ...premi un tasto..."
       
    #conta i nemici nella lista dei nemici
    for en in list_e:
        count += 1
        
    #inizializza il random
    random.seed()
    if list_e:
      #genera le coordinate dei proiettili 
      r = random.randint(0, count - 1) #seleziona il nemico dalla lista
      x = list_e[r].x
      y = list_e[r].y
    
      #carica il proiettile nel gioco
      bem.add(x,y,5)

#Gestore Eventi
def get_event(events):
    global dx #carica variabili esterni alla funzione
    
    for event in events:
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == 275: #destra
                dx = 5
            elif event.key == 276: #sinistra
                dx = -5
            elif event.key == 32: #spazio
                ship.fire()
        elif event.type == KEYUP:
            if event.key in (275 , 276):
                dx = 0

#caricamento griglia dei nemici di spaceinvaders
enemy_grid(enemy)
Gioco = True
#Per layout testo
font = pygame.font.Font(None, 30)

#Gioco in funzione 
while Gioco:

   #Gestisce gli eventi da tastiera, e mouse/joystick    
    get_event(pygame.event.get())

    ship.x += dx
    
    #Ritmo di sparo dei nemici
    if (count % time == 0):
        shoot_player(enemy)
        
    #Controlla l'impatto dei proiettili dei nemici con navicella
    ship.check_collision(bem)
    
    #Aggiorna i dati, posizioni dei vari oggetti   
    ship.update()
    enemy.update()
    exp.update()
    bm.update()
    bem.update()    
    
    #Colora lo sfondo di nero
    surf.fill((0,0,0))
    
    #Renderizza i dati precedentemente aggiornati
    enemy.render()
    exp.render()
    ship.render()
    bm.render()
    bem.render()
    
    #Permette ai nemici di sparare ogni tot sec...
    count += 1
    
    #----------opzioni di render---------------------
    clock.tick(50) #render ogni 50 millisec.
    #------------------------------------------------
    if (enemy.check_defeat())or(ship.check_collision(bem)):     
       defeat = " Defeat, You Lose! | ...premi un tasto..."
    #-----Mostra i points e vite della navicella-----
    lives = "vite = " + str(ship.life)
    textImg = font.render( lives , 1, (15,255,15))
    surf.blit( textImg, (800,10) )
    #------------------------------------------------
    points = "points = " + str(enemy.point * 10)
    textImg1 = font.render( points , 1, (0,255,255))
    surf.blit( textImg1, (800,50) )
    #------------------------------------------------    
    textImg1 = font.render( defeat , 1, (255,0,0))
    surf.blit( textImg1, (300,350) )
    #------------------------------------------------
    textImg1 = font.render( victory , 1, (250,110,51))
    surf.blit( textImg1, (300,350) )
    #------------------------------------------------
           
    #Scrive a scermo il testo vite, points
    screen.blit( surf, (0,0) )
    
    #Permette la visualizzazione di tutto
    pygame.display.flip()
    if(victory)or(defeat):
      Gioco = False
         
while not pygame.event.get():
      count += 1
print("Arrivederci")
