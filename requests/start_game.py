import pygame
import sys
from pygame.locals import *

from map import Map
from tokens import control_token, battle_token


def run():
    pygame.init()

    WIN_WIDTH = 1540  # Ширина создаваемого окна
    WIN_HEIGHT = 890  # Высота (пока ровно под карту, потом буду менять)
    DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную

    screen = pygame.display.set_mode((500, 500), HWSURFACE | DOUBLEBUF | RESIZABLE)
    pygame.display.set_caption("Battle For Rokugan")
    backgroung_color = (255, 255, 255)
    background_image = pygame.image.load('BattleForRokugan_content/bg.jpg')
    mapp = Map(screen)

    while True:
        pygame.event.pump()
        event = pygame.event.wait()
        screen.blit(background_image, (0, 0))
        if event.type == VIDEORESIZE:
            screen = pygame.display.set_mode(
                event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
            screen.blit(pygame.transform.scale(background_image, event.dict['size']), (0, 0))
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # screen.fill(backgroung_color)
        # bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
        # будем использовать как фон
        mapp.output()

        CT1 = control_token(screen, "dragon", 1, 8)
        CT1.output()
        CT2 = control_token(screen, "unicorn", 1, 6)
        CT2.output()
        CT3 = control_token(screen, "crab", 0, 3)
        CT3.output()

        pygame.display.flip()

        # screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        pygame.display.update()  # обновление и вывод всех изменений на экран

# run()
