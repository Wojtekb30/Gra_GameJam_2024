import random
import pickle

# Define the wall object
wall = {
    'name': 'wall',
    'id': 'text_with_name',
    'size_multiplier': (1, 1, 1),
    'position_diff': (0, 0, 0),
    'color': (0, 0, 0, 1),
    'blocked': True,
    'hidden': False
}

# Set the size of the matrix
matrix_size = 15

# Create a matrix with random objects (wall or None)
map_list = [[None for _ in range(matrix_size)] for _ in range(matrix_size)]

# Create the outer border of walls
for i in range(matrix_size):
    map_list[0][i] = wall  # Top border
    map_list[matrix_size - 1][i] = wall  # Bottom border
    map_list[i][0] = wall  # Left border
    map_list[i][matrix_size - 1] = wall  # Right border

# Create the next inner border of None
for i in range(1, matrix_size - 1):
    map_list[1][i] = None  # Top inner border
    map_list[matrix_size - 2][i] = None  # Bottom inner border
    map_list[i][1] = None  # Left inner border
    map_list[i][matrix_size - 2] = None  # Right inner border

# Fill the inner part of the matrix with random walls or None
for i in range(2, matrix_size - 2):
    for j in range(2, matrix_size - 2):
        map_list[i][j] = random.choice([wall, None])

# Print the matrix
for row in map_list:
    for cell in row:
        if cell is None:
            print("None", end="\t")
        else:
            print("wall", end="\t")
    print()

# Save the map to a file using Pickle
with open('map1.pkl', 'wb') as f:
    pickle.dump(map_list, f)
