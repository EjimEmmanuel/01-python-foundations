"""Player identity (not terminal input and not computer strategy)."""


class Player:
    def __init__(self, name, symbol):
        name = name.strip() if isinstance(name, str) else ""
        if not 4 <= len(name) <= 30:
            raise ValueError("Player names must contain 4–30 characters.")
        if symbol not in ("X", "O"):
            raise ValueError("Player symbol must be X or O.")
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return f"Player(name={self.name!r}, symbol={self.symbol!r})"
