# driver.rb
# This contains the "driver" class, which holds all the local data for a game
# instance, does the mainloop, handles input and in general brings everything 
# together.

require 'input'


class Driver
   def initialize( screen )
      @screen = screen
      @input = 0
      @map = 0

      @continue = true

      print "Driver initialized\n"
   end

   def handleEvents 
      while event = SDL::Event2.poll
         case event
         when SDL::Event2::KeyDown
            case event.sym
            when UP_BUTTON
               print "Up!\n"
            when DOWN_BUTTON
               print "Down!\n"
            when LEFT_BUTTON
               print "Left!\n"
            when RIGHT_BUTTON
               print "Right!\n"

            when ACTION_BUTTON
               print "Action!\n"
            when BACK_BUTTON
               print "Back!\n"

            when SDL::Key::Q
               @continue = false
            end

         when SDL::Event2::Quit
            @continue = false 
         end
      end      
   end


   def mainloop
      currentColor = 0
      image = SDL::Surface.load( "images/tiletest.png" )
      while @continue
         handleEvents
         @screen.fillRect( 0, 0, 300, 300, currentColor )

         SDL.blitSurface2( image, [0,0,0,0], @screen, [currentColor,200] )


         @screen.flip
         currentColor = (currentColor + 1) % 500
      end
   end
end
