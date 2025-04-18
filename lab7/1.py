import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((1280,720))

mick = pygame.image.load('image/clock.png')
min = pygame.image.load('image/min_hand.png')
sec = pygame.image.load('image/sec_hand.png')

mick = pygame.transform.scale(mick, (533, 400))
min = pygame.transform.scale(min, (533, 400))
sec = pygame.transform.scale(sec, (533, 400))

min_rect = min.get_rect(center=(606,420))
sec_rect = sec.get_rect(center=(606,420))

game = True

while game:
    
    date = datetime.datetime.now()
    second = date.second
    minute = date.minute
    
    sec_angle = (-second * 6) + 60
    min_angle = (-minute * 6) - 60
        
    min_rot = pygame.transform.rotate(min, min_angle) 
    min_rect = min_rot.get_rect(center=(606,420))
    
    sec_rot = pygame.transform.rotate(sec, sec_angle)
    sec_rect = sec_rot.get_rect(center=(606,420))
    
    screen.fill("white")     
    screen.blit(mick, (340, 210))
    screen.blit(min_rot, min_rect.topleft)
    screen.blit(sec_rot,  sec_rect.topleft)
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

pygame.quit()
