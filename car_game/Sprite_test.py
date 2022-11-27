import pygame
import random
from random import randint

pygame.init()

W = 1020
H = 720
FPS = 70

RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Звук =======================================================
pygame.mixer.music.load('music/cars.mp3')
# Окно =======================================================
pygame.init()
pygame.mixer.init()
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
# Grafic ======================================================
car_img = pygame.image.load('img/super_car1.png')
bg_img = pygame.image.load('img/way.jpg')
bad_cars = ['img/car1.png', 'img/car2.png', 'img/uaz.png', 'img/slize.png', 'img/super_car1.png',
 'img/super_car2.png', 'img/super_car3.png']
# Menu Grafic =================================================
bg_menu = pygame.image.load('img/start_fone.jpg')
start_btn = pygame.image.load('img/start.jpg')
exit_btn = pygame.image.load('img/exit.jpg')
shop_btn = pygame.image.load('img/shop.jpg')
# SHOP ================================================== SHOP
car1 = pygame.image.load('img/super_car1.png')
car2 = pygame.image.load('img/super_car2.png')
car3 = pygame.image.load('img/super_car3.png')
car4 = pygame.image.load('img/car1.png')
car5 = pygame.image.load('img/car2.png')
car6 = pygame.image.load('img/slize.png')
car7 = pygame.image.load('img/uaz.png')
car8 = pygame.image.load('img/super_car4.png')
# Поворот =====================================================
car_up = car_img
car_left = pygame.transform.rotate(car_img, 4)
car_right = pygame.transform.rotate(car_img, -4)

# SCREEN - 4 ============================================================================== 4
def shop():
    global car1, car2, car3, car4, car5, car6, car7, car8
    global car_img, car_up, car_left, car_right
    shop = True
    sc.fill((150, 150, 150))
    font = pygame.font.SysFont('Serif', 46)
    font2 = pygame.font.SysFont('Serif', 16)
    text = font.render('Чтобы выбран машину нажмите на клавишу:__', True, (0, 255, 0))
    
    ter1 = font2.render(f'клавишу: {1}', True, (0, 255, 0))
    ter2 = font2.render(f'клавишу: {2}', True, (0, 255, 0))
    ter3 = font2.render(f'клавишу: {3}', True, (0, 255, 0))
    ter4 = font2.render(f'клавишу: {4}', True, (0, 255, 0))
    ter5 = font2.render(f'клавишу: {5}', True, (0, 255, 0))
    ter6 = font2.render(f'клавишу: {6}', True, (0, 255, 0))
    ter7 = font2.render(f'клавишу: {7}', True, (0, 255, 0))
    ter8 = font2.render(f'клавишу: {8}', True, (0, 255, 0))

    sc.blit(ter1, (40, 270))
    sc.blit(ter2, (140, 270))
    sc.blit(ter3, (240, 270))
    sc.blit(ter4, (340, 270))
    sc.blit(ter5, (440, 270))
    sc.blit(ter6, (540, 270))
    sc.blit(ter7, (640, 270))
    sc.blit(ter8, (740, 270))
        
    sc.blit(text, (20, 40))
    sc.blit(car1, (50, 150))
    sc.blit(car2, (150, 150))
    sc.blit(car3, (250, 150))
    sc.blit(car4, (350, 150))
    sc.blit(car5, (450, 150))
    sc.blit(car6, (550, 150))
    sc.blit(car7, (650, 150))
    sc.blit(car8, (750, 150))

    while shop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shop = False
                pygame.quit
            key = pygame.key.get_pressed()
            if key[pygame.K_q]:
                menu()
            if key[pygame.K_1]:
                car.image = car1
                car_up = car_img
                car_left = pygame.transform.rotate(car_img, 4)
                car_right = pygame.transform.rotate(car_img, -4)
            if key[pygame.K_2]:
                car.image = car2
                car_up = car2
                car_left = pygame.transform.rotate(car2, 4)
                car_right = pygame.transform.rotate(car2, -4)
            if key[pygame.K_3]:
                car.image = car3
                car_up = car3
                car_left = pygame.transform.rotate(car3, 4)
                car_right = pygame.transform.rotate(car3, -4)
            if key[pygame.K_4]:
                car.image = car4
                car_up = car4
                car_left = pygame.transform.rotate(car4, 4)
                car_right = pygame.transform.rotate(car4, -4)
            if key[pygame.K_5]:
                car.image = car5
                car_up = car5
                car_left = pygame.transform.rotate(car5, 4)
                car_right = pygame.transform.rotate(car5, -4)
            if key[pygame.K_6]:
                car.image = car6
                car_up = car6
                car_left = pygame.transform.rotate(car6, 4)
                car_right = pygame.transform.rotate(car6, -4)
            if key[pygame.K_7]:
                car.image = car7
                car_up = car7
                car_left = pygame.transform.rotate(car7, 4)
                car_right = pygame.transform.rotate(car7, -4)
            if key[pygame.K_8]:
                car.image = car8
                car_up = car8
                car_left = pygame.transform.rotate(car8, 4)
                car_right = pygame.transform.rotate(car8, -4)
        
        pygame.display.update()

# Игрок ======================================================================= Car
class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = car_img
        self.rect = self.image.get_rect()
        self.rect.centerx = W / 2
        self.rect.bottom = H / 1.8

    def update(self):
        if flLeft:
            car.rect.x -= 5
        if flRight:
            car.rect.x += 5
        if self.rect.right > W:
            self.rect.right = W
        if self.rect.left < 0:
            self.rect.left = 0
    
# Враг ======================================================================== Mob
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        bad_car = random.choice(bad_cars)
        bot = pygame.image.load(bad_car)
        self.image = bot
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W - self.rect.width)
        self.rect.y = random.randrange(-100, -99)
        self.speedy = random.randrange(2, 7)
       
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > H + 10:
            self.rect.x = random.randrange(W - self.rect.width)
            self.rect.y = random.randrange(-100, -99)
            self.speedy = random.randrange(2, 7)
        hits2 = pygame.sprite.spritecollide(car, mobs, False)
        if hits2:
            pygame.mixer.music.stop()
            self.rect.x += 1000
            scene2()

# SCREEN - 2 ==================================================================== 2
def scene2():
    global score, flLeft, flRight, count, game
    lose = True
    clock.tick(FPS)
    sc.fill(BLACK)
    font = pygame.font.SysFont('arial', 60)
    text = font.render('Вы Проиграли !', True, (255, 255, 255))
    text2 = font.render(f'score {score}', True, (255, 255, 255))
    btn_restart = font.render('restart', True, (0, 255, 0))

    sc.blit(text, (360, 300))
    sc.blit(text2, (380, 360))
    pygame.display.update()
    score = 0

    while lose:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lose = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    car.rect.centerx = W / 2
                    car.rect.bottom = H / 1.8
                    flLeft = flRight = False
                    game = True
                    scene1()
                if event.key == pygame.K_q:
                    menu()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
car = Car()
all_sprites.add(car)
n = 8
for i in range(n):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

count = -5000
camera_x = 0
game = True
score = 0
flLeft = flRight = False

# SCREEN - 1 ============================================================================= 1
def scene1():
    global flLeft, flRight, score, count, camera_x, n
    game = True
    pygame.mixer.music.play(-1)
    while game:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    flLeft = True
                    car.image = car_left
                elif event.key == pygame.K_RIGHT:
                    flRight = True
                    car.image = car_right
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    flLeft = flRight = False
                    car.image = car_up 
                if event.key == pygame.K_q:
                    pygame.mixer.music.stop()
                    menu()
                
        all_sprites.update()
        if game == True:
            score += 1
            f1 = pygame.font.SysFont('arial', 30)
            text = f1.render(f'score {score}', True, (0, 0, 0))
        if car.rect != 0:
            count += 25
            if count >= 70:
                count = -5000

        sc.blit(bg_img, (camera_x, count))
        all_sprites.draw(sc)
        sc.blit(text, (10, 10))
        pygame.display.flip()

    pygame.quit()

# SCREEN - 3 ================================================================================== 3
def menu():
    global flLeft, flRight, bg_menu, start_btn, exit_btn, shop_btn
    menu = True
    sc.blit(bg_menu, (0, 0))

    pygame.draw.rect(sc, (0, 0, 0), [40, 150, 300, 100])
    sc.blit(start_btn, (40, 150))

    pygame.draw.rect(sc, (0, 0, 0), [40, 300, 300, 100])
    sc.blit(shop_btn, (40, 300))

    pygame.draw.rect(sc, (0, 0, 0), [40, 450, 300, 100])
    sc.blit(exit_btn, (40, 450))
    

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                pygame.quit
            key = pygame.key.get_pressed()
            if key[pygame.K_s]:
                m.rect.x += 1000
                car.rect.centerx = W / 2
                car.rect.bottom = H / 1.8
                flLeft = flRight = False
                scene1()
            if key[pygame.K_a]:
                shop()
            if key[pygame.K_d]:
                pygame.quit()
            

        pygame.display.flip()

menu()