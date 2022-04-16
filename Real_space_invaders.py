######################################################
#              -- SPACE_INVADERS --                  #
#                                                    #
#            Author: Supragya Seth                   #
#                                                    #
#                                                    #
#                                                    #
#                                                    #
#                                                    #
######################################################

# Import Libraries
import pygame 

#sceen Constants

XMODE = 800
YMODE = 600
SHIPX = 100
SHIPY = 75
speedm = 0.6
speedp = 0.4

pygame.init()

# Game images
background = 'background.jpg'
bg = pygame.image.load(background)
bg = pygame.transform.scale(bg, (XMODE, YMODE))
defImg = 'defender.png'
defender = pygame.image.load(defImg)
defender = pygame.transform.scale(defender,(SHIPX, SHIPY))
missile = 'missile.png'
missile = pygame.image.load(missile)
missile = pygame.transform.scale(missile,(20, 40))
alien = 'alien.png'
alien = pygame.image.load(alien)
alien = pygame.transform.scale(alien,(40, 40))


# Lists
aliens = []
projectile = []

# Setup Screen
screen = pygame.display.set_mode((XMODE, YMODE))

# Ticks
clock = pygame.time.Clock()

#Classes
class Things:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Defender(Things):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

class Projectile(Things):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def draw(self, dt):
        super().draw()
        self.y -= speedm * dt

class Alien(Things):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        super().draw()
        self.y += 0.1

    def collision_test(self):
        for x in projectile:
            if (x.x < self.x + 40 and x.x > self.x - 40 and x.y < self.y + 40 and x.y > self.y - 40):
                projectile.remove(x)
                aliens.remove(self)



#Player spawn
defender = Defender(XMODE / 2, YMODE * 0.8, defender)

#Enemy spawn
margin = 30
width = 50

for x in range(margin, XMODE- margin, width):
    for y in range(margin, int(YMODE / 2), width):
        aliens.append(Alien(x, y, alien))

def displayText(text):
    font = pygame.font.SysFont('', 50)
    message = font.render(text, False, (255, 255, 255))
    screen.blit(message, (200, 160))

#Clock initializatiom
clock = pygame.time.Clock()

# game loop
running = True
while running:

    dt = clock.tick(60)

    screen.blit(bg,(0,0))
    defender.draw()

    for x in aliens:
        x.draw()
        x.collision_test()

    for x in projectile:
        x.draw(dt)

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        defender.x -= speedp * dt if defender.x > 20 else 0
    elif pressed[pygame.K_RIGHT]:
        defender.x += speedp * dt if defender.x < XMODE - 100 else 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE  :
            projectile.append(Projectile(defender.x + 15, defender.y - 40, missile))

    for Alien in aliens:
        Alien.draw()
        Alien.collision_test
        if Alien.y > YMODE -150:
            displayText("GAME OVER")

    if len(aliens) <= 0:
        displayText("YOU WIN")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()