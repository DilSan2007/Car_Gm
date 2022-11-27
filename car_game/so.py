import pygame
import random
import time

W = 1020
H = 720
FPS = 68

# Окно =======================================================
pygame.init()
pygame.mixer.init()
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
# Звук =======================================================
pygame.mixer.music.load('music/cars.mp3')
# Grafic ======================================================
car_img = pygame.image.load('img/super_car1.png')
bg_img = pygame.image.load('img/way.jpg')
bad_cars = ['img/car1.png', 'img/car2.png', 'img/uaz.png', 'img/slize.png', 'img/super_car1.png',
 'img/super_car2.png', 'img/super_car3.png', 'img/super_car5.png']
# Menu Grafic =================================================
bg_menu = pygame.image.load('img/start_fone.jpg')
start_btn = pygame.image.load('img/start.jpg')
exit_btn = pygame.image.load('img/exit.jpg')
shop_btn = pygame.image.load('img/shop.jpg')
maps_btn = pygame.image.load('img/maps.jpg')
restart_btn = pygame.image.load('img/restart.png')
back_btn = pygame.image.load('img/back.png')
# SHOP ================================================== SHOP
car1 = pygame.image.load('img/super_car1.png')
car2 = pygame.image.load('img/super_car2.png')
car3 = pygame.image.load('img/super_car3.png')
car4 = pygame.image.load('img/car1.png')
car5 = pygame.image.load('img/car2.png')
car6 = pygame.image.load('img/slize.png')
car7 = pygame.image.load('img/uaz.png')
car8 = pygame.image.load('img/super_car4.png')
car9 = pygame.image.load('img/super_car5.png')
# Поворот =====================================================
car_up = car_img
car_left = pygame.transform.rotate(car_img, 4)
car_right = pygame.transform.rotate(car_img, -4)
# Money =======================================================
money_img = pygame.image.load('money/Sprite-1.png')

# SCREEN - 4 ============================================================================== 4
def shop():
    global car1, car2, car3, car4, car5, car6, car7, car8, car9
    global car_img, car_up, car_left, car_right
    global back_btn
    shop = True
    sc.fill((150, 150, 150))
    font = pygame.font.SysFont('Serif', 46)
    font2 = pygame.font.SysFont('Serif', 16)
    text = font.render('Выберите себе машину', True, (0, 255, 0))
    sc.blit(back_btn, (0, 0))
    backs = Button(0, 0, back_btn)
        
    sc.blit(text, (200, 40))
    carb1 = Button(50, 150, car1)
    carb2 = Button(150, 150, car2)
    carb3 = Button(250, 150, car3)
    carb4 = Button(350, 150, car4)
    carb5 = Button(450, 150, car5)
    carb6 = Button(550, 150, car6)
    carb7 = Button(650, 150, car7)
    carb8 = Button(750, 150, car8)
    carb9 = Button(850, 150, car9)
    sc.blit(car1, (50, 150))
    sc.blit(car2, (150, 150))
    sc.blit(car3, (250, 150))
    sc.blit(car4, (350, 150))
    sc.blit(car5, (450, 150))
    sc.blit(car6, (550, 150))
    sc.blit(car7, (650, 150))
    sc.blit(car8, (750, 150))
    sc.blit(car9, (850, 150))

    while shop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shop = False
                pygame.quit
            pos = pygame.mouse.get_pos()
            if backs.rect.collidepoint(pos): # ============================ MENU == ]
                if pygame.mouse.get_pressed()[0] == 1:
                    menu()
            if carb1.rect.collidepoint(pos): # ============================ 1
                if pygame.mouse.get_pressed()[0] == 1:
                    car.image = car1
                    car_up = car1
                    car_left = pygame.transform.rotate(car1, 4)
                    car_right = pygame.transform.rotate(car1, -4)
            if carb2.rect.collidepoint(pos): # ============================ 2
                if pygame.mouse.get_pressed()[0] == 1:
                    car.image = car2
                    car_up = car2
                    car_left = pygame.transform.rotate(car2, 4)
                    car_right = pygame.transform.rotate(car2, -4)
            if carb3.rect.collidepoint(pos): # ============================ 3
                if pygame.mouse.get_pressed()[0] == 1:
                    car.image = car3
                    car_up = car3
                    car_left = pygame.transform.rotate(car3, 4)
                    car_right = pygame.transform.rotate(car3, -4)
            if carb4.rect.collidepoint(pos): # ============================ 4
                if pygame.mouse.get_pressed()[0] == 1:
                    car.image = car4
                    car_up = car4
                    car_left = pygame.transform.rotate(car4, 4)
                    car_right = pygame.transform.rotate(car4, -4)
            if carb5.rect.collidepoint(pos): # ============================ 5
                if pygame.mouse.get_pressed()[0] == 1:
                    car.image = car5
                    car_up = car5
                    car_left = pygame.transform.rotate(car5, 4)
                    car_right = pygame.transform.rotate(car5, -4)
            if carb6.rect.collidepoint(pos): # ============================ 6
                if pygame.mouse.get_pressed()[0] == 1:
                    car.image = car6
                    car_up = car6
                    car_left = pygame.transform.rotate(car6, 4)
                    car_right = pygame.transform.rotate(car6, -4)
            if carb7.rect.collidepoint(pos): # ============================ 7
                if pygame.mouse.get_pressed()[0] == 1:
                    car.image = car7
                    car_up = car7
                    car_left = pygame.transform.rotate(car7, 4)
                    car_right = pygame.transform.rotate(car7, -4)
            if carb8.rect.collidepoint(pos): # ============================ 8
                if pygame.mouse.get_pressed()[0] == 1:
                    car.image = car8
                    car_up = car8
                    car_left = pygame.transform.rotate(car8, 4)
                    car_right = pygame.transform.rotate(car8, -4)
            if carb9.rect.collidepoint(pos): # ============================ 9
                if pygame.mouse.get_pressed()[0] == 1:
                    car.image = car9
                    car_up = car9
                    car_left = pygame.transform.rotate(car9, 4)
                    car_right = pygame.transform.rotate(car9, -4)
        
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
        if self.rect.right > 970:# W
            self.rect.right = 970
        if self.rect.left < 50: # 0
            self.rect.left = 50
    
# Враг ======================================================================== Mob
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        bad_car = random.choice(bad_cars)
        bot = pygame.image.load(bad_car)
        self.image = bot
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, 970)
        self.rect.y = random.randrange(-100, -99)
        self.speedy = random.randrange(2, 7)
       
    def update(self):
        global health, money
        self.rect.y += self.speedy
        if self.rect.top > H + 10:
            self.rect.x = random.randrange(50, 970)
            self.rect.y = random.randrange(-100, -99)
            self.speedy = random.randrange(2, 7)
        hits2 = pygame.sprite.spritecollide(car, mobs, False, pygame.sprite.collide_rect)
        if hits2:
            health -= 2
            car.rect.x -= 1
        if health == 0:
            pygame.mixer.music.stop()
            self.rect.x += 1000
            scene2()
# Монета ======================================================================= Money
class Money(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = money_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, 970)
        self.rect.y = random.randrange(-100, -99)
        self.speedy = random.randint(1, 5)

    def update(self):
        global money
        self.rect.y += self.speedy
        if self.rect.top > H + 10:
            self.rect.x = random.randrange(50, 970)
            self.rect.y = random.randrange(-100, -99)
            self.speedy = random.randint(1, 5)
        hits3 = pygame.sprite.spritecollide(car, mys, False, pygame.sprite.collide_rect)
        if hits3:
            self.rect.x += 10000
            money += 1
# Кнопка ======================================================================= Button
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        sc.blit(self.image, (self.rect.x, self.rect.y))

# SCREEN - 2 ==================================================================== 2
def scene2():
    global score, flLeft, flRight, count, game, health, money, restart_btn, back_btn
    lose = True
    clock.tick(FPS)
    sc.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 60)
    text = font.render('Вы Проиграли !', True, (255, 255, 255))
    text2 = font.render(f'score {score}', True, (255, 255, 255))
    text_money = font.render(f'Вы собрали {money} монет', True, (255, 255, 255))

    sc.blit(back_btn, (320, 430))
    sc.blit(restart_btn, (660, 430))
    backs = Button(320, 430, back_btn)
    restarts = Button(660, 430, restart_btn)
    sc.blit(text, (340, 200))
    sc.blit(text2, (360, 260))
    sc.blit(text_money, (300, 320))
    pygame.display.update()
    score, money = 0, 0

    while lose:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lose = False
                pygame.quit()
            pos = pygame.mouse.get_pos()
            if restarts.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    health = 200
                    car.rect.centerx = W / 2
                    car.rect.bottom = H / 1.8
                    flLeft = flRight = False
                    game = True
                    scene1()
            if backs.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    menu()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
mys = pygame.sprite.Group()
car = Car()
all_sprites.add(car)
n = 8
for i in range(n):
    time.sleep(2)
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
for i in range(4):
    time.sleep(2)
    my = Money()
    all_sprites.add(my)
    mys.add(my)

count = -5000
camera_x = 0
game = True
score = 0
flLeft = flRight = False
health = 200
money = 0

# SCREEN - 1 ============================================================================= 1
def scene1():
    global flLeft, flRight, score, count, camera_x, n, health, money
    left = pygame.image.load('btn/left.png')
    right = pygame.image.load('btn/right.png')
    lefts = Button(50, 590, left)
    rights = Button(870, 590, right)
    game = True
    pygame.mixer.music.play(-1)
    while game:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            pos = pygame.mouse.get_pos()
            if lefts.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    flLeft = True
                    car.image = car_left
            if rights.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    flRight = True
                    car.image = car_right
            if pygame.mouse.get_pressed()[0] == 0:
                flLeft = flRight = False
                car.image = car_up 
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
                
        all_sprites.update()
        if money == 100:
            score += 1500
            money = 0
        if game == True:
            score += 1
            f1 = pygame.font.SysFont('arial', 30)
            text = f1.render(f'score {score}', True, (50, 255, 50))
            text2 = f1.render(f'Money: {money}', True, (20, 255, 20))
        if car.rect != 0:
            count += 25
            if count >= 70:
                count = -5000

        sc.blit(bg_img, (camera_x, count))
        sc.blit(left, (50, 590))
        sc.blit(right, (870, 590))
        all_sprites.draw(sc)
        sc.blit(text, (10, 10))
        sc.blit(text2, (W / 2, 10))
        pygame.draw.rect(sc, (255, 0, 0), [800, 10, 200, 10])
        pygame.draw.rect(sc, (0, 255, 0), [800, 10, health, 10])
        pygame.display.flip()

    pygame.quit()

# SCREEN - 3 ================================================================================== 3
def menu():
    global flLeft, flRight, bg_menu, start_btn, exit_btn, shop_btn, maps_btn
    carry = car.image
    menu = True
    sc.blit(bg_menu, (0, 0))
    pygame.draw.rect(sc, (150, 150, 150), [718, 194, 120, 200])
    sc.blit(carry, (756, 240))
    
    sc.blit(start_btn, (40, 120))
    sc.blit(maps_btn, (40, 240))
    sc.blit(shop_btn, (40, 360))
    sc.blit(exit_btn, (40, 480))

    starts = Button(40, 120, start_btn)
    maps = Button(40, 240, maps_btn)
    shops = Button(40, 360, shop_btn)
    exits = Button(40, 480, exit_btn)
        
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                pygame.quit
            pos = pygame.mouse.get_pos()
            if starts.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    scene1()
            if maps.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    mapb()
            if shops.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    shop()
            if exits.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.quit()

        pygame.display.flip()

# bg ====== shop ============== image ===================
b1 = pygame.image.load('img/way-bg.jpg')
b2 = pygame.image.load('img/way2-bg.jpg')
b3 = pygame.image.load('img/way3-bg.jpg')
b4 = pygame.image.load('img/way4-bg.jpg')

bg2 = pygame.image.load('img/way2.jpg')
bg3 = pygame.image.load('img/way3.jpg')
bg4 = pygame.image.load('img/way4.jpg')
def mapb():
    global bg_img, back_btn
    map = True

    sc.fill((100, 100, 100))

    while map:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                map = False
                pygame.quit()

        sc.blit(back_btn, (0, 0)) # =====
        sc.blit(b1, (0, 140))
        sc.blit(b2, (250, 140))
        sc.blit(b3, (500, 140))
        sc.blit(b4, (750, 140))
        backs = Button(0, 0, back_btn) # ======
        bb1 = Button(0, 140, b1)
        bb2 = Button(250, 140, b2)
        bb3 = Button(500, 140, b3)
        bb4 = Button(750, 140, b4)
        
        pygame.display.flip()

        pos = pygame.mouse.get_pos()
        if backs.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                menu()
        if bb1.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                bg_img = b1
        if bb2.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                bg_img = bg2
        if bb3.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                bg_img = bg3
        if bb4.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                bg_img = bg4

menu()