"""Reusable teaching boards. Use only in tests, not game implementation."""
from stone_lines.game import Game
from stone_lines.player import Player


def state(board, turn='X', phase='placement', stones=None):
    """Build a controlled game state; arguments are nine screen cells."""
    if len(board) != 9:
        raise ValueError('Expected exactly nine positions')
    g = Game(Player('Emma', 'X'), Player('Robot', 'O'))
    g.board = [value if value in ('X','O') else str(i+1) for i,value in enumerate(board)]
    g.current_player = turn
    g.phase = phase
    g.stones_placed = stones if stones is not None else sum(c in ('X','O') for c in board)
    return g
