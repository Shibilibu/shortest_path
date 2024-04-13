Shortest Route Finder

Overview

This Python function, find_shortest_route, calculates the shortest path between two nodes in a graph using Dijkstra's algorithm. It takes a list of edges, a start node, and an end node as input, and returns the shortest path as a list of nodes.

Usage
To use this function, follow these steps:

Define your list of edges in the format [{"from": "A", "to": "B", "weight": 1}, ...].
Set your start and end nodes.
Call the function find_shortest_route(edges, start_node, end_node).
The function will return the shortest path as a list of nodes.
Example:

python
Copy code
edges = [{"from": "A", "to": "B", "weight": 1}, {"from": "B", "to": "C", "weight": 3},
         {"from": "B", "to": "E", "weight": 3.5}, {"from": "C", "to": "E", "weight": 4},
         {"from": "C", "to": "D", "weight": 2.5}, {"from": "D", "to": "G", "weight": 2.5},
         {"from": "G", "to": "F", "weight": 3.5}, {"from": "E", "to": "F", "weight": 2},
         {"from": "F", "to": "H", "weight": 2.5}, {"from": "H", "to": "H", "weight": 1}]

start_node = 'C'
end_node = 'F'

shortest_route = find_shortest_route(edges, start_node, end_node)
print(shortest_route)  # Output: ['C', 'D', 'G', 'F']
Input Format
edges: List of dictionaries representing edges in the graph. Each dictionary should contain the keys 'from', 'to', and 'weight'.
Output Format
The function returns the shortest path as a list of nodes.

License
This project is licensed under the MIT License.
