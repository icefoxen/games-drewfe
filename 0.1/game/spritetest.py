import pygame
from pygame.locals import *
from sprite import *

pygame.init()

s = Sprite( 'test.sprite' )
scr = pygame.display.set_mode( (400, 300) )
s.setAnim( 'standAnim' )

x = 0
while True:
   scr.fill( (0,0,0) )
   s.draw( scr, 200, 150 )
   s.anim( pygame.time.get_ticks() )
   pygame.display.flip()

   x += 1
   #if x % 90 == 0:
   #s.setAnim( 'otherStand' )
   #elif x % 40 == 0:
   #   s.setAnim( 'standAnim' )
