#!/bin/usr/env python

from spaceinv.enemy import Enemy
from spaceinv.explosion import ExplosionManager
from sys import exit
import pygame

#gestore nemici
class EnemyManager(object):
    def __init__(self, surf):
        self._enemies = [] #lista di nemici vuota
        self._surf = surf #surface per il disegno dei nemici
        self.point = 0 #punteggio per il player
        self.count = 0 #per rendere progressivo l'aumento della velocita
        
    #aggiunge nemico in posizione(x,y) + tipo di nemico    
    def add(self, x, y, e_type):
        #creo oggetto nemico da Enenmy --> enemy.py
        enemy = Enemy( self._surf)
        enemy.init(e_type) #inizializzo nemico(tipo nemico)
        #posiziono nemico sullo schermi
        enemy.x = x
        enemy.y = y
        #lo aggiungo alla lista dei nemici
        self._enemies.append(enemy)
        return enemy

    def update(self):
        flip = 0 #variabile per invertire e far scalare movimento dei nemici 
        #aggiornamento nemici piu controllo di posizione 
        for en in self._enemies:
            en.update()
            #verifica se i nemici sono giunti ai bordi del gioco
            if not flip:
                if en.x + en.w >= 800:
                    flip = 1
                    self.count += 1 #numero di scalate
                elif en.x <= 0:
                    flip = 1
                    self.count += 1 #numero di scalate
        if flip: #una volta ogni due discese i nemici raddoppiano la velocita
            for en in self._enemies:
                en.speed_x = - en.speed_x
                en.y += en.h
                if (self.count % 2 == 0):
                    if en.speed_x > 0:  #raumento velocita nemico
                          en.speed_x = en.speed_x + 2 
                    elif en.speed_x < 0:
                          en.speed_x = en.speed_x - 2
    #renderizza nemico
    def render(self):
        for en in self._enemies:
            en.render()
    #verifica collisione con proiettili del player
    def collide(self, bullet):
        count = 0 #variabile d'appoggio per rimozione nemici
        for enemy in self._enemies:
            if enemy.collide(bullet): #carica la collisione da Sprite
                del self._enemies[count]
                self.point += 1 #aggiornamento punteggio player *10
                return enemy
            count += 1            
        return None
    #controlla se i nemici hanno invaso la terra
    def check_defeat(self):    
        for en in self._enemies:
            if (en.y >= 600): #limite massimo raggiungibile dai nemici --> player perde
               return True
