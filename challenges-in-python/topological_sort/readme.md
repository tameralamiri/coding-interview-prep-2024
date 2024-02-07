# Topological Sort
Topological sort is a linear ordering of vertices in a directed graph such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. This is only possible for Directed Acyclic Graphs (DAGs), as cycles would prevent a vertex from being linearly ordered before another if they must also come after it.

## How It Works:
* Kahn's Algorithm or DFS (Depth-First Search) are common methods to achieve a topological sort.
* Kahn's Algorithm works by repeatedly removing nodes with no incoming edges (indegrees of zero) and removing all edges leading from them.
* DFS Approach involves recursively visiting nodes, ensuring that all descendants are visited before the node itself is finalized in the order.

## When to Use:
Topological sorting is used when you have dependencies among tasks and need to order them. It's applicable in scenarios like:

* Scheduling Jobs from given dependencies among jobs.
* Course Scheduling problems where some courses have prerequisites.
* Build Systems where certain tasks must be performed before others.
* Package Dependency Resolution in software projects.

## Example Challenges:
1. Course Schedule: Determine if it's possible to finish all courses given prerequisite relations.
2. Alien Dictionary: Given a sorted dictionary of an alien language, find the order of characters in the alphabet.
3. Minimum Height Trees: For an undirected graph, find all nodes that can be a tree root to ensure minimum height trees.
4. Compilation Order: Given a list of projects and dependencies, find an order in which the projects can be compiled.

## Real-Life Applications:
* Build Systems: Determining the order in which source files should be compiled.
* Package Managers: Resolving the order in which packages should be installed or updated based on dependencies.