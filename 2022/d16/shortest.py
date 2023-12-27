# ChatGPT generated

from collections import defaultdict, deque

def shortest_path_lengths(graph):
    # Initialize a dictionary to hold the shortest path lengths from each node to every other node
    shortest_paths = defaultdict(lambda: defaultdict(int))
    
    # Iterate over each node in the graph
    for start_node in graph:
        # Initialize a queue to hold the nodes that we need to visit, and a dictionary to track the
        # shortest path lengths to each node
        queue = deque([start_node])
        visited = defaultdict(int)
        visited[start_node] = 0
        
        # While there are nodes in the queue, iterate over them
        while queue:
            current_node = queue.popleft()
            current_distance = visited[current_node]
            
            # Iterate over each neighbor of the current node
            for neighbor in graph[current_node]:
                # If we have not yet visited the neighbor, add it to the queue and update its shortest
                # path length in the visited dictionary
                if neighbor not in visited:
                    visited[neighbor] = current_distance + 1
                    queue.append(neighbor)
        
        # After we have visited all nodes reachable from the start node, update the shortest_paths
        # dictionary with the shortest path lengths from the start node to all other nodes
        for node, distance in visited.items():
            shortest_paths[start_node][node] = distance
    
    return shortest_paths
