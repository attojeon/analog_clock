##################################################
# pygame - 삼각함수 사용하여 회전하는 시계바늘을 구현해 봄
#
# 참고 사이트 
# https://pygame.org
# https://pygame.org/docs/
##################################################

import pygame
import time
import math

pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("아날로그 시계")

x = int(width//2)
y = int(height//2)
hourLength = 180
minLength = 220
secLength = 220
r = 250
timeFont = pygame.font.Font("font/DS-DIGI.TTF", 48)
txt12 = timeFont.render("12", True, (255,255,255))
txt3 =  timeFont.render("3", True, (255,255,255))
txt6 =  timeFont.render("6", True, (255,255,255))
txt9 =  timeFont.render("9", True, (255,255,255))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    strTime = time.strftime("%I%M%S")
    print(strTime)
    _h = int(strTime[0:2])
    _m = int(strTime[2:4])
    _s = int(strTime[4:6])

    # hour
    # pygame의 0도는 오른쪽, 수학의 0도는 윗쪽 그래서 -90
    xh = x + math.cos(math.radians(_h*5*6-90)) * hourLength
    yh = y + math.sin(math.radians(_h*5*6-90)) * hourLength 

    # min
    xm = x + math.cos(math.radians(_m*6-90)) * minLength
    ym = y + math.sin(math.radians(_m*6-90)) * minLength 

    # sec
    xs = x + math.cos(math.radians(_s*6-90)) * secLength
    ys = y + math.sin(math.radians(_s*6-90)) * secLength 

    # 그리기 
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255,255,255), (x, y), r, 2)
    screen.blit(txt12, (x-24, 4))
    screen.blit(txt3, (width-40, y-24))
    screen.blit(txt6, (x-24, height-52))
    screen.blit(txt9, (10, y-24))
    pygame.draw.line(screen, (255, 255, 0), (x, y), (xh, yh), 2)
    pygame.draw.line(screen, (255, 255, 0), (x, y), (xm, ym), 2)
    pygame.draw.line(screen, (255, 0, 0), (x, y), (xs, ys), 2)
    pygame.draw.circle(screen, (255,255,255), (x, y), 10)
    pygame.display.update()

print('메인루프 종료')
pygame.quit()
