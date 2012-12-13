#!/usr/bin/env ruby
# drewfe.rb
# This is the startup file for DrewFE.
# Run this.

require 'sdl'

require 'driver'

def run
   SDL.init( SDL::INIT_EVERYTHING )
   SDL::WM::setCaption( 'DrewFE', '' )

   screen = SDL::setVideoMode( 800, 600, 16, SDL::SWSURFACE )

   driver = Driver.new( screen )
   driver.mainloop

   #

end

run
