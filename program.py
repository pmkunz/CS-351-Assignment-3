from typing import Optional, List
from graph_impl import Graph, Vertex, Edge
from graph_interfaces import IGraph, IVertex, IEdge

import csv
import os

def read_graph(file_path: str) -> IGraph: 
    """" reads the graph from a csv file  """
    #with header:
    #source, destination, highway, distance
    #and constructs a directed graph


    graph = Graph()
    
    """Read the graph from the file and return the graph object"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Graph file not found: {file_path}")

    #...

#...
     #...

def print_dfs(graph: IGraph, start_vertex: IVertex) -> None: 
    """Print the DFS traversal of the graph starting from the start vertex"""
    raise NotImplementedError  

def print_bfs(graph: IGraph, start_vertex: IVertex) -> None: 
    """Print the BFS traversal of the graph starting from the start vertex"""
    raise NotImplementedError  


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