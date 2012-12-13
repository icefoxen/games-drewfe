# team.rb
# A team represents a collection of units, their alignment, statistics,
# all that good stuff.  All units from the same team go on the same turn.


ALIGN_PLAYER = 0
ALIGN_ENEMY = 1
ALIGN_NEUTRAL = 2
ALIGN_ALLY = 3

class Team
	def initializer
		@name = ''
		@banner = 0
		@alignment = ALIGN_PLAYER
		@units = []
		@castle = 0
	end
end
