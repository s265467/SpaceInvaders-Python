#!/usr/bin/env python

from gamelib.sprite import Sprite

class Bullet(Sprite):
    #inizializza le variabili globali per la classe Bullet
    def __init__(self, surf):
        super (Bullet, self).__init__(surf) #inizializza Sprite

        self.update_rate = 0 # velocita aggiornamento animazione
        self.speed_y = 0 # velocita verticale del proiettile all'inizio del gioco
    #carica immagine del proiettile
    def init(self):
        self.load("gfx", [ "bullet_enemy.png"])
    #provoca lo spostamento del proiettile
    def update(self):
        self.y += self.speed_y
    #renderizza il proiettile
    def render(self):
        self.blit()
#gestore dei proiettili
class BulletEnManager(object):
    #inizializza le variabili della classe B.E.M
    def __init__(self, surf):
        self._surf = surf #surface
        self._bullets = [] #lista proiettili vuota
    #aggiunge un proiettile in posizione x,y a velocita dy
    def add(self, x, y, dy):
        b = Bullet(self._surf) #inizializza classe Bullet
        b.init() 
        #setta caratteristiche del proiettile
        b.x = x
        b.y = y
        b.speed_y = dy
        #carica proiettile nella lista
        self._bullets.append(b)
        return b
    #aggiorna proiettili
    def update(self):
        rem_list = [] #lista per la rimozione dei proiettili
        count = 0 #variabile di appoggio
        #controlla i proiettili da eliminare
        for b in self._bullets:
            b.update()
            if b.y <= 0:
                rem_list.append(count)
            if b.y >= 700:
                rem_list.append(count)
            count += 1

        rem_list.reverse() #ricalcola la lista 

        for b in rem_list: #rimuove i proiettili dalla lista 
            del self._bullets[b]
    #renderizza i proiettili            
    def render(self):
        for b in self._bullets :
            b.render()
