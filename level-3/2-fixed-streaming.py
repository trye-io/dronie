import pygame
from djitellopy import Tello
import numpy as np # домоміжний пакет для конвертації зображення
import cv2 # домоміжний пакет для конвертації зображення

pygame.init()

screen = pygame.display.set_mode((960, 720))

FPS = 30 # кількість кадрів за секунду
clock = pygame.time.Clock() # допоміжний об'єкт для відстеження часу

is_flying = True

drone = Tello()

drone.connect()

drone.streamon()

frame_read = drone.get_frame_read() 

# drone.takeoff()

left_right_velocity = 0
forward_backward_velocity = 0
up_down_velocity = 0
yaw_velocity = 0

while is_flying: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # drone.land()
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

    # drone.send_rc_control(
    #     left_right_velocity,
    #     forward_backward_velocity,
    #     up_down_velocity,
    #     yaw_velocity
    # )

    frame = frame_read.frame 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # змінємо колірну модель
    frame = np.rot90(frame) # повертаємо зображення на 90 градусів
    frame = np.flipud(frame) # перевертаємо зображення догори дригом
    frame = pygame.surfarray.make_surface(frame) 
    screen.blit(frame, (0, 0)) 

    pygame.display.flip() 

    clock.tick(FPS) # дозволяє притримати час за одну ітерацію, щоб домогтись 
                    # певної кількості кадрів за секнуду