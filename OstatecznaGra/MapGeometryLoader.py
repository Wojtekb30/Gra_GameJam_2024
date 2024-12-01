import pickle
import RenderBirdCore
import copy
import time
import math
from QuestController import *
import pygame

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


def render_map(RenderBirdObject: RenderBirdCore.RenderBirdCore, map_list, camera, initial_camera_position,question_mark_y_mod: int,quests,floor_height=-1, world_height=2, start_x=-1, start_z=-1):
    wall_color = normalize_color((216, 255, 149, 255)) #Zmien przezroczystosc ze 100 na 255
    wall_color_with_edge = normalize_color((180, 220, 120, 255))
    floor_color = normalize_color((125, 133, 113, 255))
    ceiling_color = normalize_color((211, 211, 211, 255))
    
    #quests = QuestController()
    
    last_checkpoint_color_number=0
    
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
                if cell['id'] == "wall":
                    if cell['frame']==True:
                        sciana = RenderBirdObject.RectangularPrism(
                        color_sides=True, color_front=wall_color_with_edge, color_back=wall_color_with_edge,
                        color_bottom=wall_color_with_edge, color_left=wall_color_with_edge, color_right=wall_color_with_edge,
                        color_top=wall_color_with_edge,
                        width=1, depth=1, height=world_height,
                        position=[start_x + x, floor_height + 1,
                                  start_z + z]
                        )
                    
                        RenderBirdObject.RectangularPrism(
                            color_sides=False, frame_color=(0, 0, 0, 1),
                            width=1.005, depth=1.002, height=world_height + 0.002,
                            position=[start_x + x, floor_height + 1,
                                      start_z + z]).draw()
                    else:
                        sciana = RenderBirdObject.RectangularPrism(
                        color_sides=True, color_front=wall_color, color_back=wall_color,
                        color_bottom=wall_color, color_left=wall_color, color_right=wall_color,
                        color_top=wall_color,
                        width=1, depth=1, height=world_height,
                        position=[start_x + x, floor_height + 1,
                                  start_z + z]
                        )
                    sciana.draw()
                    detect_distance=0.8
                    while len(camera.detect_objects_in_view([sciana],detect_distance,88))>0: 
                        camera.move(0,0,-0.05)
                    camera.rotate(0,90,0)
                    while len(camera.detect_objects_in_view([sciana],detect_distance,88))>0: 
                        camera.move(0,0,-0.05)
                    camera.rotate(0,90,0)
                    while len(camera.detect_objects_in_view([sciana],detect_distance,88))>0: 
                        camera.move(0,0,-0.05)
                    camera.rotate(0,90,0)
                    while len(camera.detect_objects_in_view([sciana],detect_distance,88))>0: 
                        camera.move(0,0,-0.05)
                    camera.rotate(0,90,0)
                    
                    
                #else:
                if cell['id'] == "quest": 
                    if quests.all_done==False:
                        quest_x = start_x + x
                    else:
                        quest_x = 1000
                        
                    n=0
                    if len(quests.finished_xs)>0:
                        #print(quests.finished_xs)
                        while n<len(quests.finished_xs):
                            if quest_x==quests.finished_xs[n] and start_z + z==quests.finished_zs[n]:
                                quest_x = 1000
                            n=n+1
                    
                    quest_mark = RenderBirdObject.Model3D_STL("pytajnik.stl",None,(255,50,50,255),
                                                              [quest_x, floor_height+0.7+(math.sin(question_mark_y_mod)/5),start_z + z],0.5,(90*3,0,360*math.sin(question_mark_y_mod)/2))
                    
                    
                    quest_mark_hitbox = RenderBirdObject.RectangularPrism(width=0.5,height=1,depth=0.5,color_sides=False, frame_color=(0,0,1,1),
                                        position=[quest_x, floor_height + 1 ,start_z + z])
                    quest_mark.draw()
                    quest_mark_hitbox.draw()
                    
                    if len(camera.detect_objects_in_view([quest_mark_hitbox],2,10))>0 and RenderBirdObject.key_pressed(pygame.K_i):
                        if quests.all_done==False:
                            was_fullscreen_used = RenderBirdObject.is_fullscreen
                            RenderBirdObject.exit_fullscreen()
                            time.sleep(0.5)
                            quests.run_quest(quest_mark_hitbox)
                            if was_fullscreen_used == True:
                                time.sleep(0.5)
                                RenderBirdObject.toggle_fullscreen()
                                time.sleep(1)
                
                
                
                
                
                
                
                if cell['id']=="checkpoint":
                    checkpoint_colors = [(0,1,0,1),(0,1,1,1),(1,1,0,1),(1,0,0,1)]
                    #Zielony, Jasnoniebieski, Żółty, Czerwony
                    checkpoint = RenderBirdObject.RectangularPrism(width=0.5,height=0.5,depth=0.5,color_sides=False, frame_color=checkpoint_colors[last_checkpoint_color_number],
                                        position=[start_x + x, floor_height + 1 ,start_z + z])
                    checkpoint.draw()
                    
                    
                    if len(camera.detect_objects_in_view([checkpoint],2,20))>0 and RenderBirdObject.key_pressed(pygame.K_i):
                        quests.checkpoint_processor(checkpoint.frame_color)
                        quests.set_render_2d_color_shape_index(checkpoint.frame_color)
                    
                    last_checkpoint_color_number+=1
                    if last_checkpoint_color_number>3:
                        last_checkpoint_color_number=0
                        
                   

                                                         
                        

