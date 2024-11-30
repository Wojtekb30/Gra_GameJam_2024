import pickle
import RenderBirdCore
import copy
import time
import math

def load_map_file(file:str):
    map_list=[]
    with open(file, 'rb') as file:
        map_list = pickle.load(file)
    return map_list

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


def render_map(RenderBirdObject: RenderBirdCore.RenderBirdCore, map_list, camera, initial_camera_position,question_mark_y_mod: int,floor_height=-1, world_height=2, start_x=-1, start_z=-1):
    wall_color = normalize_color((216, 255, 149, 255)) #Zmien przezroczystosc ze 100 na 255
    floor_color = normalize_color((125, 133, 113, 255))
    ceiling_color = normalize_color((211, 211, 211, 255))
    #ceiling_color = normalize_color((211, 211, 211, 255))
    #floor_position_recalc = calculate_side(start_x, start_z, len(map_list), len(map_list[0]))

    RenderBirdObject.RectangularPrism(
        width=1000, height=1, depth=1000,
        position=[0,floor_height+2.5,0],
        color_sides=True, color_back=ceiling_color, color_bottom=ceiling_color,
        color_front=ceiling_color, color_left=ceiling_color, color_right=ceiling_color,
        color_top=ceiling_color
    ).draw()

    RenderBirdObject.RectangularPrism(
        width=1000, height=1, depth=1000,
        position=[0,floor_height-0.5,0],
        color_sides=True, color_back=floor_color, color_bottom=floor_color,
        color_front=floor_color, color_left=floor_color, color_right=floor_color,
        color_top=floor_color
    ).draw()
 


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

    # Draw walls and frames.
    for z, row in enumerate(map_list):
        for x, cell in enumerate(row):
            if cell is not None:
                if cell['id'].lower() == "wall":
                    # Draw the wall
                    sciana = RenderBirdObject.RectangularPrism(
                        color_sides=True, color_front=wall_color, color_back=wall_color,
                        color_bottom=wall_color, color_left=wall_color, color_right=wall_color,
                        color_top=wall_color,
                        width=1, depth=1, height=world_height,
                        position=[start_x + x, floor_height + 1,
                                  start_z + z]
                    )
          
                    RenderBirdObject.RectangularPrism(
                            color_sides=False, frame_color=(0, 0, 0, 1),
                            width=1.005, depth=1.0015, height=world_height + 0.001,
                            position=[start_x + x, floor_height + 1,
                                      start_z + z]).draw()
                    sciana.draw()
                    detect_distance=0.8
                    while len(camera.detect_objects_in_view([sciana],detect_distance,90))>0: 
                        camera.move(0,0,-0.01)
                    camera.rotate(0,90,0)
                    while len(camera.detect_objects_in_view([sciana],detect_distance,90))>0: 
                        camera.move(0,0,-0.01)
                    camera.rotate(0,90,0)
                    while len(camera.detect_objects_in_view([sciana],detect_distance,90))>0: 
                        camera.move(0,0,-0.01)
                    camera.rotate(0,90,0)
                    while len(camera.detect_objects_in_view([sciana],detect_distance,90))>0: 
                        camera.move(0,0,-0.01)
                    camera.rotate(0,90,0)
                    
                    
                #else:
                if cell['id'].lower() == "teleport": #change to quest or something
                    
                    quest_mark = RenderBirdObject.Model3D_STL("pytajnik.stl",None,(0,0,255,255),
                                                              [start_x + x, floor_height+0.8+(math.sin(question_mark_y_mod)/4),start_z + z],0.5,(90*3,0,360*math.sin(question_mark_y_mod)/2))
                    
                    
                    quest_mark_hitbox = RenderBirdObject.RectangularPrism(width=0.5,height=0.5,depth=0.5,color_sides=False, frame_color=(0,0,255//2,0),
                                        position=[start_x + x, floor_height + 1 ,start_z + z])
                    quest_mark.draw()
                    quest_mark_hitbox.draw()
                    
                                                         
                        

