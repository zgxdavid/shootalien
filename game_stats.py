# coding=utf-8

import json

class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.high_score = 0
        numbers = [0]
        
        try:
            with open(self.ai_settings.history_score_file) as f1:
                numbers = json.load(f1)
                self.high_score = max(numbers)
        except FileNotFoundError:
            with open(self.ai_settings.history_score_file, 'w') as f1:
                json.dump(numbers, f1)
                
        self.reset_stats()
        self.game_active = False
        self.level = 1
        
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        
       
            
    
        
