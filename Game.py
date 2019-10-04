import pygame
pygame.init()
import time
import random

gray=(119,119,110)
black=(0,0,0)
red=(255,0,0)
green=(0,200,0)
blue=(0,0,200)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)
display_width=800
display_height=600

gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Car Game")
clock=pygame.time.Clock()
carimg=pygame.image.load("car.jpg")
backgroundpic=pygame.image.load("grass.jpg")
yellow_strip= pygame.image.load("yellow_strip.jpg")
strip=pygame.image.load("strip.jpg")
intro_background=pygame.image.load("game.jpg")
intruction_background=pygame.image.load("game2.jpg")
pause_img=pygame.image.load("pause.jpg")
pause=True
car_width = 62


def paused():
    global pause

    while pause:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplay.blit(pause_img,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_object("PAUSED",largetext)
        TextRect.center=((display_width/2),(display_height/2))
        gamedisplay.blit(TextSurf,TextRect)
        button("CONTINUE",150,450,150,50,green,bright_green,"unpause")
        button("RESTART",350,450,150,50,blue,bright_blue,"play")
        button("MAIN MENU",550,450,200,50,red,bright_red,"menu")
        pygame.display.update()
        clock.tick(30)

def unpaused():
    global pause
    pause=False
    print("start play")

def countdown_background():
    font = pygame.font.SysFont(None,25)
    x = (display_width*0.45)
    y = (display_height*0.8)
    background()
    gamedisplay.blit(carimg,(x,y))
    text=font.render("DODGED: 0",True,black)
    score=font.render("SCORE: 0",True,red)
    gamedisplay.blit(text,(0,50))
    gamedisplay.blit(score,(0,30))
    button("PAUSE",650,0,150,50,blue,bright_blue,"pause")

def countdown():
    countdown= True

    while countdown:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplay.fill(gray)
        countdown_background()
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_object("3", largetext)
        TextRect.center=((display_width/2),(display_height/2))
        gamedisplay.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(1)
        gamedisplay.fill(gray)
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_object("2", largetext)
        TextRect.center= ((display_width / 2), (display_height / 2))
        gamedisplay.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(1)
        gamedisplay.fill(gray)
        countdown_background()
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_object("1",  largetext)
        TextRect.center= ((display_width / 2), (display_height / 2))
        gamedisplay.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(1)
        gamedisplay.fill(gray)
        countdown_background()
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_object("GO!!!",largetext)
        TextRect.center=((display_width/2),(display_height/2))
        gamedisplay.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(1)
        game_loop()






def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplay.blit(intro_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_object("CAR GAME", largetext)
        TextRect.center=(400,100)
        gamedisplay.blit(TextSurf,TextRect)
        button("START",150,520,100,50,green,bright_green,"play")
        button("QUIT",550,520,100,50,red,bright_red,"quit")
        button("INSTRUCTION",300,520,200,50,blue,bright_blue,"intro")
        pygame.display.update()
        clock.tick(50)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplay,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action =="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()




    else:
        pygame.draw.rect(gamedisplay,ic,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf, textrect=text_object(msg, smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplay.blit(textsurf, textrect)


def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplay.blit(intruction_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext = pygame.font.Font('freesansbold.ttf', 20)
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)
        textSurf,textRect=text_object("Ths is a car game inw hich you need dofge the coming car",smalltext)
        textRect.center=((350),(200))
        TextSurf,TextRect=text_object("INSTRUCTION",largetext)
        TextRect.center=((400),(100))
        gamedisplay.blit(TextSurf,TextRect)
        gamedisplay.blit(textSurf,textRect)
        stextSurf,stextRect=text_object("ARROW LEFT: LEFT TURN",smalltext)
        stextRect.center=((150),(400))
        hTextSurf, hTextRect = text_object("ARROW RIGHT: RIGHT TURN", smalltext)
        hTextRect.center = ((150), (450))
        atextSurf, atextRect = text_object("A: ACCELERATOR", smalltext)
        atextRect.center = ((150), (500))
        rtextSurf, rtextRect = text_object("B : BRAKE", smalltext)
        rtextRect.center = ((150), (550))
        ptextSurf, ptextRect = text_object("P : PAUSE", smalltext)
        ptextRect.center = ((150), (350))
        sTextSurf, sTextRect = text_object("CONTROL ", smalltext)
        sTextRect.center = ((150), (300))
        gamedisplay.blit(sTextSurf,sTextRect)
        gamedisplay.blit(stextSurf,stextRect)
        gamedisplay.blit(hTextSurf,hTextRect)
        gamedisplay.blit(atextSurf,atextRect)
        gamedisplay.blit(rtextSurf,rtextRect)
        gamedisplay.blit(ptextSurf,ptextRect)
        button("BACK",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)





def score_system(passed,score):
    font=pygame.font.SysFont(None,25)
    text=font.render("passed"+str(passed),True,black)
    score = font.render("passed" + str(score), True, red)
    gamedisplay.blit(text,(0,50))
    gamedisplay.blit(score, (0, 30))


def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic = pygame.image.load("car1.jpg")
    elif obs==1:
        obs_pic = pygame.image.load("car2.jpg")
    elif obs==2:
        obs_pic = pygame.image.load("car3.jpg")
    elif obs == 3:
        obs_pic = pygame.image.load("car4.jpg")
    elif obs==4:
        obs_pic = pygame.image.load("car5.jpg")
    elif obs==5:
        obs_pic = pygame.image.load("car6.jpg")
    elif obs==6:
        obs_pic = pygame.image.load("car7.jpg")
    gamedisplay.blit(obs_pic,(obs_startx,obs_starty))



def text_object(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_object(text,largetext)
    textrect.center=((display_width/2,(display_height/2)))
    gamedisplay.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def crash():
    message_display("YOU CRASHED")

def background():
    gamedisplay.blit(backgroundpic,(0,0))
    gamedisplay.blit(backgroundpic,(0,200))
    gamedisplay.blit(backgroundpic,(0,400))
    gamedisplay.blit(backgroundpic,(700,0))
    gamedisplay.blit(backgroundpic,(700,200))
    gamedisplay.blit(backgroundpic,(700,400))
    gamedisplay.blit(yellow_strip,(400,0))
    gamedisplay.blit(yellow_strip,(400,100))
    gamedisplay.blit(yellow_strip,(400,200))
    gamedisplay.blit(yellow_strip, (400, 300))
    gamedisplay.blit(yellow_strip, (400, 400))
    gamedisplay.blit(yellow_strip, (400, 500))
    gamedisplay.blit(strip,(100,0))
    gamedisplay.blit(strip, (100,100))
    gamedisplay.blit(strip, (100, 200))
    gamedisplay.blit(strip, (680, 0))
    gamedisplay.blit(strip, (680, 100))
    gamedisplay.blit(strip, (680, 200))



def car(x,y):
    gamedisplay.blit(carimg,(x,y))


def game_loop():
    global pause
    x = (display_width*0.45)
    y=(display_height*0.8)
    x_change= 0
    obstacle_speed = 9
    obs = 0
    y_change=0
    obs_startx= random.randrange(200,(display_width-200))
    obs_starty= -750
    obs_width= 62
    obs_height=126
    passed=0
    level = 0
    score = 0



    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=+5
                if event.key == pygame.K_a:
                    obstacle_speed+=2
                if event.key==pygame.K_b:
                    obstacle_speed-=2
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0


        x += x_change

        gamedisplay.fill(gray)
        background()
        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed

        car(x,y)
        score_system(passed,score)
        if x>680-car_width or x<90:
            crash()
        if x>display_width-(car_width+90) or x <90:
            crash()
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,7)
            passed = passed+1
            score= passed*10
            if int(passed)%10==0:
                level = level + 1
                obstacle_speed+=2
                largetext = pygame.font.Font("freesansbold.ttf", 80)
                textsurf, textrect = text_object("LEVEL"+str(level), largetext)
                textrect.center = ((display_width / 2, (display_height / 2)))
                gamedisplay.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        if y<obs_starty+obs_height:
            if x>obs_startx and x <obs_startx + obs_width or x + car_width > obs_startx and x +car_width < obs_startx + obs_width:
                crash()

        button("PAUSED", 650, 0 , 150, 50, blue, bright_blue, "pause")

        pygame.display.update()
        clock.tick(60)
intro_loop()
game_loop()
pygame.quit()
quit()
