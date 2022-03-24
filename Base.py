import pygame,sys
from pygame.locals import *
import math,random


def hcf(x, y):
   """该函数返回两个数的最大公约数"""

   # 获取最小值
   if x > y:
       smaller = y
   else:
       smaller = x

   for i in range(1, smaller + 1):
       if((x % i == 0) and (y % i == 0)):
           hcf = i

   return hcf




A = 6  # 可以修改
B = 60  #也可以修改
C = 2  #还是可以修改
mode = 2      #可以修改，但是会影响游戏玩法
adding = [2,3,5,7]  #这个又双叒叕可以修改
Font = 'Exo-Regular-webfont.ttf'




pygame.init()

def make_color(h,s,v):
    if s == 0:
        return (v,v,v)
    else:
        I = int(h/60)
        F = h/60 - I
        aa = v * (1 - s)
        bb = v * (1 - s * F)
        cc = v * (1 - s * (1 - F))
        if I == 0:
            return(v,cc,aa)
        elif I == 1:
            return(bb,v,aa)
        elif I == 2:
            return(aa,v,cc)
        elif I == 3:
            return(aa,bb,v)
        elif I == 4:
            return(cc,aa,v)
        elif I == 5:
            return(v,aa,bb)
        else:
            return make_color(h%360,s,v)





icon = pygame.image.load('20486426icon.png')


sc = pygame.display.set_mode((A*B,A*B+round(B/1.5)))
pygame.display.set_caption('20486426')
pygame.display.set_icon(icon)

main = [('-')for i in range(A**2)]



main_tile = [None for i in range(A**2)]
main_tile2 = [None for i in range(A**2)]

score=0

f = pygame.font.Font(Font,B//2)




    


def add():
    global main
    t = 1
    if '-' in main:
        while main[t] != '-':
            t = random.randint(0,A**2-1)
        main[t] = adding[random.randint(0,len(adding)-1)]

def cmi(x1,x2):
    return int(main[x1])-main[x1] == 0 and int(main[x2])-main[x2] == 0 and main[x1] != 0 and main[x2] != 0
def move(x1,x2):
    global main,score
    if main[x1] != '-':
        if main[x2] == '-':
            main[x2]=main[x1]
            main[x1]='-'
        elif main[x2] == main[x1]:
            main[x2] = main[x1]*2
            main[x1] = '-'
            score += main[x2]
        elif main[x2] + main[x1] == 0:
            if mode == 1 or mode == 3:
                score -= main[x2]
                main[x2] = '-'
                main[x1] = '-'
        elif cmi(x1,x2):
            if hcf(abs(main[x1]),abs(main[x2])) > 1:
                if mode == 2 or mode == 3:
                    main[x2] = main[x2]+main[x1]
                    main[x1] = '-'
                    score += main[x2]






def m2(f,s):
    move(f,f+s)



def moven(f,s,n):
    global main
    if n == 2:
        m2(f,s)
    else:
        if [(main[f+s*(i+1)])for i in range(n-2)] == [('-')for i in range(n-2)]:
            move(f,f+(n-1)*s)
        moven(f,s,n-1)


def ma(f,s):
    for i in range(A-1,0,-1):
        moven(f+(i-1)*s,s,A-i+1)


def mu():
    for i in range(A):
        ma(A*A-A+i, -A)
    add()


def md():
    for i in range(A):
        ma(i, A)
    add()


def ml():
    for i in range(A):
        ma(i*A+A-1, -1)
    add()

def mr():
    for i in range(A):
        ma(i*A, 1)
    add()


def made(t):
    return (round(t[0]*255),round(t[1]*255),round(t[2]*255))


print(made(make_color(0,1,1)))
for i in range(C):
    add()
while 1:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYUP:
            if e.key == K_UP or e.key == K_w:
                mu()
            if e.key == K_DOWN or e.key == K_s:
                md()
            if e.key == K_LEFT or e.key == K_a:
                ml()
            if e.key == K_RIGHT or e.key == K_d:
                mr()
    


    sc.fill((255,255,255))
    for a in range(A**2):
        
        if main[a] != '-':
            main_tile[a] = pygame.draw.rect(sc, made(make_color(5*abs(main[a]),1,1)), pygame.Rect(B*(a % A), math.floor(a/A)*B, B, B), 0)
            sc.blit(f.render(str(main[a]), False, (0, 0, 0)), (B*(a % A), math.floor(a/A)*B))
            main_tile2[a] = None
        else:
            main_tile[a] = pygame.draw.rect(sc, (100, 100, 100), pygame.Rect(B*(a % A), math.floor(a/A)*B, B, B), 0)
            main_tile2[a] = pygame.draw.rect(sc, (200, 200, 200), pygame.Rect(B*(a % A), math.floor(a/A)*B, B, B), 2)
    sc.blit(f.render('Your score is ' + str(score),False ,(0,0,0)),(0,A*B))
    
    pygame.display.update()
