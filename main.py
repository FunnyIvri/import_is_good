import pygame
import keyboard

# root setup
run = True
root_size = (400, 400)
root = pygame.display.set_mode(root_size)
# player setup
pos = [200, 200]
player_size = (100, 100)
# player sprite setup
player = pygame.image.load("player.png").convert()
player = pygame.transform.scale(player, player_size)
player_rect = player.get_rect()
player_rect.center = pos
x = root.blit(player, player_rect)
# bullet setup
bullet_size = (25, 25)
bulletpos = [200, 800]
shoots_fired = False
bullet = pygame.draw.rect(root, "red", (bulletpos, bullet_size))
# general setup
speed = 10
clock = pygame.time.Clock()

while run:
    if keyboard.is_pressed("a"):
        pos[0] = pos[0] - speed
        player_rect.center = pos
    elif keyboard.is_pressed("d"):
        pos[0] = pos[0] + speed
        player_rect.center = pos
    if shoots_fired:
        print(speed, pos)
        bulletpos[1] = bulletpos[1] - speed

    root.fill("black")

    root.blit(player, player_rect)
    bullet = pygame.draw.rect(root, "red", (bulletpos, bullet_size))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keyname = pygame.key.name(event.key)
            if keyname == "space":

                bulletpos[0] = player_rect.centerx
                bulletpos[1] = player_rect.centery
                bullet.centery = bullet.centery - 75
                bullet = pygame.draw.rect(root, "red", (bulletpos, bullet_size))
                shoots_fired = True
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(10)
pygame.quit()
