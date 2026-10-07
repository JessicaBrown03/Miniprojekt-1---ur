import pygame
import math
from datetime import datetime

height = 640
width = 640

pygame.init()
screen=pygame.display.set_mode((height,width))

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((255,255,255))

    # Tegn cirklen
    radius=200
    pygame.draw.circle(screen,(222, 189, 242),(height/2,width/2),radius,width=3)

    # Tegn timestreger
    start = (height/2,width/2)
    angle = 0
    angle_offset = 360/12

    for line_counter in range(12):
        angle=(360/12*line_counter)
        x_start = start[0] + 180 *math.cos(math.radians(angle))
        y_start = start[1] + 180 * math.sin(math.radians(angle))
        x_end = start[0] + 200 * math.cos(math.radians(angle))
        y_end = start[1] + 200 * math.sin(math.radians(angle))
        pygame.draw.line(screen,(222, 189, 242),(x_start,y_start),(x_end,y_end),2)

    # Tegn minutstreger
    for line_counter in range(60):
        angle=(360/60*line_counter)
        x_start = start[0] + 195 *math.cos(math.radians(angle))
        y_start = start[1] + 195 * math.sin(math.radians(angle))
        x_end = start[0] + 200 * math.cos(math.radians(angle))
        y_end = start[1] + 200 * math.sin(math.radians(angle))
        pygame.draw.line(screen,(222, 189, 242),(x_start,y_start),(x_end,y_end),2)

    # visere
    now = datetime.now()
    seconds = now.second
    minutes = now.minute
    hours = now.hour

    #Sekundviser
    grad_sec = seconds*6-90
    x = start[0]+radius*math.cos(math.radians(grad_sec))
    y = start[1]+radius*math.sin(math.radians(grad_sec))    
    pygame.draw.line(screen,(235, 33, 77),start,(x,y),width=1)

    # Minutviser
    grad_min = minutes*6-90
    x = start[0]+150*math.cos(math.radians(grad_min))
    y = start[1]+150*math.sin(math.radians(grad_min))    
    pygame.draw.line(screen,(0,0,0),start,(x,y),width=2)

    # Timeviser
    grad_hour = hours*30-90
    x = start[0]+100*math.cos(math.radians(grad_hour))
    y = start[1]+100*math.sin(math.radians(grad_hour))    
    pygame.draw.line(screen,(0,0,0),start,(x,y),width=3)

    # Timetal
    font = pygame.font.Font(None,30)

    for i in range(1, 13):
        angle_number = math.radians(i * 30 - 90)
        x = 320 + 165 * math.cos(angle_number)
        y = 320 + 165 * math.sin(angle_number)
        text = font.render(str(i), True, (65, 22, 92))
        text_rect = text.get_rect(center=(x,y))
        screen.blit(text,text_rect)

    pygame.display.flip()