import pygame
import time 
import random
import sys

# initializing all the modules in pygame
pygame.init()


# while making a game storing the values in variables is a good practice as later it is easy to put the variables in places where we want them.
# storing color values in variables for later use.
blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
gray = (128,128,128)
yellow = (255,255,0)
dark = (100,100,100)
light = (170,170,170)


# storing the distance in variables for later use.
dis_width = 400
dis_height = 300
x1 = dis_width/2
y1 = dis_height/2
x1_change = 0
y1_change = 0


# storing the snake block size and speed in variables for later use
snake_block = 10
snake_speed = 10
with open("High_Score.txt", "r") as f:
    high_score = f.read()

# creating a font styles for later use
font_style = pygame.font.SysFont('bahnschrift', 25)
score_font = pygame.font.SysFont('comicsansms', 35)
font = pygame.font.SysFont('Arial', 25)
smallfont = pygame.font.SysFont('Corbel',25)


# storing the track of time in a variable
clock = pygame.time.Clock()

# defining functions to be used later
# high score function
def high(high_score):
    value_high = score_font.render("High Score: " + str(high_score), True, yellow)
    dis.blit(value_high, [0,30])
# defining a single line message to be displayed on the screen when needed
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [0, 80])
# defining a multiline message to be displayed on the screen when needed
def multi_message(text, pos, font, color):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = dis_width,dis_height
    x2,y2 = pos
    for line in words:
        for word in line:
            word_dis = font.render(word, 0, color)
            word_width, word_height = word_dis.get_size()
            if x2 + word_width >= max_width:
                x2 = pos[0]
                y2 += word_height
            dis.blit(word_dis, (x2,y2))
            x2 += word_width + space
        x2 = pos[0]
        y2 += word_height
# defining our snake 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
# defining the current score
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0,0])


# Text to be displayed
text =" You Lost!\nWant to Try Again? "
text_2 = smallfont.render('Q - Quit' , True , red)
text_3 = smallfont.render('Space - Play-Again' , True , red)
text_4 = smallfont.render('Or', True, red)
text_5 = "Congrats!!!\nYou have beat the HighScore\nCurrent HighScore:"


# making a display for the game and defining its size and giving it features
# giving it a title
# after every new update iin the screen we should always update the display using pygame.display .update()
# or else changes made won't be displayed
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake')
pygame.display.update()


# we are making this game loop function which would include the main game
def gameloop():
    # this global variable will decide whether or not to display the high score
    global flag_score
    flag_score = 0

    game_over = False
    game_close = False
    # initializing score value to be 0
    score = 0
    # reading the high score to compare with latest score
    with open("High_Score.txt", "r") as f:
        high_score = f.read()

    # making variables for our snake so as to increase its size each time it eats the food
    # initial length of the snake =1
    snake_List = []
    Length_of_snake = 1

    # storing the distance in variables for later use.
    dis_width = 400
    dis_height = 300
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0

    # creating food and producing randomly within the limits of the screen
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # making a loop for the game to start and if the game is over it will quit
    while not game_over:


        # making the x button functional to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            # key bindings up,down,left,right
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        
        # making a loop for the game which would take conformation from the user, that soes he want to quit or not
        while game_close :
            
            # coloring the display
            dis.fill(blue)
            
            if flag_score ==1:
                multi_message(text_5 + str(high_score),(5,5),font,yellow)
            else:
                multi_message(text,(15,20),font,red)

            
            for event in pygame.event.get():
                # making the x button functional to quit
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                # creating buttons to quit and play again
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 100 <= mouse[0] <= 100 + 140 and 100 <= mouse[1] <= 100 + 40:
                        game_over = True
                        game_close = False
                    
                    if 100 <= mouse[0] <= 100 + 180 and 200 <= mouse[1] <= 200 + 40:
                        gameloop()
                
                # creating keys to quit and play again
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameloop()  
    
            mouse = pygame.mouse.get_pos()
            if 100 <= mouse[0] <= 110 + 145 and 100 <= mouse[1] <= 100 + 40:
                pygame.draw.rect(dis,yellow,[110, 100, 145, 40])
            else:
                pygame.draw.rect(dis, black,[110 , 100, 145, 40])
            

            if 100 <= mouse[0] <= 100 + 200 and 200 <= mouse[1] <= 200 + 40:
                pygame.draw.rect(dis,yellow,[100, 200, 200, 40])    
            else:
                pygame.draw.rect(dis, black,[100 , 200, 200, 40])

            dis.blit(text_2, (100 + 40, 110))
            dis.blit(text_3, (100 + 5, 210))
            dis.blit(text_4, (160 , 160))
            pygame.display.update()

        

    
        # making boundries, if the snake touches the boundry then the game will be over
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # moving the snake   
        x1 = x1 + x1_change
        y1 = y1 + y1_change

        # filling the background with color
        dis.fill(gray)

        # drawing a snake body
        # maintaining the score and high score
        pygame.draw.rect(dis, light, [x1,y1,snake_block,snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x ==snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        score_main = Length_of_snake - 1
        
        if score_main > int(high_score):
            high_score = score_main
            with open("High_Score.txt", "w") as f:
                f.write(str(high_score))
            flag_score = 1
        
        
        high(high_score)
        your_score(Length_of_snake - 1)

        pygame.display.update()
        # drawing food
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        # making the snake eat the food
        if x1 == foodx and y1 ==foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake +=1
        pygame.display.update()
    
        # maintaining the speed of the moving snake which will increase as the snake eats food
        clock.tick(snake_speed + Length_of_snake-1)
    if flag_score == 1:
        multi_message(text_5 + str(high_score),(0,75),font,yellow)
    else:
        message("You Lost!", red)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()

gameloop()