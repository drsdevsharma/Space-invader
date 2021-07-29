# Import libarbry
import pygame
import math
import random

# Window of our game
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption(' Space Invader ')

# Window Background
Background = pygame.image.load("Background.png")
Background = pygame.transform.scale(Background,(800,620))


# Window icon 
icon = pygame.image.load("Space invader icon.png")
pygame.display.set_icon(icon)

# Player 
playerimg = pygame.image.load("Player.png")


Enemy_Red = pygame.image.load("Enemy red.png")
Enemy_Blue = pygame.image.load("Enemy blue.png")
Enemy_Green = pygame.image.load("Enemy green.png")
Enemy_Purple = pygame.image.load("Enemy purple.png")


# Bullet
class bullet:
	def __init__(self, x , y ):
		self.x = x
		self.y = y
		self.Bulletimg = pygame.image.load("Bullet.png")
	
	def Draw( self ,x ,y):
		screen.blit( self.Bulletimg ,(x,y))
	
	def move( self , BulletY_change):
		self.y += BulletY_change

# Enemy
class enemy:
	color_map = {
	"Red": Enemy_Red,
	"Blue": Enemy_Blue,
	"Green": Enemy_Green,
	"Purple": Enemy_Purple 
	}
	def __init__(self, x , y , color):
		self.x = x
		self.y = y 
		self.color = color
	
	def Draw(self):
		enemyimg = self.color_map[self.color]
		screen.blit(enemyimg , (self.x ,self.y))

	def move(self , enemy_change):
		self.y += enemy_change

# Function
def player( x , y):
	screen.blit( playerimg,(x,y))


def Collide(enemyx , enemyy , bulletx ,bullety):
	dist = math.sqrt(math.pow(enemyx - bulletx , 2) + math.pow(enemyy - bullety , 2))
	if dist < 30:
		return True
	else:
		return False

# Main function
def main():

	# Variables 
	playerX = 370
	playerY = 512
	playerX_change = 0
	Bullets = []
	Bullet_change = 4
	Enemys = []
	Enemy_change = 1.5
	Score = 0 
	Level = 1
	Lives = 3
	run = True
	count = 0 


	while run :
		screen.fill((0,0,0))             # Fill the screen with Black color
		screen.blit(Background, (0,0))   # Draw the Backgorund image
			
		if  len(Bullets) <= 0:           # Initilize Bullets for player
			px =64
			Bullet_len = 8
			for i in range(Bullet_len):
				Bullet = bullet(playerX + 16 , 560 + px*i)
				Bullets.append(Bullet)
		if len(Bullets) == count:
			hwk = 1
			for BulleT in Bullets:
				if BulleT.y == 560 and hwk == 1:
					print("CHutiya h tu")
					hwk = 0
					count = 0
		


		if len(Enemys) <= 0:  
			if (Score // 20) == 0:
				Level += 1  
         # Initilize Enemys   
			for i in range(5 * Level):
				Enemy = enemy(random.randrange(0,740), random.randrange(-1000 , -100) , random.choice(["Blue","Red","Green","Purple"]))
				Enemys.append(Enemy)
	

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					playerX_change = -4
				if event.key == pygame.K_RIGHT:
					playerX_change = 4
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
					playerX_change = 0
		for Enemy in Enemys[:]:
			if Collide(playerX , playerY , Enemy.x ,Enemy.y):
				Lives -= 1
				Enemys.remove(Enemy)
			if Enemy.y >= 600:
				Lives -= 1
				Enemys.remove(Enemy)
			else:
				for Bullet in Bullets[:]:
					Collision = Collide(Enemy.x , Enemy.y , Bullet.x , Bullet.y)
					if Collision:
						Score += 1
						Enemys.remove(Enemy)
						Bullets.remove(Bullet)
						count = len(Bullets)
						Bullet = bullet(playerX + 16 , Bullet.y)
						Bullets.append(Bullet)
					

		playerX += playerX_change

		# Boundries
		if playerX < 0:
			playerX = 0
		elif playerX > 736:
			playerX = 736

		player( playerX ,playerY)

		# Try to counter overlap problem
		# Draw Enemys 
		for i in range(len(Enemys)):
			if Enemys[i].y >= 0:
				Enemys[i].Draw()
			Enemys[i].move(Enemy_change)
		
		for i in range(len(Bullets)):
			if Bullets[i].y == 500:
				Bullets[i].x = playerX + 16
			BulletX = Bullets[i].x
			BulletY = Bullets[i].y
			if BulletY <= 10:
				Bullets[i].x = playerX + 16
				Bullets[i].y = 500
			if BulletY <= 500:
				Bullets[i].Draw(BulletX , BulletY)
			Bullets[i].move( -Bullet_change )


		if Lives == 0 :
			print(Score)
			run = False
		pygame.display.update()

main()