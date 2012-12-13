#!/usr/bin/env python
#
# To start off, we just want to make a map out of tiles.
# 
# Simon Heath
# 15/9/2005
import os, pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

# Test tile image
if pygame.image.get_extended():
   IMAGE = pygame.image.load( "images/tiletest2.png" )
else:
   raise "Waaah!  No extended images!"

# We want an object to build a big map.
class Map:
   def __init__( s ):
      s.tile = IMAGE
      s.w, s.h = s.tile.get_size()
      s.x = 24
      s.y = 24
      s.grid = [[s.tile for i in range( s.x )] for j in range( s.y )]

   def setTile( s, x, y, t ):
      s.grid[y][x] = t

   def getTile( s, x, y ):
      s.grid[y][x]


class MapDrawer:
   def __init__( s, map, surf ):
      s.map = map
      s.surf = surf
      # The rect it blits to
      s.screenRect = ()
      # The window of tiles it's blitting
      s.screenWindow = ()

   def draw( s ):
      yoff = 0
      xoff = 0
      for y in s.map.grid:
         for x in y:
            s.surf.blit( x, (xoff, yoff) )
            xoff += s.map.w - 1
         xoff = 0
         yoff += s.map.h



def main():
   pygame.init()
   screen = pygame.display.set_mode( (640, 480) )
   clock = pygame.time.Clock()

   m = Map()
   md = MapDrawer( m, screen )



   while 1:
      clock.tick(60)
      md.draw()
      pygame.display.flip()
      print "Looped!"
      
      for event in pygame.event.get():
         if event.type == QUIT:
            return
         elif event.type == KEYDOWN and (event.key == K_ESCAPE \
                                         or event.key == K_q):
            return

         
if __name__ == '__main__': main()
