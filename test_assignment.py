import ast
import inspect
import textwrap

import pytest

from assignment import (
    read_line,
    reverse_lines,
    merge_files,
    find_score,
    update_score,
)


def calls_in(function):
    tree = ast.parse(textwrap.dedent(inspect.getsource(function)))
    names = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            names.append(node.func.attr)
    return names


@pytest.mark.parametrize("content, line_number, expected", [
    ["Mon\nTue\nWed\n", 1, "Mon"],
    ["Mon\nTue\nWed\n", 2, "Tue"],
    ["Mon\nTue\nWed\n", 3, "Wed"],
    ["Mon\nTue", 2, "Tue"],
    ["Mon\nTue\nWed\n", 4, ""],
    ["Mon\nTue\nWed\n", 0, ""],
    ["", 1, ""],
])
def test1_read_line(tmp_path, content, line_number, expected):
    path = tmp_path / "days.txt"
    path.write_text(content)
    assert read_line(path, line_number) == expected


def test1_uses_readline(tmp_path):
    names = calls_in(read_line)
    assert "readline" in names, "read_line() must use readline()."
    assert "readlines" not in names, "Use readline(), not readlines()."
    assert "read" not in names, "Use readline(), not read()."
    path = tmp_path / "days.txt"
    path.write_text("Mon\nTue\nWed\n")
    assert read_line(path, 2) == "Tue"


@pytest.mark.parametrize("content, expected, expected_count", [
    ["one\ntwo\nthree\n", "three\ntwo\none\n", 3],
    ["one\ntwo\nthree", "three\ntwo\none\n", 3],
    ["only\n", "only\n", 1],
    ["", "", 0],
])
def test2_reverse_lines(tmp_path, content, expected, expected_count):
    source = tmp_path / "in.txt"
    destination = tmp_path / "out.txt"
    source.write_text(content)
    result = reverse_lines(source, destination)
    assert destination.read_text() == expected
    assert result == expected_count


def test2_source_unchanged(tmp_path):
    source = tmp_path / "in.txt"
    destination = tmp_path / "out.txt"
    source.write_text("one\ntwo\n")
    reverse_lines(source, destination)
    assert source.read_text() == "one\ntwo\n"
    assert destination.read_text() == "two\none\n"


@pytest.mark.parametrize("first_content, second_content, expected, expected_count", [
    ["Bat\nSaraa\n", "Anu\nDorj\n", "Bat\nSaraa\nAnu\nDorj\n", 4],
    ["Bat\nSaraa", "Anu\n", "Bat\nSaraa\nAnu\n", 3],
    ["", "Anu\n", "Anu\n", 1],
    ["Bat\n", "", "Bat\n", 1],
    ["", "", "", 0],
])
def test3_merge_files(tmp_path, first_content, second_content, expected, expected_count):
    first = tmp_path / "class_a.txt"
    second = tmp_path / "class_b.txt"
    destination = tmp_path / "all.txt"
    first.write_text(first_content)
    second.write_text(second_content)
    result = merge_files(first, second, destination)
    assert destination.read_text() == expected
    assert result == expected_count


def test3_replaces_old_destination(tmp_path):
    first = tmp_path / "class_a.txt"
    second = tmp_path / "class_b.txt"
    destination = tmp_path / "all.txt"
    first.write_text("Bat\n")
    second.write_text("Anu\n")
    destination.write_text("OLD DATA\n")
    merge_files(first, second, destination)
    assert destination.read_text() == "Bat\nAnu\n"
    assert first.read_text() == "Bat\n"
    assert second.read_text() == "Anu\n"


SCORES = "Bat,78\nSaraa,91\nTuguldur,65\nAnu,88\n"


@pytest.mark.parametrize("name, expected", [
    ["Bat", 78],
    ["Saraa", 91],
    ["Anu", 88],
    ["Tuguldur", 65],
])
def test4_find_score(tmp_path, name, expected):
    path = tmp_path / "scores.txt"
    path.write_text(SCORES)
    assert find_score(path, name) == expected


@pytest.mark.parametrize("content, name", [
    [SCORES, "Dorj"],
    [SCORES, "bat"],
    ["", "Bat"],
    ["Bat,78\n\nSaraa,91\n\n", "Anu"],
])
def test4_not_found(tmp_path, content, name):
    path = tmp_path / "scores.txt"
    path.write_text(content)
    assert find_score(path, name) == -1


@pytest.mark.parametrize("name, new_score, expected", [
    ["Saraa", 95, "Bat,78\nSaraa,95\nTuguldur,65\nAnu,88\n"],
    ["Bat", 0, "Bat,0\nSaraa,91\nTuguldur,65\nAnu,88\n"],
    ["Anu", 100, "Bat,78\nSaraa,91\nTuguldur,65\nAnu,100\n"],
])
def test5_update_score(tmp_path, name, new_score, expected):
    path = tmp_path / "scores.txt"
    path.write_text(SCORES)
    assert update_score(path, name, new_score) == True
    assert path.read_text() == expected


@pytest.mark.parametrize("content, name", [
    [SCORES, "Dorj"],
    [SCORES, "saraa"],
    ["", "Bat"],
])
def test5_name_not_found(tmp_path, content, name):
    path = tmp_path / "scores.txt"
    path.write_text(content)
    assert update_score(path, name, 50) == False
    assert path.read_text() == content
