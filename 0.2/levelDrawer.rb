# levelDrawer.rb
# This takes a Level object, and... draws it!  All of it.
# Really, it only draws the map and character sprites and such.
# The GUI and such is drawn seperately.
# This does no input handling or anything, either.

require 'level'

class LevelDrawer
   def initialize( screen, level )
      @screen = screen
      @level = level
      @currentX = 0
      @currentY = 0
      @screenW = 0 # XXX
      @screenH = 0 # XXX
   end

   def drawLevel
   end

   # TODO: Make it do bounds-checking
   def moveTo( x, y )
      @currentX = x
      @currentY = y
   end
end
