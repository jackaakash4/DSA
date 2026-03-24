#bfs
from collections import defaultdict

class Graph:
    
    #constructor
    def __init__(self):
        self.graph = defaultdict(list)

    #function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)


    #function to pring a bfs of graph
    def bfs(self, s):

        #mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        #create a queue for bfs
        queue = []

        #mark the source node ad visited and enque it
        queue.append(s)
        visited[s] = True

        while queue:

            #dequeue a verteex from 
            #queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            #get all adjacent vertices of the dequeued vertex s.
            #if an adjacent has not been visited
            #then mark it visited and enqueue it

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


    #driver code
    if __name__ = '__main__':

        #create a graph given in the diagram
        g = Graph()
        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(1, 2)

        g.BFS(2)
