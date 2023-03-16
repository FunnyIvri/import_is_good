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
        self.player = pygame.image.load("player.png").convert()
        self.player = pygame.transform.scale(self.player, size)
        self.player_rect = self.player.get_rect()
        self.player_rect.center = pos

#no need for class just assign
#class Other_space_class:
player = Player_creator("player.png", [100, 100], [400, 400], 10)
bulletlist = []
run = True
while run:

    root.fill("black")
    root.blit(text, textRect)
    textRect.center = (60, 60)
    player.show()

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
                newbullet.bulletpos[1] = player.player_rect.centery
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
