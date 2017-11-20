# class that holds the game state

# TODO: complete everything listed below

# this class will hold:
# bricks: list of instances of class Brick
# paddle: instance of class Paddle
# ball: instance of class Ball
# displayables: list of instances of class Displayable
# score: int

# init function should take in:
# list of Bricks, score
# init function should generate:
# paddle pos (based off of constants in GameConstants)
# ball initial x/y:
#   x is center of screen, y is random
# ball initial dx/dy (random)



# classes that need to be made (these go into the gameClasses folder):
# Position: stores x, y: float; also used as a general (x, y) storage class
# Velocity: stores dx, dy: float
# Animation: stores image (or images) along with image width/height
# HitBox: extends Position; additionally stores a width and height: int
# HitCircle: extends Position; additionally stores a radius: int
# each game object class (brick, paddle, ball) contains some of these classes
# for example, the Brick class will have a Position and Animation component
# making hitbox/hitcircle extend position is so that the Velocity class can apply to them
#   the getPosition() method will return a Position, that is incremented by dx/dy from Velocity
#   this allows it to also return a hitbox or hitcircle

# game class definitions (also go in gameClasses):
# Ball:
#  HitCircle, Velocity, Animation
# Paddle:
#  HitBox, Velocity, Animation
#    should paddles be able to move vertically?
# Brick:
#  HitBox, Animation
#    bricks don't have velocity
# Displayable:
#  Position, Velocity, Animation, lifespan: int
#    used for various graphical effects
#    e.g. bricks shattering and falling after being destroyed
#    lifespan counts down to 0, then object is removed
#      or set it to -1 for permanent lifespan
