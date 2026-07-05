import pygame

pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
q_list = [
    "Out of pokemon's 19 types, how many is it possible to be immune to at one time?"
]
a_list = [("medium", "19")]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
