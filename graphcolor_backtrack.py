# def graph_coloring(adj_matrix):
#     colors = [-1] * len(adj_matrix)
    
#     def is_safe(node, color):
#         for neighbor in range(len(adj_matrix)):
#             if adj_matrix[node][neighbor] == 1 and colors[neighbor] == color:
#                 return False
#         return True
    
#     def graph_color_helper(node):
#         if node == len(adj_matrix):
#             return True
        
#         for color in range(len(adj_matrix)):
#             if is_safe(node, color):
#                 colors[node] = color
#                 if graph_color_helper(node + 1):
#                     return True
#                 colors[node] = -1
        
#         return False
    
#     if graph_color_helper(0):
#         chromatic_number = max(colors) + 1
#         return chromatic_number, colors
#     else:
#         return None

# # Sample input adjacency matrix
# adj_matrix = [[0, 1, 1, 0, 0],
#               [1, 0, 1, 1, 1],
#               [1, 1, 0, 1, 0],
#               [0, 1, 1, 0, 1],
#               [0, 1, 0, 1, 0]]

# result = graph_coloring(adj_matrix)
# if result is not None:
#     chromatic_number, colors = result
#     print(f"Chromatic number: {chromatic_number}")
#     print("Node colors:")
#     for node, color in enumerate(colors):
#         print(f"Node {node+1}: {color+1}")
# else:
#     print("No valid coloring found")

def graph_coloring(adj_matrix):
    colors = [-1] * len(adj_matrix)
    
    def is_safe(node, color):
        for neighbor in range(len(adj_matrix)):
            if adj_matrix[node][neighbor] == 1 and colors[neighbor] == color:
                return False
        return True
    
    def graph_color_helper(node):
        if node == len(adj_matrix):
            return True
        
        for color in range(len(adj_matrix)):
            if is_safe(node, color):
                colors[node] = color
                if graph_color_helper(node + 1):
                    return True
                colors[node] = -1
        
        return False
    
    if graph_color_helper(0):
        chromatic_number = max(colors) + 1
        return chromatic_number, colors
    else:
        return None

# Take adjacency matrix input from user
n = int(input("Enter the number of nodes: "))
adj_matrix = []
for i in range(n):
    row = list(map(int, input(f"Enter the adjacency matrix row for node {i+1}: ").split()))
    adj_matrix.append(row)

result = graph_coloring(adj_matrix)
if result is not None:
    chromatic_number, colors = result
    print(f"Chromatic number: {chromatic_number}")
    print("Node colors:")
    for node, color in enumerate(colors):
        print(f"Node {node+1}: {color+1}")
else:
    print("No valid coloring found")
