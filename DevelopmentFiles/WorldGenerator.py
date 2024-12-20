import pickle
import random

#0 - nic
#1 - sciana
#2 - quest
#3 - checkpoint
#4 - ciemniejsza sciana z ramka


matrix = [
    [1, 4, 1, 1, 1, 4, 1, 1, 0, 1, 4, 1, 1, 4, 1],
    [4, 0, 1, 0, 3, 1, 0, 1, 0, 4, 2, 4, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 4, 1, 0, 4, 0, 4, 1, 4, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 4, 0, 1],
    [1, 0, 0, 0, 0, 4, 1, 0, 4, 1, 0, 0, 0, 1, 1],
    [1, 0, 4, 1, 1, 1, 0, 0, 1, 1, 0, 4, 1, 1],
    [1, 0, 1, 1, 1, 3, 0, 1, 1, 1, 2, 1, 1, 1],
    [1, 0, 1, 1, 4, 4, 0, 0, 2, 1, 4, 1, 1, 1],
    [1, 0, 0, 0, 0, 4, 1, 1, 1, 4, 3, 0, 0, 1],
    [1, 0, 4, 1, 0, 4, 1, 1, 4, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 2, 1, 1, 1, 1, 1, 1, 4, 3, 4, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 4, 1, 0, 0, 0, 1],
    [1, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]



objects = []

for y, row in enumerate(matrix):
    object_row = []
    for x, cell in enumerate(row):
        if cell == 0:
            object_row.append(None)  
        elif cell == 1:
            object_row.append({
                "id": "wall",
                "position": (x, y, 0),
                "name": f"#wall{x}_{y}",
                "blocked": True,
                "color": (0, 0, 0, 1),
                "texture": "",
                "hidden": False,
                "frame": False
            }) 
        elif cell == 2:
            object_row.append({
                "id": "quest",
                "position": (x, y, 0),
                "name": f"#quest{x}_{y}",
                "color": (0, 0, 0, 1),
                "texture": "",
                "blocked": True,
                "hidden": False,
                "destination_x": random.randint(0, 14),
                "destination_y": random.randint(0, 14),
            })  
        elif cell == 3:
            object_row.append({
                "id": "checkpoint",
                "position": (x, y, 0),
                "name": f"#checkpoint{x}_{y}",
                "color": (0, 0, 0, 1),
                "texture": "",
                "hidden": False,
                "completed": True,
                "quest_directory": random.choice(["quest1.py", "quest2.py", "quest3.py"]),
            })
        elif cell == 4:
            object_row.append({
                "id": "wall",
                "position": (x, y, 0),
                "name": f"#wall{x}_{y}",
                "blocked": True,
                "color": (0, 0, 0, 1),
                "texture": "",
                "hidden": False,
                "frame": True
            }) 
    objects.append(object_row)


with open('world.pkl', 'wb') as f:
    pickle.dump(objects, f)

with open('world.pkl', 'rb') as f:
    objects = pickle.load(f)

def display_objects():
    for row in objects:
        row_str = ""
        for obj in row:
            if obj is None:
                row_str += "- "
            elif obj["id"] == "wall":
                row_str += "# "
            elif obj["id"] == "checkpoint":
                row_str += "C "
            elif obj["id"] == "quest":
                row_str += "Q "
        print(row_str)

display_objects()


