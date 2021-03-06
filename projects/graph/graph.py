"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Initiate a blank set
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            # Add v2 as a neighbor to v1
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex id
        queue = Queue()
        queue.enqueue(starting_vertex)

        # Create a set to store visited vertices
        visited = set()

        # While the queue is not empty
        while queue.size() > 0:
            # Get current vertex 
            current = queue.dequeue()
            # If that vertex has not been visited
            if current not in visited:
                # Visit it
                print(current)
                # Mark as visited
                visited.add(current)
                # add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(current):
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex id
        stack = Stack()
        stack.push(starting_vertex)

        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty
        while stack.size() > 0:
            # Pop the last vertex
            current = stack.pop()
            # If that vertex has not been visited
            if current not in visited:
                # Visit it
                print(current)
                # Mark it as visited
                visited.add(current)
                # add all neighbors to the back of the stack
                for neighbor in self.get_neighbors(current):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, vistited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex in vistited:
            return
        else:
            vistited.add(starting_vertex)
            print(starting_vertex)
            neighbors = self.get_neighbors(starting_vertex)
            
            
            if len(neighbors) == 0:
                return None
            
            for neighbor in neighbors:
                self.dft_recursive(neighbor, vistited)
                
                

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue a path to the starting vertex id
        queue = Queue()
        path = [starting_vertex]
        queue.enqueue(path)
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty
        while queue.size() > 0:
            # Dequeue the first PATH
            current = queue.dequeue()
            # Grab the last vertex from the PATH
            last = current[-1]
            # check if the last path is the target and return current if so
            if last is destination_vertex:                
                return current

            # If that vertex has not been visited
            if last not in visited:
                # check if it's the target
                # Mark it as visited
                visited.add(last)
                
                # Then add a path to its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last):
                    copy = current[:]
                    copy.append(neighbor)
                    queue.enqueue(copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        path = [starting_vertex]
        stack.push(path)

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty
        while stack.size() > 0:
            # Dequeue the first PATH
            current = stack.pop()
            # Grab the last vertex from the path
            last = current[-1]

            if last is destination_vertex:                
                return current

            # If that vertex has not been visited
            if last not in visited: 
                # Mark it as visited
                visited.add(last)

                # Then add a path to its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last):
                    copy = current[:]
                    copy.append(neighbor)
                    stack.push(copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """      
        if len(path) == 0:
            path.append(starting_vertex)
             
        
        # base case
        if starting_vertex == destination_vertex:
            return path
    
        visited.add(starting_vertex)
        print(starting_vertex)
        neighbors = self.get_neighbors(starting_vertex)
        
        if len(neighbors) == 0:
            return None
        
        for neighbor in neighbors:
            if neighbor not in visited:
                new_path = path + [neighbor]
                result = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                
                if result is not None:
                    return result
        
       

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
