import pygame
import random
def promah(rockethitbox, dom1, vuisota, shir):
    '''Аналогичен функции puli'''
    if rockethitbox.colliderect(dom1):
        rockethitbox.y -= vuisota    #возвращает хитбокс ракеты(а следовательно и её спрайт) вверх
        rockethitbox.x = random.randint(10, shir-24) #меняет координату по x на случайную
        return 1
    else:
        return 0

def puli(ourrocket, rockethitbox, vuisota, shir):
    '''Просчитывает коллизию двух объектов, берёт на вход два объекта класса Rect(ourrocket и rockethitbox), возвращвет 1 в случаи коллизи, 0 в обратном , отправляет один из них(rockethitbox) наверх на высоту окна и со случайной координатой х'''
    if rockethitbox.colliderect(ourrocket):
        rockethitbox.y -= vuisota
        rockethitbox.x = random.randint(10, shir-24)
        return 1
    else:
        return 0
