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
        self.help = "List commands:\n" \
                    "-E                 exit client\n" \
                    "-H                 help reference\n" \
                    "-S                 show start message\n" \
                    "-SysInfo           system info\n" \
                    "-SwapReadiness     swap readiness value\n" \
                    "-SetCaste          set your caste\n" \
                    "-GetWinner         get winners ids\n"

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
        elif command == '-SysInfo':
            print(f"Round: {self.vms.round}\n"
                  f"Which phase: {self.vms.phase}\n"
                  f"Players count: {self.vms.players_count}\n"
                  f"Players: ")
            for player in self.vms.players:
                print(f"Name: {player.name}, "
                      f"Player_id: {player.player_id}, "
                      f"Readiness: {player.readiness}")
            print(f"Whose move: {self.vms.whose_move}\n"
                  f"Free casts: {self.vms.free_casts}\n")
        elif command == '-SwapReadiness':
            print(f"All players ready? - {self.vms.swap_player_readiness_value()}\n")
        elif command == '-SetCaste':
            print(f"Free casts: {self.vms.free_casts}")
            caste = input("Enter caste:\n")
            print(f"Correct? - {self.vms.set_caste(caste)}\n")
        elif command == '-GetWinner':
            print(f"Winners ids: {self.vms.get_winner()}\n")

    def run(self):
        print(self.start_message)
        while True:
            command = input("Please, enter a command (-H to help)\n")
            self.parser(command)
