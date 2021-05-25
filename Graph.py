#  File: Graph.py

#  Description: Test deletion of edges, deletion of vertices, bfs, and dfs in graph.

class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack is empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


class Graph(object):
    def __init__(self):
        self.Vertices = []  # list of Vertex objects
        self.adjMat = []  # adjacency matrix

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # given a label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight(self, fromVertexLabel, toVertexLabel):
        start = self.get_index(fromVertexLabel)

        # vertices don't exist
        end = self.get_index(toVertexLabel)
        if start == -1 or end == -1:
            return -1

        # if the edge exists
        if self.adjMat[start][end] > 0:
            return self.adjMat[start][end]
        return -1 # else

    # get a copy of the list of Vertex objects
    def get_vertices(self):
        for i in self.Vertices:
            print(i)

    # delete an edge from the adjacency matrix
    def delete_edge(self, fromVertexLabel, toVertexLabel):
        # find index of the from vertex and the to vertex
        start = self.get_index(fromVertexLabel)
        end = self.get_index(toVertexLabel)

        # decrease corresponding adjacent matrix values by 1
        self.adjMat[start][end] = self.adjMat[start][end] - 1
        self.adjMat[end][start] = self.adjMat[end][start] - 1

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex(self, vertexLabel):
        ind = self.get_index(vertexLabel)
        n = len(self.adjMat)

        # remove column of matrix
        for j in range(n):
            self.adjMat[j].pop(ind)

        # remove row of matrix
        self.adjMat.pop(ind)

        # remove vertex from vertex list
        self.Vertices.pop(ind)

    # get a list of immediate neighbors (Vertex objects) that you
    # can go to from a vertex return an empty list if there are none
    def get_neighbors(self, vertexLabel):
        neighb_list = []
        ind = self.get_index(vertexLabel)
        # if vertexLabel DNE
        if ind == -1:
            return []
        # add neighbors of vertex to neighb_list
        for j in range(len(self.adjMat[ind])):
            if (self.adjMat[ind][j] != 0):
                neighb_list.append(self.Vertices[j])
        # no neighbors exists
        if len(neighb_list) == 0:
            return []
        return neighb_list

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if (not self.has_vertex(label)):
            self.Vertices.append(Vertex(label))

            # add a new column in the adjacency matrix
            nVert = len(self.Vertices)
            for i in range(nVert - 1):
                (self.adjMat[i]).append(0)

            # add a new row for the new Vertex
            new_row = []
            for i in range(nVert):
                new_row.append(0)
            self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # do the depth first search in a graph
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # visit the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)

        # the stack is empty, let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # do the breadth first search in a graph
    def bfs(self, v):
        # create the Queue
        theQueue = Queue()

        # mark vertex v as visited and enqueue
        self.Vertices[v].visited = True
        print(self.Vertices[v])
        theQueue.enqueue(v)

        # while the queue is not empty
        while theQueue.is_empty() == False:
            cur = theQueue.dequeue() # dequeue top and set as current
            adj = self.get_adj_unvisited_vertex(cur)
            while adj != -1:
                self.Vertices[adj].visited = True
                print (self.Vertices[adj])
                theQueue.enqueue(adj) # enqueue all adjacent vertices
                adj = self.get_adj_unvisited_vertex(cur) # visit all unvisited adj vertices

        # the stack is empty, let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

def main():
    # create the Graph object
    cities = Graph()

    # open the file for reading
    in_file = open("./graph.txt", "r")

    # read the number of Vertices
    num_vertices = int((in_file.readline()).strip())

    # add the vertices to the list
    for i in range(num_vertices):
        city = (in_file.readline()).strip()
        cities.add_vertex(city)

    # read the edges and add them to the adjacency matrix
    num_edges = int((in_file.readline()).strip())

    for i in range(num_edges):
        edge = (in_file.readline()).strip()
        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])

        cities.add_directed_edge(start, finish, weight)


    # read the starting vertex for dfs and bfs
    start_vertex = (in_file.readline()).strip()

    # get the index of the starting vertex
    start_index = cities.get_index(start_vertex)

    # read file for vertices to delete edge
    del_vertices = (in_file.readline())
    del_vertices = del_vertices.split(" ")
    final_vertices = []
    for word in del_vertices:
       final_vertices.append(word.strip("\n"))

    # read file for vertex to delete
    del_vertex = (in_file.readline()).strip()


    # do the depth first search
    print("Depth First Search")
    cities.dfs(start_index)
    print()

    # do the breadth first search
    print("Breadth First Search")
    cities.bfs(start_index)
    print()

    # test the deletion of edge
    print("Deletion of an edge")
    cities.delete_edge(final_vertices[0], final_vertices[1])
    print()

    # print the adjacency matrix
    print("Adjacency Matrix")
    for i in range(num_vertices):
        for j in range(num_vertices):
            print(cities.adjMat[i][j], end=" ")
        print()
    print()

    # test deletion of vertex
    print("Deletion of a vertex")
    print()
    cities.delete_vertex(del_vertex)

    # print list of vertices
    print("List of Vertices")
    cities.get_vertices()
    print()

    # print the adjacency matrix
    num_vertices = len(cities.adjMat[0])
    print("Adjacency Matrix")
    for i in range(num_vertices):
        for j in range(num_vertices):
            print(cities.adjMat[i][j], end=" ")
        print()
    print()

    # close the file
    in_file.close()


main()
