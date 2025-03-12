import pygame

pygame.init()
clock = pygame.time.Clock()

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
angle = 55
angle2 = -5

while game:
    
    if angle % 360 == 55: 
        angle2 -=5
        
    min_rot = pygame.transform.rotate(min, angle2) 
    min_rect = min_rot.get_rect(center=(606,420))
    
    sec_rot = pygame.transform.rotate(sec, angle)
    sec_rect = sec_rot.get_rect(center=(606,420))
    
    screen.fill("white")     
    screen.blit(mick, (340, 210))
    screen.blit(min_rot, min_rect.topleft)
    screen.blit(sec_rot,  sec_rect.topleft)
    
    angle -= 5
    clock.tick(1)
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

pygame.quit()


