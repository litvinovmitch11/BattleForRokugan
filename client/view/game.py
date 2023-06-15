from sys import exit

import pygame.time
from pygame.locals import *
from map import *
from view_model import *
from tokens import ControlToken, BattleToken, SpecialToken


def run_game(client_id, name, game_id, reg: Register, vms: ViewModelSystem, vmh: ViewModelHand, vmb: ViewModelBoard):
    pygame.init()

    win_width = 1540
    win_height = 900
    display = (win_width, win_height)

    screen = pygame.display.set_mode(display, HWSURFACE | DOUBLEBUF | RESIZABLE)
    pygame.display.set_caption("Battle For Rokugan")
    background_image = pygame.image.load('../client/resources/bg.jpg')

    reg.add(vms)
    reg.add(vmh)
    reg.add(vmb)
    clock = pygame.time.Clock()
    my_caste = None
    caste_chose_flag = False

    ApplyButton = Button(screen, 'ApplyButton', 100, 40)
    ApplyButton2 = Button(screen, 'ApplyButton', 100, 40)
    ReadyButton = Button(screen, 'ReadyButton', 150, 40)
    ReadyButtons = [ReadyButton]

    unuse_card_button = Button(screen, 'UnuseCard', 100, 40)

    input_box1 = InputBox(1300, 400, 70, 32)
    input_box2 = InputBox(1300, 460, 70, 32)
    input_box3 = InputBox(1300, 520, 70, 32)

    input_box4 = InputBox(20, 550, 40, 32)
    input_box5 = InputBox(20, 600, 40, 32)

    input_boxes = [input_box1, input_box2, input_box3, input_box4, input_box5]

    input_box = InputBox(1300, 400, 70, 32)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if vms.round == 0:
                input_box.handle_event(event)
            # elif 0 < vms.round < 6:
            for box in input_boxes:
                box.handle_event(event)

        f1 = pygame.font.Font(None, 36)
        f2 = pygame.font.Font(None, 80)

        player_names_text = []
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
        if vms.round == -1 or len(vmh.active) == 1:
            ReadyButton.draw(100, 700)
            if ReadyButton.clicked:
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
            for ct in vmb.control_tokens:
                if ct.province_id != -1:
                    visibility = "close"
                    if ct.visible:
                        visibility = "open"
                    ControlToken(screen, ct.caste, visibility, ct.province_id).output()
            i = 0
            for bt in vmh.active:
                print("bt from active", bt.caste, bt.visible, bt.power, 31, i)
                BT = BattleToken(screen, bt.caste, "open", bt.type, bt.power, 31, i)
                BT.image = pygame.transform.scale(BT.image, (60, 60))
                BT.output()
                i += 1
            for bt in vmb.battle_tokens:
                if not bt.in_active and bt.on_board_first != -1:
                    print("bt from board", bt.caste, bt.visible, bt.type, bt.power, bt.on_board_first,
                          bt.on_board_second)
                    BattleToken(screen, bt.caste, bt.visible, bt.type, bt.power, bt.on_board_first,
                                bt.on_board_second).output()
            for st in vmb.special_tokens:
                SpecialToken(screen, st.token, st.province_id).output()
            i = 0
            for card in vmh.cards:
                if card.player_id == client_id:
                    Card(screen, card.card_id, 10 + i * 70, 680).output()
                    i += 1
            if vms.whose_move == client_id:
                unuse_card_button.draw(140, 500)
                for box in input_boxes:
                    box.draw(screen)
                for box in input_boxes:
                    box.update()
                ApplyButton.draw(1300, 570)
                ApplyButton2.draw(20, 500)
                if unuse_card_button.clicked:
                    vmh.unused_card()
                    unuse_card_button.clicked = 0
                if ApplyButton.clicked:  # вывод токена по заданным параметрам в трех текстовиках после нажания Apply
                    if input_box1.text.isdigit():
                        if -1 < int(input_box1.text) < len(vmh.active):
                            if input_box2.text.isdigit():
                                if -1 < int(input_box2.text) < 31:
                                    if input_box3.text.isdigit():
                                        if -1 < int(input_box3.text) < 31:
                                            BT_to_place = vmh.active[int(input_box1.text)]
                                            print(BT_to_place.id, int(input_box2.text), int(input_box3.text))
                                            print(vmh.put_battle_token(int(BT_to_place.id), int(input_box2.text),
                                                                       int(input_box3.text)))
                                            ApplyButton.clicked = 0
                #print(len(vmh.active))

                    # input_box1.text, input_box2.text, input_box3.text = '', '', ''
                if ApplyButton2.clicked:  # использование карты
                    if input_box4.text.isdigit() and -1 < int(input_box4.text) < len(vmh.cards):
                        card_to_use = vmh.cards[int(input_box4.text)]
                        vmh.use_card(card_to_use.card_id, list(map(int, input_box5.text.split())))
                        ApplyButton2.clicked = 0
            else:
                input_box1.text, input_box2.text, input_box3.text, input_box4.text, input_box5.text = '', '', '', '', ''
        if vms.round == 6:
            screen.fill((255, 255, 255))
            gameover = f2.render('Game Over', True, (0, 77, 255))
            winner_is = f2.render(f'Победитель: {vms.get_winner()}', True, (0, 77, 255))
            screen.blit(gameover, (730, 300))
            screen.blit(winner_is, (700, 400))
        screen.blit(count_of_players, (10, 280))
        screen.blit(id, (10, 60))
        screen.blit(round_text, (10, 20))
        nameCnt = 0
        for name in player_names_text:
            screen.blit(name, (10, 100 + nameCnt * 30))
            nameCnt += 1
        screen.blit(now_moves1, (10, 400))
        screen.blit(now_moves2, (10, 430))

        pygame.display.flip()

        pygame.display.update()
        clock.tick(1)
