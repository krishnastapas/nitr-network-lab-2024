def DSDV(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    next_hop = [-1] * n
 
    dist[start] = 0
 
    for _ in range(n - 1):
        for u in range(n):
            for v in graph[u]:
                if dist[u] + 1 < dist[v]:
                    dist[v] = dist[u] + 1
                    next_hop[v] = u
 
    return dist, next_hop
 
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = [
        [1, 2],     # Node 0: Connected to nodes 1 and 2
        [0, 3],     # Node 1: Connected to nodes 0 and 3
        [0, 3, 4],  # Node 2: Connected to nodes 0, 3, and 4
        [1, 2, 4],  # Node 3: Connected to nodes 1, 2, and 4
        [2, 3]      # Node 4: Connected to nodes 2 and 3
    ]
 
    numNodes = len(graph)
 
    # Find shortest paths from all nodes
    for i in range(numNodes):
        shortestDistances, next_hop = DSDV(graph, i)
        print("Shortest paths from node", i, ":")
        for j in range(numNodes):
            print("Node", j, ":", shortestDistances[j], "Next hop:", next_hop[j])
        print()