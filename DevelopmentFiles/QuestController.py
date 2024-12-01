from AllQuests import *
import random
import os

class QuestController:
    def __init__(self):
        self.quest_id = [1,2,3,5]
        self.tip_id = [0,1,2]
        self.all_done = False
        
    def read_success_file(self):
        filename = 'AnswerCorrect.txt'
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return bool(int(file.read()))
        else:
            return False 
        
    def run_quest(self):
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
        print(result)
        if result==True:
            self.quest_id.remove(num)
            self.tip_id.remove(tip)
            
        if os.path.exists('AnswerCorrect.txt'):
            os.remove('AnswerCorrect.txt')
            
        if len(self.tip_id)<1:
            self.all_done = True
        
