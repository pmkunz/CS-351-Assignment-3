from __future__ import annotations
from typing import List, Optional, Tuple, TypeVar

from graph_interfaces import IEdge, IGraph, IVertex

# Implementation definitions
# You should implement the bodies of the methods required by the interface protocols.

T = TypeVar('T')

class Graph[T](IGraph[T]):

    def __init__(self):
        self._vertices = []

    def get_vertices(self) -> List[IVertex]:
        return list(self._vertices)
        
    def get_edges(self) -> List[IEdge]:
        """ collects all edges from vertices """
        edges: List[IEdge] = []
        for v in self._vertices: 
            edges += v.get_edges()
        return edges

    def add_vertex(self, vertex: IVertex) -> None:
        self._vertices.append(vertex)
    
    def remove_vertex(self, vertex_name: str) -> None:
        for vertex in list(self._vertices):
            if vertex.get_name() == vertex_name:
                self._vertices.remove(vertex)
                continue

            # Account for the edges:
            for edge in list(vertex.get_edges()):
                if edge.get_destination().get_name() == vertex_name:
                    vertex.remove_edge(edge.get_name())

    def add_edge(self,edge: IEdge, from_vertex_name: Optional[str] = None) -> None:
        """ Add edge if it's connected to the same destination """
        # for e in self._edges:
        #     if e.get_name() == edge.get_name() and e.get_destination().get_name() == edge.get_destination().get_name():
        #         return  # if it is a duplicate, do nothing
        #     self._edges.append(edge)

        if from_vertex_name:
            for vertex in self._vertices:
                if vertex.get_name() == from_vertex_name:
                    vertex.add_edge(edge)
                    break

    def remove_edge(self, edge_name: str) -> None:
        """ removes any edges with this name from all vertices """
        for v in self._vertices:
            for e in list(v.get_edges()):
                if e.get_name() == edge_name:
                    v.remove_edge(edge_name)

class Vertex(IVertex):

    def __init__(self, name: str) -> None:
        self.name = name
        self._edges: List[IEdge[T]] = []
        self._visited: bool = False
        self._coordinates: Tuple[float, float] = (0,0)
        self._data: Optional[T] = None

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def add_edge(self, edge: IEdge[T]) -> None:
        self._edges.append(edge)

    def remove_edge(self, edge_name: str) -> None:
        """ removes the edge by name """
        for e in list(self._edges):
            if e.get_name() == edge_name:
                self._edges.remove(e)

    def get_edges(self) -> List[IEdge]:
        return list(self._edges)

    def set_visited(self, visited: bool) -> None:
        self._visited = visited 

    def is_visited(self) -> bool:
        return self._visited

class Edge(IEdge):
    
    def __init__(self, name: str, destination: IVertex, weight: float = 0) -> None:
        self._name = name
        self._destination: IVertex = destination
        self._weight = weight

    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name: str) -> None:
        self._name = name

    def get_destination(self) -> IVertex:
        return self._destination
    
    def get_weight(self) -> float:
        return self._weight
    
    def set_weight(self, weight: float) -> None:
        self._weight = weight