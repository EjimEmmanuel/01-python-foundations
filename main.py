import time
import game 
import constant as c
from rich import print
from rich.console import Console
import player as p
import storage as s

console = Console()


""" Helper function"""
def view_rules():
    print("Rules of the game:")
    print("1. The game is played on a 3x3 grid.")
    print("2. Players take turns placing their stones (X or O) on the grid.")
    print("3. The first player to align three of their stones in a row, column, or diagonal wins.")
    print("4. If all valid six positions are filled and no player has won, the game commences into movement phase: movement of stones to connected positions.")

"""game setup function"""

def create_game(player_X=None, player_O=None):
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]   
    if player_X is None and player_O is None:
        name_x = p.Player.get_player_name("X")
        name_O = p.Player.get_player_name("O")
        player_X = p.Player(name_x, "X")
        player_O = p.Player(name_O, "O")
    return game.Game(board, player_X.symbol, player_X.name, "placement", player_X, player_O, 0)
    

def Placement_loop(gameClass, just_storage):
    console.print(f"[dim White]Placement onging...[/dim White]")
    gameClass.board_display()  
    placement_index = gameClass.placement(gameClass.current_player, gameClass.player_X.name if gameClass.current_player == "X" else gameClass.player_O.name)
    gameClass.board[placement_index] =  gameClass.current_player 
    console.print(f"You chose to place your stone at position: {placement_index + 1}")
    gameClass.stone_placed += 1
    if gameClass.stone_placed >= 5:
        check = gameClass.check_winner(gameClass.board, gameClass.current_player)
        if check:
            gameClass.board_display() 
            won_lines = [num + 1 for line in c.winning_lines if all(gameClass.board[pos] == gameClass.current_player for pos in line) for num in line]
            console.print(f"Player {gameClass.current_player} wins on board positions: {won_lines }!", style="bold blue on black")
            gameClass.add_score(gameClass.current_player, just_storage)
            time.sleep(2)
            if gameClass.new_round():
                run_game()
            else:
                exit()
        else:
            console.print(f"Player {gameClass.current_player} has not won yet. The game continues.")
            console.print("Placement phase is over. Moving to movement phase.")
    gameClass.switch_player()

def Movement_loop(gameClass, just_storage):
    gameClass.current_phase = "movement"
    console.print(f"[dim White]Movement phase is onging...[/dim White]")
    gameClass.board_display()
    player_source, player_destination = gameClass.Movement(gameClass.board, gameClass.current_player)
    gameClass.board[player_source] = str(player_source + 1)
    gameClass.board[player_destination] = gameClass.current_player
    gameClass.board_display()
    print(f"You chose to move your stone from position: {player_source + 1} to position: {player_destination + 1}")
    check = gameClass.check_winner(gameClass.board, gameClass.current_player)
    if check:
        gameClass.board_display() 
        won_lines = [num + 1 for line in c.winning_lines if all(gameClass.board[pos] == gameClass.current_player for pos in line) for num in line]
        console.print(f"Player {gameClass.current_player} wins on board positions: {won_lines}!", style="bold blue on black")
        gameClass.add_score(gameClass.current_player, just_storage)
        console.print()
        time.sleep(2)
        if gameClass.new_round():
            run_game()
        else:
            exit()
    else:
        gameClass.switch_player()
        return False


def run_game():
    storage = s.initialize_statistics()
    gameClass = create_game()
    if gameClass.player_X.name not in storage:
        storage[gameClass.player_X.name] = {"games": 0, "wins": 0, "losses": 0}
    if gameClass.player_O.name not in storage:
        storage[gameClass.player_O.name] = {"games": 0, "wins": 0, "losses": 0}
    s.dump_statistics(storage)
    while True:
        print("[bold blue]STONE LINES[/bold blue]")
        if gameClass.stone_placed < 6:
            Placement_loop(gameClass, storage)
        elif gameClass.stone_placed == 6 and not gameClass.check_winner(gameClass.board, gameClass.current_player):
            print("[dim white]Movement phase is going on...[/dim white]")
            Movement_loop(gameClass, storage)
            continue

def main():
    console.print("WELCOME TO STONE LINES", style="bold red on white")
    print("")
    console.print("TERMINAL EDITION", style="dim green on white")
    console.print("=" * 50)
    print("")

    while True:
        print("1. Start Game")
        print("2. View Rules")
        print("3. Quit")
        choose = input("Choose any option: ")
        if choose == "1":
            print("Starting the game...")
            run_game()
        elif choose == "2" or choose.lower() == "help" or choose.lower() == "r":
            view_rules()
        elif choose == "3" or choose.lower() == "quit" or choose.lower() == "q":
            print("Quitting the game...")
            exit()
        else:
            print("Invalid option. Please choose 1, 2, or 3.")
            continue


if __name__ == "__main__":  
    main()