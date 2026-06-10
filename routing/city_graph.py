"""
Module 5: City Network Graph
Implement an adjacency list graph representation to calculate paths.
"""

class CityGraph:
    def __init__(self):
        # Adjacency list format: { intersection_id: { neighboring_intersection: travel_time } }
        self.network = {}

    def add_intersection(self, intersection_id: str) -> None:
        """TODO: Add a node representing a street intersection if it doesn't exist."""
        # YOUR CODE HERE
        pass

    def add_road(self, from_int: str, to_int: str, travel_time: float) -> None:
        """
        TODO: Add a directed, weighted edge representing a street from one 
        intersection to another with its associated travel time.
        """
        # YOUR CODE HERE
        pass

    def calculate_shortest_pickup_time(self, start_int: str, end_int: str) -> float:
        """
        TODO: Implement a shortest-path algorithm (e.g., Dijkstra's algorithm) 
        to find the absolute shortest travel time from the driver's intersection 
        (start_int) to the rider's intersection (end_int).
        
        Tip: You may use your DispatchPriorityQueue from Task 1 if modified, 
        or build a basic tracking array/dictionary to find the minimum unvisited vertex.
        Return float('inf') if no route connects the two intersections.
        """
        # YOUR CODE HERE
        pass
