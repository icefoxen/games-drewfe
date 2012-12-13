import pygame
from pygame.locals import *
from map import *

a = Map( 'test.map' )
scr = pygame.display.set_mode( (400, 300) )


a.draw( scr, 0, 0, 400, 300 )
pygame.display.flip()
#a.printTileset()
while True:
   pass
