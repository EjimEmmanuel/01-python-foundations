import constant as c
class Game:

    def __init__(self, board, current_player, current_phase, winner_state):
        self.board = board
        self.current_player = current_player
        self.current_phase = current_phase
        self.winner_state = winner_state
        

    """ winning logic"""
    def check_winner(self, board, current_player):
        for line in c.winning_lines:
            first = board[line[0]]
            second = board[line[1]] 
            third = board[line[2]]
            if first == current_player and second == current_player and third == current_player:
                return True
        return False

    """ The game loop"""
    

    """ board displaying """

    def board_display(self):
        print(f"{self.board[0]} ───── {self.board[1]} ───── {self.board[2]}")
        print(r"│ \     │     / │")
        print(r"│   \   │   /   │")
        print(f"{self.board[3]} ───── {self.board[4]} ───── {self.board[5]}")
        print(r"│   /   │   \   │")
        print(r"│ /     │     \ │")
        print(f"{self.board[6]} ───── {self.board[7]} ───── {self.board[8]}")
    """ player switching"""
    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    """get placement position"""
    def get_placement_position(self, current_player):
        while True:
            raw_placement = input(f"Player {current_player}, please select a position to place your stone (1-9): ").strip()
            if not raw_placement.isdigit():
                print("Invalid input. Please enter a valid number between 1 to 9.")
                continue
            elif int(raw_placement) not in range(1, 10):
                print("Invalid input. Please enter a valid number between 1 to 9.")
                continue
            else:
                player_position = int(raw_placement) - 1 
                if self.board[player_position] in ["O", "X"]:
                    print("Spot already occupied. Please enter a number between 1 to 9.")
                    continue
                return player_position  
    def get_movement_position(self, current_player, connections):
        while True:
            raw_source = input(f"Player {current_player}, please select your stone to move: ").strip()
            if not raw_source.isdigit():
                print("Invalid input. Please enter a valid number between 1 to 9.")
                continue
            elif int(raw_source) not in range(1, 10):
                self.board_display()
                print("Invalid input. Please enter a valid number between 1 to 9.")
                continue
            elif self.board[int(raw_source) - 1] != current_player:
                self.board_display()
                print("You can only move your own stone. Please select your valid stone position.")
                continue 
            else:
                real_source = int(raw_source) - 1 
                break
        while True:
            self.board_display()
            raw_destination = input(f"Player {current_player}, please select your stone's destination : ").strip()
            if not raw_destination.isdigit():
                print("Invalid input. Please enter a valid number between 1 to 9.")
                continue
            elif int(raw_destination) not in range(1, 10):
                print("Invalid input. Please enter a valid number between 1 to 9.")
                continue
            elif self.board[int(raw_destination) - 1] in ["X", "O"]:
                print("Invalid input. Please enter a valid empty destination.")
                continue
            elif int(raw_destination) - 1 not in connections[real_source]:
                self.board_display()
                print("Invalid input. Please enter a valid connected destination.")
                continue
            else:
                real_destination = int(raw_destination) - 1
                return real_source, real_destination


    def Movement(self, board, current_player):
        s, d = self.get_movement_position(current_player, c.connections)
        return s, d 
    """ placement still follows"""
    def placement(self, current_player):
        player_position = self.get_placement_position(current_player)
        print
        return player_position
