#
# sprite.py
# A sprite object.  It draws itself on a surface, handles animations
# from a sheet or strip, and can have arbitrary animation sequences
# specified in a config file.
#
#  Sprite Sheet
#  ------> anim frames
# |oooooo
# |xxxxxx
# |yyyyyy
# |zzzzzz
# v
# different sprites or variations of the same sprite
#
# Simon Heath
# 19/9/2005

import os, pygame
from pygame.locals import *

from loader import *

# ...iiiinteresting.  If a class has a variable whose default object
# is non-atomic, that object is shared between all instances of the
# class.  In other words, it's treated like Java's static members.
class Sprite:
   cfgfile = ""
   img = ()
   imgFile = ""
   frameW = 0
   frameH = 0
   numFramesW = 0
   numFramesH = 0
   sourceRect = ()

   #frame = 0
   #strips = 0

   # "anim" is a hashtable of lists of 2-element lists.
   # yaml doesn't do tuples, which is what I'd prefer, but oh well.
   anims = {}
   currentAnimName = ""
   currentAnim = []
   currentFrameIndex = 0

   animLoop = False
   animDelay = 0
   lastAnim = 0

   screenX = 0
   screenY = 0
   dstX = 0
   dstY = 0


   def __init__( s, cfgfile ):
      s.cfgfile = cfgfile
      cfg = cfgloader.get( cfgfile )
      s.imgFile = cfg['imgFile']
      s.img = imgloader.get( s.imgFile )
      s.frameW = cfg['frameW']
      s.frameH = cfg['frameH']
      rct = s.img.get_rect()
      s.numFramesW = rct.w / s.frameW
      s.numFramesH = rct.h / s.frameH
      s.animDelay = cfg['animDelay']
      s.sourceRect = Rect( (0, 0, s.frameW, s.frameH) )
      s.sourceRect.w = s.frameW
      s.sourceRect.h = s.frameH
      s.sourceRect.x = 0
      s.sourceRect.y = 0

      s.anims = cfg['anims']
      

   def draw( s, screen, x, y ):
      screen.blit( s.img, (x, y), s.sourceRect )


   def setAnim( s, animname ):
      s.currentAnimName = animname
      s.currentFrameIndex = 0
      s.currentAnim = s.anims[animname]
      firstFrame = s.currentAnim[0]
      s.sourceRect.x = firstFrame[0] * s.frameW
      s.sourceRect.y = firstFrame[1] * s.frameH
      #print s.cfgfile, s.sourceRect
      

   def setAnimLoop( s, loop ):
      s.animLoop = loop

   def setAnimDelay( s, delay ):
      s.animDelay = 0

   def anim( s, t ):
      if (t - s.lastAnim) > s.animDelay:
         s.lastAnim = t
         s.nextFrame()


   def nextFrame( s ):
      s.currentFrameIndex += 1
      if s.currentFrameIndex > (len( s.currentAnim ) - 1):
         s.currentFrameIndex = 0
      # Life would be nicer if currentAnim held tuples instead of
      # 2-element lists, but I don't wanna bother converting them
      # and this works anyway.  I'm not sure it would even make
      # much difference, internally or externally.
      s.sourceRect.x = s.currentAnim[s.currentFrameIndex][0] * \
                       s.frameW
      s.sourceRect.y = s.currentAnim[s.currentFrameIndex][1] * \
                       s.frameH
      

   def prevFrame( s ):
      s.currentFrameIndex -= 1
      if s.currentFrameIndex < 0:
         s.currentFrameIndex = len( s.currentAnim ) - 1
      s.sourceRect.x = s.currentAnim[s.currentFrameIndex][0] * \
                       s.frameW
      s.sourceRect.y = s.currentAnim[s.currentFrameIndex][1] * \
                       s.frameH

   def frameNumber( s, i ):
      return s.currentAnim

   def setAnimDelay( s, i ):
      s.animDelay = i
   def getAnimDelay( s, i ):
      return s.animDelay
   
   def setAlpha( s, i ):
      s.img.set_alpha( i )

   def getAlpha( s ):
      return s.img.get_alpha()
