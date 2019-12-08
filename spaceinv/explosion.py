#!/usr/bin/env python

from gamelib.sprite import Sprite

class Explosion(Sprite):
    def __init__(self, surf):
        super (Explosion, self).__init__(surf)
        #variabili globali
        self.update_rate = 0.2 #velocita esplosioni
        self.frames = 10
        
    #inizializzazione dell'esplosione (carica immagini in memoria)
    def init(self):
        self.load("gfx", ["exp-01.png","exp-02.png"])
    
    #aggiorna immagini esplosione
    def update(self):
        super(Explosion, self).update()
        self.frames -= 1
        
    #renderizza esplosione
    def render(self):
        self.blit()

#gestore esplosioni
class ExplosionManager(object):
    def __init__(self, surf): #carico variabili grafica 
        self._surf = surf
        self._explosions = [] #lista globale esplosioni
        
    #aggiunge esplosione dove avvenuta collisione
    def add(self, x, y):
        b = Explosion(self._surf) #crea oggetto esplosione
        b.init()
        b.x = x
        b.y = y
        #aggiunge esplosione alla lista
        self._explosions.append(b)
        return b
        
    #aggiorna esplosioni 
    def update(self):
        rem_list = [] #lista per rimozione esplosione
        count = 0     #variabile di appoggio per rimozione
        for b in self._explosions:
            b.update()
            if b.frames <= 0: #verifica dell'avvenuta fine dell'animazione
                rem_list.append(count)
            count += 1
        rem_list.reverse()
       #rimozione degli elementi da rem_list
        for b in rem_list:
            del self._explosions[b]
    #rendering esplosione
    def render (self):
        for b in self._explosions: #rendering simultaneo
            b.render()
