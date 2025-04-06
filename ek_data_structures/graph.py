class Graph:
    def __init__(self):
        # Adjacency list to store graph
        self.graph = {}

    def add_vertex(self, vertex):
        """ Adds a vertex to the graph. """
        if vertex not in self.graph:
            self.graph[vertex] = []
        else:
           raise ValueError(f"Vertex {vertex} already exists in the graph.")

    def add_edge(self, vertex1, vertex2):
        """ Adds an edge between vertex1 and vertex2. """
        if vertex1 not in self.graph:
            raise KeyError(f"Vertex {vertex1} does not exist in the graph.")
        if vertex2 not in self.graph:
            raise KeyError(f"Vertex {vertex2} does not exist in the graph.")
        
        # Add edge in both directions (undirected graph)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def remove_vertex(self, vertex):
        """ Removes a vertex and its associated edges. """
        if vertex not in self.graph:
            raise KeyError(f"Vertex {vertex} does not exist in the graph.")
        
        # Remove all edges to this vertex
        for adj in list(self.graph[vertex]):
            self.graph[adj].remove(vertex)
        # Remove the vertex itself
        del self.graph[vertex]


    def remove_edge(self, vertex1, vertex2):
        """ Removes the edge between vertex1 and vertex2. """
        if vertex1 not in self.graph:
            raise KeyError(f"Vertex {vertex1} does not exist in the graph.")
        if vertex2 not in self.graph:
            raise KeyError(f"Vertex {vertex2} does not exist in the graph.")
        if vertex2 not in self.graph[vertex1]:
            raise ValueError(f"Edge between {vertex1} and {vertex2} does not exist.")
        if vertex1 not in self.graph[vertex2]:
            raise ValueError(f"Edge between {vertex2} and {vertex1} does not exist.")
        
        # Remove the edge
        self.graph[vertex1].remove(vertex2)
        self.graph[vertex2].remove(vertex1)

    def has_edge(self, vertex1, vertex2):
        """ Checks if there's an edge between vertex1 and vertex2. """
        if vertex1 not in self.graph:
            raise KeyError(f"Vertex {vertex1} does not exist in the graph.")
        if vertex2 not in self.graph:
            raise KeyError(f"Vertex {vertex2} does not exist in the graph.")
        return vertex2 in self.graph[vertex1]

    def dfs(self, start_vertex, visited=None):
        """ Performs Depth-First Search starting from the given vertex. """
        if start_vertex not in self.graph:
            raise KeyError(f"Vertex {start_vertex} does not exist in the graph.")
        
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex, end=" ")

        for neighbor in self.graph.get(start_vertex, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start_vertex):
        """ Performs Breadth-First Search starting from the given vertex. """
        if start_vertex not in self.graph:
            raise KeyError(f"Vertex {start_vertex} does not exist in the graph.")
        
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def display_graph(self):
        """ Prints the graph in adjacency list format. """
        return print(self.graph)

    def find_path(self, start, end, path=None):
        """ Finds a path between two vertices using DFS. """
        if start not in self.graph:
            raise KeyError(f"Vertex {start} does not exist in the graph.")
        if end not in self.graph:
            raise KeyError(f"Vertex {end} does not exist in the graph.")
        
        if path is None:
            path = []
        path.append(start)
        if start == end:
            return path
        if start not in self.graph:
            return None
        for neighbor in self.graph[start]:
            if neighbor not in path:
                new_path = self.find_path(neighbor, end, path.copy())
                if new_path:
                    return new_path
        return None

    def search(self, vertex):
        """ Searches for a vertex in the graph. Returns True if found, else False. """
        return vertex in self.graph
