# # What is Kruskal’s Algorithm?
# # Kruskal’s Algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a graph.

# # Minimum Spanning Tree (MST):
# # A subset of edges that connects all vertices
# # No cycles
# # Minimum total edge weight


# # Key Idea

# # Kruskal works by:
# # Sorting all edges in increasing order of weight
# # Picking the smallest edge
# # Adding it only if it doesn’t form a cycle
# # Repeat until we have (V - 1) edges

# # To efficiently detect cycles, it uses a data structure called Disjoint Set Union (Union-Find).

# # Why Kruskal is Useful?
# # Network design (roads, cables, pipelines)
# # Clustering problems
# # Efficient MST building for sparse graphs


# class DSU:
#     def __init__(self, n):
#         self.parent = list(range(n))
#         self.rank = [0] * n

#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])  # Path compression
#         return self.parent[x]

#     def union(self, x, y):
#         rootX = self.find(x)
#         rootY = self.find(y)

#         if rootX != rootY:
#             # Union by rank
#             if self.rank[rootX] > self.rank[rootY]:
#                 self.parent[rootY] = rootX
#             elif self.rank[rootX] < self.rank[rootY]:
#                 self.parent[rootX] = rootY
#             else:
#                 self.parent[rootY] = rootX
#                 self.rank[rootX] += 1
#             return True
#         return False


# def kruskal(n, edges):
#     """
#     n = number of vertices
#     edges = list of (u, v, weight)
#     """
#     edges.sort(key=lambda x: x[2])  # sort by weight
#     dsu = DSU(n)

#     mst = []
#     total_weight = 0

#     for u, v, w in edges:
#         if dsu.union(u, v):
#             mst.append((u, v, w))
#             total_weight += w

#     return mst, total_weight


# # Example usage
# edges = [
#     (0, 1, 10),
#     (0, 2, 6),
#     (0, 3, 5),
#     (1, 3, 15),
#     (2, 3, 4)
# ]

# n = 4
# mst, cost = kruskal(n, edges)

# print("MST:", mst)
# print("Total Cost:", cost)



#   case 1 : differemet heights

# Tree A (height 3) + Tree B (height 1)
    #   A
    #  /
    # B

# so now height remains same as 3 therefore no rank increases


# Case 2: Same ranks
# Tree A (height 2) + Tree B (height 2)
# Merge:

#         A
#        /
#       B

# Now the longest path becomes:

# Height increased from 2 → 3
# So we do:
# rank[root] += 1

# Because when you join two trees of equal height, the longest path in the resulting tree grows by exactly one edge—no more.


#  prims algorithm

# import heapq
# def prim(n, adj):
#     """
#     n = number of nodes
#     adj = adjacency list
#     {node: [(neighbor, weight), ...]}
#     """
#     visited = [False] * n
#     min_heap = [(0, 0)]  # (weight, node)

#     total_cost = 0
#     mst = []

#     while min_heap:
#         weight, u = heapq.heappop(min_heap)

#         if visited[u]:
#             continue

#         visited[u] = True
#         total_cost += weight

#         # store edge (optional)
#         mst.append((u, weight))

#         for v, w in adj[u]:
#             if not visited[v]:
#                 heapq.heappush(min_heap, (w, v))

#     return mst, total_cost


# # Example usage
# adj = {
#     0: [(1, 10), (2, 6), (3, 5)],
#     1: [(0, 10), (3, 15)],
#     2: [(0, 6), (3, 4)],
#     3: [(0, 5), (1, 15), (2, 4)]
# }

# mst, cost = prim(4, adj)
# print("MST:", mst)
# print("Total Cost:", cost)



# import heapq

# def dijkstra(n, adj, source):
#     """
#     n = number of nodes
#     adj = {node: [(neighbor, weight), ...]}
#     source = starting node
#     """
#     dist = [float('inf')] * n
#     dist[source] = 0

#     min_heap = [(0, source)]  # (distance, node)

#     while min_heap:
#         d, u = heapq.heappop(min_heap)

#         # Skip if already processed with better distance
#         if d > dist[u]:
#             continue

#         for v, w in adj[u]:
#             if dist[u] + w < dist[v]:
#                 dist[v] = dist[u] + w
#                 heapq.heappush(min_heap, (dist[v], v))

#     return dist


# # Example usage
# adj = {
#     0: [(1, 4), (2, 1)],
#     1: [(3, 1)],
#     2: [(1, 2), (3, 5)],
#     3: []
# }

# print(dijkstra(4, adj, 0))



# def bellman_ford(n, edges, source):
#     """
#     n = number of nodes
#     edges = list of (u, v, weight)
#     source = starting node
#     """
#     # Step 1: initialize distances
#     dist = [float('inf')] * n
#     dist[source] = 0

#     # Step 2: relax edges (n-1) times
#     for _ in range(n - 1):
#         for u, v, w in edges:
#             if dist[u] != float('inf') and dist[u] + w < dist[v]:
#                 dist[v] = dist[u] + w

#     # Step 3: detect negative cycle
#     for u, v, w in edges:
#         if dist[u] != float('inf') and dist[u] + w < dist[v]:
#             print("Negative cycle detected")
#             return None

#     return dist


# # Example usage
# edges = [
#     (0, 1, -1),
#     (0, 2, 4),
#     (1, 2, 3),
#     (1, 3, 2),
#     (1, 4, 2),
#     (3, 2, 5),
#     (3, 1, 1),
#     (4, 3, -3)
# ]

# n = 5
# source = 0

# print(bellman_ford(n, edges, source))


# # dist = [0, ∞, ∞]
# # dist = [0, 4, 1]


# def floyd_warshall(n, graph):
#     """
#     n = number of nodes
#     graph = adjacency matrix
#     """
#     dist = [row[:] for row in graph]  # copy matrix

#     for k in range(n):          # intermediate node
#         for i in range(n):      # source
#             for j in range(n):  # destination
#                 if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
#                     dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

#     return dist


# # Example usage
# INF = float('inf')

# graph = [
#     [0,   3, INF, 7],
#     [8,   0, 2,   INF],
#     [5, INF, 0,   1],
#     [2, INF, INF, 0]
# ]

# result = floyd_warshall(4, graph)

# for row in result:
#     print(row)