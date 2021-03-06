import pygame        #Цель игры - охранять город от вражеских боеголовок, посредством запуска своих, управляя ракетницей стрелками и стреляя на Q(дальный выстрел) и W(ближний выстрел)
import sys          #За попадания очки добавляются, за пропущенные рокеты - уменьшаюся. При отрицательном счёте игра оканчивается
import random       #мой код частично опирался на https://github.com/techwithtim/PygameForBeginners, но не имеет ни одной целиком заимствованоой строчки
import os    #для более универсального пути к ассету(работает на любой ОС)
from collision import promah
from collision import puli
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
clock = pygame.time.Clock()    #для задавания кадровой частоты в последствии
rocketnotnormal = pygame.image.load(os.path.join('rocket.png')) #загружаем спрайт ракеты
rocketflipped = pygame.transform.scale(rocketnotnormal, (30, 30))  #уменьшаем её
rocket = pygame.transform.flip(rocketflipped, 0, 180)  #переворачиваем её
dom1 = pygame.Rect(0,vuisota-68,shir, 200)  #город, который атакуют
sootnosheniyakuba = 50       #сторона куба, репрезентирующего ракетницу
rocketlauncher = pygame.Rect(shir//2-25,vuisota-68,sootnosheniyakuba, sootnosheniyakuba)    #Задаём квадрат ракетницы
speed = 15  #скорость перемещения игрока
scores = pygame.font.SysFont("comicsans", 40)  #импортирую шрифт comicsans
ourrocketsootnoocheniya = 100
rockethitbox = pygame.Rect(random.randint(10, 1000), 0, 40, 40)
rockethitbox1 = pygame.Rect(random.randint(10, 1000), -400, 40, 40)
rockethitbox2 = pygame.Rect(random.randint(10, 1000), -1000, 40, 40)   #берём отрицательные координаты, чтобы ракеты появлялись с задержкой от начала игры
rockethitbox3 = pygame.Rect(random.randint(10, 1000), -10000, 40, 40)
rockethitbox4 = pygame.Rect(random.randint(10, 1000), -40000, 40, 40)

def upravlenie (keys, rocketlauncher):
    '''Функция, отвечающая за управление. Берёт на вход данные с клавиш(keys), полученные с помощью pygame.key.get_pressed() и также объект класса Rect (rocketlauncher), котороый и будет перемещаться со скоростью, равной переменной заданной в коде ранее - speed '''
    if keys[pygame.K_LEFT] and rocketlauncher.x - speed > 0:  # управление - кнопки влево и вправо. второе условие нужно для того, чтобы не выходить за границы экрана
        rocketlauncher.x -= speed
    if keys[pygame.K_RIGHT] and rocketlauncher.x + speed < shir - sootnosheniyakuba:  # если не вычесть длинну самой ракетницы, доходить до конца не будет
        rocketlauncher.x += speed

def vuvodisobrajeniya():
    '''Функция отрисовки всего(фона, числа очков, вражеских ракет,города, пушки), также отвечает за падение ракет. Требует кучу переменных, прописанных до этого в коде: цвета - vecherneenebo, white, black; переменная score и соответсвующие приготовления, связанные с выводом текста; загруженный спрайт rocket и 5 итераций его хитбоксов rockethitbox(1,2,3,4) - по сущности, хитбоксы просто прямоугольники класса Rect, к которым также относятся dom1 и rocketlauncher'''
    screen.fill(vecherneenebo)  # делаем фон
    scoreout = scores.render(f"Score: {score}", 1, (white))  # рендер числа очков
    screen.blit(scoreout, (10, 10))  #вывод числа очков
    screen.blit(rocket, (rockethitbox.x, rockethitbox.y))   #спрайт каждой из ракет прикреплён к её хитбоксу, чтобы можно было расчитать коллизию
    screen.blit(rocket, (rockethitbox1.x, rockethitbox1.y))  #вывод спрайтов
    screen.blit(rocket, (rockethitbox2.x, rockethitbox2.y))
    screen.blit(rocket, (rockethitbox3.x, rockethitbox3.y))
    screen.blit(rocket, (rockethitbox4.x, rockethitbox4.y))
    rockethitbox.y += 2
    rockethitbox1.y += 3
    rockethitbox2.y += 4  #разные вражеские ракеты разные и по сложности и имеют разную скорость падения
    rockethitbox3.y += 5
    rockethitbox4.y += 6
    pygame.draw.rect(screen, black, dom1, 0)
    pygame.draw.rect(screen, white, rocketlauncher, 0) #вывод объектоа класса Rect(прямоугольников)
    pygame.display.flip()  # вывод изображения
while True: #бесконечный цикл
    clock.tick(30)  #ограничеваем кадровую частоту 30-ю кадрами
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     #корректный выход по нажатию на крест
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:   # в случаи нажатия на клавишу
            if event.key == pygame.K_q:    # если нажали на Q
                ourrocket = pygame.Rect(rocketlauncher.x-ourrocketsootnoocheniya//2, 100, ourrocketsootnoocheniya, ourrocketsootnoocheniya)
                if puli(ourrocket, rockethitbox, vuisota, shir)==1:
                    score+=1
                if puli(ourrocket, rockethitbox1, vuisota, shir)==1: 
                    score+=1
                if puli(ourrocket, rockethitbox2, vuisota, shir)==1:   #через фунцию смотрим, произошла ли коллизия ракеты с пулей, если да - добавляем очки
                    score+=1
                if puli(ourrocket, rockethitbox3, vuisota, shir)==1:
                    score+=1
                if puli(ourrocket, rockethitbox4, vuisota, shir)==1:
                    score+=1
            if event.key == pygame.K_w:   # если нажали на W
                ourrocket = pygame.Rect(rocketlauncher.x-ourrocketsootnoocheniya//2, 600, ourrocketsootnoocheniya, ourrocketsootnoocheniya)
                if puli(ourrocket, rockethitbox, vuisota, shir)==1:
                    score+=1
                if puli(ourrocket, rockethitbox1, vuisota, shir)==1:
                    score+=1
                if puli(ourrocket, rockethitbox2, vuisota, shir)==1:
                    score+=1
                if puli(ourrocket, rockethitbox3, vuisota, shir)==1:
                    score+=1
                if puli(ourrocket, rockethitbox4, vuisota, shir)==1:
                    score+=1

    keys = pygame.key.get_pressed()
    upravlenie(keys, rocketlauncher)
    if promah(rockethitbox, dom1, vuisota, shir) == 1:
        score -=1
    if promah(rockethitbox1, dom1, vuisota, shir) == 1:
        score -=1
    if promah(rockethitbox2, dom1, vuisota, shir) == 1:  #через фунцию смотрим, произошла ли коллизия  города(dom1) c ракетой, если да - убавляем очки
        score -=1
    if promah(rockethitbox3, dom1, vuisota, shir) == 1:
        score -=1
    if promah(rockethitbox4, dom1, vuisota, shir) == 1:
        score -=1
    if score < 0 :    #выход из игры при отрицательном счёте
        screen.fill(red)
        pygame.display.flip()
        sys.exit()
    vuvodisobrajeniya()


pygame.quit()
