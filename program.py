from typing import Optional, List
from graph_impl import Graph, Vertex, Edge
from graph_interfaces import IGraph, IVertex, IEdge

import csv
import os

def read_graph(file_path: str) -> IGraph: 
    """" reads the graph from a csv file (graph.txt).
    uses source, destination, highway, distance
    and constructs a directed graph
     """

    graph = Graph()
    
    """Read the graph from the file and return the graph object"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Graph file not found: {file_path}")

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            source_name = row["source"].strip()
            dest_name = row["destination"].strip()
            edge_name = row["highway"].strip()
            distance = float(row["distance"])

            # Source vertex
            source_vertex = None
            for v in graph.get_vertices():
                if v.get_name() == source_name:
                    source_vertex = v
                    break
            if source_vertex is None:
                source_vertex = Vertex(source_name)
                graph.add_vertex(source_vertex)

            # Destination vertex
            dest_vertex = None
            for v in graph.get_vertices():
                if v.get_name() == dest_name:
                    dest_vertex = v
                    break
            if dest_vertex is None:
                dest_vertex = Vertex(dest_name)
                graph.add_vertex(dest_vertex)

            #Edge:
            edge = Edge(edge_name, dest_vertex, distance)
            graph.add_edge(edge, from_vertex_name=source_name)

    return graph


def print_dfs(graph: IGraph, start_vertex: IVertex) -> None: 
    """Print the DFS traversal of the graph starting from the start vertex"""
    
    visited = set()
    order = []                          # track the traversal order

    def dfs(v: IVertex):
        if v.get_name() in visited:
            return 
        visited.add(v.get_name())
        order.append(v.get_name())      # track the traversal order
        print(v.get_name())

        for edge in v.get_edges():
            dfs(edge.get_destination())

    print("\nDFS Traversal:")
    dfs(start_vertex)
    print() 

    # Paste output in DFS.txt file:
    with open('DFS.txt', 'w') as f:
        f.write('\n'.join(order))


def print_bfs(graph: IGraph, start_vertex: IVertex) -> None: 
    """Print the BFS traversal of the graph starting from the start vertex"""
    
    # Reset all vertices
    for v in graph.get_vertices():
        v.set_visited(False)

    visited_order = []
    to_visit = [start_vertex]
    start_vertex.set_visited(True)

    while to_visit:
        current = to_visit.pop(0)                   # remove the first element
        visited_order.append(current.get_name())

        for edge in current.get_edges():
            neighbor = edge.get_destination()
            if not neighbor.is_visited():
                neighbor.set_visited(True)
                to_visit.append(neighbor)

    print("BFS Traversal:")
    for v in visited_order:
        print(v)

    # Paste output in BFS.txt file:
    with open('BFS.txt', 'w') as f:
        f.write('\n'.join(visited_order))


def main() -> None:
    graph: IGraph = read_graph("graph.txt")
    start_vertex_name: str  = input("Enter the start vertex name: ")

    # Find the start vertex object
    start_vertex: Optional[IVertex]= next((v for v in graph.get_vertices() if v.get_name() == start_vertex_name), None)

    if start_vertex is None:
        print("Start vertex not found")
        return
    
    print_dfs(graph, start_vertex)
    print_bfs(graph, start_vertex)


if __name__ == "__main__":
    main()