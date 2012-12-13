import pygame
from pygame.locals import *

import teams
import character
import graphics
from level import *

def main():
   pygame.init()

   scr = pygame.display.set_mode( (400, 300) )
   t = teams.Team( 'test.team' )
   p = character.Character( 'simon.chr' )
   t.addUnit( p )
   a = Level( scr, 'test.level', [t] )

   a.mapx = 0
   a.mapy = 0
   # Map should error-check this!
   # ...no, that'll happen as part of the character movement.
   p.xCord = 3
   p.yCord = 3

   while True:
      a.draw()
      a.doAnim()
      pygame.display.flip()
      

if __name__ == '__main__':
   main()
