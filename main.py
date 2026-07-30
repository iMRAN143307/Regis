import pygame
import random
import sys
import os

SONG_END = pygame.USEREVENT + 1
CHECK_ANSWER = pygame.USEREVENT + 2
INCORRECT = pygame.USEREVENT + 3
CORRECT = pygame.USEREVENT + 4
DONE_POINT_ALLOCATION = pygame.USEREVENT + 5
GAME_END = pygame.USEREVENT + 6

pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()
screen = pygame.display.set_mode((1440, 960))
running = True
fontObj = pygame.font.Font(None, 30)
mode = "question"
team1_points = [0, 0, 0, 0, 0, 0]
team2_points = [0, 0, 0, 0, 0, 0]
point_allocation_rects = [(72, 580, 144, 144), (360, 580, 144, 144), (648, 580, 144, 144), (936, 580, 144, 144), (1224, 580, 144, 144), (648, 180, 144, 144)]
key_cooldown = 240
clickx = None
clicky = None
team_answering = 1

q_list = [
    "Out of pokemon's 19 types, how many is it possible to be immune to at one time?",
    "What is the highest base Speed stat of any pokemon?",
    "The ability 'As One' is an oxymoron because it actually combines how many abilities?",
    "'Muk' is able to hurl sludge at opponents, and is therefore given which type?",
    "In double battles, the most popular move is not an attack. What is it?",
    "'Garganacl' has an ability that makes it take half damage from which type?",
    "Despite being a Water-type, 'Walking Wake' prefers which weather condition?",
    "How many pokemon can set up the 'Snow' weather condition with an ability?",
    "If an 'Onix' lives for 100 years, its composition changes to become like which precious gem?",
    "'Gholdengo' is made of gold, though its in-game type is actually an alloy. Which alloy is this?",
    "'Detect' always works the first time, and has a 1/3 chance to work the second time. What are the odds it works on the 3rd time?",
    "What was the first ever pure flying type pokemon introduced in Pokemon GO?",
    "'Rotom' in its Washing Machine form has two weaknesses. By levitating in the air, it gets rid of which weakness?",
    "'Perrserker' is the only pokemon that gets the ability 'Steely Spirit', which increases its Steel-type damage by how many times?",
    "The legendary pokemon 'Landorus-Therian' has an ability that weakens opponents whenever it hits the field. What is this ability called?",
    "The transport pokemon 'Lapras', when in its Gigantamax form, is said to be able to carry how many thousands of people?",
    "Instead of a Mega Stone, 'Rayquaza' uses a cosmic object to mega evolve. What cosmic object is this?",
    "'Dedenne' cannot generate much electricity because its organs are not fully developed. What does it do when it is low on electricity?",
    "Because it has an incredibly powerful ability, 'Shedinja' has which base stat reduced to just 1?",
    "A pokemon has a Base Stat Total of 480, and each of its 6 base stats is equal to the others. What number does it have in each base stat?",
    "The status move 'Spore' will put any pokemon to sleep except for grass types and those wearing which item?",
    "The first time you challenge Gym Leader 'Korrina' in pokemon X and Y, she does not use a full team of 6, instead using how many pokemon?",
    "Name one of the two pokemon types first introduced in pokemon Gold and Silver.",
    "Out of pokemon's 19 types, how many pokemon types exist in the pokemon Trading Card Game?"
]
a_list = [
    ("medium", "19"),
    ("medium", "200"),
    ("easy", "2"),
    ("medium", "poison"),
    ("hard", "protect"),
    ("enduring", "ghost"),
    ("terrifying", "sun"),
    ("bone-chilling", "8 or 9, depending on the counting"),
    ("enduring", "diamond"),
    ("pointed", "steel"),
    ("easy", "1/9"),
    ("hard", "tornadus"),
    ("shocking", "ground"),
    ("pointed", "1.5x"),
    ("hard", "intimidate"),
    ("bone-chilling", "5"),
    ("terrifying", "meteorite"),
    ("shocking", "sleep"),
    ("medium", "health or hp"),
    ("easy", "80"),
    ("hard", "safety goggles"),
    ("easy", "2"),
    ("medium", "dark or steel"),
    ("medium", "11")
]

special_difficulty = {
    "enduring": 0,
    "bone-chilling": 1,
    "pointed": 2,
    "shocking": 3,
    "terrifying": 4,
}

current_num = random.randint(0, len(q_list) - 1)
used_nums = set()

def resource_path(relative_path):
    try:
        base_path = sys.MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def load_and_scale(filename, size, transparency=None):
    if transparency == None:
        unscaled = pygame.image.load(resource_path(f"{filename}.png")).convert()
    else:
        unscaled = pygame.image.load(resource_path(f"{filename}.png")).convert_alpha()
    return pygame.transform.scale(unscaled, size)

regirock = load_and_scale("regirock", (144, 144))
regice = load_and_scale("regice", (144, 144))
registeel = load_and_scale("registeel", (144, 144))
regieleki = load_and_scale("regieleki", (144, 144))
regidrago = load_and_scale("regidrago", (144, 144))
regigigas = load_and_scale("regigigas", (144, 144))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CHECK_ANSWER:
            mode = "answer_checking"
        if event.type == INCORRECT:
            used_nums.add(current_num)
            if len(used_nums) == len(q_list):
                pygame.event.post(pygame.event.Event(GAME_END))
            else:
                current_num = random.randint(0, len(q_list) - 1)
                while current_num in used_nums:
                    current_num = random.randint(0, len(q_list) - 1)
                mode = "question"
            if team_answering == 1:
                team_answering = 2
            else:
                team_answering = 1
        if event.type == CORRECT:
            mode = "point_allocation"
        if event.type == DONE_POINT_ALLOCATION:
            used_nums.add(current_num)
            if len(used_nums) == len(q_list):
                pygame.event.post(pygame.event.Event(GAME_END))
            else:
                current_num = random.randint(0, len(q_list) - 1)
                while current_num in used_nums:
                    current_num = random.randint(0, len(q_list) - 1)
                mode = "question"
            if team_answering == 1:
                team_answering = 2
            else:
                team_answering = 1
        if event.type == GAME_END:
            mode = "celebration"
        if event.type == pygame.MOUSEBUTTONDOWN and key_cooldown == 0:
            key_cooldown = 240
            clickx, clicky = event.pos

    if key_cooldown != 0:
        key_cooldown -= 1
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            key_cooldown = 240
            pygame.event.post(pygame.event.Event(INCORRECT))
        if keys[pygame.K_RETURN]:
            key_cooldown = 240
            pygame.event.post(pygame.event.Event(CHECK_ANSWER))
        if keys[pygame.K_ESCAPE]:
            key_cooldown = 240
            pygame.event.post(pygame.event.Event(CORRECT))

    if mode == "question":
        screen.fill("black")
        screen.blit(fontObj.render(q_list[current_num], True, (255, 255, 255), None), (10, 10))

    elif mode == "answer_checking":
        screen.fill("black")
        screen.blit(fontObj.render(a_list[current_num][1], True, (255, 255, 255), None), (640, 10))
        screen.blit(fontObj.render(a_list[current_num][0], True, (255, 255, 255), None), (10, 10))

    elif mode == "point_allocation":

        screen.fill("black")
        screen.blit(regirock, point_allocation_rects[0])
        screen.blit(regice, point_allocation_rects[1])
        screen.blit(registeel, point_allocation_rects[2])
        screen.blit(regieleki, point_allocation_rects[3])
        screen.blit(regidrago, point_allocation_rects[4])
        screen.blit(regigigas, point_allocation_rects[5])

        points = 0
        if a_list[current_num][0] == "easy":
            points = 10
        elif a_list[current_num][0] == "medium":
            points = 20
        elif a_list[current_num][0] == "hard":
            points = 30

        for rect in point_allocation_rects:
            if team1_points[point_allocation_rects.index(rect)] >= 60 or team2_points[point_allocation_rects.index(rect)] >= 60:
                rect_surface = pygame.Surface((144, 144))
                rect_surface.set_alpha(128)
                rect_surface.fill((0, 0, 0))
                screen.blit(rect_surface, rect)
            elif clickx is not None and clicky is not None:
                if clickx > rect[0] and clickx < rect[0] + rect[2] and clicky > rect[1] and clicky < rect[1] + rect[3]:
                    clickx = None
                    clicky = None
                    if team_answering == 1:
                        team1_points[point_allocation_rects.index(rect)] += points
                        print(team1_points)
                    else:
                        team2_points[point_allocation_rects.index(rect)] += points
                        print(team2_points)
                    break

    elif mode == "celebration":
        screen.fill("black")
        screen.blit(fontObj.render("Congratulations", True, (255, 255, 255), None), (10, 10))

    pygame.display.flip()

pygame.quit()
