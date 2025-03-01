class Graph:
  def __init__(self, graph_dict):
    self.graph_dict = graph_dict

  def is_eulerian(self):
    odd_degree_vertices = 0
    for vertex in self.graph_dict:
      if len(self.graph_dict[vertex]) % 2 != 0:
        odd_degree_vertices += 1
    if odd_degree_vertices == 0:
      return "Eulerian Circuit exists"
    elif odd_degree_vertices == 2:
      return "Eulerian Path exists"
    else:
      return "No Eulerian Path or Circuit exists"

graph = {
  'A': ['B', 'C'],
  'B': ['A', 'C', 'D'],
  'C': ['A', 'B', 'D'],
  'D': ['B', 'C']
}

g = Graph(graph)
result = g.is_eulerian()
print(result)