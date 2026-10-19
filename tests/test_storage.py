import json

import pytest

from stone_lines.storage import ensure_player, load_statistics, record_result, save_statistics


def test_missing_statistics_is_empty(tmp_path):
    assert load_statistics(tmp_path / "missing.json") == {}


def test_write_read_statistics(tmp_path):
    path = tmp_path / "data" / "stats.json"
    statistics = {"Emma": {"wins": 2}}
    save_statistics(statistics, path)
    assert load_statistics(path) == statistics
    assert not path.with_name("stats.json.tmp").exists()


def test_bad_json_has_clear_error(tmp_path):
    path = tmp_path / "broken.json"
    path.write_text("{invalid json")
    with pytest.raises(ValueError, match="Cannot read"):
        load_statistics(path)


def test_wrong_json_shape_rejected(tmp_path):
    path = tmp_path / "wrong.json"
    path.write_text("[]")
    with pytest.raises(ValueError, match="JSON object"):
        load_statistics(path)


def test_record_x_win_tracks_both_players():
    stats = {}
    record_result(stats, "Emma", "Chioma", "X")
    assert stats["Emma"]["games"] == 1
    assert stats["Emma"]["wins"] == 1
    assert stats["Chioma"]["losses"] == 1
    assert stats["Emma"]["opponents"]["Chioma"]["wins"] == 1
    assert stats["Chioma"]["opponents"]["Emma"]["losses"] == 1


def test_record_o_win_tracks_both_players():
    stats = {}
    record_result(stats, "Emma", "Chioma", "O")
    assert stats["Chioma"]["wins"] == 1
    assert stats["Emma"]["losses"] == 1


def test_record_draw_tracks_both_players():
    stats = {}
    record_result(stats, "Emma", "Chioma", "draw")
    assert stats["Chioma"]["draws"] == 1
    assert stats["Emma"]["draws"] == 1
    assert stats["Emma"]["opponents"]["Chioma"]["draws"] == 1


def test_old_statistics_are_extended_safely():
    stats = {"Emma": {"games": 1, "wins": 1, "losses": 0, "opponents": {}}}
    assert ensure_player(stats, "Emma")["draws"] == 0


def test_reject_same_name_and_unknown_result():
    with pytest.raises(ValueError):
        record_result({}, "Emma", "emma", "X")
    with pytest.raises(ValueError):
        record_result({}, "Emma", "Chioma", None)
