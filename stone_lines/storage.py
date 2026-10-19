"""Statistics JSON storage, separated from game rules and terminal UI."""

import json
from pathlib import Path

# This absolute path works even when `python /path/to/main.py` is run elsewhere.
DEFAULT_PATH = Path(__file__).resolve().parent.parent / "data" / "statistics.json"


def load_statistics(file_path=None):
    path = Path(file_path) if file_path is not None else DEFAULT_PATH
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as file:
            records = json.load(file)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read statistics file: {path}") from exc
    if not isinstance(records, dict):
        raise ValueError("Statistics file must contain a JSON object.")
    return records


def save_statistics(statistics, file_path=None):
    """Write JSON atomically to avoid leaving a half-written file."""
    path = Path(file_path) if file_path is not None else DEFAULT_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_name(path.name + ".tmp")
    with temporary_path.open("w", encoding="utf-8") as file:
        json.dump(statistics, file, indent=2, ensure_ascii=False)
        file.write("\n")
    temporary_path.replace(path)


def ensure_player(statistics, name):
    """Support old Week 5 records that did not include a draws field."""
    entry = statistics.setdefault(name, {})
    for key in ("games", "wins", "losses", "draws"):
        entry.setdefault(key, 0)
    entry.setdefault("opponents", {})
    return entry


def record_result(statistics, name_x, name_o, result):
    """Update a finished match exactly once (call from the app only)."""
    if name_x.casefold() == name_o.casefold():
        raise ValueError("Player names must differ.")
    if result not in ("X", "O", "draw"):
        raise ValueError("Result must be X, O, or draw.")
    x = ensure_player(statistics, name_x)
    o = ensure_player(statistics, name_o)
    for own, opponent_name in ((x, name_o), (o, name_x)):
        own["games"] += 1
        opposing = own["opponents"].setdefault(opponent_name, {})
        for key in ("games", "wins", "losses", "draws"):
            opposing.setdefault(key, 0)
        opposing["games"] += 1
    if result == "draw":
        x["draws"] += 1
        o["draws"] += 1
        x["opponents"][name_o]["draws"] += 1
        o["opponents"][name_x]["draws"] += 1
    else:
        winner, loser = (x, o) if result == "X" else (o, x)
        winner_name, loser_name = (name_x, name_o) if result == "X" else (name_o, name_x)
        winner["wins"] += 1
        loser["losses"] += 1
        winner["opponents"][loser_name]["wins"] += 1
        loser["opponents"][winner_name]["losses"] += 1
