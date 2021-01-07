import pygame, sys, random

pygame.init()
clock = pygame.time.Clock()
def restart():
    ball.center = (screen_width/2,screen_height/2)
def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <=0 or ball.bottom >=screen_height:
        ball_speed_y *= -1
    if ball.left<=0 or ball.right>=screen_width:
        restart()
        ball_speed_x *= random.choice((-1,1))
        ball_speed_y *= random.choice((-1,1))
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *=-1
        
def player_animation():
    if player.top <=0:
        player.top = 0
    if player.bottom >=screen_height:
        player.bottom = screen_height

def opponent_animation():
    if opponent.top <= ball.y:
        opponent.top += opponent_speed
    if opponent.bottom >= ball.y:
        opponent.bottom -=opponent_speed
    if opponent.top <=0:
        opponent.top =0
    if opponent.bottom >=screen_height:
        opponent.bottom = screen_height
screen_width = 720
screen_height = 360
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("pong")

ball = pygame.Rect(screen_width/2-7,screen_height/2-7,14,14)
player = pygame.Rect(screen_width-10,screen_height/2-35,5,35)
opponent = pygame.Rect(5,screen_height/2-35,5,35)

back_color = (130, 224, 170)
light_grey = (203, 67, 53)

ball_speed_x = 3
ball_speed_y = 3
player_speed = 0
opponent_speed = 3
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed +=7
    ball_animation()
    player_animation()

    opponent_animation()
    player.y += player_speed
   
    screen.fill(back_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))


    pygame.display.flip()
    clock.tick(60)