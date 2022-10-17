import pygame 
import random
from pygame import mixer
from coordinates import coordinates,Snakes,Ladders

pygame.init()
WIDTH = 600
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake and Ladder")
icon = pygame.image.load("cd.png")
pygame.display.set_icon(icon)
bg = pygame.image.load("snk.jpg")
font = pygame.font.Font('freesansbold.ttf',30)

mixer.music.load("bg.mp3")
mixer.music.set_volume(30)
mixer.music.play(-1)
# Game chance 
game_chance = "Player 1"
snakebite = False
ladder=False

# Player 1 
p1disk = pygame.image.load("compact-diska.png")
p1X=10
p1Y=560
p1_position =1
p1_first_chance = False
p1num=""

def player1(pos):
    x,y = coordinates[pos]
    screen.blit(p1disk,(x,y))
    
def player1_move():
    global p1X,p1Y,p1_first_chance,p1_position,p1num
    if p1_first_chance:
        new_num = dice_roll()
        p1num=str(new_num)
        p1_position+= new_num
        p1X,p1Y = coordinates[p1_position]
        p1_first_chance=False
    else:
        num = dice_roll()
        p1num=str(num)
        if num ==6 and p1_position==1:
            p1_first_chance=True
        elif p1_position!=1 and p1_first_chance==False:
            if p1_position+num <=100:
                p1_position+= num
                p1X,p1Y = coordinates[p1_position]





# player 2
p2disk = pygame.image.load("compact-diskb.png")
p2X=15
p2Y=560
p2_position =1
p2_first_chance = False
p2num=""
def player2(pos):
    x,y= coordinates[pos]
    screen.blit(p2disk,(x,y))

def player2_move():
    global p2X,p2Y,p2_first_chance,p2_position,p2num
    if p2_first_chance:
        new_num = dice_roll()
        p2num=str(new_num)
        p2_position+= new_num
        p2X,p2Y = coordinates[p2_position]
        p2_first_chance=False
    else:
        num = dice_roll()
        p2num=str(num)
        if num ==6 and p2_position==1:
            p2_first_chance=True
        elif p2_position!=1 and p2_first_chance==False:
            if p2_position+num <=100:
                p2_position+= num
                p2X,p2Y = coordinates[p2_position]


def dice_roll ():
    return random.randint(1,6)
def check_snakes(x):
    global snakebite
    if x in Snakes.keys():
        snakebite=True
        return Snakes[x]
    return x
def check_ladders(x):
    global ladder
    if x in Ladders.keys():
        ladder=True
        return Ladders[x]
    return x
nfont=pygame.font.Font('freesansbold.ttf',20)
about=pygame.font.Font('freesansbold.ttf',9)
def status():
    global p1num,p2num,game_chance
    notice ="Left-control for player 1"
    notice1="Right-control for player 2 "
    p1 = nfont.render("Player 1 ",True,(52,52,200))
    p2 = nfont.render("Player 2 ",True,(52,52,200))
    p1_dice =nfont.render(f"Dice : {p1num}",True,(152,52,100))
    p2_dice=nfont.render(f"Dice : {p2num}",True,(150,52,100))
    noticef= nfont.render(notice,True,(250,50,50))
    noticef1= nfont.render(notice1,True,(250,50,50))
    gc = nfont.render(f"{game_chance} Chance",True,(10,10,250))
    abt = about.render("developed by Sanjeev kumar Singh",True,(0,0,0))
    screen.blit(p1,(15,620))
    screen.blit(p1_dice,(15,660))
    screen.blit(noticef,(155,620))
    screen.blit(noticef1,(155,645))
    screen.blit(gc,(180,670))
    screen.blit(p2,(480,620))
    screen.blit(p2_dice,(480,660))
    screen.blit(abt,(4,690))

def  gameloop():
    global p1X,p1Y,p2X,p2Y,game_chance,p1_position,p2_position,p1num,p2num,snakebite,ladder
    game_over = True
    window_state = True
    game_end=False
    while window_state:

        while game_over:
            screen.fill((200,200,200))
            if game_end:
                # game_over_text()
                if p1_position==100:
                    winner="Player 1"
                elif p2_position==100:
                    winner="Player 2"
                win = font.render(f"{winner} wins the game ",True,(250,50,50))
                screen.blit(win,(70,200))
            startfont = font.render("Press 'P' to play and 'Q' to quit",True,(50,50,200))
            screen.blit(startfont,(70,280))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window_state=False
                    game_over=False
                if event.type== pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over=False
                        window_state=False
                    if event.key == pygame.K_p:
                        # print(coordinates)
                        game_over=False
                        game_end=False
                        p1_position=1
                        p2_position=1
                        p1num=""
                        p2num=""
                        game_chance="Player 1"

            pygame.display.update()

        if window_state:
            screen.fill((100,250,100))
            screen.blit(bg,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window_state=False
                if event.type== pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over=True
                        if event.key == pygame.K_LCTRL:
                            if game_chance=="Player 1":
                                dicesound = mixer.Sound("DiceRoll.wav")
                                dicesound.play()
                                player1_move()
                                if p1_first_chance==True:
                                    game_chance="Player 1"
                                else:
                                    game_chance="Player 2"
                                    p2num=""
                            if p1_position ==100:
                                gameoversound = mixer.Sound("gameover.wav")
                                gameoversound.play()
                                game_end=True
                                game_over=True
                                
                        if event.key == pygame.K_RCTRL:
                            if game_chance=="Player 2":
                                dicesound = mixer.Sound("DiceRoll.wav")
                                dicesound.play()
                                player2_move()
                                if p2_first_chance:
                                    game_chance="Player 2"
                                else:
                                    game_chance="Player 1"
                                    p1num=""
                            if p2_position==100:
                                gameoversound = mixer.Sound("gameover.wav")
                                gameoversound.play()
                                game_end=True
                                game_over=True
            
            if snakebite:
                snakesound = mixer.Sound("snakebite.wav")
                snakesound.play()
                snakebite=False
            if ladder:
                laddersound = mixer.Sound("ladder.wav")
                laddersound.play()
                ladder=False
            status()
            player1(p1_position)
            player2(p2_position)
            p1_position=check_snakes(p1_position)
            p2_position=check_snakes(p2_position)
            p1_position=check_ladders(p1_position)
            p2_position=check_ladders(p2_position)
            # print(f"p1x ={p1X} , y={p2Y}")
            pygame.display.update()

gameloop()


#  X= 10,550
# Y = 560,20