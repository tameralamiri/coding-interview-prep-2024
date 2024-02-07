# Solving the "Compilation Order" Challenge
# Challenge Description:
# Given a list of projects and a list of dependencies 
# (where a dependency [a, b] means project a depends on project b and b needs to be compiled before a), 
# determine a valid order in which the projects can be compiled. If no valid order exists, return an empty list.

# Approach:
# Use Kahn's Algorithm for Topological Sorting.
# 1. Create an adjacency list and an indegree list.
# 2. Initialize a queue with all nodes with indegree 0.
# 3. Pop from the queue and add to the result list.
# 4. For each neighbor of the popped node, decrement the indegree. If the indegree becomes 0, add to the queue.
# 5. Repeat until the queue is empty.
# 6. If the result list is not equal to the number of nodes, return an empty list.

from collections import defaultdict, deque

def compile_order(projects, dependencies):
    adj_list = defaultdict(list)
    indegree = defaultdict(int)
    for project in projects:
        indegree[project] = 0
    for dependency in dependencies:
        adj_list[dependency[1]].append(dependency[0])
        indegree[dependency[0]] += 1
    queue = deque([project for project in projects if indegree[project] == 0]) # Initialize queue with nodes with indegree 0
    result = []
    while queue:
        project = queue.popleft() # Pop from the queue
        result.append(project) # Add to the result list
        for neighbor in adj_list[project]: # For each neighbor of the popped node
            indegree[neighbor] -= 1 # Decrement the indegree
            if indegree[neighbor] == 0: # If the indegree becomes 0, add to the queue
                queue.append(neighbor)
    return result if len(result) == len(projects) else []

# Test cases
print(compile_order(["a", "b", "c"], [("a", "b"), ("b", "c")])) # ["c", "b", "a"]
print(compile_order(["a", "b", "c"], [("a", "b"), ("b", "c"), ("c", "a")])) # []