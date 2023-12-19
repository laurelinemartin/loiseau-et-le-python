+###############################
#### L'Oiseau et le Python ####
####     Stage Ete 2022    ####
####    Laureline Martin   ####
###############################
import random  
import sys 
import pygame
from pygame.locals import * 

class Pipe():
	x = 600
	y = 0
	width = 40
	height = 0
	move = 7
	window = None
	color = (0, 255, 0)
	def __init__(self, window, x):
		self.x = x
		self.height = random.randint(110, 300)
		self.window = window
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def getWidth(self):
		return self.width
	def getHeight(self):
		return self.height
	def setX(self, x):
		self.x = x
	def setHeight(self, height):
		self.height = height
	def movePipe(self):
		self.setX(self.x-self.move)
		pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
	def isOut(self):
		if self.x + self.width < 0:
			return True
		return False

class Bird():
	x = 120
	y = 300
	size = 20
	color = (255, 0, 0)
	elevation = 30
	fall_velocity = 2
	window = None
	def __init__(self, y, window):
		super(Bird, self).__init__()
		self.y = y
		self.window = window
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def getSize(self):
		return self.size
	def draw(self):
		#pygame.draw.circle(self.window, (0,0,0), (self.x, self.y+self.elevation), self.size)
		pygame.draw.circle(self.window, self.color, (self.x, self.y), self.size)
	def jump(self):
		self.y = self.y - self.elevation
		#self.draw()
	def fall(self):
		self.y = self.y + self.fall_velocity

def isGameOver(bird, pipe):
	if bird.getY()-bird.getSize() < pipe.getHeight() and bird.getX()+bird.getSize() > pipe.getX() and bird.getX()-bird.getSize() < pipe.getX()+pipe.getWidth():
		return True
	if bird.getY()+bird.getSize() > HEIGHT or bird.getY()-bird.getSize()<0 :
		return True
	return False

def plus1(bird, pipe): 
	if bird.getY()-bird.getSize() > pipe.getHeight() and bird.getX()+bird.getSize() > pipe.getX() and bird.getX()-bird.getSize() < pipe.getX()+pipe.getWidth():
		return True
	return False

#Variables 
WIDTH = 600
HEIGHT = 499
FRAME_CLOCK = pygame.time.Clock()

score = 0
run = True
saut = False
framepersecond = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))   
window.fill((0,0,0))
pygame.display.set_caption('Flappy Bird') 
pygame.init()  
framepersecond_clock = pygame.time.Clock()
bird = Bird(300, window)
pipe1 = Pipe(window, 600)
pipe2 = Pipe(window, 800)
pipe3 = Pipe(window, 1000)

pipes = {pipe1, pipe2, pipe3}

while run:
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			run = False
		elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
			saut = True
			bird.jump()
	if saut == True:
		bird.fall()
	for pipe in pipes:
		if pipe.isOut():
			pipe.setX(WIDTH)
			pipe.setHeight(random.randint(110, HEIGHT-3*bird.getSize()))
		if isGameOver(bird, pipe):
			run = False
		if plus1(bird, pipe):
			score += 1

	window.fill((0,0,0))
	bird.draw()
	for pipe in pipes:
		pipe.movePipe()
	pygame.display.update()
	framepersecond_clock.tick(framepersecond)

print("Score : {0}".format(score))
pygame.quit()
