#
# map.py
# ...okay.  This is the map object.  It handles loading a map,
# drawing it, moving things around on it, getting the locations of
# certain objects, pathing & movement rules, and such fun stuff.
#
# It does NOT handle combat, turn-generation, input events, GUI,
# conversations, interaction/trigger events, or any of that fun stuff.
#
# TILESETS:
# Tilesets are just gonna be a big sheet/strip of images.  The map file
# will tell you how wide/high each tile is.  The map data itself is just
# an array of numbers, each referring to a tile.
# ....hmm.  Yes.  The "hardness" of each tile, how many movement it takes
# to pass through, depends on the tile number.  0-15 takes 0 movement
# (cannot be moved through), 16-31 takes 1 movement, 32-47 takes 2 movement,
# and so on.  Other tiles can have other properties.
# ...with our new sprite class, this will have to be rather rethought.
# Could just be a list alongside the tileset attribute in the map file that
# gives the move cost of each type of tile
#
# Simon Heath
# 16/9/2005


import loader, character, sprite


# Terrain type constants.
OCEAN = 0
FOREST = 1
PLAINS = 2
ROAD = 3
MOUNTAIN = 4
BIGMOUNTAIN = 5
DESERT = 6
TERRAINS = {
   "ocean" : 0,
   "forest" : 1,
   "plains" : 2,
   "road" : 3,
   "mountain" : 4,
   "bigmountain" : 5,
   "desert" : 6
   }

# Move costs for the various terrains... indexed by terrain #.
# Imperfect...  mounted units go worse over mountains and forests
# etc.  -1 means "can't go over it".
# ...not quite sure how these should work, really...
MOVECOSTS = [-1, 2, 1, 0.75, 3, -1, 3]


# Okay.  Either terrain type is part of the map, or the tile.
# Either terrain type is just a movement cost, or a handle that
# you can get the movement cost for.


# The map itself is a two-dimensional array of numbers.
# Each number is an index into tileset, which holds the
# possible sprites for the map, and terrainset, which holds the
# actual terrain type.
#
# Okay.  What we REALLY want is to be able to associate a tile sprite
# with a terrain type, which implies a movement cost.  We represent
# this tile by a number in the grid.
class Map:
   grid = []
   mapw = 0
   maph = 0
   tilew = 0
   tileh = 0
   tileset = []  # List of sprites
   terrainset = [] # List of terrain types
   mapfile = ""
   
   def __init__( s, mapfile ):
      mapdata = loader.cfgloader.get( mapfile )
      s.mapfile = mapfile
      s.tilew = mapdata['tilew']
      s.tileh = mapdata['tileh']
      # This is the "iterate function over list" map, not "make a map" map.
      s.tileset = map( sprite.Sprite, mapdata['tileset'] )
      for x in s.tileset:
         x.setAnim( "mapanim" )
         #print x.sourceRect
      terrainset = mapdata['terrainset']
      for x in range( 0, len( terrainset ) ):
         s.terrainset.append( TERRAINS[ terrainset[x] ] )
      
      s.grid = mapdata['map']
      s.mapw = len( s.grid )
      s.maph = len( s.grid[0] )
      s._verifyMapDimensions()

   def _verifyMapDimensions( s ):
      for x in s.grid:
         if len( x ) != s.maph:
            raise "map._verifyMapDimensions: There's a column in map %s that isn't %d!" % (s.mapfile, s.maph)
              


   def getTile( s, x, y ):
      return s.grid[x][y]

   def setTile( s, x, y, t ):
      s.grid[x][y] = t

   def setTileSet( s, t ):
      s.tileset = t

   def getTileMoveCost( s, x, y ):
      tile = s.grid[x][y]
      tiletype = s.terrainset[tile]
      return MOVECOSTS[tiletype]

   # This does pathfinding!
   # A*.  Weird stuff.
   def getDistance( s, x1, y1, x2, y2 ):
      return 1

   def getTileSubset( s, x, y, w, h ):
      tiles = s.grid[x:w]
      for i in range( 0, len( tiles ) ):
         tiles[i] = tiles[i][y:h]

      return tiles

   # Moves the character to the given point with pathfinding,
   # going through intermediate points.
   def walkCharacter( s, n, x, y ):
      ()

   def printTileset( s ):
      for x in s.tileset:
         print x.sourceRect

   # Draws the map on the given surface, within the given TILE
   # bounds.
   def draw( s, screen, viewx, viewy, vieww, viewh ):
      xoff = 0
      yoff = 0
      for column in s.grid[viewx:(viewx+vieww + 1)]:
         for item in column[viewy:(viewy+viewh + 1)]:
            s.tileset[item].draw( screen, xoff, yoff )
            yoff += s.tileh
         yoff = 0
         xoff += s.tilew


##    def draw( s, screen, mapx, mapy, screenw, screenh ):
##       xoff = 0
##       yoff = 0
##       for x in s.grid[mapx:(mapx+screenw)]:
##          for y in x[mapy:(mapy+screenh)]:
##             print "Foo", mapy, screenh
##             #print len( x[mapy:(mapy+screenh)] )
##             s.tileset[y].draw( screen, xoff, yoff )

##             #print s.tileset[y].cfgfile
##             #print "Drew tile", y, "at", xoff, yoff, "from", s.tileset[y].sourceRect
##             yoff += s.tileh
##             if yoff > screenh:
##                #print "yoff looped at", yoff
##                yoff = 0
##                break
##          yoff = 0
##          xoff += s.tilew
##          if xoff > screenh:
##             #print "xoff looped at", xoff
##             xoff = 0
##             break

   # Hmmm, this could be useful...  draws the given sprite at the
   # given tile location, essentially doing gameworld/screenworld
   # conversion.
   # Sprites that overlap tiles a little could be a problem, if they don't
   # do it to the left and down.  Hmm, just center the sprite?
   # That would work NICE...
   def drawAt( s, screen, sprite, objx, objy, screenRect ):
      # Map co-ords of screen
      screenx, screeny, screenw, screenh = screenRect
      # Sanity checks
      if objx < screenx or objy < screeny or objx > (screenx + screenw) \
            or objy > (screeny + screenh):
         return
      objscreenx = (objx - screenx) * s.tilew
      objscreeny = (objy - screeny) * s.tileh
      sprite.draw( screen, objscreenx, objscreeny )
      

   def anim( s, t ):
      for x in s.tileset:
         x.anim( t )
