print("STONE LINES")

positional_winning_lines = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [3,5,7] ]

indexed_winning_lines = []

for line in positional_winning_lines:
    temp = []
    for x in line:
        x -= 1
        temp.append(x)
    indexed_winning_lines.append(temp)


class Game:
    winning_lines = indexed_winning_lines
    connections = {
    0: [1, 3, 4],
    1: [0, 2, 4],
    2: [1, 4, 5],
    3: [0, 4, 6],
    4: [0, 1, 2, 3, 5, 6, 7, 8],
    5: [2, 4, 8],
    6: [3, 4, 7],
    7: [4, 6, 8],
    8: [4, 5, 7],
}
    def __init__(self, board, current_player, current_phase, winner_state):
        self.board = board
        self.current_player = current_player
        self.current_phase = current_phase
        self.winner_state = winner_state
        

    """ winning logic"""
    def check_winner(self, board, current_player):
        for line in self.winning_lines:
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
        s, d = self.get_movement_position(current_player, self.connections)
        return s, d 
    """ placement still follows"""
    def placement(self, current_player):
        player_position = self.get_placement_position(current_player)
        print
        return player_position

stone_placed = 0
""" Argument creator for the game """
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]   
gameClass = Game(board, "X", current_phase="placement", winner_state=None)

"""the main function """
def Placemen_loop():
    print(f"Placement onging...")
    gameClass.board_display()  
    placement_index = gameClass.placement(gameClass.current_player)
    gameClass.board[placement_index] =  gameClass.current_player 
    print(f"You chose to place your stone at position: {placement_index + 1}")
    global stone_placed
    stone_placed += 1
    if stone_placed >= 5:
        check = gameClass.check_winner(gameClass.board, gameClass.current_player)
        if check:
            gameClass.board_display() 
            print(f"Player {gameClass.current_player} wins!")
            exit()
        else:
            print(f"Player {gameClass.current_player} has not won yet. The game continues.")
    gameClass.switch_player()

def Movement_loop():
    print("Placement phase is over. Moving to movement phase.")
    gameClass.current_phase = "movement"
    gameClass.board_display()
    player_source, player_destination = gameClass.Movement(gameClass.board, gameClass.current_player)
    gameClass.board[player_source] = str(player_source + 1)
    gameClass.board[player_destination] = gameClass.current_player
    gameClass.board_display()
    print(f"You chose to move your stone from position: {player_source + 1} to position: {player_destination + 1}")
    check = gameClass.check_winner(gameClass.board, gameClass.current_player)
    if check:
        gameClass.board_display() 
        print(f"Player {gameClass.current_player} wins!")
        return True
    else:
        gameClass.switch_player()
        return False

def main():
    while True:
        if stone_placed < 6:
            Placemen_loop()
        elif stone_placed == 6 and not gameClass.check_winner(gameClass.board, gameClass.current_player):
            Movement_loop()
            continue
                


if __name__ == "__main__":  
    main()