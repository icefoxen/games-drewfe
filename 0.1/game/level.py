#
# level.py
# This is the class that handles the main map-game.  It's the real
# core of the game, I guess.  Handling of character stat screens, menus,
# start screens, etc, are all handled by different objects.
#
# This handles the mainloop, basic I/O, 
#
# Simon Heath
# 19/9/2005

import os, pygame
from pygame.locals import *

import loader, map, input, sprite


class Level:
   map = ()
   screen = ()
   level = ""
   # These define the VIEWPORT of the map!
   viewx = 0
   viewy = 0
   vieww = 16
   viewh = 15

   cursorx = 0
   cursory = 0
   cursorSprite = ()

   teams = []
   units = []

   events = []
   
   def __init__( s, screen, level, teams ):
      cfg = loader.cfgloader.get( level )
      s.screen = screen
      s.level = level
      s.map = map.Map( cfg['map'] )
      s.teams = teams
      s.cursorSprite = sprite.Sprite( "cursor.sprite" )
      s.cursorSprite.setAnim( "normal" )

   def draw( s ):
      s.map.draw( s.screen, s.viewx, s.viewy, s.vieww, \
                  s.viewh )
      for x in s.teams:
         for char in x.getUnits():
            s.map.drawAt( s.screen, char.sprite, char.xCord, char.yCord, \
                          (s.viewx, s.viewy, s.vieww, s.viewh) )

      s.drawCursor()

   def addTeam( s, t ):
      s.teams.append( t )

   def getTeam( s, t ):
      return s.teams[t]

   # Moves the cursor to a given position, doing error-checking.
   # If the cursor moves off bounds of the screen, the screen follows,
   # so this could be a way to move the screen around... esp. with a
   # "centerOnCursor()" method.
   def moveCursor( s, x, y ):
      if x < 0 or x >= s.map.mapw:
         return
      elif x < s.viewx:
         s.viewx = x
      elif  x > s.viewx + s.vieww:
         s.viewx += 1
      
      if y < 0 or y >= s.map.maph:
         return
      elif y < s.viewy:
         s.viewy = y
      elif y > (s.viewy + s.viewh):
         s.viewy += 1
      
      s.cursorx = x
      s.cursory = y

   def moveCursorLeft( s ):
      s.moveCursor( s.cursorx - 1, s.cursory )
      
   def moveCursorRight( s ):
      s.moveCursor( s.cursorx + 1, s.cursory )
      
   def moveCursorUp( s ):
      s.moveCursor( s.cursorx, s.cursory - 1 )
      
   def moveCursorDown( s ):
      s.moveCursor( s.cursorx, s.cursory + 1 )

   def drawCursor( s ):
      s.map.drawAt( s.screen, s.cursorSprite, s.cursorx, s.cursory, \
                          (s.viewx, s.viewy, s.vieww, s.viewh) )



   def doAnim( s ):
      t = pygame.time.get_ticks()
      for x in s.teams:
         x.animUnits( t )
         pygame.display.flip()
      s.cursorSprite.anim( t )

   # Hmmm...  This is... tricky.
   # We have to display the move area, letting the cursor move around
   # within it.
   # When the confirm button is hit, we have to do the move anim and sound,
   # when the cancel button is hit, we go back...
   #
   # Hmmm.... modes...  Would it be worth it to build a real architecture
   # for that?  Perhaps not, since the modes tend to be pretty damn 
   # different.  We're already gonna have different objects for battles
   # and char screens and such.
   def doCharacterMove( s, char, fromx, fromy, tox, toy ):
      return


   def doInput( s ):
      pygame.event.pump()

      # Polling
#      keys = pygame.key.get_pressed()

#      if keys[input.keyUp]:
#         s.moveCursorUp()
#      elif keys[input.keyDown]:
#         s.moveCursorDown()
#      elif keys[input.keyLeft]:
#         s.moveCursorLeft()
#      elif keys[input.keyRight]:
#         s.moveCursorRight()

      # Hrm, this gives an error.  It DOES quit though!
#      if keys[input.keyQuit]:
#         pygame.quit()


      # Or, we can do events and use the key repeat settings.
      # Works pretty handily, actually.
      keys = pygame.event.get( [KEYDOWN] )
      for x in keys:
         if x.key == input.keyQuit:
            pygame.quit()
            
         elif x.key == input.keyUp:
            s.moveCursorUp()
         elif x.key == input.keyDown:
            s.moveCursorDown()         
         elif x.key == input.keyLeft:
            s.moveCursorLeft()            
         elif x.key == input.keyRight:
            s.moveCursorRight()

   def mainloop( s ):
      pygame.key.set_repeat( 200, 30 )
      while True:
         s.screen.fill( (0,0,0) )
         s.doInput()
         s.draw()
         s.doAnim()
         pygame.display.flip()
