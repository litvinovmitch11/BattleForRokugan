import pygame
import sys
from pygame.locals import *
import map
from tokens import ControlToken, BattleToken


def run_game():
    pygame.init()

    WIN_WIDTH = 1540  # Ширина создаваемого окна
    WIN_HEIGHT = 890  # Высота (пока ровно под карту, потом буду менять)
    DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную

    screen = pygame.display.set_mode((1540, 890), HWSURFACE | DOUBLEBUF | RESIZABLE)
    pygame.display.set_caption("Battle For Rakugan")
    backgroung_color = (255, 255, 255)
    background_image = pygame.image.load('BattleForRokugan_content/bg.jpg')
    mapp = map.Map(screen)
    # abuility = map.PlayersAbuility(screen, "unicorn")

    f1 = pygame.font.Font(None, 36)
    round_text = f1.render('Раунд 1', True, (0, 77, 255))
    player_names_text = [f1.render('Камиль 1', True, (0, 77, 255)), f1.render('Камиль 2', True, (0, 77, 255)),
                         f1.render('Камиль 3', True, (0, 77, 255))]

    now_moves1 = f1.render('Сейчас ходит:', True, (0, 77, 255))
    now_moves2 = f1.render('Камиль 1', True, (0, 77, 255))

    tokens_text = f1.render('Здесь список токенов (левый - имба)', True, (180, 0, 0))

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
        mapp.output()
        # abuility.output()
        screen.blit(round_text, (10, 20))
        nameCnt = 0
        for name in player_names_text:
            screen.blit(name, (10, 100 + nameCnt * 30))
            nameCnt += 1
        screen.blit(now_moves1, (10, 400))
        screen.blit(now_moves2, (10, 430))
        screen.blit(tokens_text, (500, 700))
        bt_in_province = []
        ct_in_province = []

        # CT1 = control_token(screen, "dragon", "open", 29)
        # ct_in_province.append(CT1)
        # CT1.output()
        # CT2 = control_token(screen, "unicorn", "open", 6)
        # ct_in_province.append(CT2)
        # CT2.output()
        # CT3 = control_token(screen, "crab", "close", 3)
        # ct_in_province.append(CT3)
        # CT3.output()
        #
        # BT1 = battle_token(screen, "crane", "open", "infantry", 1, 30, 0)
        # bt_in_province.append(BT1)
        # BT1.output()
        # BT2 = battle_token(screen, "unicorn", "open", "infantry", 1, 0, 1)
        # bt_in_province.append(BT2)
        # BT2.output()

        pygame.display.flip()

        # screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        pygame.display.update()  # обновление и вывод всех изменений на экран

# run()
