import pygame, random

WIDTH = 280
HEIGHT = 550
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiditch")
clock = pygame.time.Clock()

def draw_text(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)



def draw_shield_bar(surface, x, y, percentage):
	BAR_LENGHT = 0
	BAR_HEIGHT = 0
	fill = int((percentage / 100) * BAR_LENGHT)
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

	


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("img/player.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH // 2
		self.rect.bottom = HEIGHT - 10
		self.speed_x = 0
		self.shield = 100

	def update(self):
		self.speed_x = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -5
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 5
		self.rect.x += self.speed_x
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0

'''
	def shoot(self):
		bullet = Bullet(self.rect.centerx, self.rect.top)
		all_sprites.add(bullet)
		bullets.add(bullet)
		#laser_sound.play()
'''
class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(meteor_images)
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-140, -100)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)

	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.top > HEIGHT + 10 or self.rect.left < -40 or self.rect.right > WIDTH + 40:
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-140, - 100)
			self.speedy = random.randrange(1, 10)
'''
class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("img/laser1.png")
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()
'''



def show_go_screen():
	screen.blit(background, [0,0])
	draw_text(screen, "Press Key", 20, WIDTH // 2, int(HEIGHT * 3/4))
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYUP:
				waiting = False


meteor_images = []
meteor_list = ["img/meteorGrey_big1.png"]
for img in meteor_list:
	meteor_images.append(pygame.image.load(img).convert())



# Cargar imagen de fondo
background = pygame.image.load("img/background.png").convert()


#pygame.mixer.music.play(loops=-1)

#### ----------GAME OVER
game_over = True
running = True
while running:
	if game_over:

		show_go_screen()

		game_over = False
		all_sprites = pygame.sprite.Group()
		meteor_list = pygame.sprite.Group()
		bullets = pygame.sprite.Group()

		player = Player()
		all_sprites.add(player)
		for i in range(8):
			meteor = Meteor()
			all_sprites.add(meteor)
			meteor_list.add(meteor)

		score = 0


	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.shoot()


	all_sprites.update()


	# Checar colisiones - jugador - meteoro
	hits = pygame.sprite.spritecollide(player, meteor_list, True)
	for hit in hits:
		player.shield -= 25
		meteor = Meteor()
		all_sprites.add(meteor)
		meteor_list.add(meteor)
		if player.shield <= 0:
			game_over = True

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	#Marcador
	draw_text(screen, str(score), 25, WIDTH // 2, 10)

	# Escudo.
	draw_shield_bar(screen, 5, 5, player.shield)

	pygame.display.flip()
pygame.quit()