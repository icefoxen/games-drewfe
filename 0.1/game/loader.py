#
# loader.py
# This is a resource loader that makes sure resources have only
# been loaded once.  Resources are sounds, config files, images,
# and just about anything else.
#
# Simon Heath
# 15/9/2005

import os, pygame
from pygame.locals import *

import config

colorkey = (255, 0, 128)
currentmusic = ()

class ResourceLoader:
   rdir = ""
   rtable = {}
   loadFunc = {}
   def __init__( s, dir, loadFunc ):
      s.rdir = dir
      s.loadFunc = loadFunc

   # Ditches all the cached resources
   # Useful mainly for re-loading things after changes.
   def purge( s ):
      s.rtable = {}

   # Ditches a certain cached resource.
   def remove( s, name ):
      s.rtable.pop( name )

   def get( s, name ):
      if s.rtable.has_key( name ):
         return s.rtable[name]
      else:
         itm = s.loadFunc( (s.rdir + name) )
         s.rtable[name] = itm
         return itm


def loadImage( s ):
   print "Image %s loaded" % s
   a = pygame.image.load( s )
   a.set_colorkey( colorkey )
   return a

def loadSound( s ):
   print "Sound %s loaded" % s
   return pygame.mixer.Sound( s )

def loadConfig( s ):
   print "Config %s loaded" % s
   return config.ConfigLoader( s )

imgloader = ResourceLoader( "images/", loadImage )
soundloader = ResourceLoader( "sounds/", loadSound )
cfgloader = ResourceLoader( "config/", loadConfig )


def playMusic( music ):
   s = soundloader.get( music )
   currentmusic.stop()
   currentmusic = s
   currentmusic.play( -1 )  # -1 means infinate loop.

def playSound( sound ):
   return
