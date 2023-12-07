import pygame
from djitellopy import Tello
import numpy as np 
import cv2 

pygame.init()

screen = pygame.display.set_mode((960, 720))

# створюємо об'єкт для написання тексту
font = pygame.font.SysFont("retrocomputerpersonaluse", size = 20)

FPS = 30 
clock = pygame.time.Clock() 

is_flying = True

drone = Tello()

drone.connect()

drone.streamon()

frame_read = drone.get_frame_read() 

# розкоментовуємо керування дроном
drone.takeoff()

left_right_velocity = 0
forward_backward_velocity = 0
up_down_velocity = 0
yaw_velocity = 0

while is_flying: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drone.land()
            drone.streamoff()
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

    frame = frame_read.frame 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    frame = np.rot90(frame) 
    frame = np.flipud(frame) 
    frame = pygame.surfarray.make_surface(frame) 
    screen.blit(frame, (0, 0)) 

    # Виводимо інформацію на екран
    screen.blit(font.render("Battery: " + str(drone.get_battery()) + "%", True, (164, 251, 147)), (15, 690))
    screen.blit(font.render("TOF: " + str(drone.get_distance_tof()) + "cm", True, (164, 251, 147)), (325, 690))
    screen.blit(font.render("Temperature: " + str(drone.get_temperature()) + "C", True, (164, 251, 147)), (645, 690))

    pygame.display.flip() 

    clock.tick(FPS)