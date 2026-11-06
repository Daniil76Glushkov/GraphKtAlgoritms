
import sys


class GraphAdjList:
   
    
    def __init__(self):
        self.adj_list = {}
    
    def add_vertex(self, vertex):
       
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    
    def add_edge(self, u, v):
       
       
        self.add_vertex(u)
        self.add_vertex(v)
        
        
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)
    
    def has_edge(self, u, v):
       
        if u in self.adj_list and v in self.adj_list[u]:
            return True
        return False
    
    def neighbors(self, vertex):
       
        if vertex in self.adj_list:
            return self.adj_list[vertex]
        return []
    
    def display(self):
       
        print("Список смежности:")
        for vertex in sorted(self.adj_list.keys()):
            neighbors = ', '.join(sorted(self.adj_list[vertex]))
            print(f"  {vertex}: [{neighbors}]")
    
    def memory_usage(self):
        
        
        vertices_count = len(self.adj_list)
        
        edges_count = sum(len(neighbors) for neighbors in self.adj_list.values())
        total = vertices_count + edges_count
        return {
            'vertices': vertices_count,
            'edges': edges_count,
            'total': total
        }


class GraphAdjMatrix:
    
    def __init__(self):
        self.vertices = []
        self.matrix = []
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
           
            n = len(self.vertices)
           
            self.matrix.append([0] * n)
            
            for row in self.matrix[:-1]:
                row.append(0)
    
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        
      
        u_idx = self.vertices.index(u)
        v_idx = self.vertices.index(v)
        
       
        self.matrix[u_idx][v_idx] = 1
        self.matrix[v_idx][u_idx] = 1
    
    def has_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            u_idx = self.vertices.index(u)
            v_idx = self.vertices.index(v)
            return self.matrix[u_idx][v_idx] == 1
        return False
    
    def neighbors(self, vertex):
       
        if vertex not in self.vertices:
            return []
        
        vertex_idx = self.vertices.index(vertex)
        neighbors = []
        for i, connected in enumerate(self.matrix[vertex_idx]):
            if connected == 1:
                neighbors.append(self.vertices[i])
        return neighbors
    
    def display(self):
        print("\nМатрица смежности:")
      
        header = "    " + "  ".join(sorted(self.vertices))
        print(header)
        
      
        sorted_vertices = sorted(self.vertices)
        for vertex in sorted_vertices:
            idx = self.vertices.index(vertex)
            row = [str(self.matrix[idx][self.vertices.index(v)]) for v in sorted_vertices]
            print(f"  {vertex}  " + "  ".join(row))
    
    def memory_usage(self):
        
        vertices_count = len(self.vertices)
       
        matrix_size = len(self.vertices) ** 2
        total = vertices_count + matrix_size
        return {
            'vertices': vertices_count,
            'matrix_size': matrix_size,
            'total': total
        }


def main():
    print("=" * 60)
    print("Реализация неориентированного графа")
    print("V = {A, B, C, D, E}")
    print("E = {AB, AC, BC, BD, CE}")
    print("=" * 60)
    
    
    g1 = GraphAdjList()
    edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'E')]
    
    for u, v in edges:
        g1.add_edge(u, v)
    
    g1.display()
    mem1 = g1.memory_usage()
    print(f"\nПамять (список смежности):")
    print(f"  Вершины: {mem1['vertices']}")
    print(f"  Связи: {mem1['edges']}")
    print(f"  Всего элементов: {mem1['total']}")
    
    
    g2 = GraphAdjMatrix()
    for u, v in edges:
        g2.add_edge(u, v)
    
    g2.display()
    mem2 = g2.memory_usage()
    print(f"\nПамять (матрица смежности):")
    print(f"  Вершины: {mem2['vertices']}")
    print(f"  Размер матрицы: {mem2['matrix_size']}")
    print(f"  Всего элементов: {mem2['total']}")
    
    print("\n" + "=" * 60)
    print(f"Список смежности использует: {mem1['total']} элементов")
    print(f"Матрица смежности использует: {mem2['total']} элементов")
    print(f"Разница: {mem2['total'] - mem1['total']} элементов")


if __name__ == "__main__":
    main()
