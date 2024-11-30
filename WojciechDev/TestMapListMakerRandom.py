import pickle

# Define the wall object
wall = {
    'name': 'wall',
    'id': 'wall',
    'size_multiplier': (1, 1, 1),
    'position_diff': (0, 0, 0),
    'color': (0, 0, 0, 1),
    'blocked': True,
    'hidden': False
}

# Set the size of the matrix to 10x20 (rows x columns)
matrix_size_x = 9  # Number of rows
matrix_size_y = 19  # Number of columns

# Create a 10x20 matrix filled with walls
map_list = [[wall for _ in range(matrix_size_y)] for _ in range(matrix_size_x)]

# Print the matrix
for row in map_list:
    for cell in row:
        print("wall", end="\t")
    print()

# Save the map to a file using Pickle
with open('test_map.pkl', 'wb') as f:
    pickle.dump(map_list, f)
