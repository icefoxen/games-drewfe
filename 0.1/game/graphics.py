#
# graphics.py
# Miscellanious graphics routines and constants.
# Notably:
# Screen-fade
# Screen-flash
#
# Simon Heath
# 24/9/2005


SCREENW = 640
SCREENH = 480
TILEW = 16
TILEH = 16
TILEX = 40
TILEY = 30

import pygame
from pygame.locals import *


def flashScreen( surf ):
   bak = surf.copy()
   surf.fill( (255,255,255) )
   pygame.display.flip()
   pygame.time.delay( 150 )
   surf.blit( bak, (0,0) )
   pygame.display.flip()


