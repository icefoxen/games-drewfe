# character.rb
# A character class.
# Fairly simple, really.  Just has a lot of data and a few basic methods.
# TODO: Make all this load from a config file

# Weapon proficiencies
SWORD = 0
AXE = 1
SPEAR = 2
BOW = 3
LIGHT = 4
DARK = 5
ANIMA = 6
STAFF = 7

RANK_NONE = 6
RANK_E = 5
RANK_D = 4
RANK_C = 3
RANK_B = 2
RANK_A = 1
RANK_S = 0



MOVE_FOOT = 0
MOVE_HORSE = 1
MOVE_FLYING = 2



class Character
   def initialize
      # Meta-info
      @name = "Dude"
      @class = "Swordfighter"
      @movement = 0
      @movementmode = MOVE_FOOT

      # Stats
      @maxhp = 0
      @hp   = @maxhp
      @str  = 0
      @mag  = 0
      @spd  = 0
      @skl  = 0
      @luck = 0
      @def  = 0
      @mdef = 0
      @con  = 0

      # Stat growths.  1.0 is 100%
      @hpg   = 0.0
      @strg  = 0.0
      @magg  = 0.0
      @spdg  = 0.0
      @sklg  = 0.0
      @luckg = 0.0
      @defg  = 0.0
      @mdefg = 0.0
      @cong  = 0.0

      # Weapon profs
      @profs = {
         SWORD => RANK_NONE,
         AXE => RANK_NONE,
         SPEAR => RANK_NONE,
         BOW => RANK_NONE,
         LIGHT => RANK_NONE,
         DARK => RANK_NONE,
         ANIMA => RANK_NONE,
         STAFF => RANK_NONE 
      }

      # Other stuff
      @kills = 0
      @exp = 0
      @level = 1
      @items = []
      @equipped = 0
      @promoclass = "Nothing"


      # Map data
      @x = 0
      @y = 0
      @waypoint = 0
      @hasGone = false

      # Drawing stuff
      @portrait = 0
      @sprite = 0
   end


   def equip( x )
   end

   def addItem( x )
   end

   def removeItem( x )
   end

   def tradeItem( character, x )
   end

   def gainExp( exp )
   end

   def levelUp
   end

   def levelUpRandom
   end

   # XXX: ???
   def levelUpConstant
   end

   def capStats
   end

   def promote
   end

   def takeDamage( d )
      @hp -= d
   end

   def heal( d )
      @hp += d
      if @hp > @maxhp then
         @hp = @maxhp
      end
   end

   def isDead
      return @hp <= 0
   end

   def moveTo( x, y )
      @x = x
      @y = y
   end

end
