#!/usr/bin/env python

from gamelib.sprite import Sprite
#crea un Nemico
class Enemy(Sprite):
    def __init__(self, surf): #carica grafica da Sprite
        super(Enemy, self).__init__(surf)
        #definisce la velocita di default dei nemici
        self.speed_x = 2
    #carica 2 immagini del nemico di tipo e_type per animazione  
    def init(self, enemy_type):
        self._type = enemy_type
        self.load("gfx",["nemico_"+self._type+"_01.png", "nemico_"+self._type+"_02.png"])
    #aggiorna posizione nemico
    def update(self):
        super(Enemy,self).update()
        self.x += self.speed_x
    #renderizza il nemico
    def render(self):
        self.blit()
