import pygame

pygame.init()

musics =['music/TIWD.mp3','music/asap.mp3','music/heartless.mp3']
m = 0
images =['image/play.jpeg','image/next.jpeg','image/rewind.jpeg','image/stop.jpeg']
image = [pygame.image.load(img) for img in images]  
cur_img = 0

bgs =['image/a.jpeg','image/b.jpeg','image/c.jpeg']
bg = [pygame.image.load(img) for img in bgs]  
cur = 0
pygame.mixer.music.load(musics[m])

screen = pygame.display.set_mode((640,640))
pygame.display.set_caption("player")

game = True
  
while game:
    screen.blit(pygame.transform.scale(bg[cur], (640,560)),(0,0))
    screen.blit(pygame.transform.scale(image[cur_img], (80,80)),(280,560))
    screen.blit(pygame.transform.scale(image[1], (80,80)),(360,560))
    screen.blit(pygame.transform.scale(image[2], (80,80)),(200,560))  
    cur = m
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_w:
                pygame.mixer.music.play()
                cur_img = 3
            elif event.key == pygame.K_SPACE:
                pygame.mixer.music.stop()
                cur_img = 0
            elif event.key == pygame.K_d:
                m = (m + 1) % len(musics)
                pygame.mixer.music.load(musics[m])
                pygame.mixer.music.play()
            elif event.key == pygame.K_a:
                m = (m - 1) % len(musics)
                pygame.mixer.music.load(musics[m])
                pygame.mixer.music.play()
                
    pygame.display.update()
    
pygame.quit()            