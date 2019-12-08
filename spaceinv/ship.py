#!/usr/bin/env python

from gamelib.sprite import Sprite
from spaceinv.bullet import BulletManager
from spaceinv.explosion import ExplosionManager
from sys import exit

#classe che definisce giocatore
class Ship(Sprite):
    #inizializza variabili globali e carica funzioni classe Sprite
    def __init__(self, surf):
        super (Ship ,self).__init__(surf) #inizializza funzioni classe Sprite
        #variabili globali
        self.life = 3
        self.update_rate = 0
        self.y = 650 #posizione verticale sullo schermo del giocatore
        
    #carica immagine navicella spaceinvaders
    def init(self, bm):
        self.load("gfx", ["player.png"])
        self._bm = bm
        
    #definisce i limiti massimi della navicella    
    def update(self):
        if self.x < 5: self.x = 5
        if self.x > 740: self.x = 740
        
    #renderizza la navicella
    def render(self):
        self.blit()
        
    #permette di sparare alla navicella
    def fire(self):
        self._bm.add(self.x +(self.w/2)-8, self.y, -4)
        
    #verifica la collisione con i proiettili nemici 
    def check_collision(self,bulletenmanager):
        self.bem = bulletenmanager
        count = 0
        #controlla la posizione simultanea di tutti i proiettili nemici in campo        
        for b in self.bem._bullets:
            if(b.x >= self.x)and(b.y >= self.y)and(b.x <= (self.x+self.w))and(self.y <= (self.y+self.h)):
                self.life -= 1
                b.x = 1000          
        #riduce la vita di un' unita
        if self.life <= 0:
           return True
