from rich.console import Console


console = Console()


class Player:
    def __init__(self, name, symbol, score=0):
        self.name = name
        self.symbol = symbol
        self.score = score
    @staticmethod
    def get_player_name(symbol):
        while True:
            name = console.input(f"Player {symbol}, please enter your name: ")
            match  name:
                case "":
                    console.print("Name cannot be empty. Please enter a valid name.", style="bold red")
                case _ if 4 <= len(name) <= 30:
                    name = name
                    return name
                case _:
                    console.print("Invalid name. Please enter a name with 5-30 characters.", style="bold red")
                    continue

