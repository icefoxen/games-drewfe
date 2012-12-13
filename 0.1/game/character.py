#
# character.py
# A character is ANY type of unit, person, whatever.  This includes generic
# enemy units.  There can be more of one character.
#
# Simon Heath
# 16/9/2005

import loader
import sprite
import random


class Character:
   # Non-character info
   cfgfile = ""

   # Stats
   name = "Noninit"
   cls = "Noninit"
   movement = 0
   movementMode = "foot"  # other modes include "mounted" and "flying"

   hp = 0
   maxhp = 0
   strength = 0
   magic = 0
   speed = 0
   skill = 0
   luck = 0
   defense = 0
   mdefense = 0
   constitution = 0

   # Stat growths... 1.0 is 100%
   hpg = 0.0
   strengthg = 0.0
   magicg = 0.0
   speedg = 0.0
   skillg = 0.0
   luckg = 0.0
   defenseg = 0.0
   mdefenseg = 0.0

   # Weapon proficiencies
   # 6 is none, 5 is E, 4 is D, etc... 0 is S.
   weaponType = "weapon"  # or "magic"
   sword = 6
   axe = 6
   spear = 6
   bow = 6
   
   light = 6
   dark = 6
   anima = 6
   staff = 6

   # Weapon proficiency experience
   swordExp = 0
   axeExp = 0
   spearExp = 0
   bowExp = 0
   lightExp = 0
   darkExp = 0
   animaExp = 0
   staffExp = 0

   # Other stuff
   kills = 0
   experience = 0
   level = 1
   items = []
   equippedWeapon = 0
   promotedcls = "Noninit"
   
   portrait = ()
   portraitFile = "null.png"
   sprite = ()
   spriteFile = "null.png"
   attackAnim = ()
   attackFile = ""
   charID = 0
   team = 0

   # Map data
   xCord = 0
   yCord = 0
   waypoint = 0
   hasGone = False

   def __init__( s, cfgfile ):
      cfg = loader.cfgloader.get( cfgfile )
      s.cfgfile = cfgfile
      s.name = cfg['name']
      s.cls = cfg['class']
      s.movement = cfg['movement']
      s.movementMode = cfg['movementMode']

      s.maxhp = cfg['maxhp']
      s.hp = s.maxhp
      s.strength = cfg['strength']
      s.magic = cfg['magic']
      s.speed = cfg['speed']
      s.skill = cfg['skill']
      s.luck = cfg['luck']
      s.defense = cfg['defense']
      s.mdefense = cfg['mdefense']
      s.constitution = cfg['constitution']

      s.hpg = cfg['hpg']
      s.strengthg = cfg['strengthg']
      s.magicg = cfg['magicg']
      s.speedg = cfg['speedg']
      s.skillg = cfg['skillg']
      s.luckg = cfg['luckg']
      s.defenseg = cfg['defenseg']
      s.mdefenseg = cfg['mdefenseg']

      s.weaponType = cfg['weaponType']
      s.sword = cfg['sword']
      s.axe = cfg['axe']
      s.spear = cfg['spear']
      s.bow = cfg['bow']
      s.light = cfg['light']
      s.dark = cfg['dark']
      s.anima = cfg['anima']
      s.staff = cfg['staff']

      s.experience = cfg['experience']
      s.level = cfg['level']
      s.promotedcls = cfg['promotedcls']
      s.items = []
      s.equippedWeapon = 0

      s.portraitFile = cfg['portraitFile']
      s.spriteFile = cfg['spriteFile']
      s.portrait = loader.imgloader.get( s.portraitFile )
      s.sprite = sprite.Sprite( s.spriteFile )
      s.sprite.setAnim( 'standAnim' )

   def getItems( s ):
      return s.items

   def setItems( s, itms ):
      s.items = itms

   def getItem( s, i ):
      return s.items[i]
   def addItem( s, i ):
      s.items.append( i )
   def delItem( s, i ):
      s.items.remove( i )

   def equipWeapon( s, i ):
      s.eqippedWeapon = i

   # Hmm, the levelling up is too invisible here...
   def addExp( s, e ):
      if s.level < 30:
         s.exp += e
         if s.exp > 99:
            s.exp = s.exp % 100
            s.levelUp()

   def levelUp( s ):
      if s.level != 30:
         s.level += 1
         if random.random() < s.hpg:
            s.maxhp += 1
         if random.random() < s.strengthg:
            s.strength += 1
         if random.random() < s.magicg:
            s.magic += 1
         if random.random() < s.speedg:
            s.speed += 1
         if random.random() < s.skillg:
            s.skill += 1
         if random.random() < s.luckg:
            s.luck += 1
         if random.random() < s.defenseg:
            s.defense += 1
         if random.random() < s.mdefenseg:
            s.mdefense += 1

         if s.maxhp > 100:
            s.maxhp = 100
         if s.strength > 30:
            s.strength = 30
         if s.magic > 30:
            s.magic = 30
         if s.speed > 30:
            s.speed = 30
         if s.skill > 30:
            s.skill = 30
         if s.luck > 30:
            s.luck = 30
         if s.defense > 30:
            s.defense = 30
         if s.mdefense > 30:
            s.mdefense = 30
         

   # Promotion will probably have fixed stat increases depending
   # on class.  Will probably increase your con also.
   def promote( s ):
      s.cls = s.promotedcls

   def damage( s, d ):
      s.hp -= d

   def heal( s, j ):
      s.hp += j
      if s.hp > s.maxhp:
         s.hp = s.maxhp

   def setHP( s, h ):
      s.hp = h

   def isDead( s ):
      return s.hp < 1

   def moveTo( s, x, y ):
      s.xCord = x
      x.yCord = y

   def getLoc( s ):
      return (s.xCord, s.yCord)

   def getX( s ):
      return s.xCord

   def getY( s ):
      return s.yCord

   def writeAllStats( s ):
      print "Name: %s" % s.name
      print "Cfgfile: %s" % s.cfgfile
      print "Class: %s" % s.cls
      print "Movement: %s" % s.movement
      print "Movement Mode: %s" % s.movementMode
      print "Max HP: %s" % s.maxhp
      print "Current HP: %s" % s.hp
      print "Strength: %s" % s.strength
      print "Magic: %s" % s.magic
      print "Speed: %s" % s.speed
      print "Skill: %s" % s.skill
      print "Luck: %s" % s.luck
      print "Defense: %s" % s.defense
      print "Magic Defense: %s" % s.mdefense

      print "HPg: %s" % s.hpg
      print "Strengthg: %s" % s.strengthg
      print "Magicg: %s" % s.magicg
      print "Speedg: %s" % s.speedg
      print "Skillg: %s" % s.skillg
      print "Luckg: %s" % s.luckg
      print "Defenseg: %s" % s.defenseg
      print "Magic Defenseg: %s" % s.mdefenseg
      
      print "Weapon Type: %s" % s.weaponType
      print "Sword: %s" % s.sword
      print "Axe: %s" % s.axe
      print "Spear: %s" % s.spear
      print "Bow: %s" % s.bow
      print "Light: %s" % s.light
      print "Dark: %s" % s.dark
      print "Anima: %s" % s.anima
      print "Staff: %s" %  s.staff
      
      print "Kills: %s" % s.kills
      print "Exp: %s" % s.experience
      print "Level: %s" % s.level
      print "Items: %s" % s.items
      print "Equipped weapon: %s" % s.equippedWeapon
      print "Promote class: %s" % s.promotedcls
      print "Portrait: %s" % s.portraitFile
      print "Sprite: %s" %  s.spriteFile

   def writeBasicStats( s ):
      print "Name: %s" % s.name
      print "Class: %s" % s.cls
      print "Max HP: %s" % s.maxhp
      print "Strength: %s" % s.strength
      print "Magic: %s" % s.magic
      print "Speed: %s" % s.speed
      print "Skill: %s" % s.skill
      print "Luck: %s" % s.luck
      print "Defense: %s" % s.defense
      print "Magic Defense: %s" % s.mdefense
      print "Exp: %s" % s.experience
      print "Level: %s" % s.level
