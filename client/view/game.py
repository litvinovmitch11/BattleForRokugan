from sys import exit

import pygame.time
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
    background_image = pygame.image.load('../resources/bg.jpg')

    reg.add(vms)
    reg.add(vmh)
    reg.add(vmb)
    clock = pygame.time.Clock()
    my_caste = None
    # for pl in vms.players:
    #  if pl.player_id == client_id:
    #    my_caste = pl.caste
    caste_chose_flag = False

    ApplyButton = Button(screen, 'ApplyButton', 100, 40)
    ApplyButton2 = Button(screen, 'ApplyButton', 100, 40)
    ReadyButton = Button(screen, 'ReadyButton', 150, 40)
    ReadyButtons = [ReadyButton]

    input_box1 = InputBox(1300, 400, 70, 32)
    input_box2 = InputBox(1300, 460, 70, 32)
    input_box3 = InputBox(1300, 520, 70, 32)

    input_box4 = InputBox(40, 250, 40, 32)
    input_box5 = InputBox(90, 250, 40, 32)

    input_boxes = [input_box1, input_box2, input_box3, input_box4, input_box5]

    input_box = InputBox(1300, 400, 70, 32)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if vms.round == 0:
                input_box.handle_event(event)
            elif 0 < vms.round < 6:
                for box in input_boxes:
                    box.handle_event(event)

        # ability = map.PlayersAbility(screen, "unicorn")
        # game = view_model.Game(game_id, client_id)
        # pl = view_model.Player(client_id, name)
        f1 = pygame.font.Font(None, 36)
        f2 = pygame.font.Font(None, 80)

        player_names_text = []
        # game.add_player(client_id, name)
        if vms.players:
            for player in vms.players:
                player_names_text.append(f1.render(player.name, True, (0, 77, 255)))

        now_moves1 = f1.render('Вы ходите?:', True, (0, 77, 255))
        now_moves2 = f1.render(f'{"Да" if vms.whose_move == client_id else "Нет"}', True, (0, 77, 255))
        round_text = f1.render(f'Раунд {vms.round if vms.round else 0}', True, (0, 77, 255))
        count_of_players = f1.render(f'Игроков: {vms.players_count if vms.players_count else 0}', True, (0, 77, 255))
        id = f1.render(f'ID игры: {game_id}', True, (0, 77, 255))

        pygame.event.pump()
        event = pygame.event.wait()
        screen.blit(background_image, (0, 0))
        if event.type == VIDEORESIZE:
            screen = pygame.display.set_mode(
                event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
            screen.blit(pygame.transform.scale(background_image, event.dict['size']), (0, 0))
            pygame.display.flip()
        mapp = Map(screen)
        mapp.output()

        if caste_chose_flag:
            PlayersAbility(screen, my_caste).output()
        if vms.round == -1:
            if len(ReadyButtons) > 0:
                ReadyButton.draw(100, 700)
                if ReadyButton.clicked:
                    ReadyButtons = []
                    vms.swap_player_readiness_value()
        if vms.round == 0:
            if not caste_chose_flag:
                num_of_but = 0
                for caste in vms.free_casts:
                    but = Button(screen, f'Choose_{caste}', 200, 40)
                    but.draw(1300, 10 + 50 * num_of_but)
                    if but.clicked:
                        pygame.time.delay(500)
                        if vms.set_caste(but.button_type[7:]):
                            my_caste = but.button_type[7:]
                            caste_chose_flag = True
                            break
                    num_of_but += 1
            else:
                if vms.whose_move == client_id:
                    apply_button = Button(screen, 'ApplyButton', 100, 40)
                    input_box.draw(screen)
                    input_box.update()
                    apply_button.draw(1300, 450)
                    if apply_button.clicked:
                        if not input_box.text.isdigit() or int(input_box.text) > 29 or int(
                                input_box.text) < 0:
                            pass
                        else:
                            if vmh.put_control_token(int(input_box.text)):
                                pass
                        input_box.text = ''
            for ct in vmb.control_tokens:
                if ct.province_id != -1:
                    ControlToken(screen, ct.caste, "close", ct.province_id).output()
            i = 0
            for bt in vmh.active:
                BattleToken(screen, bt.caste, bt.visible, bt.type, bt.power, 31, i).output()
                i += 1

        if 0 < vms.round < 6:
            i, j = 0, 0
            for pl in vms.players:
                for token in vmh.get_someone_reset(pl.player_id):
                    BattleToken(screen, token.caste, "open", token.type, token.power, 1100 + i * 40, 70 + j * 40)
                    i += 1
                    if i == 12:
                        i = 0
                        j += 1
            for ct in vmb.control_tokens:
                visibility = "close"
                if ct.visible:
                    visibility = "open"
                ControlToken(screen, ct.caste, visibility, ct.province_id).output()
            i = 0
            for bt in vmh.active:
                BT = BattleToken(screen, bt.caste, "open", bt.type, bt.power, 31, i)
                BT.image = pygame.transform.scale(BT.image, (60, 60))
                BT.output()
                i += 1
            for bt in vmb.battle_tokens:
                if not bt.in_active:
                    BattleToken(screen, bt.caste, bt.visible, bt.type, bt.power, bt.on_board_first,
                                bt.on_board_second).output()
            i = 0
            for card in vmh.cards:
                Card(screen, card.card_id, 10 + i * 70, 230).output()
                i += 1
            if vms.whose_move == client_id:
                for box in input_boxes:
                    box.update()
                for box in input_boxes:
                    box.draw(screen)
                ApplyButton.draw(1300, 570)
                ApplyButton2.draw(200, 250)

                if ApplyButton.clicked:  # вывод токена по заданным параметрам в трех текстовиках после нажания Apply
                    if input_box1.text.isdigit() and -1 < int(
                            input_box1.text) < 30 and input_box2.text.isdigit() and -1 < int(
                        input_box2.text) < 30 and input_box3.text.isdigit() and -1 < int(input_box3.text) < 30:
                        BT_to_place = vmh.active[int(input_box1.text)]
                        if vmh.put_battle_token(BT_to_place.id, int(input_box2.text), int(input_box3.text)):
                            pass
                input_box1.text, input_box2.text, input_box3.text = '', '', ''
                if ApplyButton2.clicked:  # использование карты
                    if input_box4.text.isdigit() and -1 < int(input_box4.text) < len(vmh.cards):
                        card_to_use = vmh.cards[int(input_box4.text)]
                        vmh.use_card(card_to_use.card_id, list(map(int, input_box5.text.split())))
        if vms.round == 6:
            screen.fill((255, 255, 255))
            gameover = f2.render('Game Over', True, (0, 77, 255))
            winner_is = f2.render(f'Победитель: {vms.get_winner()}', True, (0, 77, 255))
            screen.blit(gameover, (730, 300))
            screen.blit(winner_is, (700, 400))

            # BT_to_place = BattleToken(screen, BT_to_place_taken.caste, "close", BT_to_place_taken.typee,
            #                          BT_to_place_taken.power, input_box2.text, input_box3.text)
            # BT_to_place.output()

        # for token in vmb.battle_tokens:
        #   BattleToken(screen, token.caste, token.visible, token.typee, token.power, token.prov_from,
        #              token.prov_to).output()
        # for token in vmb.control_tokens:
        #    ControlToken(screen, token.caste, token.visible, token.prov)
        # for token in vmh.active:
        #   BattleToken(screen, token.caste, token.visible, token.typee, token.power, token.prov_from,
        #              token.prov_to).output()
        screen.blit(count_of_players, (10, 280))
        screen.blit(id, (10, 60))
        screen.blit(round_text, (10, 20))
        nameCnt = 0
        for name in player_names_text:
            screen.blit(name, (10, 100 + nameCnt * 30))
            nameCnt += 1
        screen.blit(now_moves1, (10, 400))
        screen.blit(now_moves2, (10, 430))
        '''
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
        '''
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
    background_image = pygame.image.load('resources/bg.jpg')
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
