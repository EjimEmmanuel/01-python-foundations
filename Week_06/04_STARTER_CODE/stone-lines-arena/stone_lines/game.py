"""Pure Stone Lines rules and state; this module never prompts or prints.

Action format is intentionally fixed for the Week 6 tasks:
    ("place", index)         for indexes 0..8
    ("move", source, target)  for indexes 0..8

The active player is game.current_player ("X" or "O").
"""

from .constants import CONNECTIONS, EMPTY_BOARD, SYMBOLS, WINNING_LINES
from .player import Player


class Game:
    """Manage one Stone Lines match. Start a new Game for a rematch."""

    def __init__(self, player_x, player_o):
        if not isinstance(player_x, Player) or not isinstance(player_o, Player):
            raise TypeError("Game requires two Player objects.")
        if player_x.symbol != "X" or player_o.symbol != "O":
            raise ValueError("Player symbols must be X and O, in that order.")
        if player_x.name.casefold() == player_o.name.casefold():
            raise ValueError("Players must have different names.")
        self.player_x = player_x
        self.player_o = player_o
        self.board = list(EMPTY_BOARD)
        self.current_player = "X"
        self.phase = "placement"
        self.stones_placed = 0
        self.winner = None       # "X", "O", or None
        self.finished = False
        self.result = None       # "X", "O", "draw", or None
        self.turns_taken = 0

    def player_for(self, symbol):
        if symbol == "X":
            return self.player_x
        if symbol == "O":
            return self.player_o
        raise ValueError("Unknown player symbol.")

    @staticmethod
    def opponent(symbol):
        if symbol == "X":
            return "O"
        if symbol == "O":
            return "X"
        raise ValueError("Unknown player symbol.")

    @staticmethod
    def is_empty_at(board, index):
        return board[index] not in SYMBOLS

    def check_winner(self, symbol, board=None):
        """Return True if this symbol currently occupies a winning line."""
        if symbol not in SYMBOLS:
            raise ValueError("Unknown player symbol.")
        positions = self.board if board is None else board
        return any(all(positions[i] == symbol for i in line) for line in WINNING_LINES)

    def winning_positions(self, symbol):
        return [tuple(i for i in line) for line in WINNING_LINES
                if all(self.board[i] == symbol for i in line)]

    def get_legal_actions(self):
        """Return every action allowed for the ACTIVE player, in stable order.

        Do not mutate the game. The computer strategies must use this API.
        """
        if self.finished:
            return []
        if self.phase == "placement":
            return [("place", i) for i in range(9)
                    if self.is_empty_at(self.board, i)]
        if self.phase == "movement":
            return [("move", source, target)
                    for source in range(9)
                    if self.board[source] == self.current_player
                    for target in CONNECTIONS[source]
                    if self.is_empty_at(self.board, target)]
        raise ValueError("Unknown game phase.")

    def apply_action(self, action):
        """Validate and execute one action, then update turn/phase/result.

        Invalid actions raise ValueError and leave ALL game state unchanged.
        There is intentionally no terminal input and no scoring here.
        """
        # Reject bool and float indexes even if Python would compare them equal
        # to an integer (True == 1 and 1.0 == 1).
        valid_shape = (
            isinstance(action, tuple)
            and len(action) in (2, 3)
            and action[0] in ("place", "move")
            and all(type(index) is int for index in action[1:])
        )
        if not valid_shape or action not in self.get_legal_actions():
            raise ValueError("That action is not legal in the current game state.")
        kind = action[0]
        if kind == "place":
            _, target = action
            self.board[target] = self.current_player
            self.stones_placed += 1
        else:
            _, source, target = action
            self.board[source] = str(source + 1)
            self.board[target] = self.current_player
        self.turns_taken += 1
        actor = self.current_player
        if self.check_winner(actor):
            self.winner = actor
            self.finished = True
            self.result = actor
            return
        if self.phase == "placement" and self.stones_placed == 6:
            self.phase = "movement"
        self.current_player = self.opponent(actor)
        # A match with no moves available is a draw; avoids an unplayable turn.
        # Repeated positions are NOT automatically a draw (future lesson topic).
        if self.phase == "movement" and not self.get_legal_actions():
            self.finished = True
            self.result = "draw"

    def copy(self):
        """Return an independent game snapshot, preserving all important state."""
        other = Game(Player(self.player_x.name, "X"),
                     Player(self.player_o.name, "O"))
        other.board = self.board.copy()
        other.current_player = self.current_player
        other.phase = self.phase
        other.stones_placed = self.stones_placed
        other.winner = self.winner
        other.finished = self.finished
        other.result = self.result
        other.turns_taken = self.turns_taken
        return other

    def preview_action(self, action):
        """Return the resulting snapshot, without modifying this game."""
        preview = self.copy()
        preview.apply_action(action)
        return preview
