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


def test_connected_components_two_groups():
    edges = [
        ("A", "B"),
        ("B", "C"),
        ("D", "E"),
    ]

    assert count_connected_components(edges) == 2


def test_connected_components_single_group():
    edges = [
        ("A", "B"),
        ("B", "C"),
        ("C", "A"),
    ]

    assert count_connected_components(edges) == 1


def test_connected_components_three_groups():
    edges = [
        ("A", "B"),
        ("C", "D"),
        ("E", "F"),
    ]

    assert count_connected_components(edges) == 3


def test_connected_components_empty_edges():
    assert count_connected_components([]) == 0


def test_connected_components_treats_edges_as_undirected():
    edges = [
        ("B", "A"),
        ("B", "C"),
        ("E", "D"),
    ]

    assert count_connected_components(edges) == 2