import pygame

pygame.init()

screen = pygame.display.set_mode((1080, 720))

is_flying = True

while is_flying: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_flying = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Швидкість дорівнює 50")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print("Швидкість дорівнює 0")