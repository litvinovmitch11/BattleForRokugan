import sys


class ConsoleDraw:
    def __init__(self, player_id, name, game_id, reg, vms, vmh, vmb):
        self.player_id = player_id
        self.name = name
        self.game_id = game_id
        self.reg = reg
        self.vms = vms
        self.vmh = vmh
        self.vmb = vmb
        self.start_message = "-----------------------------------------------------\n" \
                             "Well, now you can control game from console!\n" \
                             f"Your name: {self.name}, Your game_id: {self.game_id}, Your player_id: {self.player_id}\n"
        self.card_help = "Description all cards by id:\n" \
                         "id 1:    Движение к цели. Выберите 2 подконтрольные вам провинции и " \
                         "поместите в каждую из них 1 жетон контроля лицевой стороной вверх\n" \
                         "args:    индекс провинции под владением, индекс провинции под владением (разные)\n\n" \
                         "id 2:    Огни восстания. Уберите из любой провинции жетон мира" \
                         "Если вы контролируете эту провинцию, поместите в неё 2 жетона контроля " \
                         "лицевой стороной вверх\n" \
                         "args:    индекс провинции с жетоном мира внутри\n\n" \
                         "id 3:    Очищиние. Уберите из любой провинции жетон выжженой земли. " \
                         "Затем поместите в эту провинцию 2 ваших жетона контроля и " \
                         "переверните один из них лицевой стороной вверх\n" \
                         "args:    индекс провинции с жетоном вызженной земли внутри\n\n" \
                         "id 4:    Культурный обмен. Выберите провинцию под вашим контролем " \
                         "и провинцию под контролем противника. Поменяйте местами все жетоны контроля в вашей " \
                         "провинции со всеми жетонами контроля в провинции противника (не переворачивайте их)\n" \
                         "args:    индекс провинции под владением, индекс провинции под владением другого игрока\n\n" \
                         "id 5:    Выход к морю. Выберите континентальную провинцию и поместите в неё жетон гавани. " \
                         "Теперь эта провинция считается прибрежной\n" \
                         "args:    индекс матириковой провинции\n\n" \
                         "id 6:    Славная битва. Выберите провинцию и поместите в неё жетон славы. " \
                         "В этой провинции нельзя размещать жетон дипломатии и погрома\n" \
                         "args:    индекс провинции без жетона славы и вызженной земли\n\n" \
                         "id 7:    Кодекс чести. Выберите 2 провинции (кроме Теневых земель) " \
                         "и поместите в каждую из них жетон бонуса к чести +1\n" \
                         "args:    индекс любой провинция (не Теневая), индекс любой провинция (не Теневая)\n\n" \
                         "id 8:    Богатый урожай. Выберите провинцию под вашим контролем и поместите в неё" \
                         " 2 жетона контроля лицевой стороной вверх\n" \
                         "args:    индекс провинции под владением\n\n" \
                         "id 9:    Процветание. Выберите провинцию (кроме Теневых земель)" \
                         " и поместите в неё жетон бонуса к чести +2\n" \
                         "args:    индекс любой провинции (не Теневой)\n\n" \
                         "id 10:   Власть ужаса. (Вы можете сыграть эту карту в начале вашего хода в фазе " \
                         "размещения) Уберите свой жетон контроля из любой провинции, кроме Теневых земель. " \
                         "Затем уберите с поля 2 особых жетона или меньше\n" \
                         "args:    индекс провинции под контролем, индекс провинции с особым жетоном, индекс типа " \
                         "особого жетона (от 0 до 6) (по желанию можно добавить:" \
                         " индекс провинции с особым жетоном, индекс типа особого жетона (от 0 до 6))\n\n" \
                         "id 11:   Умерщвление слабых. (Вы можете сыграть эту карту в начале вашего хода в фазе" \
                         " размещения) Сбросьте жетон битвы из своего актива. В этот ход вы не размещаете " \
                         "жетон битвы. Затем раскройте 2 любых жетона битвы на поле и отправьте в сброс их кланов\n" \
                         "args:    индекс жетона битвы из актива, индекс жетона битвы на поле (не своего), " \
                         "индекс жетона битвы на поле (не своего)"

        self.help = "List commands:\n" \
                    "-E                 exit client\n" \
                    "-H                 help reference\n" \
                    "-S                 show start message\n" \
                    "-SI                system info\n" \
                    "-SR                swap readiness value\n" \
                    "-SC                set your caste\n" \
                    "-GW                get winners ids and score\n" \
                    "-PCT               put control token\n" \
                    "-PBT               put battle token\n" \
                    "-GSR               get someone reset\n" \
                    "-HC                card help\n" \
                    "-SAC               show info about all cards\n" \
                    "-SAT               show info about all tokens\n" \
                    "-UC                use card\n" \
                    "-UNC               unused card\n"

    def register(self):
        self.reg.add(self.vms)
        self.reg.add(self.vmh)
        self.reg.add(self.vmb)

    def parser(self, command):
        if command == '-E':
            sys.exit()
        elif command == '-H':
            print(self.help)
        elif command == 'S':
            print(self.start_message)
        elif command == '-SI':
            print(f"Round: {self.vms.round}\n"
                  f"Which phase: {self.vms.phase}\n"
                  f"Whose move: {self.vms.whose_move}\n"
                  f"Players count: {self.vms.players_count}\n"
                  f"Players: ")
            for player in self.vms.players:
                print(f"Name: {player.name}, "
                      f"Player_id: {player.player_id}, "
                      f"Readiness: {player.readiness}, "
                      f"Caste: {player.caste}")
            print()
        elif command == '-SR':
            print(f"All players ready? - {self.vms.swap_player_readiness_value()}\n")
        elif command == '-SC':
            print(f"Free casts: {self.vms.free_casts}")
            caste = input("Enter caste:\n")
            print(f"Correct? - {self.vms.set_caste(caste)}\n")
        elif command == '-GW':
            print(f"Winners ids: {self.vms.get_winner()}")
            print(f"Score:")
            for score in self.vms.get_score():
                print(f"Player_id: {score.player_id}, Score: {score.score}")
            print()
        elif command == '-PCT':
            print(f"Possible position control token:")
            print(self.vmb.possible_position_control_token)
            province_id = input("Enter province id:\n")
            if not province_id.isdigit():
                print("Invalid input!\n")
                return
            province_id = int(province_id)
            print(f"Correct? - {self.vmh.put_control_token(province_id)}\n")
        elif command == '-PBT':
            print("Possible battle tokens:")
            for token in self.vmh.active:
                print(f"Token_id: {token.id}, "
                      f"Caste: {token.caste}, "
                      f"Power: {token.power}, "
                      f"Type: {token.type}, "
                      f"In active: {token.in_active}, "
                      f"In reset: {token.in_reset}, "
                      f"On board from: {token.on_board_first}, "
                      f"On board to: {token.on_board_second}, "
                      f"Visible: {token.visible}")
            token_id = input("Enter token id:\n")
            if not token_id.isdigit():
                print("Invalid input!\n")
                return
            token_id = int(token_id)
            print("Possible position battle token:")
            print('   ', end='')
            for i in range(31):
                print(i, end=' ' * (3 - len(str(i))))
            print()
            for num, line in enumerate(self.vmb.possible_position_battle_token):
                print(num, end=' ' * (3 - len(str(num))))
                for num2, item in enumerate(line.cell):
                    print(item, end='  ')
                print()
            province_id_from = input("Enter province id from:\n")
            province_id_to = input("Enter province id to:\n")
            if not province_id_to.isdigit() or not province_id_from.isdigit():
                print("Invalid input!\n")
                return
            province_id_to, province_id_from = int(province_id_to), int(province_id_from)
            print(f"Correct? - {self.vmh.put_battle_token(token_id, province_id_from, province_id_to)}\n")
        elif command == '-GSR':
            some_one_id = input("Enter someone id:\n")
            if not some_one_id.isdigit():
                print("Invalid input!\n")
                return
            some_one_id = int(some_one_id)
            print(f"{some_one_id} reset:")
            for token in self.vmh.get_someone_reset(some_one_id):
                print(f"Token_id: {token.id}, "
                      f"Caste: {token.caste}, "
                      f"Power: {token.power}, "
                      f"Type: {token.type}, "
                      f"In active: {token.in_active}, "
                      f"In reset: {token.in_reset}, "
                      f"On board from: {token.on_board_first}, "
                      f"On board to: {token.on_board_second}, "
                      f"Visible: {token.visible}")
            print()
        elif command == '-HC':
            print(self.card_help)
        elif command == '-SAC':
            print("All cards:")
            for card in self.vmh.cards:
                print(
                    f"Player id: {card.player_id}, Card id: {card.card_id}, Caste: {card.caste}, Used: {card.used} "
                    f"Data:", end=" ")
                for num in card.data:
                    print(num.data, end=' ')
                print()
            print()
        elif command == '-SAT':
            print("All battle tokens:")
            for token in self.vmb.battle_tokens:
                print(f"Token_id: {token.id}, "
                      f"Caste: {token.caste}, "
                      f"Power: {token.power}, "
                      f"Type: {token.type}, "
                      f"In active: {token.in_active}, "
                      f"In reset: {token.in_reset}, "
                      f"On board from: {token.on_board_first}, "
                      f"On board to: {token.on_board_second}, "
                      f"Visible: {token.visible}")
            print("All control tokens:")
            for token in self.vmb.control_tokens:
                print(f"Token_id: {token.id}, "
                      f"Caste: {token.caste}, "
                      f"Power: {token.power}, "
                      f"Province id: {token.province_id}, "
                      f"Visible: {token.visible}")
            print("All special tokens:")
            for token in self.vmb.special_tokens:
                print(f"Token type: {token.token}, "
                      f"Province id: {token.province_id}")
            print()
        elif command == '-UC':
            card_id = input("Enter card_id:\n")
            if not card_id.isdigit():
                print("Invalid input!\n")
                return
            card_id = int(card_id)
            card_data = list(map(int, input("Enter card data:\n").split()))
            print(f"Correct? - {self.vmh.use_card(card_id, card_data)}\n")
        elif command == '-UNC':
            print(f"Correct? - {self.vmh.unused_card()}")

    def run(self):
        print(self.start_message)
        while True:
            command = input("Please, enter a command (-H to help)\n")
            self.parser(command.strip())
