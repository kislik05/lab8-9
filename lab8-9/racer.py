import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ad_files/car1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 500

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ad_files/car2.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 540)
        self.rect.y = -60

class Coin100(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ad_files/100tg.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 540)
        self.rect.y = -60

class Coin200(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ad_files/200tg.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 540)
        self.rect.y = -60

player = Player()
enemies = pygame.sprite.Group()
enemies.add(Enemy())
coins = pygame.sprite.Group()
coins.add(Coin100())
coins.add(Coin200())

speed_ch = pygame.USEREVENT+1 # увелич. скорости
pygame.time.set_timer(speed_ch, 5000)

image = pygame.image.load("ad_files/200tg.png")
done = False
score = 0
C_one = 0
C_two= 0
w, h = image.get_size()
angle = 0
speed = 10 
pos = (screen.get_width() / 2, screen.get_height() / 2)

def blitRotate(surf, image, pos, originPos, angle):
   
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    rotated_offset = offset_center_to_pivot.rotate(angle)

    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    surf.blit(rotated_image, rotated_image_rect)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == speed_ch and speed <= 30:
            speed += 5

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and player.rect.y < 500:
        player.rect.y += 15
    if keys[pygame.K_UP] and player.rect.y > 0:
        player.rect.y -= 15
    if keys[pygame.K_RIGHT] and player.rect.x < 540:
        player.rect.x += 15
    if keys[pygame.K_LEFT] and player.rect.x > 0:
        player.rect.x -= 15

    for enemy in enemies:
        if enemy.rect.y > 600:
            enemy.rect.y = -60
            enemy.rect.x = random.randint(0, 540)
        enemy.rect.y += speed

    for coin in coins:
        if coin.rect.y > 600:
            coin.rect.y = -60
            coin.rect.x = random.randint(0, 540)
        coin.rect.y += 10

    # Проверка столкновений игрока с врагами
    if pygame.sprite.spritecollide(player, enemies, False):
        blitRotate(screen, image, pos, (w / 2, h / 2), angle)
        print("Столкновение с врагом!")
        done = True

    # Проверка столкновений игрока с монетками
    for coin in coins:
        if pygame.sprite.collide_rect(player, coin):
            if isinstance(coin, Coin100):
                C_one += 1
                score += 100
            elif isinstance(coin, Coin200):
                C_two += 1
                score += 200
            coin.rect.x = random.randint(0, 540)
            coin.rect.y = random.randint(0, 100)

    screen.fill((250, 250, 250))
    screen.blit(player.image, player.rect)

    enemies.draw(screen)
    enemies.update()

    coins.draw(screen)
    coins.update()

    pygame.display.flip()
    clock.tick(60)

print("Игра окончена! Ваш счет:", score)
print("Монеты в 100тг:", C_one, "штуки")
print("Монеты в 200тг:", C_two, "штуки")

pygame.quit()