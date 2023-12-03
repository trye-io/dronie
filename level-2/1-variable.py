import pygame

pygame.init()

screen = pygame.display.set_mode((1080, 720))

is_flying = True

left_right_velocity = 0

while is_flying: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_flying = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_right_velocity = 50

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_right_velocity = 0

    print(left_right_velocity)