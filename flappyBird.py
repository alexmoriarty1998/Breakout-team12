# Sub Raizada		CSCI-C 200
# Flappy Bird final
# All the work herein is solely mine
#  except for some of the graphics, which come from closely observing the original
#  Flappy Bird game and from https://www.spriters-resource.com/resources/sheets/57/59894.png
# Also thanks to the Zombie Bird tutorial at http://www.kilobolt.com/introduction.html
#  for details about the original implementation

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 680

import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

###############################################################################
### constants #################################################################
###############################################################################
BIRD_RADIUS = 17
BIRD_DIAMETER = BIRD_RADIUS * 2
WALL_WIDTH = 64
CAP_HEIGHT = 30 # size of pipe caps
CAP_WIDTH = 4 # width increase at pipe caps
WALL_SPACING = 180 # horizontal spacing between walls
WALL_GAP = 176 # vertical hole in walls
WALL_BUFFER = 80 # minimum distance from wall hole to edge of screen
WALL_SPEED = -1 * 60
WORLD_BOT_PADDING = 102 # space used up by grass/sand part of background
BG_COLOR = (50, 200, 255)

BG_DAY_IMG = pygame.image.load("img\\bgDay.png")
BG_NIGHT_IMG = pygame.image.load("img\\bgNight.png")
PIPE_IMG = pygame.image.load("img\\pipe.png")
PIPE_CAP_TOP_IMG = pygame.image.load("img\\pipe_cap_top.png")
PIPE_CAP_BOT_IMG = pygame.image.load("img\\pipe_cap_bot.png")
BIRD_1_RISING_IMG = pygame.image.load("img\\bird1r.png").convert_alpha()
BIRD_1_NETURAL_IMG = pygame.image.load("img\\bird1n.png").convert_alpha()
BIRD_1_FALLING_IMG = pygame.image.load("img\\bird1f.png").convert_alpha()
BIRD_2_RISING_IMG = pygame.image.load("img\\bird2r.png").convert_alpha()
BIRD_2_NETURAL_IMG = pygame.image.load("img\\bird2n.png").convert_alpha()
BIRD_2_FALLING_IMG = pygame.image.load("img\\bird2f.png").convert_alpha()
BIRD_3_RISING_IMG = pygame.image.load("img\\bird3r.png").convert_alpha()
BIRD_3_NETURAL_IMG = pygame.image.load("img\\bird3n.png").convert_alpha()
BIRD_3_FALLING_IMG = pygame.image.load("img\\bird3f.png").convert_alpha()

###############################################################################
### class definitions #########################################################
###############################################################################
class Wall:
	WALL_COLOR = (0, 180, 0)

	def __init__(self, xPos):
		self.x = xPos
		self.top = random.randint(WALL_BUFFER, SCREEN_HEIGHT - WALL_BUFFER - WALL_GAP - WORLD_BOT_PADDING)
		self.bot = self.top + WALL_GAP
		self.scored = False # flip to true once bird has passed -> count score and set to false

	def update(self, dt):
		if not birdAlive:
			return
		if self.x <= -WALL_WIDTH:
			self.reset()
		self.x += WALL_SPEED * dt

	def reset(self):
		buffer = self.x + WALL_WIDTH
		self.x = buffer + 3*WALL_SPACING + 2*WALL_WIDTH
		self.top = random.randint(WALL_BUFFER, SCREEN_HEIGHT - WALL_BUFFER - WALL_GAP - WORLD_BOT_PADDING)
		self.bot = self.top + WALL_GAP

	def draw(self, screen):
		# draw main pipe
		for i in range(self.top):
			screen.blit(PIPE_IMG, (self.x, i))
		for i in range(self.bot, SCREEN_HEIGHT - WORLD_BOT_PADDING):
			screen.blit(PIPE_IMG, (self.x, i))
		# draw pipe caps
		# bird is oval but hitbox is circle... draw pipe gap as smaller than it is to minimize visually unexplainable deaths
		screen.blit(PIPE_CAP_TOP_IMG, (self.x - CAP_WIDTH, self.top - CAP_HEIGHT + 5))
		screen.blit(PIPE_CAP_BOT_IMG, (self.x - CAP_WIDTH, self.bot - 5))

class Bird:
	BIRD_COLOR = (255, 0, 0)

	GRAV_ACCEL = 1000
	MAX_SPEED = 450
	JUMP_SPEED = -1 * 425

	def __init__(self):
		self.x = int(SCREEN_WIDTH/8)
		self.y = int(SCREEN_HEIGHT/2)
		self.dy = 0
		self.rot = 0
		self.alive = True
		self.type = random.randint(1, 3)
		self.animState = 0

	def getImg(self):
		if self.type == 1:
			if self.animState == 1:
				return BIRD_1_RISING_IMG
			if self.animState == 0:
				return BIRD_1_NETURAL_IMG
			else: return BIRD_1_FALLING_IMG
		if self.type == 2:
			if self.animState == 1:
				return BIRD_2_RISING_IMG
			if self.animState == 0:
				return BIRD_2_NETURAL_IMG
			else: return BIRD_2_FALLING_IMG
		if self.type == 3:
			if self.animState == 1:
				return BIRD_3_RISING_IMG
			if self.animState == 0:
				return BIRD_3_NETURAL_IMG
			else: return BIRD_3_FALLING_IMG

	def update(self, dt):
		self.dy += self.GRAV_ACCEL* dt
		if self.dy >= self.MAX_SPEED:
			self.dy = self.MAX_SPEED
		self.y += self.dy * dt

		if self.y < BIRD_RADIUS - 5:
			self.y = BIRD_RADIUS - 5
			self.dy = 0

		# falling - rotate clockwise to 90 degrees beyond horizontal
		if self.dy >= 0:
			self.rot -= 480 * dt
			if self.rot < -90:
				self.rot = -90

		# rising - rotate clockwise to 20 degrees above horizontal
		if self.dy <= 200:
			self.rot += 480 * dt
			if self.rot > 20:
				self.rot = 20

		if self.dy < 0 or self.rot < 0:
			self.animState = -1
		elif self.dy >= 200:
			self.animState = 1
		else: self.animState = 0

		# kill self on contact with ground
		if self.y + BIRD_RADIUS > SCREEN_HEIGHT - WORLD_BOT_PADDING:
			self.kill()

	def flap(self):
		if self.alive:
			self.dy = self.JUMP_SPEED

	def draw(self, canvas):
		rotatedImg = pygame.transform.rotate(self.getImg(), self.rot)
		screen.blit(rotatedImg, (int(self.x - rotatedImg.get_width()/2), int(self.y - rotatedImg.get_height()/2)))

	def kill(self):
		self.alive = False
		global birdAlive
		birdAlive = False

###############################################################################
### global variables ##########################################################
###############################################################################
clock = pygame.time.Clock()
scoreFont = pygame.font.SysFont("monospace", 75, True)
textFont = pygame.font.SysFont("monospace", 35, True)
dayBG = False
timeToSwapBG = -1
score = 0
bird = Bird()
birdAlive = True
walls = []
def genWalls():
	for i in range(3):
		walls.append(Wall(int(SCREEN_WIDTH * (2/3)) + i * WALL_WIDTH + i * WALL_SPACING))
genWalls();

def reset():
	global walls, birdAlive, score
	bird.__init__()
	birdAlive = True
	walls = []
	genWalls()
	score = 0

###############################################################################
### collision detection #######################################################
###############################################################################
def dist(x1, y1, x2, y2):
	return ((x1-x2)**2 + (y1-y2)**2)*(1/2)

def collide(wall, bird):
	birdX = bird.x
	birdY = bird.y
	wallLeftX = wall.x
	wallRightX = wall.x + WALL_WIDTH
	wallTop = wall.top
	wallBot = wall.bot

	# case 1: bird is left of wall - must be within BIRD_RADIUS of wall for collision potential
	if wallLeftX - BIRD_RADIUS <= birdX < wallLeftX:
		# bird either is at same y as wall and partially inside, or clips a corner of the wall
		if birdY <= wallTop or birdY >= wallBot:
			bird.kill()
		if dist(birdX, birdY, wallLeftX, wallTop) <= BIRD_RADIUS or dist(birdX, birdY, wallLeftX, wallBot) <= BIRD_RADIUS:
			bird.kill()
	# case 2: bird is right of wall - very close to case 1
	if wallRightX < birdX <= wallRightX + BIRD_RADIUS:
		# bird either is at same y as wall and partially inside, or clips a corner of the wall
		if birdY <= wallTop or birdY >= wallBot:
			bird.kill()
		if dist(birdX, birdY, wallRightX, wallTop) <= BIRD_RADIUS or dist(birdX, birdY, wallRightX, wallBot) <= BIRD_RADIUS:
			bird.kill()
	# case 3: bird is between left/right bounds of pipe - collision if above/below gap in pipe
	if wallLeftX <= birdX <= wallRightX:
		if birdY < wallTop + BIRD_RADIUS or birdY > wallBot - BIRD_RADIUS:
			bird.kill()

###############################################################################
### scoring ###################################################################
###############################################################################
def checkScore(wall, bird):
	# if bird is alive and wall hasn't been counted yet and bird has passed through wall
	global score
	if bird.alive and not wall.scored and bird.x > wall.x + WALL_WIDTH / 2:
		score += 1
		wall.scored = True

def drawScore():
	# to create an outline around text, it is drawn multiple times, slightly shifted each time,
	# in the outline color, and the main text is finally drawn in its color at the center
	drawable = scoreFont.render(str(score), 1, (0, 0, 0))
	drawX = int(SCREEN_WIDTH/2 - drawable.get_width()/2)
	screen.blit(drawable, (drawX-1, 75-1))
	screen.blit(drawable, (drawX+1, 75+1))
	screen.blit(drawable, (drawX+1, 75-1))
	screen.blit(drawable, (drawX-1, 75+1))
	drawable = scoreFont.render(str(score), 1, (255, 255, 255))
	screen.blit(drawable, (drawX, 75))

def drawEndText():
	BASE = SCREEN_HEIGHT / 2 - 75
	SPACING = 10
	
	drawStr1 = "Oh no! Flappy"
	drawStr2 = "Bird failed! His"
	drawStr3 = "final score was " + str(score) + "."
	drawStr4 = "Press R to restart."
	
	drawable1 = textFont.render(drawStr1, 1, (0, 0, 0))
	drawable2 = textFont.render(drawStr2, 1, (0, 0, 0))
	drawable3 = textFont.render(drawStr3, 1, (0, 0, 0))
	drawable4 = textFont.render(drawStr4, 1, (0, 0, 0))
	drawX1 = int(SCREEN_WIDTH/2 - drawable1.get_width()/2)
	drawX2 = int(SCREEN_WIDTH/2 - drawable2.get_width()/2)
	drawX3 = int(SCREEN_WIDTH/2 - drawable3.get_width()/2)
	drawX4 = int(SCREEN_WIDTH/2 - drawable4.get_width()/2)
	height1 = drawable1.get_height()
	height22 = int(drawable2.get_height()/2)
	height3 = drawable1.get_height()
	
	screen.blit(drawable1, (drawX1 + 1, BASE - height22 - height1 - SPACING + 1))
	screen.blit(drawable1, (drawX1 - 1, BASE - height22 - height1 - SPACING + 1))
	screen.blit(drawable1, (drawX1 + 1, BASE - height22 - height1 - SPACING - 1))
	screen.blit(drawable1, (drawX1 - 1, BASE - height22 - height1 - SPACING - 1))
	screen.blit(drawable2, (drawX2 + 1, BASE - height22 + 1))
	screen.blit(drawable2, (drawX2 - 1, BASE - height22 + 1))
	screen.blit(drawable2, (drawX2 + 1, BASE - height22 - 1))
	screen.blit(drawable2, (drawX2 - 1, BASE - height22 - 1))
	screen.blit(drawable3, (drawX3 + 1, BASE + height22 + SPACING + 1))
	screen.blit(drawable3, (drawX3 - 1, BASE + height22 + SPACING + 1))
	screen.blit(drawable3, (drawX3 + 1, BASE + height22 + SPACING - 1))
	screen.blit(drawable3, (drawX3 - 1, BASE + height22 + SPACING - 1))
	screen.blit(drawable4, (drawX4 + 1, BASE + height22 + SPACING + height3 + SPACING * 8 + 1))
	screen.blit(drawable4, (drawX4 - 1, BASE + height22 + SPACING + height3 + SPACING * 8 + 1))
	screen.blit(drawable4, (drawX4 + 1, BASE + height22 + SPACING + height3 + SPACING * 8 - 1))
	screen.blit(drawable4, (drawX4 - 1, BASE + height22 + SPACING + height3 + SPACING * 8 - 1))

	drawable1 = textFont.render(drawStr1, 1, (255, 255, 255))
	drawable2 = textFont.render(drawStr2, 1, (255, 255, 255))
	drawable3 = textFont.render(drawStr3, 1, (255, 255, 255))
	drawable4 = textFont.render(drawStr4, 1, (255, 255, 255))
	screen.blit(drawable1, (drawX1, BASE - height22 - height1 - SPACING))
	screen.blit(drawable2, (drawX2, BASE - height22))
	screen.blit(drawable3, (drawX3, BASE + height22 + SPACING))
	screen.blit(drawable4, (drawX4, BASE + height22 + SPACING + height3 + SPACING * 8))
	
###############################################################################
### game loop #################################################################
###############################################################################
while(1):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			# exit shortcuts: escape, q, e, ctrl-w, or alt-f4 (only checks for w or f4, not the full combo)
			if event.key == pygame.K_ESCAPE or event.key == pygame.K_q or event.key == pygame.K_e or event.key == pygame.K_w or event.key == pygame.K_F4:
				sys.exit()
			if event.key == pygame.K_SPACE:
				bird.flap()
			if event.key == pygame.K_r:
				reset()
		if event.type == pygame.MOUSEBUTTONDOWN:
			bird.flap()
	
	if birdAlive:
		timeToSwapBG -= 1/60.0
	if timeToSwapBG <= 0:
		dayBG = not dayBG
		timeToSwapBG = 18

	if dayBG:
		screen.blit(BG_DAY_IMG, (0, 0))
	else: screen.blit(BG_NIGHT_IMG, (0, 0))

	for i in walls:
		i.update(1/60.0)
		i.draw(screen)
		collide(i, bird)
		checkScore(i, bird)
	
	if birdAlive:
		drawScore()

	bird.update(1/60.0)
	bird.draw(screen)

	if not birdAlive:
		drawEndText()

	pygame.display.flip()
	clock.tick(60)
