def graph_coloring(adj_matrix):
    colors = {}
    nodes = len(adj_matrix)
    available = [True] * nodes
    
    for node in range(nodes):
        for neighbor in range(nodes):
            if adj_matrix[node][neighbor] == 1 and neighbor in colors:
                available[colors[neighbor]] = False
                
        color = 0
        while not available[color]:
            color += 1
        colors[node] = color
        available = [True] * nodes
        
    chromatic_number = max(colors.values()) + 1
    return chromatic_number, colors

# Sample input adjacency matrix
adj_matrix = [[0, 1, 1, 0, 0],
              [1, 0, 1, 1, 1],
              [1, 1, 0, 1, 0],
              [0, 1, 1, 0, 1],
              [0, 1, 0, 1, 0]]

chromatic_number, colors = graph_coloring(adj_matrix)
print(f"Chromatic number: {chromatic_number}")
print("Node colors:")
for node, color in colors.items():
    print(f"Node {node+1}: {color+1}")
