class Graph(object):

    def __init__(self,*args,**kwargs):
        self.node_neighbors = {}  # Define vertex and adjacent vertex set as dictionary structure
        self.visited = {}  # Define the visited vertex set as a dictionary structure

    def add_nodes(self,nodelist):

        for node in nodelist:
            self.add_node(node)

    def add_node(self,node):
        if not node in self.nodes():
            self.node_neighbors[node] = []

    def add_edge(self,edge):
        u,v = edge
        if(v not in self.node_neighbors[u]) and ( u not in self.node_neighbors[v]):  # Here you can add your own side pointing to yourself
            self.node_neighbors[u].append(v)

            if(u!=v):
                self.node_neighbors[v].append(u)

    def nodes(self):
        return self.node_neighbors.keys()


    def breadth_first_search(self,root=None):  # Breadth first requires the queue structure
        queue = []
        order = []
        def bfs():
            while len(queue)> 0:
                node  = queue.pop(0)
                self.visited[node] = True
                self.node_neighbors[node].sort()
                for n in self.node_neighbors[node]:
                    if (not n in self.visited) and (not n in queue):
                        queue.append(n)
                        order.append(n)

        if root:
            queue.append(root)
            order.append(root)
            bfs()

        for node in self.nodes():
            if not node in self.visited:
                queue.append(node)
                order.append(node)
                bfs()
        # print(order)
        return order
        
def bfs(graph, S, D):
    queue = [(S, [S])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == D:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest(graph, S, D):
    try:
        return next(bfs(graph, S, D))
    except StopIteration:
        return None

if __name__ == '__main__':
    g = Graph()
    n = int(input())
    g.add_nodes([i+1 for i in range( n )])

    for i in range( n - 1 ):
        g.add_edge(tuple(input().split()))

    print(g.node_neighbors)
    # print(shortest(g, '1', '5'))