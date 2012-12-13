#
# teams.py
# An object that holds all the info on a specific team.
# The name and logo and such are properties of the team, but the
# list of actual units is not decided by this.  This just provides
# a handy way of keeping track of things.
#
# Simon Heath
# 19/9/2005


import loader


class Team:
   units = []
   logo = ""
   logoImage = ()
   name = ""
   # Values: ENEMY, PLAYER, NEUTRAL, ALLY
   alliance = "ENEMY"

   def __init__( s, cfgfile ):
      cfg = loader.cfgloader.get( cfgfile )
      s.logo = cfg['logo']
      s.logoImage = loader.imgloader.get( s.logo )
      s.name = cfg['name']
      s.alliance = cfg['alliance']

   def addUnit( s, u ):
      s.units.append( u )

   def addUnits( s, u ):
      s.units += u

   def getUnit( s, n ):
      return s.units[n]

   def getUnits( s ):
      return s.units

   # Not sure this is the Right Thing, but...
   def animUnits( s, t ):
      for x in s.units:
         x.sprite.anim( t )

   def getUnitByName( s, name ):
      for x in s.units:
         if x.name == name:
            return x
      raise ("team.getUnitByName(): Unit %s does not exist!" % name)

   def getUnitAt( s, x, y ):
      for x in s.units:
         if x.xCord == x and x.yCord == y:
            return x
      raise "team.getUnitAt: No unit there!"

   def moveUnitTo( s, unit, x, y ):
      s.units[unit].xCord = x
      s.units[unit].yCord = y


   def isCharacterAt( s, x, y ):
      for i in s.characters:
         if x == i.getX() and y == i.getY():
            return True
      return False
            

   def getCharacterAt( s, x, y ):
      for chr in s.characters:
         if chr.getX() == x and chr.getY() == y:
            return chr


