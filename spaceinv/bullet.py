#!/usr/bin/env python

from gamelib.sprite import Sprite

class Bullet(Sprite):
     
    def __init__(self, surf):
        super (Bullet, self).__init__(surf)

        self.update_rate = 0
        self.speed_y = 0
    
    def init(self):
        self.load("gfx", [ "bullet.png"])
    
    def update(self):
        self.y += self.speed_y
    
    def render(self):
        self.blit()

class BulletManager(object):
    
    def __init__(self, surf, em, exp):
        self._surf = surf
        self._bullets = []
        self._em = em
        self._exp = exp
    
    def add(self, x, y, dy):
        b = Bullet(self._surf)
        b.init()
        
        b.x = x
        b.y = y
        b.speed_y = dy

        self._bullets.append(b)
        return b

    def update(self):
        rem_list = []
        count = 0

        for b in self._bullets:
            b.update()

            if b.y <= 0:
                rem_list.append(count)
            if b.y >= 700:
                rem_list.append(count)

            count += 1

        rem_list.reverse()

        for b in rem_list:
            del self._bullets[b]

        self._check_collision()

    def _check_collision(self):
        count = 0
        rem_list = []

        for b in self._bullets:
            obj = self._em.collide(b)
            if obj :
                self._exp.add(b.x,b.y)
                rem_list.append( count )

            count += 1
        rem_list.reverse()

        for b in rem_list:
            del self._bullets[b]
            
      
    def render(self):
        for b in self._bullets :
            b.render()
            
