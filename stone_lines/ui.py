"""All terminal rendering and human prompts belong here, not in game.py."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table


class QuitMatch(Exception):
    """User requested to stop a match without recording a result."""


class TerminalUI:
    def __init__(self, console=None):
        self.console = console or Console()

    def welcome(self):
        self.console.print(Panel.fit("[bold cyan]STONE LINES: ARENA[/bold cyan]\nWeek 6 prepared edition", border_style="cyan"))

    def menu(self):
        self.console.print("\n[bold]Main menu[/bold]")
        self.console.print("1. Human vs Human")
        self.console.print("2. Human vs Computer — Random [dim](Week 6 task)[/dim]")
        self.console.print("3. Human vs Computer — Rule-Based [dim](Week 6 task)[/dim]")
        self.console.print("4. View rules")
        self.console.print("5. Quit")
        return self.console.input("Select 1–5: ").strip()

    def rules(self):
        self.console.print(Panel(
            "Two players, X and O, have three stones each.\n"
            "During placement, alternate placing on empty positions 1–9.\n"
            "After six placements without a win, move a stone to an empty connected position.\n"
            "Three stones in a row, column, or diagonal wins.\n"
            "A player with no legal movement makes the match a draw.\n"
            "Commands during a turn: [bold]help[/bold], [bold]quit[/bold].",
            title="Rules", border_style="blue"))

    def ask_name(self, symbol, other_name=None):
        while True:
            name = self.console.input(f"Name for player {symbol} (4–30 characters): ").strip()
            if not 4 <= len(name) <= 30:
                self.error("Enter a name with 4–30 characters.")
            elif other_name and name.casefold() == other_name.casefold():
                self.error("The two players must have different names.")
            else:
                return name

    @staticmethod
    def styled_cell(value):
        if value == "X":
            return "[bold red]X[/bold red]"
        if value == "O":
            return "[bold bright_blue]O[/bold bright_blue]"
        return f"[bright_yellow]{value}[/bright_yellow]"

    def board(self, game, statistics=None):
        b = [self.styled_cell(value) for value in game.board]
        board = (f"     {b[0]} ───── {b[1]} ───── {b[2]}\n"
                 "     │ \\     │     / │\n"
                 "     │   \\   │   /   │\n"
                 f"     {b[3]} ───── {b[4]} ───── {b[5]}\n"
                 "     │   /   │   \\   │\n"
                 "     │ /     │     \\ │\n"
                 f"     {b[6]} ───── {b[7]} ───── {b[8]}")
        self.console.print(Panel(board, title="Stone Lines Board", border_style="cyan"))
        table = Table(show_header=True, box=None)
        table.add_column("Player")
        table.add_column("Stone")
        table.add_column("Wins", justify="right")
        for player in (game.player_x, game.player_o):
            wins = (statistics or {}).get(player.name, {}).get("wins", 0)
            table.add_row(player.name, player.symbol, str(wins))
        self.console.print(table)
        phase = "Placement" if game.phase == "placement" else "Movement"
        self.console.print(f"Phase: [bold]{phase}[/bold]  |  Turn: [bold]{game.player_for(game.current_player).name} ({game.current_player})[/bold]")

    def error(self, message):
        self.console.print(f"[bold red]Error:[/bold red] {message}")

    def info(self, message):
        self.console.print(f"[cyan]{message}[/cyan]")

    def _number(self, message):
        """Read a human board position, handling common commands consistently."""
        while True:
            text = self.console.input(message).strip()
            if text.lower() in ("q", "quit", "exit"):
                raise QuitMatch()
            if text.lower() in ("h", "help"):
                self.rules()
                continue
            if not text.isdigit() or not 1 <= int(text) <= 9:
                self.error("Enter a position from 1 to 9, or 'help'/'quit'.")
                continue
            return int(text) - 1

    def ask_human_action(self, game):
        """Return a legal action; this method never executes it."""
        allowed = game.get_legal_actions()
        if game.phase == "placement":
            while True:
                position = self._number("Place stone at (1–9): ")
                action = ("place", position)
                if action in allowed:
                    return action
                self.error("Position is already occupied.")
        else:
            while True:
                source = self._number("Move stone from (1–9): ")
                choices = [a for a in allowed if a[1] == source]
                if not choices:
                    self.error("That stone is not yours or has no legal destination.")
                    continue
                options = ", ".join(str(a[2] + 1) for a in choices)
                self.info(f"Available destinations: {options}")
                target = self._number("Move to (1–9): ")
                action = ("move", source, target)
                if action in choices:
                    return action
                self.error("Choose an empty, connected destination from the list.")

    def finished(self, game):
        if game.result == "draw":
            self.console.print(Panel("[bold yellow]DRAW[/bold yellow]", border_style="yellow"))
        else:
            player = game.player_for(game.winner)
            self.console.print(Panel(f"[bold green]{player.name} ({game.winner}) wins![/bold green]", border_style="green"))

    def ask_replay(self):
        while True:
            reply = self.console.input("Play another match with these players? [y/n]: ").strip().lower()
            if reply in ("y", "yes"):
                return True
            if reply in ("n", "no"):
                return False
            self.error("Please enter y or n.")
