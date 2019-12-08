#!/usr/bin/env python

import pygame, os

class Sprite(object):
        def __init__(self, surf):
                self._surf = surf
         	#memorizzatore di immagini
                self._images = []
        	#contatore immagini
                self._curr_img = 0.0
		#animation updatater
                self.update_rate = 0.1
		#coordinate sprites
                self.x = 0
                self.y = 0
		#dimensione immagine
                self.w = 0 #width
                self.h = 0 #height
		#opzione per debug
                self.debug_bounding_box = False
                
        #carica le immagini della grafica
        def load(self, base_path, images):
            for img in images:
                self._images.append(pygame.image.load( os.path.join(base_path, img)) )
            self.w = self._images[0].get_width()
            self.h = self._images[0].get_height()
        #ottiene il numero del frame corrente
        def get_curr_img(self):
            return self._images[int (self._curr_img)]
        #aggiorna i frames 
        def update(self):
            self._curr_img += self.update_rate
            self._curr_img %= len ( self._images)
        #renderizza le immagini a schermo
        def blit(self):
            self._surf.blit(self.get_curr_img(), (self.x, self.y))
            if self.debug_bounding_box:
                pygame.draw.rect((self._surf, (255,0,0),(self.x, self.y, self.w, self.h)),1)
        #verifica la collisione tra Sprites
        def collide(self, s):
                if ((s.x >= self.x)and(s.x <= (self.x + self.w)))and((s.y >= self.y)and(s.y <= (self.y + self.h))):
                        return True
                return False
