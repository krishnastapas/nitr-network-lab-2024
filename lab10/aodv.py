import heapq

class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = set()
        self.sequence_number = 0

    def add_neighbor(self, neighbor):
        self.neighbors.add(neighbor)

    def __lt__(self, other):
        return self.id < other.id

class AODV:
    def __init__(self, nodes):
        self.nodes = nodes

    def route_discovery(self, source_id, destination_id):
        source_node = self.nodes[source_id]
        destination_node = self.nodes[destination_id]
        
        # Initialize data structures
        visited = set()
        heap = [(0, source_node)]
        predecessors = {}
        
        while heap:
            cost, current_node = heapq.heappop(heap)
            visited.add(current_node.id)

            if current_node.id == destination_id:
                # Build route from source to destination
                path = []
                node = destination_node
                while node.id != source_id:
                    path.append(node.id)
                    node = predecessors[node]
                path.append(source_id)
                path.reverse()
                return path
            
            for neighbor_id in current_node.neighbors:
                neighbor_node = self.nodes[neighbor_id]
                if neighbor_id not in visited:
                    heapq.heappush(heap, (cost + 1, neighbor_node))
                    predecessors[neighbor_node] = current_node
        
        return None  # No route found

# Example usage
if __name__ == "__main__":
    # Create nodes
    nodes = {i: Node(i) for i in range(1, 6)}

    # Add neighbors
    nodes[1].add_neighbor(2)
    nodes[1].add_neighbor(3)
    nodes[2].add_neighbor(1)
    nodes[2].add_neighbor(4)
    nodes[3].add_neighbor(1)
    nodes[3].add_neighbor(4)
    nodes[4].add_neighbor(2)
    nodes[4].add_neighbor(3)
    nodes[4].add_neighbor(5)
    nodes[5].add_neighbor(4)

    # Create AODV instance
    aodv = AODV(nodes)

    # Perform route discovery
    source_id = 1
    destination_id = 5
    route = aodv.route_discovery(source_id, destination_id)

    if route:
        print(f"Route from node {source_id} to node {destination_id}: {route}")
    else:
        print("Route not found.")
