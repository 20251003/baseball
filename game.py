import random
from player import Pitcher
class Game:
    def __init__(self,pitcher):
        self.pitcher = pitcher
    
    def pitcher_turn(self):


        pitch_straight_speed = self.pitcher.pitch_speed
        pitch_changeup_speed = int(self.pitcher.pitch_speed*0.9)
        
        
        for i in range(6):
            pitch_type = random.randint(0,self.pitcher.pitch_type)
            if pitch_type == 0:
                numbers = list(range((pitch_straight_speed-9),(pitch_straight_speed+11)))
            else:
                numbers = list(range((pitch_changeup_speed-9),(pitch_changeup_speed+11)))
            weights = [0] * 19
            if self.pitcher.stamina >= 70:
                weights[5:14] = [0.9/10]*10
                weights[15:20] = [0.1/5]*5
            elif self.pitcher.stamina >= 40:
                weights[:4] = [0.2/5]*4
                weights[5:14] = [0.7/10]*10
                weights[15:20] = [0.1/5]*5
            else:
                weights[:4] = [0.4/5]*4
                weights[5:14] = [0.5/10]*10
                weights[15:20] = [0.1/5]*5
            pitch_result = random.choices(numbers,weights=weights,k=1)[0]
            print(f"speed: {pitch_result} km, pitch type: {pitch_type}, stamina: {self.pitcher.stamina}")
            self.pitcher.stamina = self.pitcher.stamina - 10