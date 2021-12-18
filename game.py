import pygame        #Цель игры - охранять город от вражеских боеголовок, посредством запуска своих, управляя ракетницей стрелками и стреляя на Q(дальный выстрел) и W(ближний выстрел)
import sys          #За попадания очки добавляются, за пропущенные рокеты - уменьшаюся. При отрицательном счёте игра оканчивается
import random
import os    #для более универсального пути к ассету(работает на любой ОС)
pygame.font.init()    #для последующей вставки текста
shir = 1024
vuisota = 768     #переменные для разрешения
vecherneenebo = (100, 50, 255)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)   #задаю цвета, что бы потом к ним было бы проще обращаться
score = 0 #счётчик очков
pygame.init()
screen = pygame.display.set_mode((shir, vuisota))  #задаю разрешение
pygame.display.set_caption("Missle Command Project")   #имя окна
clock = pygame.time.Clock()
rocketnotnormal = pygame.image.load(os.path.join('rocket.png')) #загружаем спрайт ракеты
rocketflipped = pygame.transform.scale(rocketnotnormal, (30, 30))  #уменьшаем её
rocket = pygame.transform.flip(rocketflipped, 0, 180)  #переворачиваем её
dom1 = pygame.Rect(0,vuisota-68,shir, 200)  #город, который атакуют
sootnosheniyakuba = 50       #сторона куба, репрезентирующего ракетницу
rocketlauncher = pygame.Rect(shir//2-25,vuisota-68,sootnosheniyakuba, sootnosheniyakuba)    #Задаём квадрат ракетницы
speed = 15  #скорость перемещения игрока
scores = pygame.font.SysFont("comicsans", 40)
ourrocketsootnoocheniya = 100
rockethitbox=pygame.Rect(random.randint(10, 1000),0, 40, 40)
rockethitbox1 = pygame.Rect(random.randint(10, 1000), -400, 40, 40)
rockethitbox2 = pygame.Rect(random.randint(10, 1000), -1000, 40, 40)   #берём отрицательные координаты, чтобы ракеты появлялись с задержкой от начала игры
rockethitbox3 = pygame.Rect(random.randint(10, 1000), -10000, 40, 40)
rockethitbox4 = pygame.Rect(random.randint(10, 1000), -40000, 40, 40)

YESTPROBITIE = pygame.USEREVENT + 1   # ивент на случай коллизии со взрывом
NETTPROBITIYA = pygame.USEREVENT + 2  # на случай коллизии с городом

def puli(ourrocket, rockethitbox):
        ourrocket.y -= 500
        if rockethitbox.colliderect(ourrocket):
            pygame.event.post(pygame.event.Event(YESTPROBITIE))
            rockethitbox.y -= 800
            rockethitbox.x = random.randint(10, 1000)
def promah(rockethitbox, dom1):
    if rockethitbox.colliderect(dom1):
        pygame.event.post(pygame.event.Event(NETTPROBITIYA))
        rockethitbox.y -= 768
        rockethitbox.x = random.randint(10, 1000)
def upravlenie (keys, rocketlauncher):   #функция, отвечающая за управление
    if keys[pygame.K_LEFT] and rocketlauncher.x - speed > 0:  # управление - кнопки влево и вправо
        rocketlauncher.x -= speed
    if keys[pygame.K_RIGHT] and rocketlauncher.x + speed < shir - sootnosheniyakuba:  # если не вычесть длинну самой ракетницы, доходить до конца не будет
        rocketlauncher.x += speed

def vuvodisobrajeniya():
    screen.fill(vecherneenebo)  # делаем фон
    scoreout = scores.render(f"Score: {score}", 1, (white))  # рендер числа очков
    screen.blit(rocket, (rockethitbox.x, rockethitbox.y))   #спрайт каждой из ракет прикреплён к её хитбоксу, чтобы упрастить расчёт коллизии
    screen.blit(rocket, (rockethitbox1.x, rockethitbox1.y))
    screen.blit(rocket, (rockethitbox2.x, rockethitbox2.y))
    screen.blit(rocket, (rockethitbox3.x, rockethitbox3.y))
    screen.blit(rocket, (rockethitbox4.x, rockethitbox4.y))
    rockethitbox.y += 2
    rockethitbox1.y += 3
    rockethitbox2.y += 4  #разные вражеские ракеты разные и по сложности и имеют разную скорость падения
    rockethitbox3.y += 5
    rockethitbox4.y += 6
    screen.blit(scoreout, (10, 10))
    pygame.draw.rect(screen, black, dom1, 0)
    pygame.draw.rect(screen, white, rocketlauncher, 0)
    pygame.display.flip()  # вывод изображения
while True: #бесконечный цикл
    clock.tick(30)  #ограничеваем кадровую частоту 30-ю кадрами
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     #корректный выход по нажатию на крест
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                ourrocket = pygame.Rect(rocketlauncher.x-ourrocketsootnoocheniya//2, 600, ourrocketsootnoocheniya, ourrocketsootnoocheniya)
                puli(ourrocket, rockethitbox)
            if event.key == pygame.K_w:
                ourrocket = pygame.Rect(rocketlauncher.x-ourrocketsootnoocheniya//2, 1000, ourrocketsootnoocheniya, ourrocketsootnoocheniya)
                puli(ourrocket, rockethitbox)
            if event.key == pygame.K_q:
                ourrocket = pygame.Rect(rocketlauncher.x-ourrocketsootnoocheniya//2, 600, ourrocketsootnoocheniya, ourrocketsootnoocheniya)   #создаём невидимый взрыв
                puli(ourrocket, rockethitbox1)
            if event.key == pygame.K_w:
                ourrocket = pygame.Rect(rocketlauncher.x-ourrocketsootnoocheniya//2, 1000, ourrocketsootnoocheniya, ourrocketsootnoocheniya)
                puli(ourrocket, rockethitbox1)
            if event.key == pygame.K_q:
                ourrocket = pygame.Rect(rocketlauncher.x-ourrocketsootnoocheniya//2, 600, ourrocketsootnoocheniya, ourrocketsootnoocheniya)
                puli(ourrocket, rockethitbox2)
            if event.key == pygame.K_w:
                ourrocket = pygame.Rect(rocketlauncher.x-ourrocketsootnoocheniya//2, 1000, ourrocketsootnoocheniya, ourrocketsootnoocheniya)
                puli(ourrocket, rockethitbox2)
            if event.key == pygame.K_q:
                ourrocket = pygame.Rect(rocketlauncher.x-ourrocketsootnoocheniya//2, 600, ourrocketsootnoocheniya, ourrocketsootnoocheniya)
                puli(ourrocket, rockethitbox3)
            if event.key == pygame.K_w:
                ourrocket = pygame.Rect(rocketlauncher.x-ourrocketsootnoocheniya//2, 1000, ourrocketsootnoocheniya, ourrocketsootnoocheniya)
                puli(ourrocket, rockethitbox3)
            if event.key == pygame.K_q:
                ourrocket = pygame.Rect(rocketlauncher.x-ourrocketsootnoocheniya//2, 600, ourrocketsootnoocheniya, ourrocketsootnoocheniya)
                puli(ourrocket, rockethitbox4)
            if event.key == pygame.K_w:
                ourrocket = pygame.Rect(rocketlauncher.x-ourrocketsootnoocheniya//2, 1000, ourrocketsootnoocheniya, ourrocketsootnoocheniya)
                puli(ourrocket, rockethitbox4)

        if event.type == YESTPROBITIE:
            score+=1
        if event.type == NETTPROBITIYA:
            score-=1
    keys = pygame.key.get_pressed()
    upravlenie(keys, rocketlauncher)
    promah(rockethitbox, dom1)
    promah(rockethitbox1, dom1)
    promah(rockethitbox2, dom1)
    promah(rockethitbox3, dom1)
    promah(rockethitbox4, dom1)
    if score < 0 :    #выход из игры при отрицательном счёте
        screen.fill(red)
        pygame.display.flip()
        sys.exit()
    vuvodisobrajeniya()

pygame.quit()
