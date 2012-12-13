#
# config.py
#
# Config file object, loading routines, info access, all that fun stuff.
# I think we'll stick to YAML, kthx.  I'm leaving the XML stuff here
# just in case we ever need it, eg for conversations.
#
# Simon Heath
# 15/9/2005


import syck

# This really just handles the yaml loading with syck, and hangs onto
# the table.  Python tables are plenty capable for what we want here.
# Yum.
class ConfigLoader:
   tree = {}
   cfgfile = ""
   def __init__( s, cfgfile ):
      s.cfgfile = cfgfile
      
      f = open( cfgfile, 'r' )
      data = f.read()
      f.close()
      
      s.tree = syck.load( data )

   def __contains__( s, d ):
      return s.tree.__contains__( d )

   def __getitem__( s, d ):
      return s.tree[d]

   def getTree( s ):
      return s.tree

   def write( s ):
      print s.tree

   

## from xml.sax import *

## class ConfigHandler( ContentHandler ):
##    table = {}

##    def startDocument( s ):
##       print "Parsing config file..."
      
##    def endDocument( s ):
##       print "Done parsing config file"

##    def startElement( s, name, attrs ):
##       for x, y in attrs.items():
##          s.table[name + "." + x] = y

##    def __getitem__( s, i ):
##       s.table[i]

##    def __contains__( s, i ):
##       s.table.__contains__( i )

##    def write( s ):
##       print s.table


   
## h = ConfigHandler()
## parse( "foo.xml", h )
## h.write()


