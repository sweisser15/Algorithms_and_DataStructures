#  File: TopoSort.py

#  Description: Check if graph is cyclical, and if not, return a toposort.

#  Student Name: Simon Weisser

#  Student UT EID: saw3548

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 5/1/19

#  Date Last Modified: 5/3/19

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
        self.edges = [] # 2d list of all edges

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
    def add_directed_edge(self, start, finish):
        self.adjMat[start][finish] = 1
        self.edges.append([start, finish])

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def has_cycle(self):
        i = 0

        # traverse through all possible starting vertices
        while i <= len(self.Vertices) - 1:
            stack = Stack() # create new stack for each starting vertex

            # mark vertex as visited and push
            self.Vertices[i].visited = True
            stack.push(i)

            # use of backtracking to check if any vertex maps back to the starting vertex
            while (stack.is_empty() != True):
                peek = stack.peek()
                # return true if peek of stack has edge with starting vertex
                if self.has_edge(self.Vertices[peek], self.Vertices[i]):
                    return True
                else:
                    new_vert = self.get_adj_unvisited_vertex(peek) # move to adj vertex
                    if (new_vert == -1): # DNE
                        stack.pop()
                    else:
                        (self.Vertices[new_vert]).visited = True
                        stack.push(new_vert)
            i += 1 # start at the next vertex in the list

        # set all vertices back to not visited
        for vertex in self.Vertices:
            vertex.visited = False

        return False

    # has_cycle helper, returns true if two vertices
    # form an edge on the directed graph
    def has_edge(self, a, b):
        for edge in self.edges:
            if (edge[0] == a) and (edge[1] == b):
                return True
        return False

    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort(self):
        in_degrees = []

        # if graph is cyclical, return
        if self.has_cycle() == True:
            return None

        # add vertices' degrees into list in_degrees
        for i in range(len(self.Vertices)):
            degree = 0
            for edge in self.edges:
                if edge[1] == i:
                    degree += 1
            in_degrees.append(degree)

        # create empty queue
        queue = Queue()

        while True:
            zero_degree = []

            # append vertices of degree zero that have not been visited to zero_degree
            for ver in range(len(self.Vertices)):
                if (in_degrees[ver] == 0) and (self.Vertices[ver].visited == False):
                    zero_degree.append(ver)
                    self.Vertices[ver].visited = True # mark vertex as visited

            # if no more zero degree vertices, break
            if len(zero_degree) == 0:
                break

            # sort vertices at each level in alphabetical order
            zero_degree.sort()

            # enqueue elements with degree 0
            for deg in zero_degree:
                queue.enqueue(self.Vertices[deg])

            # add indices of endpoints corresponding to zero degree start points
            end_points = []
            for edge in self.edges:
                if edge[0] in zero_degree:
                    end_points.append(edge[1])

            # decrease the in degree of endpoint vertices
            for ind in end_points:
                in_degrees[ind] -= 1

        final_list = []

        # dequeue and add vertices to final_list
        while queue.is_empty() != True:
            cur = queue.dequeue()
            final_list.append(str(cur))

        # set all vertices back to not visited
        for vertex in self.Vertices:
            vertex.visited = False

        return final_list


def main():

    # create the Graph object
    cities = Graph()

    # open the file for reading
    in_file = open("./topo.txt", "r")

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
        start = str(edge[0])
        finish = str(edge[1])

        cities.add_directed_edge(cities.get_index(start), cities.get_index(finish))

    # return toposort list if graph is not cyclical
    topolist = cities.toposort()

    # print all vertices on the same line
    for vertex in topolist:
        print(vertex, end=' ')
    print()

    # close the file
    in_file.close()

main()