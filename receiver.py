import pygame
import requests as r
from codec import decode
from sys import argv, exit


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((640, 720))
pygame.display.set_caption("Received Messages")
font = pygame.font.Font("JetBrainsMono-Regular.ttf", 18)

txt = 'BACKSPACE to clear screen\n'

last = ''

while True:
    erased = False
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            screen.fill((0, 0, 0))
            erased = True

    new = r.get("http://" + argv[1]).text
    if new == last:
        continue
    try: txt += decode(new) + '\n'
    except IndexError: pass
    last = new

    if erased:
        txt = 'BACKSPACE to clear screen\n'

    x, y = 0, 0
    for ch in txt:
        if ch == '\n':
            x = 0
            y += 1
            continue
        img = font.render(ch, True, (255, 255, 255))
        screen.blit(img, (x * 10 + 5, y * 20 + 5))
        x += 1

    pygame.display.update()
