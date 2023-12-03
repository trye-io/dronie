import pygame
from djitellopy import Tello

pygame.init()

screen = pygame.display.set_mode((1080, 720))

is_flying = True

drone = Tello()

drone.connect()

drone.takeoff()

left_right_velocity = 0
forward_backward_velocity = 0
up_down_velocity = 0
yaw_velocity = 0

while is_flying: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drone.land()
            is_flying = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_right_velocity = 50
            if event.key == pygame.K_RIGHT:
                left_right_velocity = -50
            if event.key == pygame.K_UP:
                forward_backward_velocity = 50
            if event.key == pygame.K_DOWN:
                forward_backward_velocity = -50
            if event.key == pygame.K_w:
                up_down_velocity = 50
            if event.key == pygame.K_s:
                up_down_velocity = -50
            if event.key == pygame.K_a:
                yaw_velocity = 50
            if event.key == pygame.K_d:
                yaw_velocity = -50

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_right_velocity = 0
            if event.key == pygame.K_RIGHT:
                left_right_velocity = 0
            if event.key == pygame.K_UP:
                forward_backward_velocity = 0
            if event.key == pygame.K_DOWN:
                forward_backward_velocity = 0
            if event.key == pygame.K_w:
                up_down_velocity = 0
            if event.key == pygame.K_s:
                up_down_velocity = 0
            if event.key == pygame.K_a:
                yaw_velocity = 0
            if event.key == pygame.K_d:
                yaw_velocity = 0

    drone.send_rc_control(
        left_right_velocity,
        forward_backward_velocity,
        up_down_velocity,
        yaw_velocity
    )