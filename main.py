print("STONE LINES")


class Game:
    def __init__(self, board, current_player, current_phase, winner_state):
        self.board = board
        self.current_player = current_player
        self.current_phase = current_phase
        self.winner_state = winner_state

    def board_display(self):
        print(f"{self.board[0]} ───── {self.board[1]} ───── {self.board[2]}")
        print(r"│ \     │     / │")
        print(r"│   \   │   /   │")
        print(f"{self.board[3]} ───── {self.board[4]} ───── {self.board[5]}")
        print(r"│   /   │   \   │")
        print(r"│ /     │     \ │")
        print(f"{self.board[6]} ───── {self.board[7]} ───── {self.board[8]}")

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    """get placement position"""
    def get_placement_position(self, current_player, current_phase):
        while True:
            if current_phase == "placement":
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
                

    def placement(self, current_player, current_phase):
        player_position = self.get_placement_position(current_player, current_phase)
        return player_position
            

""" Argument creator for the game """
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]   

"""  The dynamic game loop that will run the game until a winner is found or the game is quit """

gameClass = Game(board, "X", current_phase="placement", winner_state=None)
stone_placed = 0
while True:
    gameClass.board_display()    
    placement_index = gameClass.placement(gameClass.current_player, current_phase="placement")
    gameClass.board[placement_index] =  gameClass.current_player 
    gameClass.switch_player()
    stone_placed += 1
    print(stone_placed)
    if stone_placed > 6:
        break