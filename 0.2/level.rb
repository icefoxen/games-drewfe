# level.rb
# This is the level object itself.
# It contains the map, teams, events, units, all that good stuff.


class Level
   def initialize( levelfile )
      cfg = Resources.getConfig( levelfile )
      @map = Map.new( cfg['level','mapfile'] )
      @teams = []

      @castles = []
      @towns = []
      @events = []
   end

   def getAllUnits
      units = @teams.collect {|x| x.getUnits}
      units.flatten!
      return units
   end
end
