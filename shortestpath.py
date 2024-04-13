def find_shortest_route(edges, start_node, end_node):
    # Initialize the distances dictionary with infinity for all nodes except the start node
    distances = {node: float('inf') for node in set(sum(([edge['from'], edge['to']] for edge in edges), []))}
    distances[start_node] = 0

    # Create a dictionary to store the predecessors of each node in the shortest path
    predecessors = {}

    # Loop until all nodes have been visited
    while distances:
        # Get the node with the smallest distance from the start node
        current_node = min(distances, key=distances.get)

        # If the current node is the end node, break the loop
        if current_node == end_node:
            break

        # Update distances and predecessors for neighbors of the current node
        for edge in edges:
            if edge['from'] == current_node:
                neighbor = edge['to']
                new_distance = distances[current_node] + edge['weight']  
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_node

        # Remove the current node from distances as it has been visited
        del distances[current_node]

    # Construct the shortest path from the predecessors dictionary
    shortest_path = [end_node]
    while end_node in predecessors:
        end_node = predecessors[end_node]
        shortest_path.append(end_node)
    shortest_path.reverse()

    return shortest_path


edges = [{"from": "A", "to": "B", "weight": 1}, {"from": "B", "to": "C", "weight": 3},
         {"from": "B", "to": "E", "weight": 3.5}, {"from": "C", "to": "E", "weight": 4},
         {"from": "C", "to": "D", "weight": 2.5}, {"from": "D", "to": "G", "weight": 2.5},
         {"from": "G", "to": "F", "weight": 3.5}, {"from": "E", "to": "F", "weight": 2},
         {"from": "F", "to": "H", "weight": 2.5}, {"from": "H", "to": "H", "weight": 1}]

start_node = 'C'
end_node = 'F'
shortest_route = find_shortest_route(edges, start_node, end_node)
print(shortest_route)