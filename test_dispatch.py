import pytest
from routing.city_graph import CityGraph

def test_city_graph_routing():
    graph = CityGraph()
    graph.add_road("Int_A", "Int_B", 5.0)
    graph.add_road("Int_A", "Int_C", 2.0)
    graph.add_road("Int_C", "Int_B", 1.5) # Dynamic detour shortcut
    graph.add_road("Int_B", "Int_D", 4.0)
    
    # Shortest path from A to B is via C (2.0 + 1.5 = 3.5) instead of direct (5.0)
    shortest_time = graph.calculate_shortest_pickup_time("Int_A", "Int_B")
    assert shortest_time == 3.5
    
    # Shortest path to terminal location D (2.0 + 1.5 + 4.0 = 7.5)
    assert graph.calculate_shortest_pickup_time("Int_A", "Int_D") == 7.5
    
    # Unreachable state test
    assert graph.calculate_shortest_pickup_time("Int_D", "Int_A") == float('inf')
