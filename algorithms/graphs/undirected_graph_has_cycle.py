class UndirectedGraph:
    def __init__(self, adj_matrix = dict()):
        self.graph = adj_matrix 
    
    def has_cycle(self, parent, node, visited):
        visited[node] = True
        for neighbor in self.graph[node]:
            print(parent, '->', node, '->', neighbor)
            if not visited.get(neighbor):
                if self.has_cycle(node, neighbor, visited):
                    return True
            elif parent != neighbor:
                return True
        return False


    def add_node(self, node, neighbor):

        self.graph[node] = self.graph.get(node, set()) | set([neighbor])
        self.graph[neighbor] = self.graph.get(neighbor, set()) | set([node])

u = UndirectedGraph()
u.add_node(1, 2)
u.add_node(2, 3)
u.add_node(2, 4)
u.add_node(4, 5)
print(u.has_cycle(None, 1, {}))
