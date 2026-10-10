import constant as c
from rich.console import Console
import storage as s

"""  object creation for the game """
console = Console()

class Game:
    def __init__(self, board, current_player, current_player_name, current_phase, player_X, player_O, stone_placed):
        self.board = board
        self.current_player = current_player
        self.current_phase = current_phase
        self.player_X = player_X
        self.player_O = player_O
        self.current_player_name = current_player_name
        self.stone_placed = stone_placed
    """ winning logic"""
    def check_winner(self, board, current_player):
        for line in c.winning_lines:
            if board[line[0]] == current_player and board[line[1]] == current_player and board[line[2]] == current_player:
                return True
        return False
    def add_score(self, current_player, storage):
        if not self.check_winner(self.board, current_player):
            return
        if current_player == "X":
            winner = self.player_X.name
            loser = self.player_O.name
            storage[winner]["opponents"].setdefault(
                loser, {"games": 0, "wins": 0, "losses": 0}
            )

            storage[loser]["opponents"].setdefault(
                winner, {"games": 0, "wins": 0, "losses": 0}
            )
            # Overall statistics when X wins
            storage[winner]["games"] += 1
            storage[winner]["wins"] += 1

            storage[loser]["games"] += 1
            storage[loser]["losses"] += 1


            ## Statistics against this particular opponent when X wins
            storage[winner]["opponents"][loser]["games"] += 1
            storage[winner]["opponents"][loser]["wins"] += 1

            storage[loser]["opponents"][winner]["games"] += 1
            storage[loser]["opponents"][winner]["losses"] += 1
            console.print(f"Player X {self.player_X.name}'s score: {storage[winner]['wins']}")
            console.print(f"Player O {self.player_O.name}'s score: {storage[loser]['wins']}")
        else:
            winner = self.player_O.name
            loser = self.player_X.name
            storage[winner]["opponents"].setdefault(
                 loser, {"games": 0, "wins": 0, "losses": 0}
             )
 
            storage[loser]["opponents"].setdefault(
                 winner, {"games": 0, "wins": 0, "losses": 0}
             )
             # Overall statistics when O wins
            storage[winner]["games"] += 1
            storage[winner]["wins"] += 1
 
            storage[loser]["games"] += 1
            storage[loser]["losses"] += 1
 
 
             ## Statistics against this particular opponent when O wins
            storage[winner]["opponents"][loser]["games"] += 1
            storage[winner]["opponents"][loser]["wins"] += 1
 
            storage[loser]["opponents"][winner]["games"] += 1
            storage[loser]["opponents"][winner]["losses"] += 1
            console.print(f"Player X {self.player_X.name}'s score: {storage[loser]['wins']}")
            console.print(f"Player O {self.player_O.name}'s score: {storage[winner]['wins']}")
        s.dump_statistics(storage)
        """ The game loop"""        

    """ board displaying and colouring """
    def colour_symbol(self, symbol):
        if symbol == "X":
            return "[bold red]X[/bold red]"
        elif symbol == "O":
            return "[bold blue]O[/bold blue]"
        else:
            return f"[yellow]{symbol}[/yellow]"
    def board_display(self):
        console.print(
            f"{self.colour_symbol(self.board[0])} "
            "[dim white]─────[/dim white] "
            f"{self.colour_symbol(self.board[1])} "
            "[dim white]─────[/dim white] "
            f"{self.colour_symbol(self.board[2])}"
        )
        console.print("[dim white]│ \\     │     / │[/dim white]")
        console.print("[dim white]│   \\   │   /   │[/dim white]")

        console.print(
            f"{self.colour_symbol(self.board[3])} "
            "[dim white]─────[/dim white] "
            f"{self.colour_symbol(self.board[4])} "
            "[dim white]─────[/dim white] "
            f"{self.colour_symbol(self.board[5])}"
        )

        console.print("[dim white]│   /   │   \\   │[/dim white]")
        console.print("[dim white]│ /     │     \\ │[/dim white]")

        console.print(
            f"{self.colour_symbol(self.board[6])} "
            "[dim white]─────[/dim white] "
            f"{self.colour_symbol(self.board[7])} "
            "[dim white]─────[/dim white] "
            f"{self.colour_symbol(self.board[8])}"
        )
    """ player switching"""
    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    """get placement position"""
    def get_placement_position(self, current_player, current_player_name):
        while True:
            raw_placement = console.input(
                f"Player {self.colour_symbol(current_player)} "
                f"({current_player_name})'s Turn — "
                "[bold white]please select a position to place your stone (1-9):[/bold white] "
            ).strip()      
            if not raw_placement.isdigit():
                self.board_display()
                print("You entered an invalid digit. Pls enter a valid number from 1 to 9.")
                continue
            elif int(raw_placement) not in range(1, 10):
                self.board_display()
                console.print("[blink red] you entered a number not in board range. Pls enter a valid number btw 1 to 9.[/blink red]")
                continue
            else:
                player_position = int(raw_placement) - 1 
                if self.board[player_position] in ["O", "X"]:
                    self.board_display()
                    console.print("[blink red]Spot already occupied. Please enter a number between 1 to 9.[/blink red]")
                    continue
                return player_position  
    def get_movement_position(self, current_player, current_player_name, connections):
        while True:
            raw_source = console.input(
                f"Player {self.colour_symbol(current_player)} "
                f"({current_player_name})'s Turn — "
                "[bold white]please select a position of your stone (1-9):[/bold white] "
            ).strip()          
            if not raw_source.isdigit():
                console.print("[blink red] Invalid input. Please enter a valid number between 1 to 9.[/blink red]")
                continue
            elif int(raw_source) not in range(1, 10):
                self.board_display()
                console.print("[blink red]you entered a number not in board range. Pls enter a valid number btw 1 to 9.[/blink red]")
                continue
            elif self.board[int(raw_source) - 1] != current_player:
                self.board_display()
                console.print("You can only move your own stone: Please select your valid stone position.", style="red on white")
                continue 
            else:
                real_source = int(raw_source) - 1 
                break
        available_destinations = []
        pos = connections[real_source]
        for p in pos:
            if self.board[p] not in ["X", "O"]:
                available_destinations.append(p + 1) 
        while True:
            self.board_display()
            raw_destination = console.input(
                f"Player {self.colour_symbol(current_player)} "
                f"({current_player_name})'s Turn — "
                f"please select your stone's destination: "
                f"[dim yellow]available destinations: [/dim yellow][bold yellow]{available_destinations}[/bold yellow]: "
            ).strip()      
            if not raw_destination.isdigit():
                self.board_display()
                print("[blink red]You entered an invalid digit. Pls enter a valid number btw 1 to 9.[/blink red]")
                continue
            elif int(raw_destination) not in range(1, 10):
                self.board_display()
                print("[blink red]You entered a number not in board range. Pls enter a valid number btw 1 to 9.[/blink red]")
                continue
            elif self.board[int(raw_destination) - 1] in ["X", "O"]:
                self.board_display()
                print("[blink red]Invalid input. Please enter a valid empty destination.[/blink red]")
                continue
            elif int(raw_destination) - 1 not in connections[real_source]:
                self.board_display()
                print("[blink red]Invalid input. Please enter a valid connected destination.[/blink red]")
                continue
            else:
                real_destination = int(raw_destination) - 1
                return real_source, real_destination
    def new_round(self):
        while True:
            new_round_input = console.input(f"[bold white] Do you really want to play again!!!: [y/n] [/bold white]")
            if new_round_input == "yes" or new_round_input == "y":
                return True
            elif new_round_input == "no" or new_round_input == "n":
                console.print("Thank you for playing Stone Lines! Goodbye!", style="bold red on black")
                return False            
            else:
                console.print("Invalid input. Please enter - [yes/no or y/n].", style="bold red on black")
                continue
        
    def Movement(self, current_player):
        return self.get_movement_position(current_player, self.player_X.name if self.current_player == "X" else self.player_O.name , c.connections)
    """ placement still follows"""
    def placement(self, current_player, current_player_name):
        return self.get_placement_position(current_player, current_player_name)



