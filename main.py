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
    "If an 'Onix' lives for 100 years, its composition changes to become like which precious gem?",
    "'Gholdengo' is made of gold, though its in-game type is actually an alloy. Which alloy is this?",
    "'Detect' always works the first time, and has a 1/3 chance to work the second time. What are the odds it works on the 8th time?",
]
a_list = [
    ("medium", "19"),
    ("medium", "200"),
    ("easy", "2"),
    ("medium", "poison"),
    ("hard", "protect"),
    ("enduring", "ghost"),
    ("terrifying", "sun"),
    ("bone-chilling", "8 or 9"),
    ("enduring", "diamond"),
    ("pointed", "steel"),
    ("hard", "1/729"),
]

special_difficulty = {
    "enduring": "regirock",
    "bone-chilling": "regice",
    "pointed": "registeel",
    "shocking": "regieleki",
    "terrifying": "regidrago",
}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
