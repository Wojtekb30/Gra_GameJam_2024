import RenderBirdCore
from MapGeometryLoader import *
import pygame

r = RenderBirdCore.RenderBirdCore()

fpslimit = r.FPS_Limiter(30)

r.set_background_color(176, 196, 222)

mapa = load_map_file('map1.pkl')

while r.running == True:
    fpslimit.code_start_point()
    r.clear_screen()
    
    render_map(r,mapa)
    
    if r.key_pressed(pygame.K_w): 
        r.camera.move(0,0,0.05) 
    if r.key_pressed(pygame.K_s): 
        r.camera.move(0,0,-0.05) 
    if r.key_pressed(pygame.K_a): 
        r.camera.move(-0.05,0,0) 
    if r.key_pressed(pygame.K_d): 
        r.camera.move(0.05,0,0) 
        
    if r.key_pressed(pygame.K_e): 
        r.camera.move(0,0.05,0) 
    if r.key_pressed(pygame.K_q): 
        r.camera.move(0,-0.05,0) 
    
    #if r.key_pressed(pygame.K_UP):
    #    r.camera.rotate(1,0,0)
    #if r.key_pressed(pygame.K_DOWN):
    #    r.camera.rotate(-1,0,0)
    if r.key_pressed(pygame.K_LEFT):
        r.camera.rotate(0,-2,0)
    if r.key_pressed(pygame.K_RIGHT):
        r.camera.rotate(0,2,0)
        
    #r.camera.use_mouse_camera_controls(r.window_size_x,r.window_size_y,sensitivity=0.2,sensitivity_factor=1,reverse_horizontally=False,reverse_vertially=False,mouse_cursor_visible=True) 
    
    r.update_display()
    r.handle_close_event_direct()
    fpslimit.code_end_point_limit_framerate()
