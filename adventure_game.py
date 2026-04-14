# PURPOSE:
# My text-based adventure game involves the player exploring a forest
# and make choices that affect the outcome

# INPUTS:
# Player name
# Player choices (left/right, fight/run, etc.)

# OUTPUTS:
# Story progression
# Win or Lose outcome

# VARIABLES:
# player_name
# choice
# health
# game_over

# START
# ask player for name
# display welcome message

# set health to 100
# set game_over to False

# WHILE game_over is False
#     display story scenario (e.g. "You are in a dark forest")
#     ask player to choose direction (left or right)

#     IF player chooses left:
#        display "You encounter  a wolf"
#        ask player to fight or run

#        IF fight:
#           reduce health
#           IF health <= 0:
#              display "You Lost"
#              set game_over to True
#        ELSE:
#            display "You survived"

#        IF run:
#           display "You escaped safely"

#     IF player chooses right:
#        display "You found treasure"
#        display "You win!"
#        set game_over to True

# END