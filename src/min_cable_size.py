class Graph:
    def __init__(self, nodes=None):
      
        self.edges = []
        self.nodes = set(nodes) if nodes else set()

    def add_edge(self, start, end, weight):
        self.edges.append((weight, start, end))
        self.nodes.update([start, end])

    def find_parent(self, parent, node):
        if parent[node] == node:
            return node
        return self.find_parent(parent, parent[node])

    def kruskal_mst(self):
      
        if not self.edges:
            return -1

        
        self.edges.sort()

      
        parent = {node: node for node in self.nodes}

      
        total_weight = 0
        mst_edges = 0

       
        for weight, start, end in self.edges:
            root_start = self.find_parent(parent, start)
            root_end = self.find_parent(parent, end)

           
            if root_start != root_end:
                total_weight += weight  #Додаємо вагу ребра до загальної ваги MST.
                mst_edges += 1  #Збільшуємо кількість ребер у MST.
                parent[root_start] = root_end  #Об'єднуємо дві компоненти зв'язності.

        #Перевіряємо, чи всі вузли з'єднані. Якщо так, повертаємо загальну вагу, якщо ні - повертаємо -1.

        #Перевірка, чи всі вузли з'єднані
        if mst_edges == len(self.nodes) - 1:
            return total_weight
        else:
            return -1

def read_input_file(min_cable_path):
    edges = []
    with open(min_cable_path, "r") as file:
        for line in file:
            parts = line.split(',')
            edges.append((parts[0], parts[1], int(parts[2])))
    return edges
