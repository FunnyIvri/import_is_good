import pygame
import keyboard
pygame.font.init()
root_size = (800, 800)
root = pygame.display.set_mode(root_size)
shoots_fired = False
speed = 10
font = pygame.font.SysFont("inkfree", 60)
text = font.render("hello", True, "white")
textRect = text.get_rect()
clock = pygame.time.Clock()
class Bullet_creator:

    def __init__(self,size, pos):
        self.bulletpos = pos

        self.bullet_size = size
def showbullet(bulletlist):
     i = 0
     while i < len(bulletlist) - 1:
         if bulletlist[i].bulletpos[1] == -100:
             del bulletlist[i]
         bulletlist[i].bulletpos[1] = bulletlist[i].bulletpos[1] - player.speed
         pygame.draw.rect(root, "red", (bulletlist[i].bulletpos, bulletlist[i].bullet_size))

         i = i + 1

class Player_creator:

    def show(self):
       root.blit(self.player, self.player_rect)

    def __init__(self, image, size, pos, speed):
        self.image = image
        self.size = size
        self.pos = pos
        self.speed = speed
        self.player = pygame.image.load(image).convert()
        self.player = pygame.transform.scale(self.player, size)
        self.player_rect = self.player.get_rect()
        self.player_rect.center = pos

class Ship_creator:
    def __init__(self, image, size, pos):
        self.image = image
        self.size = size
        self.ship = pygame.image.load(image).convert()
        self.ship = pygame.transform.scale(self.ship, size)
        self.ship = pygame.transform.rotate(self.ship,180)
        self.ship_rect = self.ship.get_rect()
        self.ship_rect.center = pos
def showships(ships,root):
    for ship in ships:
        root.blit(ship.ship, ship.ship_rect)

ships = []
shipx = 0
for i in range(5):

    ship = Ship_creator("ship.png", [150,150], [shipx, 100])
    ships.append(ship)
    
    shipx = shipx + 150
player = Player_creator("player.png", [100, 100], [400, 400], 10)
bulletlist = []
run = True
while run:

    root.fill("black")
    showships(ships, root)
    root.blit(text, textRect)
    textRect.center = (60, 60)
    player.show()
    for ship in ships:

        x = ship.ship_rect.x
        y = ship.ship_rect.y


        if ship.ship_rect.left <= 0 or ship.ship_rect.right >= root_size[0]:
            y = y-10
            x = 0
        ship.ship_rect.x = x
        ship.ship_rect.y = y
    if keyboard.is_pressed("a"):
        player.pos[0] = player.pos[0] - player.speed
        player.player_rect.center = player.pos
    elif keyboard.is_pressed("d"):
        player.pos[0] = player.pos[0] + player.speed
        player.player_rect.center = player.pos
    if shoots_fired:
       showbullet(bulletlist)
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            keyname = pygame.key.name(event.key)
            if keyname == "space":
                newbullet = Bullet_creator([25,25],[-100,100])
                newbullet.bulletpos[0] = player.player_rect.centerx - 32
                newbullet.bulletpos[1] = player.player_rect.top
                print(newbullet)
                bulletlist.append(newbullet)
                print(bulletlist)
                shoots_fired = True
        if event.type == pygame.QUIT:
            run = False

    #add update
    pygame.display.update()
    clock.tick(10)
pygame.quit()
