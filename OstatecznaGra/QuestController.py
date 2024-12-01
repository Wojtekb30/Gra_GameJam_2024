from AllQuests import *
import random
import os
import RenderBirdCore
import time

class QuestController:
    def __init__(self):
        self.quest_id = [1,2,3,5] #nie uzywac questa 4
        self.tip_id = [0,1,2]
        self.all_done = False #In context of available quests
        self.finished_xs=[]
        self.finished_zs=[]
        
        self.checkpoint_order = []
        self.game_done = False
        self.checkpoint_fail = False
        
        self.render_color_number = 0
        self.render_2d_color_shape = False
        
    def set_render_2d_color_shape_index(self, color):
        self.render_2d_color_shape = True
        if color == (0,1,0,1):
            self.render_color_number=0
        if color == (0,1,1,1):
            self.render_color_number=1
        if color == (1,1,0,1):
            self.render_color_number=2
        if color == (1,0,0,1):
            self.render_color_number=3
            
    def should_I_render_2d_color(self):
        if self.render_2d_color_shape==True:
            self.render_2d_color_shape = False
            return True
        return False
        
    def checkpoint_processor(self, color):
        #Zielony, Jasnoniebieski, Żółty, Czerwony
        #checkpoint_colors = [(0,1,0,1),(0,1,1,1),(1,1,0,1),(1,0,0,1)]
        if len(self.checkpoint_order)==0:
            self.checkpoint_order.append(color)
            
        if self.checkpoint_order[-1]!=color:
            self.checkpoint_order.append(color)
            
        if self.checkpoint_order==[(0,1,0,1),(0,1,1,1),(1,1,0,1),(1,0,0,1)]:
            self.game_done = True
        
        if len(self.checkpoint_order)>=4:
            self.checkpoint_order=[]
            self.checkpoint_fail = True
        
    def check_checkpoint_fail(self):
        if self.checkpoint_fail == True:
            self.checkpoint_fail = False
            time.sleep(0.5)
            return True
        else:
            return False
        
    def read_success_file(self):
        filename = 'AnswerCorrect.txt'
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return bool(int(file.read()))
        else:
            return False 
        
    def run_quest(self,question_mark: RenderBirdCore.RenderBirdCore.RectangularPrism):
        num = random.choice(self.quest_id)
        tip = random.choice(self.tip_id)
        if num==1:
            quest1(tip)
        elif num==2:
            quest2(tip)
        elif num==3:
            quest3(tip)
        elif num==4:
            quest4(tip)
        elif num==5:
            quest5(tip)
            
        result = self.read_success_file()
        #print(result)
        if result==True:
            self.quest_id.remove(num)
            self.tip_id.remove(tip)
        
        
        if os.path.exists('AnswerCorrect.txt'):
            os.remove('AnswerCorrect.txt')
            
        if len(self.tip_id)<1:
            self.all_done = True
            
        self.finished_xs.append(question_mark.position[0])
        self.finished_zs.append(question_mark.position[2])
        
