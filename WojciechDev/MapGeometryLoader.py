import pickle
import RenderBirdCore
import copy


def load_map_file(file:str):
    map_list=[]
    with open(file, 'rb') as file:
        map_list = pickle.load(file)
    return map_list


'''def render_map(RenderBirdObject: RenderBirdCore.RenderBirdCore, map_list):
    for i in map_list:
        if i['name']=='wall':
            final_position = list(i['position'])
            for j in range(0,i['size'][0]):
                
                if i['hidden']==True:
                    final_position=(1000,1000,1000)
                else:
                    
                    final_position[0] = final_position[0]+j
                    
                for k in range(0,i['size'][2]):
                    if i['hidden']==True:
                        final_position=(1000,1000,1000)
                    else:
                        #final_position = list(i['position'])
                        final_position[1] = final_position[1]+k
                        
                    for l in range(0,i['size'][2]):
                        if i['hidden']==True:
                            final_position=(1000,1000,1000)
                        else:
                            #final_position = list(i['position'])
                            final_position[2] = final_position[2]+l
                        RenderBirdObject.Cube(size=1,position=final_position,color_sides=True).draw()          
                        #RenderBirdObject.Model3D_STL(stl_path='cube.stl',color=i['color'],texture_path=i['texture'],position=final_position,scale=5).draw()'''
                
def normalize_color(tuple_4byte):
    '''
    Use this only if you use RBGT values from 0 to 255 instead of 0-1)
    '''
    r = tuple_4byte[0]/255
    g = tuple_4byte[1]/255
    b = tuple_4byte[2]/255
    t = tuple_4byte[3]/255
    return (r,g,b,t)


def calculate_side(x, y, width, height):
    x1 = x - width / 2
    y1 = y - height / 2
    x2 = x + width / 2
    y2 = y + height / 2
    return [x1, y1, x2, y2]

                
'''def render_map(RenderBirdObject: RenderBirdCore.RenderBirdCore, map_list, floor_height=-1, world_height=2, start_x=-1, start_z=-1):
    wall_color = [0, 0, 0, 1]
    floor_color = normalize_color((125, 133, 113, 255))
    floor_position_recalc = calculate_side(start_x,start_z,len(map_list),len(map_list[0]))
    RenderBirdObject.RectangularPrism(width=3*len(map_list),height=1,depth=3*len(map_list[0]),position=[floor_position_recalc[2]*3,floor_height,2*floor_position_recalc[3]],color_sides=True,color_back=floor_color,color_bottom=floor_color,color_front=floor_color,color_left=floor_color,color_right=floor_color,color_top=floor_color).draw()
    x=-1 
    z=-1
    n=0
    height_mod=0
    for row in map_list:
        n=n+1
        x=-1
        z+=1
        for i in row:
            x=x+1
            print(x)
            print(z)
            print()
            if i!=None:
                #print(wall_color)
                wall_color[0]=wall_color[0]+0.01
                wall_color[1]=wall_color[1]+0.01
                wall_color[2]=wall_color[2]+0.01
                if i['name'].lower()=='wall':
                    RenderBirdObject.RectangularPrism(color_sides=True,color_front=wall_color,color_back=wall_color,
                    color_bottom=wall_color,color_left=wall_color,color_right=wall_color,color_top=wall_color,
                    position=[start_x+x+i['position_diff'][0],floor_height+1+height_mod+i['position_diff'][1],start_z+z+start_x+x+i['position_diff'][2]]).draw()
   ''' 
                
        
    
   
   
'''def render_map(RenderBirdObject: RenderBirdCore.RenderBirdCore, map_list, floor_height=-1, world_height=2, start_x=-1, start_z=-1):
    wall_color = normalize_color((216, 255, 149, 255))
    floor_color = normalize_color((125, 133, 113, 255))
    floor_position_recalc = calculate_side(start_x, start_z, len(map_list), len(map_list[0]))
    RenderBirdObject.RectangularPrism(width=3 * len(map_list), height=1, depth=3 * len(map_list[0]),
                                     position=[floor_position_recalc[2] * 3, floor_height-0.5, 2 * floor_position_recalc[3]],
                                     color_sides=True, color_back=floor_color, color_bottom=floor_color,
                                     color_front=floor_color, color_left=floor_color, color_right=floor_color,
                                     color_top=floor_color).draw()
    RenderBirdObject.RectangularPrism(width=3 * len(map_list), height=1, depth=3 * len(map_list[0]),
                                     position=[floor_position_recalc[2] * 3, floor_height+world_height+1-0.5, 2 * floor_position_recalc[3]],
                                     color_sides=True, color_back=floor_color, color_bottom=floor_color,
                                     color_front=floor_color, color_left=floor_color, color_right=floor_color,
                                     color_top=floor_color).draw()

    for z, row in enumerate(map_list):
        for x, i in enumerate(row):
            if i is not None:
                if i['name'].lower() == 'wall':
                    RenderBirdObject.RectangularPrism(color_sides=True, color_front=wall_color, color_back=wall_color,
                                                     color_bottom=wall_color, color_left=wall_color, color_right=wall_color,
                                                     color_top=wall_color,
                                                     width=1,depth=1,height=world_height,
                                                     position=[start_x + x, floor_height + 1 + i['position_diff'][1],
                                                              start_z + z]).draw()
                    RenderBirdObject.RectangularPrism(color_sides=False, frame_color=(0,0,0,1),
                                                     width=1.001,depth=1.001,height=world_height+0.001,
                                                     position=[start_x + x, floor_height + 1 + i['position_diff'][1],
                                                              start_z + z]).draw()'''

def render_map(RenderBirdObject: RenderBirdCore.RenderBirdCore, map_list, camera, floor_height=-1, world_height=2, start_x=-1, start_z=-1):
    wall_color = normalize_color((216, 255, 149, 100)) #Zmien przezroczystosc ze 100 na 255
    floor_color = normalize_color((125, 133, 113, 255))
    floor_position_recalc = calculate_side(start_x, start_z, len(map_list), len(map_list[0]))

    # Draw the floor
    RenderBirdObject.RectangularPrism(
        width=1000, height=1, depth=1000,
        position=[0,floor_height-0.5-0.5,0],
        color_sides=True, color_back=floor_color, color_bottom=floor_color,
        color_front=floor_color, color_left=floor_color, color_right=floor_color,
        color_top=floor_color
    ).draw()

    # Draw the ceiling
    RenderBirdObject.RectangularPrism(
        width=1000, height=floor_height+2.5+0.5, depth=1000,
        position=[0,0,0],
        color_sides=True, color_back=floor_color, color_bottom=floor_color,
        color_front=floor_color, color_left=floor_color, color_right=floor_color,
        color_top=floor_color
    ).draw()

    def check_pattern(x, z, patterns):
        """
        Check if the cell at (x, z) matches any of the specified patterns in its surroundings.
        """
        for pattern in patterns:
            matches = True
            for dz, row in enumerate(pattern):
                for dx, expected in enumerate(row):
                    nx, nz = x + dx - 1, z + dz - 1  # Adjust to check 3x3 grid around (x, z)
                    if 0 <= nx < len(map_list[0]) and 0 <= nz < len(map_list):
                        current = map_list[nz][nx]
                        if expected == "Wall" and (current is None or current["name"].lower() != "wall"):
                            matches = False
                        if expected == "None" and current is not None:
                            matches = False
                    elif expected != "None":  # Out-of-bounds cells must be None
                        matches = False
            if matches:
                return True
        return False

    # Patterns for which to draw the frame
    frame_patterns = [
        [["None", "Wall"], ["None", "None"]],
        [["Wall", "None"], ["None", "None"]],
        [["None", "Wall", "None"], ["None", "None", "None"]],
        [["None", "None", "None"], ["None", "Wall", "None"]],
        [["None", "None", "Wall"], ["None", "Wall", "Wall"], ["None", "None", "Wall"]],
        [["Wall", "None", "None"], ["Wall", "Wall", "None"], ["Wall", "None", "None"]],
        [["Wall", "Wall", "Wall"], ["None", "Wall", "None"], ["None", "None", "None"]],
        [["None", "None", "None"], ["None", "Wall", "None"], ["Wall", "Wall", "Wall"]],
        [["None", "None"], ["Wall", "None"]],
        [["None", "None"], ["None", "Wall"]],
    ]

    # Draw walls and frames
    for z, row in enumerate(map_list):
        for x, cell in enumerate(row):
            if cell is not None:
                if cell['id'].lower() == "wall":
                    # Draw the wall
                    RenderBirdObject.RectangularPrism(
                        color_sides=True, color_front=wall_color, color_back=wall_color,
                        color_bottom=wall_color, color_left=wall_color, color_right=wall_color,
                        color_top=wall_color,
                        width=1, depth=1, height=world_height,
                        position=[start_x + x, floor_height + 1,
                                  start_z + z]
                    ).draw()

                    # Draw the black frame if it matches the patterns
                    '''if check_pattern(x, z, frame_patterns):
                        RenderBirdObject.RectangularPrism(
                            color_sides=False, frame_color=(0, 0, 0, 1),
                            width=1.005, depth=1.005, height=world_height + 0.001,
                            position=[start_x + x, floor_height + 1,
                                      start_z + z]
                        ).draw()'''
          
                    RenderBirdObject.RectangularPrism(
                            color_sides=False, frame_color=(0, 0, 0, 1),
                            width=1.005, depth=1.005, height=world_height + 0.001,
                            position=[start_x + x, floor_height + 1,
                                      start_z + z]).draw()
                #else:
                if cell['id'].lower() == "teleport":
                    teleport = RenderBirdObject.RectangularPrism(width=0.5,height=0.5,depth=0.5,color_sides=False, frame_color=(255,255,255,0),
                                        position=[start_x + x, floor_height + 1,start_z + z]).draw()
                    #if teleport.check_collission

