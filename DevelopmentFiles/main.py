import RenderBirdCore #RenderBirdCore version 0.1.2
from MapGeometryLoader import *
import pygame
import time
from QuestController import *

r = RenderBirdCore.RenderBirdCore(camera_yaw=90+90)#,camera_x=0.85,camera_z=0.85)

#r.camera.rotate_pitch(-10)

fpslimit = r.FPS_Limiter(45)

r.set_background_color(176, 196, 222)

mapa = load_map_file('world.pkl')

initial_camera_position = r.camera.position

ControlsDisplayController = r.RunAfterTime(20)
ControlsImage = r.Image_2D("Controls.bmp",10,10)
IntroDisplayController = r.RunAfterTime(1) #set to 10
IntroImage = r.Image_2D("Story1.bmp",0,0,r.window_size_x,r.window_size_y)
render_controls = True
render_intro = True

WinImage = r.Image_2D("Win.bmp",-2000,0,r.window_size_x,r.window_size_y)

def return_false():
    return False
    
question_mark_y_mod=0

quests = QuestController()

while r.running == True:
    fpslimit.code_start_point()
    r.clear_screen()
    question_mark_y_mod+=0.1
    if question_mark_y_mod>=100*math.pi:
        question_mark_y_mod=0
    render_map(r,mapa,r.camera,initial_camera_position,question_mark_y_mod,quests)
    
    if r.key_pressed(pygame.K_f):
        r.toggle_fullscreen()
        time.sleep(2)
    if r.key_pressed(pygame.K_ESCAPE):
        r.safe_close()
        
    #if r.key_pressed(pygame.K_t):
    #    r.camera.rotate(0,90,0)
    #    time.sleep(1)
    
    if render_intro==False:
        if r.key_pressed(pygame.K_LSHIFT):
            mnoznik_predkosci=2
        else:
            mnoznik_predkosci=1
        if r.key_pressed(pygame.K_w):# and r.camera.forward_vector[0]>-0.5: 
            r.camera.move(0,0,0.05*mnoznik_predkosci) 
        if r.key_pressed(pygame.K_s):# and r.camera.forward_vector[0]<-0.5: 
            r.camera.move(0,0,-0.05*mnoznik_predkosci) 
        
        #if r.key_pressed(pygame.K_a): 
        #    r.camera.move(-0.05,0,0) 
        #if r.key_pressed(pygame.K_d): 
        #    r.camera.move(0.05,0,0) 
        
        if r.key_pressed(pygame.K_e): 
            r.camera.move(0,0.05,0) 
        if r.key_pressed(pygame.K_q): 
            r.camera.move(0,-0.05,0) 
    
        if r.key_pressed(pygame.K_UP):
            r.camera.rotate(1,0,0)
        if r.key_pressed(pygame.K_DOWN):
            r.camera.rotate(-1,0,0)
        if r.key_pressed(pygame.K_LEFT):
            r.camera.rotate(0,-2,0)
        if r.key_pressed(pygame.K_RIGHT):
            r.camera.rotate(0,2,0)
        
    render_controls = ControlsDisplayController.run_after_time(return_false)
    render_intro = IntroDisplayController.run_after_time(return_false)
    if render_intro == False:
        IntroImage.move(-20,0)
    else:
        r.camera.rotate(0,1,0)
        r.camera.rotate(0,-1,0)
    if render_controls == False:
        ControlsImage.move(-5,0)
    
    if ControlsImage.x>2000:
        ControlsImage.x=2000
        IntroImage.x=2000
        
    if quests.check_checkpoint_fail()==True:
        print("There was checkpoint failure")
        
    if quests.game_done==True:
        print("You won!")
        WinImage.x=0
        
    r.render_2d_objects([ControlsImage,IntroImage,WinImage]) 
    #print(r.camera.forward_vector)
    #r.camera.use_mouse_camera_controls(r.window_size_x,r.window_size_y,sensitivity=0.2,sensitivity_factor=1,reverse_horizontally=False,reverse_vertially=False,mouse_cursor_visible=True) 
    
    r.update_display()
    r.handle_close_event_direct()
    
    if quests.game_done==True:
        time.sleep(10)
        r.safe_close()
    
    fpslimit.code_end_point_limit_framerate()

