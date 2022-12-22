import pygame

pygame.init()
FPS = 50
WIDTH = 400
HEIGHT = 300
STEP = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = None
all_sprites = pygame.sprite.Group()
sound = pygame.mixer.Sound("data/in.wav")
vol = 1

# Главный Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            chennel = sound.play()
            sound.set_volume(vol)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            vol += 0.1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            vol -= 0.1
        sound.set_volume(vol)
    screen.fill(pygame.Color(0, 0, 0))
    pygame.display.flip()
    clock.tick(FPS)
