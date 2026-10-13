import networkx as nx

# Check readme.md for details on each sub-task

def calculate_node_degrees(edges: list) -> dict:
    if not edges:
        return {}

    G = nx.Graph()
    G.add_edges_from(edges)

    return dict(G.degree())

def find_shortest_path(edges: list, source: str, target: str) -> list:
    """Sub-task 2: Find the shortest path between source and target nodes."""
    graph = nx.Graph()
    graph.add_edges_from(edges)
    return nx.shortest_path(graph, source=source, target=target)

def count_connected_components(edges: list) -> int:
    """Sub-task 3: Count the number of connected components in an undirected graph."""
    pass

def compute_topological_sort(directed_edges: list) -> list:
    """Sub-task 4: Compute a topological ordering of nodes in a DAG."""
    pass

def compute_average_clustering(edges: list) -> float:
    """Sub-task 5: Compute the average clustering coefficient of an undirected graph."""
    pass

def main():
    print("Sub-task 1:", calculate_node_degrees([("A", "B"), ("B", "C"), ("B", "D")]))
    print("Sub-task 2:", find_shortest_path([("A", "B"), ("B", "C"), ("A", "C"), ("C", "D")], "A", "D"))
    print("Sub-task 3:", count_connected_components([("A", "B"), ("B", "C"), ("D", "E")]))
    print("Sub-task 4:", compute_topological_sort([("A", "B"), ("B", "C")]))
    print("Sub-task 5:", compute_average_clustering([("A", "B"), ("B", "C"), ("C", "A")]))

if __name__ == "__main__":
    main()
