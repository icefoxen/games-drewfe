# input.rb
# A class to handle input-events in a fairly abstract manner.
# Or at least provide some key-bindings.
#
# Other keys: F1-F12 for save and load like VBA?
# Menu key?

require 'sdl'

UP_BUTTON = SDL::Key::UP
DOWN_BUTTON = SDL::Key::DOWN
LEFT_BUTTON = SDL::Key::LEFT
RIGHT_BUTTON = SDL::Key::RIGHT

ACTION_BUTTON = SDL::Key::Z
BACK_BUTTON = SDL::Key::X

