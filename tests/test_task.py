from task import *
import pytest


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

from task import compute_topological_sort


def test_topological_sort_simple_chain():
    directed_edges = [
        ("A", "B"),
        ("B", "C"),
    ]

    assert compute_topological_sort(directed_edges) == ["A", "B", "C"]


def test_topological_sort_multiple_dependencies():
    directed_edges = [
        ("Task1", "Task3"),
        ("Task2", "Task3"),
        ("Task3", "Task4"),
    ]

    result = compute_topological_sort(directed_edges)

    assert set(result) == {"Task1", "Task2", "Task3", "Task4"}
    assert result.index("Task1") < result.index("Task3")
    assert result.index("Task2") < result.index("Task3")
    assert result.index("Task3") < result.index("Task4")


def test_topological_sort_compile_workflow():
    directed_edges = [
        ("compile", "test"),
        ("test", "deploy"),
    ]

    assert compute_topological_sort(directed_edges) == [
        "compile",
        "test",
        "deploy",
    ]


def test_topological_sort_empty_edges():
    assert compute_topological_sort([]) == []


def test_topological_sort_respects_all_dependencies():
    directed_edges = [
        ("A", "C"),
        ("B", "C"),
        ("C", "D"),
        ("B", "E"),
    ]

    result = compute_topological_sort(directed_edges)

    assert set(result) == {"A", "B", "C", "D", "E"}
    assert result.index("A") < result.index("C")
    assert result.index("B") < result.index("C")
    assert result.index("C") < result.index("D")
    assert result.index("B") < result.index("E")

def test_average_clustering_triangle():
    edges = [
        ("A", "B"),
        ("B", "C"),
        ("C", "A"),
    ]

    assert compute_average_clustering(edges) == pytest.approx(1.0)


def test_average_clustering_line_graph():
    edges = [
        ("A", "B"),
        ("B", "C"),
        ("C", "D"),
    ]

    assert compute_average_clustering(edges) == pytest.approx(0.0)


def test_average_clustering_triangle_with_tail():
    edges = [
        ("A", "B"),
        ("B", "C"),
        ("A", "C"),
        ("C", "D"),
    ]

    assert compute_average_clustering(edges) == pytest.approx(
        0.5833333333333334
    )


def test_average_clustering_empty_edges():
    assert compute_average_clustering([]) == 0.0


def test_average_clustering_returns_float():
    result = compute_average_clustering([("A", "B")])

    assert isinstance(result, float)