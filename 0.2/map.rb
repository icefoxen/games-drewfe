# map.rb
# Note that this is just the map itself; events and teams and
# all the other fun stuff is in level.rb
# Essentially, a map is a 2-d array of numbers, each number specifying a
# different terrain type.  It is arranged row-at-a-time.
#
# A map file is just a file with a single number on each line.  The first
# number is the width of the map, the second is the height.  The next
# <width> numbers are the tiles for the zero'th row, the <width> numbers
# after that are the first row, and so on.

# Okay.  The way these things are going to be drawn is thus:
# We're going to have an automatic layout engine to put things together with
# corners and so on.  So we have the terrain layout, here.  When we draw it,
# we're going to select which tile to draw based not on the terrain, but on
# a 2x2 grid, with the tile going at the intersection of the four terrain types.
# With nine terrain types, this results in 9^4 different combinations/tile 
# options needed.  However, there are a bunch that are just mirrors and 
# rotations, so we can cut those out one way or another.


#include 'config'

T_INVALID = 0
# Normally passable things
T_PLAINS = 1
T_ROAD = 2
# Hard-to-pass things
T_FOREST = 100
T_DESERT = 101
T_MOUNTAIN = 102

# Impassable things
T_OCEAN = 200
T_DENSEFOREST = 201
T_HIGHMOUNTAIN = 202
T_CLIFF = 203


class Map
   def initialize( filename )
      @w = 0 # These get initialized by parseMap()
      @h = 0
      @map = parseMapFile( filename )
   end

   def []( x, y )
      if x >= @w or y >= @h then
         return T_INVALID
      else
         return @map[y][x] # We store it by rows!
      end
   end

   def getMap
      return @map
   end

   def parseMapFile( filename )
      f = File.open( filename, 'r' )
      l = f.readLines
      f.close
      return parseMap( l )
   end

   def parseMap( lines )
      @w = lines[0].to_i
      @h = lines[1].to_i
      lines.slice!(0,1)

      map = []
      for i in 0..@h
         row = lines.slice( 1*i, @w*i )
         # apparently 'map' is called 'collect' in Ruby.
         row.collect! {|x| x.to_i}
         map = map.push( row )
      end
      return map
   end
end
