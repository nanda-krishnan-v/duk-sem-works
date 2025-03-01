# # def find_odd_degree_vertices(graph):
# #     degrees = {}
# #     for u, v in graph:
# #         degrees[u] = degrees.get(u, 0) + 1
# #         degrees[v] = degrees.get(v, 0) + 1
# #     odd_vertices = []
# #     for vertex, degree in degrees.items():
# #         if degree % 2 != 0:
# #             odd_vertices.append(vertex)
# #     return odd_vertices

# # def chinese_postman(graph):
# #     odd_vertices = find_odd_degree_vertices(graph)
# #     if len(odd_vertices) == 0:
# #         print("Eulerian Circuit exists")
# #         return True
# #     elif len(odd_vertices) == 2:
# #         print("Exactly two odd degree vertices exist")
# #         return True
# #     else:
# #         return False

# # graph = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (1, 3)]

# # is_eulerian = chinese_postman(graph)
# # if is_eulerian:
# #     print("A solution exists")
# # else:
# #     print("Impossible solution")

# def find_odd_degree_vertices(graph):
#     degrees = {}
#     for u, v in graph:
#         degrees[u] = degrees.get(u, 0) + 1
#         degrees[v] = degrees.get(v, 0) + 1
#     odd_vertices = []
#     for vertex, degree in degrees.items():
#         if degree % 2 != 0:
#             odd_vertices.append(vertex)
#     return odd_vertices

# def chinese_postman(graph):
#     odd_vertices = find_odd_degree_vertices(graph)
#     if len(odd_vertices) == 0:
#         return True
#     elif len(odd_vertices) == 2:
#         return True
#     else:
#         return False

# graph = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)]

# is_eulerian = chinese_postman(graph)
# if is_eulerian:
#     print("A solution exists")
# else:
#     print("Impossible solution")

def find_odd_degree_vertices(graph):
    degrees = {}
    for u, v in graph:
        degrees[u] = degrees.get(u, 0) + 1
        degrees[v] = degrees.get(v, 0) + 1
    odd_vertices = []
    for vertex, degree in degrees.items():
        if degree % 2 != 0:
            odd_vertices.append(vertex)
    return odd_vertices

def chinese_postman(graph):
    odd_vertices = find_odd_degree_vertices(graph)
    if len(odd_vertices) == 0 or len(odd_vertices) == 2:
        return True
    else:
        return False

graph1 = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)]
graph2 = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (1, 3)]

for graph in [graph1, graph2]:
    is_eulerian = chinese_postman(graph)
    if is_eulerian:
        print("A solution exists for the graph:")
        print(graph)
    else:
        print("No solution exists for the graph:")
        print(graph)