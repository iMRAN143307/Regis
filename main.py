import pygame

pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
q_list = [
    "Out of pokemon's 19 types, how many is it possible to be immune to at one time?",
    "What is the highest base speed stat of any pokemon?",
    "The ability 'As One' is an oxymoron because it actually combines how many abilities?",
    "'Muk' is able to hurl sludge at opponents, and is therefore given which type?",
    "In double battles, the most popular move is not an attack. What is it?",
    "'Garganacl' has an ability that makes it take half damage from which type?",
    "Despite being a water type, 'Walking Wake' prefers which weather condition?",
    "How many pokemon can set up the 'Snow' weather condition with an ability?",
    "It is said that if an 'Onix' lives for over 100 years, its composition changes to become like what precious gem?",
]
a_list = [
    ("medium", "19"),
    ("medium", "200"),
    ("easy", "2"),
    ("medium", "poison"),
    ("hard", "protect"),
    ("rugged", "ghost"),
    ("terrifying", "sun"),
    ("chilly", "8 or 9"),
    ("rugged", "diamond"),
]

special_difficulty = {
    "rugged": "regirock",
    "chilly": "regice",
    "sharp": "registeel",
    "energetic": "regieleki",
    "terrifying": "regidrago",
}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
