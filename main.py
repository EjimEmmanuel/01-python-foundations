import game as g
import constant as c
from rich import print
from rich.console import Console




console = Console()
stone_placed = 0
""" Argument creator for the game """
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]   
gameClass = g.Game(board, "X", current_phase="placement", winner_state=None)

"""the main function """
def Placement_loop():
    print(f"[dim White]Placement onging...[/dim White]")
    gameClass.board_display()  
    placement_index = gameClass.placement(gameClass.current_player)
    gameClass.board[placement_index] =  gameClass.current_player 
    print(f"You chose to place your stone at position: {placement_index + 1}")
    global stone_placed
    stone_placed += 1
    if stone_placed >= 5:
        check = gameClass.check_winner(gameClass.board, gameClass.current_player)
        won_lines = []
        if check:
            for line in c.winning_lines:
                if all(gameClass.board[pos] == gameClass.current_player for pos in line):
                    won_lines.append(num + 1 for num in line)
            gameClass.board_display() 
            console.print(f"Player {gameClass.current_player} wins on board positions: {won_lines }!", style="bold blue on black")
            exit()
        else:
            print(f"Player {gameClass.current_player} has not won yet. The game continues.")
            print("Placement phase is over. Moving to movement phase.")
    gameClass.switch_player()

def Movement_loop():
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
        won_lines = [num + 1 for line in c.winning_lines if all(gameClass.board[pos] == gameClass.current_player for pos in line) for num in line]
        console.print(f"Player {gameClass.current_player} wins on board positions: {won_lines}!", style="bold blue on black")
        return True
        
    else:
        gameClass.switch_player()
        return False

def main():
    while True:
        print("[bold blue]STONE LINES[/bold blue]")
        if stone_placed < 6:
            Placement_loop()
        elif stone_placed == 6 and not gameClass.check_winner(gameClass.board, gameClass.current_player):
            print("[dim white]Movement phase is going on...[/dim white]")
            Movement_loop()
            continue
                


if __name__ == "__main__":  
    main()