from task import *


def test_node_degrees_example():
    edges = [("A", "B"), ("B", "C"), ("B", "D")]

    assert calculate_node_degrees(edges) == {
        "A": 1,
        "B": 3,
        "C": 1,
        "D": 1
    }


def test_shortest_path_example():
    edges = [
        ("A", "B"),
        ("B", "C"),
        ("A", "C"),
        ("C", "D"),
    ]

    assert find_shortest_path(edges, "A", "D") == ["A", "C", "D"]


def test_shortest_path_linear_graph():
    edges = [("X", "Y"), ("Y", "Z")]

    assert find_shortest_path(edges, "X", "Z") == ["X", "Y", "Z"]


def test_shortest_path_uses_shorter_route():
    edges = [
        ("A", "B"),
        ("B", "C"),
        ("C", "D"),
        ("B", "D"),
    ]

    assert find_shortest_path(edges, "A", "D") == ["A", "B", "D"]


def test_shortest_path_treats_edges_as_undirected():
    edges = [("A", "B"), ("B", "C")]

    assert find_shortest_path(edges, "C", "A") == ["C", "B", "A"]


def test_shortest_path_direct_connection():
    edges = [("A", "B"), ("B", "C")]

    assert find_shortest_path(edges, "A", "B") == ["A", "B"]


def test_linear_path():
    edges = [("X", "Y"), ("Y", "Z")]

    assert find_shortest_path(edges, "X", "Z") == [
        "X", "Y", "Z"
    ]