import pygame
import sys,time
pygame.init()
screen = pygame.display.set_mode((991, 620))
pygame.display.set_caption("Game Mario 2D")
background = pygame.image.load("C:\\Users\\duyth\\Desktop\\project\\Mario2D\\image\\background\\1.png")
mario = pygame.image.load("C:\\Users\\duyth\\Desktop\\project\\Mario2D\\image\\figure\\main.png")
mario_rect = mario.get_rect()
mario_rect.x = 100
mario_rect.y = 500
mario_speed = 5
running = True
clock = pygame.time.Clock()
#check jump
is_jump=False
jump_start_time=0
jump_duration=0.7
jump_height=100

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  
        mario_rect.x -= mario_speed
    if keys[pygame.K_d]:  
        mario_rect.x += mario_speed
    
    #jump
    if keys[pygame.K_w] and not is_jump:
        is_jump=True
        jump_start_time=time.time()
        mario_rect.y-=jump_height
    if is_jump:
        if time.time()-jump_start_time>=jump_duration:
            mario_rect.y+=jump_height
            is_jump=False

    if keys[pygame.K_s]: 
        mario_rect.y += mario_speed
    if mario_rect.x < 0:
        mario_rect.x = 0
    if mario_rect.x > screen.get_width() - mario_rect.width:
        mario_rect.x = screen.get_width() - mario_rect.width
    if mario_rect.y < 0:
        mario_rect.y = 0
    if mario_rect.y > screen.get_height() - mario_rect.height:
        mario_rect.y = screen.get_height() - mario_rect.height
    screen.blit(background, (0, 0))
    screen.blit(mario, mario_rect)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
sys.exit()
