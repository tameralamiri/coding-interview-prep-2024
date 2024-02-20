# Graphs:
# Graphs are a collection of nodes and edges. Graphs are used to represent networks.

# Graphs can be represented in two ways:
# 1. Adjacency Matrix
# 2. Adjacency List

# 1. Adjacency Matrix:
######################
# An adjacency matrix is a 2D array of V x V vertices. Each row and column represent a vertex.
# If the value of any element a[i][j] is 1, it represents that there is an edge connecting vertex i and vertex j.
graph_matrix = [
    [0, 1, 1, 0],  # Connections for A: A -> B, A -> C
    [1, 0, 0, 1],  # Connections for B: B -> A, B -> D
    [1, 0, 0, 1],  # Connections for C: C -> A, C -> D
    [0, 1, 1, 0]   # Connections for D: D -> B, D -> C
]

# 2. Adjacency List:
###################
# An adjacency list represents a graph as an array of linked lists.
# The index of the array represents a vertex and each element in its linked list represents the adjacent vertices.
# In the below code, we use a dictionary to represent the adjacency list.
# The keys of the dictionary represent the vertices and the values represent the corresponding adjacent vertices.
graph_list = {
    "A": ["B", "D"], # Connections for A: A -> B, A -> D
    "B": ["A", "C"], # Connections for B: B -> A, B -> C
    "C": ["B", "D"], # Connections for C: C -> B, C -> D
    "D": ["A", "C"]  # Connections for D: D -> A, D -> C
}


# Graph Basic Operations:
#####################
# 0. Create a graph: 
graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C':[], 'D':[]}
print(graph)
# 1. Add a vertex: 
graph['E'] = ['A'] 
graph['A'].append('E')
print(graph)
# 2. Add an edge: 
graph['A'].append('D') 
graph['D'].append('A')
print(graph)
# 3. Remove an edge: 
graph['A'].remove('D')
graph['D'].remove('A')
print(graph)
# 4. Remove a vertex: 
del graph['A']
graph['B'].remove('A')
print(graph)
# 5. Find adjacent nodes: 
print(graph['B'])

# Graph Traversal:
#####################
# Breadth First Traversal: (BFT)
from collections import deque
def bft(graph, start):
    visited = set() # Set is more efficient than list for membership tests.
    queue = deque([start]) # Enqueue
    visited.add(start)
    while queue:
        node = queue.popleft() # Dequeue
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return list(visited)

# Depth First Traversal: (DFT)
def dft(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for node in graph[start]:
        if node not in visited:
            dft(graph, node, visited)
    return list(visited)


graph = {
    '0': ['7', '9', '11'],
    '1': ['8', '10'],
    '2': ['3', '12'],
    '3': ['2', '4', '7'],
    '4': ['3'],
    '5': ['6'],
    '6': ['5', '7'],
    '7': ['0', '3', '6', '11'],
    '8': ['1', '9', '12'],
    '9': ['0', '8', '10'],
    '10': ['1', '9'],
    '11': ['0', '7'],
    '12': ['2', '8']
}

print("BFT", bft(graph, '0'))
print("DFT:", dft(graph, '0'))

# Graph Traversal between two nodes:
def is_connected(graph, start, end):
    return end in bft(graph, start)

# Detect Cycle in a Graph:
##########################
# A cycle is a path of edges and vertices wherein a vertex is reachable from itself.
# A graph is said to be cyclic if it has cycles.
# We can use Depth First Traversal to detect a cycle in a Graph.
def is_cyclic(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for node in graph[start]:
        if node in visited:
            return True
        if is_cyclic(graph, node, visited):
            return True
    visited.remove(start)
    return False

# Topological Sort:
###################
# Topological sorting is a linear ordering of the vertices in a graph such that for every directed edge u v, vertex u comes before v in the ordering.
# Topological sorting is only possible for Directed Acyclic Graphs (DAG).
# We can use Depth First Traversal to perform topological sorting.
def topological_sort(graph):
    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            topological_sort_util(graph, node, visited, stack)
    return stack[::-1]

def topological_sort_util(graph, start, visited, stack):
    visited.add(start)
    for node in graph[start]:
        if node not in visited:
            topological_sort_util(graph, node, visited, stack)
    stack.append(start)

# Shortest Path:
################
# Shortest path algorithms are used to find the shortest path between two vertices in a graph.
# Dijkstra's Algorithm and Bellman-Ford Algorithm are two of the most popular algorithms to find the shortest path in a weighted graph.
# Bellman-Ford Algorithm can handle negative weights, whereas Dijkstra's Algorithm cannot.
# Dijkstra's Algorithm is more efficient than Bellman-Ford Algorithm.
# Dijkstra's Algorithm is a greedy algorithm and Bellman-Ford Algorithm is a dynamic programming algorithm.

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1}
}

# Dijkstra's Algorithm Implementation:
# 1. initialize the distance to all vertices as infinity and the distance to the start vertex as 0.
# 2. Add the start vertex to the priority queue.
# 3. While the priority queue is not empty, do the following:
#    - Get the vertex with the minimum distance from the priority queue.
#    - Update the distance to the neighbouring vertices.
#    - Add the neighbouring vertices to the priority queue.
# 4. Return the shortest distance to all vertices from the start vertex.
from heapq import heappop, heappush
def dijkstra(graph, start):
    # shortest distance to all vertices from start
    shortest_distance = {vertex: float('infinity') for vertex in graph}
    shortest_distance[start] = 0

    # Set of visited vertices
    visited = set()

    while visited != set(graph.keys()):
        # Get the vertex with the minimum distance
        current_vertex = min((set(shortest_distance.keys()) - visited), key=lambda vertex: shortest_distance[vertex])
        
        # Visting the neighbour vertices
        for neighbour, weight in graph[current_vertex].items():
            if neighbour not in visited:
                new_distance = shortest_distance[current_vertex] + weight
                if new_distance < shortest_distance[neighbour]:
                    shortest_distance[neighbour] = new_distance

        # Mark the current vertex as visited
        visited.add(current_vertex)

    return shortest_distance

print("Dijkstra:", dijkstra(graph, "A"))

# Graph with negative weights:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': -2, 'D': 1},  # Negative edge weight
    'D': {'B': 5, 'C': 1}
}
# Bellman-Ford Algorithm Implementation:
# 1. Initialize the distance to all vertices as infinity and the distance to the start vertex as 0.
# 2. Relax the edges: (V - 1) times: 
#   - for each edge u -> v with weight w, if the distance to u + w is less than the distance to v, update the distance to v.
#   - Relaxing the edges (V - 1) times ensures that the shortest distance to all vertices is found.
# 3. Check for negative cycles
# 4. Return the shortest distance to all vertices from the start vertex.
def bellman_ford(graph, start):
    # shortest distance to all vertices from start
    shortest_distance = {vertex: float('infinity') for vertex in graph}
    shortest_distance[start] = 0

    # Relaxing the edges: (V - 1) times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u].items():
                if shortest_distance[u] + w < shortest_distance[v]:
                    shortest_distance[v] = shortest_distance[u] + w

    # Checking for negative cycles
    for u in graph:
        for v, w in graph[u].items():
            if shortest_distance[u] + w < shortest_distance[v]:
                raise ValueError("Graph contains a negative cycle")

    return shortest_distance

print("Bellman-Ford:", bellman_ford(graph, "A"))

# Travelling Salesman Problem:
#############################
# The Travelling Salesman Problem (TSP) is a combinatorial optimization problem.
# It is a problem of finding the shortest possible route that visits each city exactly once and returns to the original city.
# The TSP is NP-hard and there is no known polynomial-time solution for it.
# Brute-force solution for the TSP has a time complexity of O(n!).
# Dynamic programming: Held-Karp Algorithm has a time complexity of O(n^2 * 2^n).
# Heuristic algorithms: Nearest Neighbour Algorithm, Genetic Algorithm, Simulated Annealing, Ant Colony Optimization, etc.

# Nearest Neighbour Algorithm Implementation for TSP:
def nearest_neighbour(graph, start):
    path = [start]
    cost = 0
    current = start
    to_visit = set(graph.keys())
    to_visit.remove(start)
    while to_visit:
        nearest = min(to_visit, key=lambda x: graph[current][x])
        cost += graph[current][nearest]
        path.append(nearest)
        to_visit.remove(nearest)
        current = nearest
    cost += graph[current][start]
    path.append(start)
    return path, cost


graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}
start_city = 'A'
tour, tour_cost = nearest_neighbour(graph, start_city)
print(f"Tour: {tour}")
print(f"Total cost: {tour_cost}")
