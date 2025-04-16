class Graph:
    def __init__(self):
        # Initialize an empty adjacency list
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        # Add a vertex to the graph
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Add an edge between vertex1 and vertex2 (undirected graph)
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def dfs(self, start_vertex):
        # Perform depth-first search starting from start_vertex
        visited = set()  # To keep track of visited vertices
        traversal_order = []  # To store the order of traversal

        def dfs_recursive(vertex):
            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)
                for neighbor in self.adjacency_list[vertex]:
                    dfs_recursive(neighbor)

        dfs_recursive(start_vertex)
        print("DFS Traversal Order:", traversal_order)


# Example usage
graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 5)

graph.dfs(1)
