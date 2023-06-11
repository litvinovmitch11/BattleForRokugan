from sys import exit
from pygame.locals import *
from map import *
from view_model import *
from tokens import ControlToken, BattleToken

def run_game(client_id, name, game_id, reg: Register, vms: ViewModelSystem, vmh: ViewModelHand, vmb: ViewModelBoard):
    pygame.init()

    win_width = 1540  # Ширина создаваемого окна
    win_height = 900  # Высота (пока ровно под карту, потом буду менять)
    display = (win_width, win_height)

    screen = pygame.display.set_mode(display, HWSURFACE | DOUBLEBUF | RESIZABLE)
    pygame.display.set_caption("Battle For Rokugan")
    background_image = pygame.image.load('BattleForRokugan_content/bg.jpg')

    reg.add(vms)

    input_box1 = InputBox(100, 100, 140, 32)
    input_box2 = InputBox(100, 300, 140, 32)
    input_boxes = [input_box1, input_box2]
    # Надо добавить vmh и vmb в reg, когда начнется 1-й раунд. Сделать это один раз за игру надо

    mapp = Map(screen)
    # ability = map.PlayersAbility(screen, "unicorn")
    # game = view_model.Game(game_id, client_id)
    # pl = view_model.Player(client_id, name)
    f1 = pygame.font.Font(None, 36)
    player_names_text = []
    # game.add_player(client_id, name)
    if vms.players:
        for player in vms.players:
            player_names_text.append(f1.render(player.name, True, (0, 77, 255)))

    now_moves1 = f1.render('Сейчас ходит:', True, (0, 77, 255))
    now_moves2 = f1.render(f'{vms.whose_move if vms.whose_move else 0}', True, (0, 77, 255))
    round_text = f1.render(f'Раунд {vms.round if vms.round else 0}', True, (0, 77, 255))
    count_of_players = f1.render(f'Игроков: {vms.players_count if vms.players_count else 0}', True, (0, 77, 255))

    clock = pygame.time.Clock()
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
                exit()
            print(event)
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)
        mapp.output()
        # for token in vmb.battle_tokens:
        #   BattleToken(screen, token.caste, token.visible, token.typee, token.power, token.prov_from,
        #              token.prov_to).output()
        # for token in vmb.control_tokens:
        #    ControlToken(screen, token.caste, token.visible, token.prov)
        # for token in vmh.active:
        #   BattleToken(screen, token.caste, token.visible, token.typee, token.power, token.prov_from,
        #              token.prov_to).output()
        PlayersAbility(screen, "crane").output()

        screen.blit(count_of_players, (10, 200))

        screen.blit(round_text, (10, 20))
        nameCnt = 0
        for name in player_names_text:
            screen.blit(name, (10, 100 + nameCnt * 30))
            nameCnt += 1
        screen.blit(now_moves1, (10, 400))
        screen.blit(now_moves2, (10, 430))
        bt_in_province = []
        ct_in_province = []

        CT1 = ControlToken(screen, "dragon", "open", 29)
        ct_in_province.append(CT1)
        CT1.output()
        CT2 = ControlToken(screen, "unicorn", "open", 6)
        ct_in_province.append(CT2)
        CT2.output()
        CT3 = ControlToken(screen, "crab", "close", 3)
        ct_in_province.append(CT3)
        CT3.output()

        BT1 = BattleToken(screen, "crane", "open", "infantry", 1, 31, 0)
        BT3 = BattleToken(screen, "crane", "open", "infantry", 1, 31, 1)
        BT4 = BattleToken(screen, "crane", "open", "infantry", 1, 31, 2)
        BT5 = BattleToken(screen, "crane", "open", "infantry", 1, 31, 3)
        BT6 = BattleToken(screen, "crane", "open", "infantry", 1, 31, 4)
        BT7 = BattleToken(screen, "crane", "open", "infantry", 1, 31, 5)
        bt_in_province.append(BT1)
        BT1.image = pygame.transform.scale(
            BT1.image, (BT1.image.get_width() * 2, BT1.image.get_height() * 2))
        BT6.image = pygame.transform.scale(
            BT6.image, (BT6.image.get_width() * 2, BT6.image.get_height() * 2))
        BT1.output()
        BT6.output()

        BT2 = BattleToken(screen, "unicorn", "open", "infantry", 1, 0, 1)
        bt_in_province.append(BT2)

        test_button = Button(screen, (50, 205, 50), 20, 500, 200, 30, 100, "aboba", (255, 255, 255))
        test_button.create_button()

        pygame.display.flip()

        pygame.display.update()  # обновление и вывод всех изменений на экран
        clock.tick(1)


# run()


"""
ЭТО ВЕРСИЯ ДО ИЗМЕНЕНИЙ, МБ ПРИГОДИТСЯ, ЕСЛИ НЕТ УДАЛЯЙТЕ СЛЕДУЮЩИМ КОММИТОМ

import pygame
import sys
from pygame.locals import *
import map
from tokens import ControlToken, BattleToken
import view_model

def run_game(client_id, name, game_id):
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
    game = view_model.Game(game_id, client_id)
    pl = view_model.Player(client_id, name)
    f1 = pygame.font.Font(None, 36)
    player_names_text = []
    # game.add_player(client_id, name)
    for player in game.players.values():
        player_names_text.append(f1.render(player.name, True, (0, 77, 255)))

    now_moves1 = f1.render('Сейчас ходит:', True, (0, 77, 255))
    now_moves2 = f1.render('Камиль 1', True, (0, 77, 255))

    tokens_text = f1.render('Здесь список токенов (левый - имба)', True, (180, 0, 0))
    round_text = f1.render(f'Раунд {game.round}', True, (0, 77, 255))
    count_of_players = f1.render(f'Игроков: {len(game.players)}', True, (0, 77, 255))

    clock = pygame.time.Clock()
    input_box1 = map.InputBox(100, 100, 140, 32)
    input_box2 = map.InputBox(100, 300, 140, 32)
    input_boxes = [input_box1, input_box2]
    done = False

    while not done:
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
                done = True
                sys.exit()
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()
        for box in input_boxes:
            box.draw(screen)
        mapp.output()
        for token in game.battle_tokens:
            BattleToken(screen, token.caste, token.visible, token.typee, token.power, token.prov_from,
                        token.prov_to).output()
        for token in game.control_tokens:
            ControlToken(screen, token.caste, token.visible, token.prov)
        for token in pl.battle_tokens:
            BattleToken(screen, token.caste, token.visible, token.typee, token.power, token.prov_from,
                        token.prov_to).output()
        map.PlayersAbility(screen, "crane").output()

        screen.blit(count_of_players, (10, 200))

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

        CT1 = ControlToken(screen, "dragon", "open", 29)
        ct_in_province.append(CT1)
        CT1.output()
        CT2 = ControlToken(screen, "unicorn", "open", 6)
        ct_in_province.append(CT2)
        CT2.output()
        CT3 = ControlToken(screen, "crab", "close", 3)
        ct_in_province.append(CT3)
        CT3.output()

        BT1 = BattleToken(screen, "crane", "open", "infantry", 1, 31, 0)
        BT3 = BattleToken(screen, "crane", "open", "infantry", 1, 31, 1)
        BT4 = BattleToken(screen, "crane", "open", "infantry", 1, 31, 2)
        BT5 = BattleToken(screen, "crane", "open", "infantry", 1, 31, 3)
        BT6 = BattleToken(screen, "crane", "open", "infantry", 1, 31, 4)
        BT7 = BattleToken(screen, "crane", "open", "infantry", 1, 31, 5)
        bt_in_province.append(BT1)
        BT1.image = pygame.transform.scale(
            BT1.image, (BT1.image.get_width() * 2, BT1.image.get_height() * 2))
        BT6.image = pygame.transform.scale(
            BT6.image, (BT6.image.get_width() * 2, BT6.image.get_height() * 2))
        BT1.output()
        BT6.output()


        BT2 = BattleToken(screen, "unicorn", "open", "infantry", 1, 0, 1)
        bt_in_province.append(BT2)

        test_button = map.Button(screen, (50,205,50), 20, 500, 200, 30, 100, "aboba", (255,255,255))
        test_button.create_button()



        pygame.display.flip()

        # screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        pygame.display.update()  # обновление и вывод всех изменений на экран
        clock.tick(200)
# run()
"""
