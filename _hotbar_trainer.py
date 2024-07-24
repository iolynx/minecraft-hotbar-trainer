from zoneinfo import available_timezones
import pygame 
import random
import os

MAXWIDTH = 1500
MAXHEIGHT = 750
cwd = os.path.realpath(__file__)
cwd = cwd.rstrip("hotbar_trainer.py")

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((MAXWIDTH, MAXHEIGHT))
pygame.display.set_caption("HotBar Trainer")
text_font = pygame.font.SysFont("Helvetica", 30)
number_font = pygame.font.SysFont("Consolas", 32)



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
clock = pygame.time.Clock()
sprite_sheet = pygame.image.load(cwd + 'widgets.png').convert_alpha()
bg_image = pygame.image.load(cwd + 'bg_test.png').convert_alpha()
target_sheet = pygame.image.load(cwd + 'target_block.png').convert_alpha()
chicken_sheet = pygame.image.load(cwd + 'chicken.png').convert_alpha()
crossbow_sheet = pygame.image.load(cwd + 'crossbow.png').convert_alpha()
axe_sheet = pygame.image.load(cwd + 'diamond_axe.png').convert_alpha()
flint_sheet = pygame.image.load(cwd + 'flint_and_steel.png').convert_alpha()
pick_sheet = pygame.image.load(cwd + 'netherrite_pick.png').convert_alpha()
steak_sheet = pygame.image.load (cwd + 'steak.png').convert_alpha()
bucket_sheet = pygame.image.load(cwd + 'water_bucket.png').convert_alpha()
bone_sheet = pygame.image.load(cwd + 'bone.png').convert_alpha()


def get_image(sheet, x, y, width, height, scale, colour):
    image = pygame.surface.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (x, y, width, height))
    image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    image.set_colorkey(colour)

    return image

tick = 60
run = True
x_coord = 578
achieved = True

if os.path.isfile(cwd + 'config.txt'):
    with open(cwd + 'config.txt') as f:
        lines = f.read(9)
    keybinds = list(lines)
else:
    keybinds = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

key_pressed = ord('1')
slotter = random.randint(0, 8) 
streak = 0
countdown = 120 
countdown_colour = (255, 255, 255)
display_tip = False
streak_text = text_font.render("Streak:", False, WHITE)
countdown_text = text_font.render("Time:", False, WHITE)
countdown_number = number_font.render("3.3", False, WHITE)
streak_is_dead = True



OBJECT_COORD_X = 586
OBJECT_COORD_Y = 706

hotbar = get_image(sprite_sheet, 0, 0, 180, 20, 2, BLACK)
selector = get_image(sprite_sheet, 0, 22, 22, 22, 2, BLACK)
target_block = get_image(target_sheet, 0, 0, 300, 300, 0.1, BLACK)
chicken = get_image(chicken_sheet, 0, 0, chicken_sheet.get_width(), chicken_sheet.get_height(), 0.2, BLACK)
crossbow = get_image(crossbow_sheet, 0, 0, crossbow_sheet.get_width(), crossbow_sheet.get_height(), 0.2, BLACK)
axe = get_image(axe_sheet, 0, 0, axe_sheet.get_width(), axe_sheet.get_height(), 0.2, BLACK)
flint = get_image(flint_sheet, 0, 0, flint_sheet.get_width(), flint_sheet.get_height(), 0.2, BLACK)
pick = get_image(pick_sheet, 0, 0, pick_sheet.get_width(), pick_sheet.get_height(), 0.2, BLACK)
steak = get_image(steak_sheet, 0, 0, steak_sheet.get_width(), steak_sheet.get_height(), 0.2, BLACK)
water_bucket = get_image(chicken_sheet, 0, 0, chicken_sheet.get_width(), chicken_sheet.get_height(), 0.2, BLACK)
bone = get_image(bone_sheet, 0, 0, bone_sheet.get_width(), bone_sheet.get_height(), 0.2, BLACK)

items = [chicken, crossbow, axe, flint, pick, steak, water_bucket, bone]
positions = []

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if str(event.key) == str(ord(keybinds[0])):
                x_coord = 578
            elif str(event.key) == str(ord(keybinds[1])):
                x_coord = 618
            elif str(event.key) == str(ord(keybinds[2])):
                x_coord = 658
            elif str(event.key) == str(ord(keybinds[3])):
                x_coord = 698
            elif str(event.key) == str(ord(keybinds[4])):
                x_coord = 738
            elif str(event.key) == str(ord(keybinds[5])):
                x_coord = 778
            elif str(event.key) == str(ord(keybinds[6])):
                x_coord = 818
            elif str(event.key) == str(ord(keybinds[7])):
                x_coord = 858
            elif str(event.key) == str(ord(keybinds[8])):
                x_coord = 898
            else: 
                break

            key_pressed = str(event.key)

    win.fill(BLACK)


    win.blit(bg_image, (35, 0))
    win.blit(hotbar, (580, 700))
    win.blit(selector, (x_coord, 698))
    win.blit(target_block, (OBJECT_COORD_X + slotter * 40, 706))
    win.blit(countdown_text, (625, 500))

    if achieved:
        slotter = random.randint(0, 8)
        available_slots = list("012345678".replace(str(slotter), ''))
        for i in range(8):
            positions.append(OBJECT_COORD_X + 40 * int(available_slots.pop(random.randint(0,7 - i))))
        achieved = False
        display_tip = False
    else:
        if chr(int(key_pressed)) == keybinds[slotter]:
            achieved = True
            countdown = max(48, 150 - streak * 2)
            if not streak_is_dead:
                streak += 1
            else:
                streak = 1
                streak_is_dead = False
        else:
            if countdown > 0.1:
                countdown -= 1
                countdown_colour = (255, max(0, countdown * 2 - 45), max(0, countdown * 2 - 45))
            else:
                countdown = 0
                countdown_colour = RED
                streak_is_dead = True
                display_tip = True

    countdown_number = number_font.render(str(round(countdown/60, 2)), False, countdown_colour)
    win.blit(countdown_number, (765, 500))
    streak_text = text_font.render("Streak:           " + str(streak), False, WHITE) 
    win.blit(streak_text, (625, 400))

    if display_tip:
        tip = text_font.render("[Choose the Target Block (    ) from your inventory]", False, WHITE)
        win.blit(tip, (440, 590))
        win.blit(target_block, (MAXWIDTH//2 - 20, 597))
        
    for i in range(8):
        win.blit(items[i], (positions[i], OBJECT_COORD_Y))

    if achieved:
        positions = []    

    pygame.display.update()
    clock.tick(tick)        

pygame.quit()
