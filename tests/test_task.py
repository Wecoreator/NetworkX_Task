from task import *


def test_node_degrees_example():
    edges = [("A", "B"), ("B", "C"), ("B", "D")]

    assert calculate_node_degrees(edges) == {
        "A": 1,
        "B": 3,
        "C": 1,
        "D": 1
    }